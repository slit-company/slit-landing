#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import re
from pathlib import Path
from typing import Iterable
from urllib.parse import quote, unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TARGET_URL = "https://letsur.ai/kr"
HTML_OUTPUT = ROOT / "kr" / "index.html"
STATE_DIR = ROOT / ".omx" / "state" / "landing-out"

SKIP_PREFIXES = ("data:", "mailto:", "tel:", "javascript:", "#")
CSS_URL_RE = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.IGNORECASE)
CSS_IMPORT_RE = re.compile(
    r"""@import\s+(?:url\(\s*)?(['"]?)(.*?)\1\s*\)?""",
    re.IGNORECASE,
)
ANCHOR_HREF_RE = re.compile(r"(<a\b[^>]*\bhref=)(['\"])([^'\"]+)(\2)", re.IGNORECASE)


class MirrorSite:
    def __init__(self, target_url: str) -> None:
        self.target_url = target_url
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/135.0.0.0 Safari/537.36"
                )
            }
        )
        self.downloaded: dict[str, str | None] = {}
        self.download_stack: set[str] = set()
        self.summary = {
            "downloaded_assets": 0,
            "failed_assets": [],
        }

    def run(self) -> None:
        html = self.fetch_text(self.target_url)
        soup = BeautifulSoup(html, "html.parser")

        for original in self.collect_html_asset_urls(soup):
            self.mirror_url(original, self.target_url)

        html = self.rewrite_anchor_links(html)

        HTML_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        HTML_OUTPUT.write_text(html, encoding="utf-8")

        self.write_root_index()
        self.write_extraction_summary(html)

    def fetch_text(self, url: str) -> str:
        response = self.session.get(url, timeout=120)
        response.raise_for_status()
        response.encoding = response.encoding or "utf-8"
        return response.text

    def collect_html_asset_urls(self, soup: BeautifulSoup) -> set[str]:
        urls: set[str] = set()

        for link in soup.find_all("link", href=True):
            rels = {rel.lower() for rel in (link.get("rel") or [])}
            if rels & {
                "stylesheet",
                "icon",
                "apple-touch-icon",
                "manifest",
                "preload",
                "prefetch",
                "modulepreload",
            }:
                urls.add(link["href"])

        for script in soup.find_all("script", src=True):
            urls.add(script["src"])

        for img in soup.find_all(["img", "source"], src=True):
            urls.add(img["src"])

        for node in soup.find_all(["img", "source"], srcset=True):
            urls.update(self.split_srcset(node["srcset"]))

        return {url for url in urls if self.is_remoteish(url)}

    def split_srcset(self, srcset: str) -> Iterable[str]:
        for part in srcset.split(","):
            part = part.strip()
            if not part:
                continue
            yield part.split()[0]

    def is_remoteish(self, value: str) -> bool:
        if not value:
            return False
        if value.startswith(SKIP_PREFIXES):
            return False
        return value.startswith(("http://", "https://", "//"))

    def normalize_url(self, value: str, base_url: str) -> str | None:
        if not value or value.startswith(SKIP_PREFIXES):
            return None
        url = urljoin(base_url, value)
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"}:
            return None
        return url

    def mirror_url(self, original_value: str, base_url: str) -> str | None:
        normalized = self.normalize_url(original_value, base_url)
        if not normalized:
            return None
        if normalized in self.downloaded:
            return self.downloaded[normalized]
        if normalized in self.download_stack:
            return None

        self.download_stack.add(normalized)
        try:
            response = self.session.get(normalized, timeout=120)
            response.raise_for_status()

            relative_path = self.local_path_for_response(normalized, response)
            save_path = ROOT / relative_path
            local_url = self.local_url_for_path(relative_path)
            save_path.parent.mkdir(parents=True, exist_ok=True)

            content_type = response.headers.get("content-type", "").lower()
            if "text/css" in content_type or save_path.suffix == ".css":
                css_text = response.text
                css_text = self.rewrite_css(css_text, normalized)
                save_path.write_text(css_text, encoding="utf-8")
            else:
                save_path.write_bytes(response.content)

            self.downloaded[normalized] = local_url
            self.summary["downloaded_assets"] += 1
            return local_url
        except Exception as exc:  # noqa: BLE001
            self.downloaded[normalized] = None
            self.summary["failed_assets"].append(
                {
                    "url": normalized,
                    "error": str(exc),
                }
            )
            return None
        finally:
            self.download_stack.discard(normalized)

    def local_path_for_response(self, url: str, response: requests.Response) -> Path:
        parsed = urlparse(url)
        raw_path = unquote(parsed.path.lstrip("/"))
        if not raw_path:
            raw_path = "index"

        path = Path(parsed.netloc) / raw_path
        content_type = response.headers.get("content-type", "").split(";")[0].strip().lower()

        if parsed.query:
            query_hash = hashlib.sha1(parsed.query.encode("utf-8")).hexdigest()[:10]
            if path.suffix:
                path = path.with_name(f"{path.stem}__q_{query_hash}{path.suffix}")
            else:
                path = path.with_name(f"{path.name}__q_{query_hash}")

        if not path.suffix:
            guessed_ext = mimetypes.guess_extension(content_type) or ""
            if guessed_ext == ".jpe":
                guessed_ext = ".jpg"
            if guessed_ext:
                path = path.with_suffix(guessed_ext)

        return path

    def local_url_for_path(self, relative_path: Path) -> str:
        return "/" + "/".join(quote(part) for part in relative_path.parts)

    def rewrite_css(self, css_text: str, source_url: str) -> str:
        def replacer(match: re.Match[str]) -> str:
            original = match.group(2).strip()
            rewritten = self.mirror_url(original, source_url)
            if not rewritten:
                return match.group(0)
            quote = match.group(1)
            return f"url({quote}{rewritten}{quote})"

        css_text = CSS_URL_RE.sub(replacer, css_text)

        def import_replacer(match: re.Match[str]) -> str:
            original = match.group(2).strip()
            rewritten = self.mirror_url(original, source_url)
            if not rewritten:
                return match.group(0)
            quote = match.group(1) or '"'
            return f'@import {quote}{rewritten}{quote}'

        return CSS_IMPORT_RE.sub(import_replacer, css_text)

    def apply_replacements(self, html: str, replacements: dict[str, str]) -> str:
        for original, rewritten in sorted(
            replacements.items(),
            key=lambda item: len(item[0]),
            reverse=True,
        ):
            html = html.replace(original, rewritten)
        return html

    def rewrite_anchor_links(self, html: str) -> str:
        def replacer(match: re.Match[str]) -> str:
            prefix, quote_char, href, suffix = match.groups()
            if href in {"#", "/kr", "/kr/"}:
                return match.group(0)
            if href.startswith("/") and not href.startswith("//"):
                href = urljoin(self.target_url, href)
            return f"{prefix}{quote_char}{href}{suffix}"

        return ANCHOR_HREF_RE.sub(replacer, html)

    def write_root_index(self) -> None:
        (ROOT / "index.html").write_text(
            """<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="refresh" content="0; url=/kr/" />
    <title>렛서 클론</title>
  </head>
  <body>
    <p><a href="/kr/">/kr/로 이동</a></p>
  </body>
</html>
""",
            encoding="utf-8",
        )

    def write_extraction_summary(self, html: str) -> None:
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        summary = {
            "target_url": self.target_url,
            "extracted_at": __import__("datetime").datetime.now().isoformat(),
            "screenshot_path": None,
            "landmark_count": {
                "nav": len(re.findall(r"<nav\b", html, re.IGNORECASE)),
                "main": len(re.findall(r"<main\b", html, re.IGNORECASE)),
                "footer": len(re.findall(r"<footer\b", html, re.IGNORECASE)),
                "form": len(re.findall(r"<form\b", html, re.IGNORECASE)),
                "section": len(re.findall(r"<section\b", html, re.IGNORECASE)),
            },
            "interactive_count": len(
                re.findall(r"<(?:a|button|input|select|textarea)\b", html, re.IGNORECASE)
            ),
            "extraction_size_kb": round(len(html.encode("utf-8")) / 1024, 1),
            "downloaded_assets": self.summary["downloaded_assets"],
            "failed_assets": self.summary["failed_assets"],
        }
        (STATE_DIR / "web-clone-extraction.json").write_text(
            json.dumps(summary, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Mirror letsur.ai/kr into this repo.")
    parser.add_argument("--url", default=DEFAULT_TARGET_URL, help="Page URL to mirror")
    args = parser.parse_args()

    mirror = MirrorSite(args.url)
    mirror.run()


if __name__ == "__main__":
    main()
