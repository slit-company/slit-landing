#!/usr/bin/env python3
"""Generate SL:IT project detail HTML pages from structured data."""

from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "kr" / "portfolio"

PROJECTS = [
    {
        "slug": "anyon",
        "category": "AI 플랫폼",
        "title": "Anyon",
        "tagline": "비개발자와 기업이 아이디어 구상부터 배포까지 한 흐름으로 실행할 수 있게 만든 AI 자동화 개발 플랫폼",
        "hero_sub": "생성형 AI를 단순 코드 생성 도구가 아니라 실제 서비스 제작 파이프라인으로 확장한 데스크톱 기반 개발 플랫폼입니다. 제품 기획, 템플릿 선택, 멀티 에이전트 개발, 외부 서비스 연동, 배포까지 이어지는 흐름을 하나의 제품 경험으로 묶었습니다.",
        "meta": [
            ("개발 기간", "2025.04 ~ 2026.02"),
            ("개발 기간 기준 커밋", "1,155 commits"),
            ("사용자 검증", "인터뷰 56명"),
        ],
        "overview": "Anyon은 Electron 기반 앱, 웹 서버 계층, 워커, 템플릿, E2E 테스트, Supabase 연동을 모두 포함한 풀스택 제품으로 운영되었습니다. 1,155개 커밋이 축적되었고, 누적 외주 매출 ₩3,700만과 수상 2건을 함께 확보한 대표 레퍼런스입니다.",
        "challenge": "기존 AI 코딩 도구는 초안 생성에는 강했지만 실제 서비스 완성 단계에서 여러 단절이 있었습니다. 비개발자에게는 개발 환경 설치·코드 구조 이해·외부 API 연결·배포 설정이 각각 별도 장벽이었고, 기업에서는 프로토타입을 실제 운영 가능한 산출물로 끌어올리는 과정에서 품질 편차와 반복 비용이 커졌습니다. 인터뷰 기반 56명 대화에서 설치·배포·외부 서비스 설정이 핵심 이탈 구간으로 반복 확인되었고, B2B 인터뷰 12곳 중 7곳에서 PoC 검토 의향이 확인되었습니다.",
        "solution": "Electron 기반 데스크톱 앱 위에 React·TypeScript UI를 구축하고, 서버 계층과 워커 계층을 분리해 기획부터 실행까지 이어지는 end to end 자동화 흐름을 구성했습니다. 단일 모델 호출 도구가 아니라 멀티 모델·멀티 런타임·멀티 채널을 조합한 작업 플랫폼에 가깝습니다. OpenAI·Anthropic·Bedrock·Google·xAI 계열 SDK와 MCP SDK를 함께 사용해 확장성을 확보했고, 로컬 SQLite와 Supabase를 병행해 데스크톱 앱의 즉시성과 클라우드 연동성을 동시에 챙겼습니다.",
        "architecture": "리포지토리는 `src/`, `server/`, `worker/`, `workers/`, `templates/`, `scaffold/`, `e2e-tests/`, `supabase/`를 축으로 나뉩니다. `src/`는 Electron 렌더러와 메인 프로세스를 함께 담는 핵심 애플리케이션 레이어로, `ipc/`·`app/`·`components/`·`db/`·`prompts/`·`supabase_admin/`·`vercel_admin/` 같은 폴더가 제품 기능과 인프라 연동을 분리합니다. `server/`는 별도 웹 계층과 서버 사이드 실행을 담당하고, `worker/`와 `workers/`는 스크린샷·서비스 워커·프록시 같은 비동기 처리 레이어로 동작합니다.",
        "highlights": [
            "Electron 기반 데스크톱 앱 안에 기획·개발·배포 흐름을 통합해 도구 전환 비용을 줄임",
            "멀티 모델 SDK와 MCP SDK를 결합해 특정 모델 종속성을 낮추고 확장 가능한 AI 실행 계층 구성",
            "Monaco와 Lexical 기반 편집 환경으로 코드 편집과 문서형 상호작용을 한 제품 안에서 처리",
            "Playwright 자동화로 외부 서비스 설정과 배포 전후 검증 흐름을 제품 경험으로 연결",
            "템플릿과 스캐폴드 구조를 별도 계층으로 운영해 생성 결과의 품질 편차를 줄이고 재사용성 확보",
            "Vitest·Playwright·Storybook 조합으로 UI·로직·사용자 흐름 검증 체계를 다층으로 구성",
        ],
        "metrics": [
            ("개발 기간 기준 커밋", "1,155 commits"),
            ("누적 외주 매출", "₩3,700만"),
            ("사용자 검증", "인터뷰 56명"),
            ("B2B 검증", "12곳 검토, 7곳 PoC 의향"),
            ("코드 품질 개선", "일관성 +34%, 에러율 -41%"),
            ("운영 효율", "평균 배포 약 3분"),
            ("비용 효율", "앱 1개당 AI API 평균 $13.28"),
            ("대외 성과", "수상 2건"),
        ],
        "stack": [
            "Electron", "React 19", "TypeScript", "TanStack Router/Query", "Jotai", "Tailwind CSS",
            "Node.js", "Next.js (server/)", "Electron IPC",
            "Better SQLite3", "Drizzle ORM", "Supabase",
            "AI SDK", "OpenAI", "Anthropic", "Amazon Bedrock", "Google", "xAI", "MCP SDK", "Playwright",
            "Monaco", "Lexical", "Shiki",
            "Vitest", "Storybook", "Vite",
        ],
        "tags": ["Electron", "React", "TypeScript", "AI Automation", "Multi-Agent Systems", "Supabase", "Playwright", "Developer Platform"],
    },
    {
        "slug": "recova",
        "category": "규제 산업",
        "title": "Recova",
        "tagline": "AI 채권추심 보이스 에이전트와 컴플라이언스 운영 시스템을 결합한 NPL 특화 자동화 제품",
        "hero_sub": "NPL 3단계 부실채권 시장을 대상으로 설계한 AI 채권추심 보이스 에이전트이자 컴플라이언스 운영 시스템입니다. 추심 업무 자체를 자동화하고 규제 리스크를 운영 레이어에서 통제하는 데 초점을 맞췄습니다.",
        "meta": [
            ("개발 기간", "2026 초 ~ 현재"),
            ("법률 분석 자산", "5개 법률"),
            ("시장 검증 데이터", "2024년 8.3조원"),
        ],
        "overview": "범용 AICC처럼 고객 응대를 넓게 다루는 제품이 아니라 추심 업무에 특화된 자동화 제품입니다. 별도 리포지토리 없이 Obsidian 기반 문서 시스템으로 기획·리서치·법률 검토·영업 문서·미팅 로그를 축적하며 진행 중이고, 1호 클라이언트 협상과 2호 파이프라인 준비가 병행되고 있습니다.",
        "challenge": "채권추심 업무는 반복 콜 비중이 높지만, 통화 횟수 제한·야간 연락 제한·제3자 접촉 위험·금지 표현 통제·소멸시효 확인·고지의무 준수 같은 규제 조건 때문에 단순 콜 자동화만으로는 도입 검토가 어렵습니다. 특히 개인채무자보호법 시행 이후에는 추심 자동화보다 먼저 컴플라이언스 운영 체계를 증명해야 합니다. 더솔인처럼 20,000개 이상 채권 계정을 다루는 현장에서는 생산성 향상과 함께 감사 가능성·위반 예방·계약 구조 안전성까지 동시에 확보하는 것이 핵심 과제였습니다.",
        "solution": "아웃바운드 AI 보이스 엔진 위에 규제 통제 로직과 감사 체계를 결합한 구조로 설계했습니다. 실시간 통화 단계에서는 7일 rolling 카운터·야간 차단·제3자 안전 모드·금지표현 필터·소멸시효 체크·고지의무 검증을 적용하고, 통화 종료 후에는 STT 기반 감사 로그를 남겨 위반 탐지와 사후 점검이 가능하도록 했습니다. 동시에 제품 외곽에는 시장 구조·해외 벤치마크·법률 해석·비용 모델·계약 리스크를 문서 자산으로 축적했습니다.",
        "architecture": "코드 리포지토리보다 운영 설계 문서가 먼저 축적된 구조입니다. Obsidian 볼트 안에서 클라이언트 허브·팔로업 로그·미팅 기록·공용 리서치·IR·영업 문서를 분리해 제품 의사결정과 사업 개발을 같은 지식 시스템으로 관리했습니다. 제품 설계 관점에서는 `Cloud STT → 실시간 텍스트 변환 → 금지표현 탐지 → 컴플라이언스 엔진 → TTS → 아웃바운드 콜 → 통화 종료 후 STT 감사 저장` 흐름을 기준으로 음성 레이어와 규제 레이어를 분리했습니다.",
        "highlights": [
            "채권추심법·개인채무자보호법·신용정보법·개인정보보호법·인공지능기본법까지 5개 법률 분석을 완료하고 제품 요구사항으로 환원",
            "7일 7회 기준의 rolling 카운터와 야간 자동 차단 로직을 핵심 제어 장치로 설계",
            "가족·지인 등 제3자 접촉 상황을 분리 대응하는 안전 모드로 민감 구간을 별도 처리",
            "금지표현 필터·소멸시효 체크·AI 통화 고지의무 검증을 하나의 컴플라이언스 레이어로 묶은 사전 차단 구조",
            "모든 통화를 STT 기반 감사 대상으로 두고 사후 점검과 리포트 작성이 가능한 운영 흐름 설계",
            "TrueAccord·Credgenics·Skit.ai 등 글로벌 벤치마크와 국내 NPL 수치를 연결해 시장 진입 논리 정교화",
            "더솔인 계약 검토 과정에서 5개 독소조항 식별, 2호 파이프라인 준비로 협상 레버리지 확보",
        ],
        "metrics": [
            ("개발 기간", "2026년 초 ~ 현재"),
            ("법률 분석 자산", "5개 법률"),
            ("시장 검증 데이터", "2024년 8.3조원 NPL 시장"),
            ("고객 검증 상태", "더솔인 20,000+ 채권 계정 PoC 협상"),
            ("계약 리스크 식별", "5개 독소조항 식별·대응 원칙 정리"),
            ("영업 확장 상태", "2호 파이프라인 준비 완료"),
        ],
        "stack": [
            "Obsidian 사업 문서 시스템",
            "Rule-based state machine", "LLM 기반 대화 제어",
            "Cloud STT 후보 비교", "TTS 후보 비교",
            "7일 rolling 카운터", "야간 차단", "제3자 안전 모드", "금지표현 필터",
            "소멸시효 체크", "고지의무 검증",
            "STT 감사 로그", "영업 파이프라인 문서화",
        ],
        "tags": ["AI Voice Agent", "Compliance Systems", "NPL Operations", "Regulated Industry", "LLM Workflow", "Auditability", "B2B Automation"],
    },
    {
        "slug": "spec-web",
        "category": "운영형 웹",
        "title": "SPEC Web",
        "tagline": "비개발자 운영팀도 직접 관리할 수 있도록 설계한 실운영형 커뮤니티 플랫폼",
        "hero_sub": "외부 브랜딩 사이트와 내부 운영 도구를 하나의 제품으로 통합한 Next.js 기반 플랫폼입니다. 단순 소개 페이지가 아니라 관리자 대시보드·출석 관리·과제 운영·콘텐츠 발행·기록 축적 기능을 함께 다루는 운영 시스템입니다.",
        "meta": [
            ("개발 기간", "2026.02.08 ~ 2026.04.13"),
            ("개발 기간 기준 커밋", "478 commits"),
            ("운영 상태", "실제 운영 사용"),
        ],
        "overview": "웹사이트 제작을 넘어 운영 체계 자체를 제품 안에 내장한 사례입니다. 478 commits가 축적되었고 실제 운영에 사용되는 플랫폼으로 안정화되었습니다.",
        "challenge": "클라이언트가 필요로 한 것은 보기 좋은 웹사이트 하나가 아니었습니다. 외부 방문자에게는 신뢰도 있는 브랜드 경험이 필요했고, 내부 운영팀에게는 콘텐츠 수정·출석 체크·과제 관리·활동 기록 누적을 한곳에서 처리할 수 있는 관리 도구가 필요했습니다. 운영 주체가 바뀌더라도 개발자 의존 없이 페이지와 데이터를 관리할 수 있어야 했고, 흩어진 도구를 오가며 생기는 운영 비용도 줄여야 했습니다.",
        "solution": "Next.js 15 App Router 기반 구조 위에 퍼블릭 페이지와 관리자 기능을 함께 배치하고, Supabase를 통해 인증과 데이터 흐름을 일원화했습니다. 비개발자 관리자 대시보드를 별도 기능으로 두어 운영팀이 직접 콘텐츠를 수정하고 게시할 수 있게 했으며, BlockNote와 Tiptap을 결합해 문서형 콘텐츠 작성 경험도 강화했습니다. 출석 관리와 과제 관리를 같은 대시보드로 통합했고, Padlet 연동으로 외부 협업 흐름을 연결했으며, 스레드형 로그 시스템으로 활동 기록이 지속적으로 축적되도록 만들었습니다.",
        "architecture": "리포지토리는 `app/`·`components/`·`lib/`·`supabase/`·`middleware.ts`를 축으로 구성됩니다. `app/`은 퍼블릭 페이지와 로그인 이후 운영 화면을 포함하는 라우팅 레이어로, 외부 노출 영역과 내부 관리 영역을 단일 코드베이스 안에서 함께 다룹니다. `components/`는 대시보드 UI·편집기 인터페이스·공통 화면 요소를 모듈 단위로 분리해 재사용성을 높이고, `lib/`는 데이터 접근·유틸리티·도메인 로직 계층으로 작동합니다. `middleware.ts`는 접근 제어와 세션 기반 분기를 처리해 관리자 기능과 일반 사용자 흐름을 구분합니다.",
        "highlights": [
            "비개발자도 직접 페이지와 운영 데이터를 다룰 수 있는 관리자 대시보드 구축으로 개발 의존도 감소",
            "출석 관리와 과제 운영을 하나의 플랫폼으로 통합해 반복 운영 업무를 웹 안에서 일관되게 처리",
            "BlockNote·Tiptap 기반 편집 환경을 붙여 문서 작성과 게시 경험을 제품 내부로 끌어옴",
            "Padlet 연동으로 외부 협업 도구와 내부 운영 흐름이 끊기지 않도록 연결",
            "스레드형 로그 시스템으로 활동 기록과 과제 이력을 구조적으로 축적",
            "Playwright 기반 검증 체계 + Vercel 배포로 실제 운영 환경 반영 속도 향상",
        ],
        "metrics": [
            ("개발 기간", "2026-02-08 ~ 2026-04-13"),
            ("개발 기간 기준 커밋", "478 commits"),
            ("운영 상태", "실제 운영에 사용된 플랫폼"),
            ("핵심 운영 기능", "관리자 대시보드·출석·과제"),
            ("외부 연동", "Padlet"),
            ("기록 자산화", "스레드형 로그 시스템 구축"),
        ],
        "stack": [
            "Next.js 15", "TypeScript", "Tailwind CSS",
            "Next.js App Router", "Supabase", "middleware.ts",
            "BlockNote", "Tiptap",
            "Padlet 연동", "Playwright", "Vercel",
        ],
        "tags": ["Next.js", "TypeScript", "Supabase", "Admin Dashboard", "Content Systems", "Operations Platform", "App Router"],
    },
    {
        "slug": "founder-sprint",
        "category": "운영 자동화",
        "title": "Founder Sprint",
        "tagline": "배치 운영·스타트업 관리·팀 협업·진행 상황 추적을 하나의 웹으로 통합한 운영 자동화 시스템",
        "hero_sub": "엑셀러레이팅 프로그램 현장에서 반복적으로 발생하는 배치 관리·스타트업 정보 정리·팀 운영·주간 진행 추적·공지와 피드백 흐름을 제품 안에 통합한 실운영형 웹입니다.",
        "meta": [
            ("개발 기간", "2026.01.21 ~ 2026.04.10"),
            ("개발 기간 기준 커밋", "160 commits"),
            ("외주 성과", "₩500만"),
        ],
        "overview": "founder-sprint-workspace 기반으로 구축한 배치 운영 자동화 웹입니다. 외주 매출 500만원으로 연결된 실운영형 구축 사례이자, 운영 조직이 스프레드시트와 수작업을 줄이고 자체 프로세스를 웹 기반으로 옮긴 사례입니다.",
        "challenge": "배치 프로그램은 배치 수가 누적될수록 참여 스타트업·팀원·멘토·Q&A·과제·세션·이벤트·오피스아워 기록이 빠르게 늘어납니다. 기존처럼 문서와 스프레드시트 중심으로 운영하면 데이터가 분산되고, 담당자 변경 시 히스토리 추적이 어려워지며, 매주 반복되는 안내와 업데이트 업무가 누적됩니다. 필요한 것은 단순 소개 사이트가 아니라 배치 운영에 필요한 실무 흐름을 하나의 웹에서 관리할 수 있는 운영 시스템이었습니다.",
        "solution": "Next.js 기반 메인 운영 앱에 Prisma·Supabase·이메일 발송·캘린더 연동·예외 추적·E2E 검증 체계를 결합해 장기 운영 가능한 관리자형 웹을 구축했습니다. 프로그램 운영에 필요한 배치·사용자 권한·스타트업 활동·Q&A·과제 제출·오피스아워·세션·피드 기능을 하나의 제품 안에서 다룰 수 있게 구성했습니다. 워크스페이스에는 핵심 서비스가 들어간 `founder-sprint/`와 별도 프론트 자산을 위한 `outsome-react/`가 함께 배치되어 있어 운영 제품과 주변 웹 자산을 분리 관리할 수 있습니다.",
        "architecture": "워크스페이스는 `founder-sprint/`와 `outsome-react/`로 나뉘며, 실제 운영 기능은 `founder-sprint/`에 집중되어 있습니다. `founder-sprint/prisma`는 데이터 모델을 관리하고, `src/app`은 인증 영역과 대시보드 영역을 분리해 관리자·멘토·참여자 흐름을 화면 단에서 구분합니다. `src/actions`·`src/lib`·`src/components`·`src/types`는 서버 액션·인증·메일 유틸리티·공통 UI·타입을 분리해 유지보수를 쉽게 합니다. 루트의 `next.config.ts`에는 Sentry 연동과 운영 설정이, `playwright.config.ts`에는 E2E 검증 체계가 배치됩니다.",
        "highlights": [
            "배치·스타트업·팀·진행 상황 관리 기능을 하나의 웹 제품으로 통합",
            "Q&A·과제·세션·오피스아워·이벤트·커뮤니티 피드까지 프로그램 운영 핵심 흐름을 구조화",
            "Prisma 스키마와 Supabase 기반 데이터 계층으로 역할·배치·활동 이력을 일관되게 관리",
            "Nodemailer와 Google APIs로 초대와 일정 관련 운영 업무를 자동화",
            "next.config.ts·Sentry 설정으로 운영 환경 예외 추적 기반 마련",
            "playwright.config.ts·e2e/ 디렉터리로 실제 사용자 플로우 검증 체계 포함",
        ],
        "metrics": [
            ("개발 기간", "2026-01-21 ~ 2026-04-10"),
            ("개발 기간 기준 커밋", "160 commits"),
            ("워크스페이스 구조", "founder-sprint/ · outsome-react/"),
            ("운영 범위", "배치·스타트업·팀·진행 상황"),
            ("외주 성과", "₩500만"),
            ("운영 가치", "반복 운영 자동화 시스템"),
        ],
        "stack": [
            "Next.js", "React", "TypeScript", "Tailwind CSS",
            "Next.js App Router", "Server Actions",
            "Prisma", "PostgreSQL", "Supabase",
            "Nodemailer", "Google APIs",
            "Sentry", "Playwright",
        ],
        "tags": ["Next.js", "TypeScript", "Prisma", "Supabase", "Operations Platform", "Workflow Automation", "Playwright", "B2B SaaS"],
    },
    {
        "slug": "lawteam-tss",
        "category": "응답 자동화",
        "title": "LawTeam TSS",
        "tagline": "법률 상담 리드를 자동 수집하고 변호사별 답변까지 연결한 로톡 전용 멀티 에이전트 응답 시스템",
        "hero_sub": "더신사 법무법인을 위해 설계한 로톡 자동 답변 시스템입니다. 질문 수집·분류·수임확률 스코어링·변호사 배정·페르소나 기반 답변 생성·자동 게시까지 이어지는 파이프라인으로 구성했습니다.",
        "meta": [
            ("개발 기간", "2026.04.15"),
            ("개발 기간 기준 커밋", "12 commits"),
            ("페르소나 자산", "변호사 4인"),
        ],
        "overview": "짧은 구축 기간 안에 멀티 에이전트 설계·도메인 지식 구조화·크롤러 확장성까지 한 번에 정리한 프로젝트입니다. 법무법인별로 포크해 재사용할 수 있는 구조로 납품 확장성도 고려했습니다.",
        "challenge": "법무법인 입장에서는 로톡 질문이 곧 신규 상담 리드이지만, 모든 질문을 사람이 실시간으로 읽고 우선순위를 가려 답변하기는 어렵습니다. 질문 도메인도 형사·이혼·부동산·의료·군형사처럼 넓고, 같은 사안이라도 어느 변호사의 톤과 전문성이 더 적합한지 판단해야 합니다. 필요한 것은 단순 자동 댓글 도구가 아니라 리드 수집부터 수임 가능성 판단·담당 변호사 선택·페르소나 일관성 있는 답변 생성까지 연결되는 자동화 체계였습니다.",
        "solution": "로톡 질문 수집 → 분류 → 수임확률 스코어링 → 변호사 배정 → 페르소나 답변 생성 → 자동 게시의 전체 흐름을 하나의 파이프라인으로 설계했습니다. `personas/`에는 변호사 4인의 말투와 전문분야를 반영한 페르소나 자산을, `knowledge/`에는 더신사 도메인 지식과 프로필 데이터를, `skills/`에는 답변 생성 규칙을, `scripts/crawlers/`에는 수집 자동화를 배치했습니다. 이 구조 덕분에 법무법인별 포크와 신규 채널 확장이 수월합니다.",
        "architecture": "리포지토리는 `personas/`·`knowledge/`·`skills/`·`scripts/`·`docs/`를 축으로 분리한 구조입니다. `personas/`는 장휘일·남희수·김연주·정준현 변호사 4인의 페르소나 자산을, `knowledge/`는 더신사 법무법인 공용 지식과 변호사별 YAML 프로필을 저장합니다. `skills/`는 답변 생성 에이전트의 시스템 프롬프트를 담아 응답 품질 기준을 고정하고, `scripts/crawlers/`는 로톡 질문 수집과 네이버 지식인 확장 여지를 준비합니다. `docs/`는 계획·작업 분담·시스템 아키텍처 문서화로 납품형 프로젝트에서도 유지보수 인수인계가 가능하도록 설계했습니다.",
        "highlights": [
            "로톡 질문을 24시간 수집하고 후속 처리까지 연결하는 자동 응답 파이프라인 설계",
            "질문 분류 이후 수임확률 스코어링 단계로 모든 리드를 동일하게 처리하지 않도록 우선순위화",
            "변호사 4인 체계를 페르소나 자산으로 분리해 전문분야와 톤을 시스템 안에 반영",
            "knowledge/와 profiles/ 구조로 법무법인 도메인 지식과 변호사 속성을 재사용 가능한 자산으로 정리",
            "scripts/crawlers/lawtalk.py 중심 구조로 이후 채널 확장을 고려한 크롤러 계층 준비",
            "skills/write-answer.md와 검증 스크립트로 답변 생성 품질과 파일 구조 일관성 유지",
        ],
        "metrics": [
            ("개발 기간", "2026-04-15"),
            ("개발 기간 기준 커밋", "12 commits"),
            ("운영 대상", "더신사 법무법인 로톡"),
            ("핵심 파이프라인", "수집→분류→스코어링→배정→생성→게시"),
            ("페르소나 자산", "변호사 4인 체계"),
            ("납품 확장성", "법무법인별 포크 운영 가능"),
        ],
        "stack": [
            "Bun", "TypeScript",
            "personas/ · knowledge/profiles/",
            "skills/write-answer.md",
            "scripts/validate.ts", "scripts/crawlers/lawtalk.py",
            "docs/plan.md · docs/task.md · docs/sys_arch.md",
        ],
        "tags": ["Bun", "TypeScript", "Multi Agent Workflow", "Lead Qualification", "Persona Systems", "Crawler", "Legal Tech"],
    },
    {
        "slug": "wireframe-ai",
        "category": "프로토타이핑",
        "title": "Wireframe AI",
        "tagline": "자연어 설명만으로 와이어프레임과 프로토타입 초안을 생성하는 AI 프로토타이핑 시스템",
        "hero_sub": "제품 아이디어를 텍스트로 설명하면 즉시 화면 구조와 프로토타입 초안으로 전환해주는 생성형 UI 제작 도구입니다. 대화 기반 인터페이스만으로 빠르게 시안을 검토할 수 있도록 설계했습니다.",
        "meta": [
            ("개발 기간", "2024.07.10 ~ 2026.01.22"),
            ("개발 기간 기준 커밋", "289 commits"),
            ("수상", "디지털 광고대상 금상"),
        ],
        "overview": "단순 데모를 넘어 생성 파이프라인·샌드박스 실행·상태 저장·결제 시스템까지 포함한 서비스형 구조로 발전한 프로젝트입니다.",
        "challenge": "초기 제품 기획 단계에서는 아이디어를 시각 구조로 옮기는 속도가 의사결정 속도를 좌우합니다. 하지만 기존 방식은 기획 문서 작성·화면 러프 스케치·프로토타입 구성·검토 과정을 각각 다른 도구에서 수행해야 해서 전환 비용이 컸습니다. 클라이언트가 원한 것은 자연어 입력만으로 화면 초안을 빠르게 만들고, 여러 모델의 응답을 비교하면서 원하는 결과를 고도화할 수 있는 흐름이었습니다. 동시에 실제 서비스로 운영하려면 생성 실행 환경의 안정성·사용자 상태 관리·과금 처리까지 함께 풀어야 했습니다.",
        "solution": "자연어 입력을 받아 와이어프레임과 프로토타입 결과물로 이어지는 end to end 생성 흐름을 설계했습니다. Next.js 14 기반 UI 위에 Vercel AI SDK를 연결해 다중 LLM 지원 구조를 만들고, 사용자 요청에 따라 서로 다른 모델을 선택하거나 비교할 수 있게 했습니다. 생성된 산출물은 Excalidraw 기반 렌더링으로 바로 확인할 수 있으며, 더 복잡한 실행은 E2B SDK 기반 샌드박스 환경에서 안전하게 처리합니다. 데이터와 상태는 Supabase·Upstash·Vercel KV를 조합해 관리했고, Stripe를 연결해 유료 사용 시나리오까지 포함했습니다.",
        "architecture": "리포지토리는 `app/`·`components/`·`lib/`·`sandbox-templates/`·`source/` 중심으로 구성됩니다. `app/`은 채팅 기반 입력 화면·결과 미리보기·결제와 계정 관련 라우트를 포함하고, `components/`는 생성 결과를 시각적으로 제어하는 UI 모듈과 공통 인터랙션 컴포넌트를 담당합니다. `lib/`는 모델 호출·상태 처리·저장 계층·결제 연동 로직을 묶는 서비스 레이어 역할을 하며, `sandbox-templates/`는 샌드박스 안에서 실행될 템플릿 자산을 관리합니다.",
        "highlights": [
            "자연어 설명을 와이어프레임과 프로토타입 초안으로 연결하는 생성 흐름을 end to end로 구현",
            "Vercel AI SDK 기반 다중 LLM 지원 구조로 모델 선택 폭과 실험 유연성 확보",
            "Excalidraw 렌더링을 제품 UI와 직접 연결해 생성 결과 즉시 검토",
            "E2B SDK 기반 샌드박스 실행 환경으로 생성 결과의 실행 안정성과 격리 확보",
            "Supabase·Upstash·Vercel KV 조합으로 세션 상태와 캐시를 분리 관리",
            "Stripe 결제 시스템 통합으로 프로토타입 도구를 실제 과금 가능한 제품으로 확장",
        ],
        "metrics": [
            ("개발 기간", "2024-07-10 ~ 2026-01-22"),
            ("개발 기간 기준 커밋", "289 commits"),
            ("핵심 생성 흐름", "자연어 → 다중 LLM → 와이어프레임/프로토타입"),
            ("실행 환경", "E2B SDK 샌드박스"),
            ("상태 관리", "Supabase · Upstash · Vercel KV"),
            ("수익화 요소", "Stripe 결제 통합"),
        ],
        "stack": [
            "Next.js 14", "Tailwind CSS", "shadcn/ui", "Radix UI",
            "Vercel AI SDK", "다중 LLM 지원",
            "E2B SDK", "Excalidraw",
            "Supabase", "Upstash", "Vercel KV",
            "Stripe", "Vercel",
        ],
        "tags": ["Next.js", "Generative UI", "Multi-LLM", "Excalidraw", "E2B", "Supabase", "Stripe", "AI Prototyping"],
    },
    {
        "slug": "lyla",
        "category": "AI 어시스턴트",
        "title": "Lyla",
        "tagline": "채팅·규칙·메모리·루틴·푸시·전화까지 하나의 제품 경험으로 묶은 AI 개인 비서 시스템",
        "hero_sub": "사용자는 하나의 연속된 대화 경험으로 인식하지만, 내부적으로는 채팅·규칙 실행·메모리 관리·관계 단계 판단·루틴 추적·푸시 알림·전화 채널이 분리된 구조로 작동하는 AI 개인 비서 제품입니다.",
        "meta": [
            ("프론트 개발 기간", "2026.03.20 ~ 2026.04.20"),
            ("프론트 커밋", "177 commits"),
            ("통합 채널", "채팅·푸시·전화"),
        ],
        "overview": "프론트 제품 리포지토리와 Lyla-backend를 결합해 운영하는 AI 개인 비서 제품입니다. 프론트 177 commits, 백엔드 초기 서버 골격이 잡혀 있으며, 사용자의 하루 운영을 지속적으로 보조하는 멀티 채널 개인 비서 제품을 목표로 합니다.",
        "challenge": "개인 비서형 제품은 채팅만 자연스럽다고 끝나지 않습니다. 사용자가 기억·선호·루틴·관계 맥락을 기대하는 동시에, 실제로는 정해진 시각의 알림·조용한 시간대 통제·전화 기반 깨우기·작업 리마인드·반복 규칙 실행까지 안정적으로 돌아가야 합니다. 문제는 좋은 답변 생성 하나가 아니라 대화 경험과 운영 자동화를 같은 제품 안에서 신뢰성 있게 연결하는 일이었습니다. 특히 푸시와 전화처럼 사용자를 먼저 깨우는 채널은 감사 가능성과 명시적 제어가 함께 설계되어야 했습니다.",
        "solution": "사용자에게는 하나의 연속된 스레드처럼 보이지만, 시스템 내부에서는 에피소드 단위 대화 처리·규칙 기반 실행·구조화된 메모리·채널별 런타임을 조합하는 아키텍처로 설계했습니다. 프론트 리포지토리는 채팅 경험·제품 문서·프로토타입·성장 실험 자산을 함께 관리하고, 백엔드에서는 Express·TypeScript 기반 API·Supabase 저장소·OpenAI와 Anthropic 연동·node-cron 스케줄러·Zod 검증 계층을 운영합니다. 채팅·규칙·메모리·관계 단계·루틴·푸시·전화가 모두 동일한 사용자 상태를 공유하도록 설계해 채널 간 맥락이 일관되게 작동합니다.",
        "architecture": "프론트 리포지토리는 `architecture/`·`technical/`·`frontend/`·`backend/`·`scripts/`·`prototypes/`·`viral/`·`design/` 구조로 정리되어 제품 설계·구현 문서·실험 자산을 한곳에서 관리합니다. 백엔드는 `src/routes`·`src/services`·`src/db`·`src/jobs`·`src/lib`·`src/middleware`로 분리되어 있으며, 채팅 SSE 스트리밍·전화 라우트·푸시 테스트·캘린더와 스케줄 API를 각각 독립 계층으로 다룹니다. `services/`에는 LLM client·context composer·memory composer·memory extractor·relationship stage·tool executor·episode manager가 들어 있어 대화와 메모리 흐름을 서비스 레벨에서 분리합니다.",
        "highlights": [
            "채팅·규칙·메모리·관계 단계·루틴·푸시·전화 도메인을 하나의 제품 모델 안에서 통합",
            "사용자에게는 하나의 연속된 스레드처럼 보이도록 설계하면서 내부적으로는 에피소드·메모리·실행 로그 분리",
            "routes/와 services/ 계층 분리로 채팅 SSE·전화·규칙·메모리·프로필·캘린더·스케줄 기능을 독립 관리",
            "OpenAI와 Anthropic 이중 LLM 경로, 컨텍스트 조합과 메모리 추출 로직을 서비스 레이어로 정리",
            "node-cron 기반 스케줄러 + 조용한 시간대 필터로 루틴·리마인드·에스컬레이션·리뷰 흐름 자동화",
            "Expo Push Notification API와 전화 채널을 함께 다뤄 앱 안팎의 리마인드 경험을 하나로 연결",
        ],
        "metrics": [
            ("프론트 개발 기간", "2026-03-20 ~ 2026-04-20"),
            ("프론트 커밋", "177 commits"),
            ("백엔드", "Express · TypeScript · Supabase"),
            ("AI 이중 경로", "OpenAI · Anthropic"),
            ("통합 채널", "채팅·푸시·전화"),
            ("핵심 도메인", "규칙·메모리·관계·루틴·스케줄"),
        ],
        "stack": [
            "Lyla 프론트 제품", "Xcode iOS 앱 구조",
            "Express", "TypeScript",
            "Supabase", "PostgreSQL",
            "OpenAI", "Anthropic",
            "node-cron", "Expo Push Notification API",
            "Zod", "SSE 스트리밍",
        ],
        "tags": ["AI Assistant", "Express", "TypeScript", "Supabase", "Memory Systems", "Notification Architecture", "Voice Channel", "Multi Channel UX"],
    },
    {
        "slug": "nexus-acp",
        "category": "개발 도구",
        "title": "Nexus ACP",
        "tagline": "터미널 중심 AI 에이전트 개발 환경을 네이티브 GUI 워크스페이스로 전환한 개발 도구",
        "hero_sub": "Claude Code를 포함한 AI 에이전트 기반 개발 환경을 시각적 워크스페이스로 재구성한 Tauri 기반 개발 도구입니다. 세션 관리·코드 편집·프로토콜 연동·로컬 앱 배포·서버 데이터 계층까지 함께 다룹니다.",
        "meta": [
            ("개발 기간", "2025.06.19 ~ 2026.01.06"),
            ("개발 기간 기준 커밋", "400 commits"),
            ("앱 형태", "Tauri 네이티브"),
        ],
        "overview": "GUI 전환 도구이면서 동시에 네이티브 앱 구조와 데이터 운영 체계까지 정비한 고밀도 개발 프로젝트입니다.",
        "challenge": "AI 에이전트 개발 도구는 강력하지만 대부분 터미널과 텍스트 로그 중심으로 설계되어 있습니다. 이 방식은 숙련된 개발자에게는 효율적이지만, 세션 상태 추적·명령 결과 비교·파일 컨텍스트 확인·코드 수정 같은 작업을 한눈에 다루기 어렵게 만듭니다. 클라이언트가 필요로 한 것은 CLI의 강점을 버리지 않으면서도 Claude Code 같은 에이전트 환경을 GUI로 풀어내는 작업 공간이었습니다. 여기에 더해 장기 운영을 위해 로컬 앱 레이어와 서버 레이어를 분리하고, 기존 SQLite 중심 흐름을 PostgreSQL 기반 구조로 마이그레이션하는 과제도 함께 있었습니다.",
        "solution": "React·TypeScript·Vite 기반 프론트엔드에 Radix UI와 Tailwind를 결합해 세션 중심 인터페이스를 설계하고, Monaco를 붙여 코드 편집과 결과 확인을 같은 화면 안에서 처리할 수 있게 했습니다. 데스크톱 런타임은 Tauri로 구성해 웹 기술 스택의 생산성을 유지하면서도 네이티브 앱 형태로 배포할 수 있게 했고, ACP 연동 계층을 통해 AI 에이전트 상호작용을 GUI 안에서 다룰 수 있도록 설계했습니다. 서버 측에서는 PostgreSQL 기반 저장 구조를 정비하고 SQLite에서 PostgreSQL로의 마이그레이션 흐름을 정리했습니다.",
        "architecture": "리포지토리는 `src/`·`src-tauri/`·`server/`·`docs/`·`scripts/` 구조를 중심으로 나뉩니다. `src/`는 세션 뷰·작업 패널·코드 편집 인터페이스 같은 사용자 경험 레이어를 담당하고, `src-tauri/`는 네이티브 앱 패키징과 시스템 연동을 처리하는 런타임 계층입니다. `server/`는 ACP 기반 상호작용을 보조하는 서버 기능과 데이터 저장 계층을 담당하며, PostgreSQL 중심 구조로 마이그레이션된 백엔드 흐름을 담습니다.",
        "highlights": [
            "Claude Code를 포함한 AI 에이전트 개발 환경을 GUI 워크스페이스로 전환하는 제품 포지셔닝 구체화",
            "React·Radix UI·Monaco 조합으로 세션 탐색과 코드 편집을 한 화면 안에서 다룰 수 있게 설계",
            "Tauri 기반 네이티브 앱 구조로 웹 기술 생산성과 데스크톱 배포 경험을 함께 확보",
            "ACP 연동 계층으로 터미널 중심 프로토콜 상호작용을 시각적 인터페이스 안으로 끌어옴",
            "SQLite → PostgreSQL 마이그레이션으로 데이터 지속성과 장기 운영 기반 강화",
            "src/·src-tauri/·server/·docs/·scripts/ 레이어 분리로 개발 도구 구조를 명확히 유지",
        ],
        "metrics": [
            ("개발 기간", "2025-06-19 ~ 2026-01-06"),
            ("개발 기간 기준 커밋", "400 commits"),
            ("제품 포지셔닝", "AI 에이전트 GUI 전환 도구"),
            ("앱 형태", "Tauri 네이티브 앱"),
            ("핵심 편집 환경", "Monaco 통합"),
            ("데이터 전환", "SQLite → PostgreSQL"),
        ],
        "stack": [
            "React", "TypeScript", "Vite", "Tailwind CSS", "Radix UI",
            "Tauri",
            "Monaco", "ACP",
            "PostgreSQL",
            "Bun",
        ],
        "tags": ["Tauri", "React", "TypeScript", "ACP", "Monaco", "PostgreSQL", "Developer Tools", "Native App"],
    },
    {
        "slug": "treedi",
        "category": "AI UX 실험",
        "title": "TREEDI",
        "tagline": "질문 흐름을 선형 채팅에서 트리 구조 탐색으로 바꾼 AI 학습 인터페이스 실험",
        "hero_sub": "AI와의 대화를 단순 채팅 로그가 아니라 탐색 가능한 지식 구조로 바꾸기 위해 만든 트리 기반 학습 도구입니다. 컨텍스트 오염 문제를 구조적으로 해결하는 데 초점을 맞췄습니다.",
        "meta": [
            ("개발 기간", "2025.09.23 ~ 2025.10.24"),
            ("개발 기간 기준 커밋", "483 commits"),
            ("문제 공감", "20명 중 18명"),
        ],
        "overview": "React 기반 웹 애플리케이션과 Electron 위젯, Supabase 저장 구조, OpenAI 연동을 함께 실험한 제품입니다. 483개 커밋이 축적되었습니다.",
        "challenge": "AI를 학습 보조 도구로 쓰는 사용자는 한 답변을 읽는 순간 여러 갈래의 추가 질문이 생깁니다. 그러나 일반적인 채팅 인터페이스에서는 새 질문을 기존 맥락 위에 이어 붙여야 하므로 서로 다른 탐색 흐름이 한 대화에 뒤섞이며 컨텍스트 오염이 발생합니다. 이 문제는 답변 정확도뿐 아니라 사용자의 인지 부담으로도 이어집니다. 인터뷰 20명 중 18명이 이 문제에 공감했고, 100명 관찰 중 82명이 실제로 AI를 학습에 활용하고 있다는 점도 확인되었습니다.",
        "solution": "각 질문과 답변을 트리 노드로 취급하고, 하나의 응답에서 파생되는 여러 궁금증을 별도 브랜치로 분기할 수 있도록 설계했습니다. 한 주제를 깊게 파고드는 동시에 다른 방향의 탐구를 독립된 컨텍스트로 유지할 수 있습니다. 제품 경험은 웹 버전과 Electron 위젯 버전으로 병행 실험되었습니다. 웹에서는 트리 탐색과 콘텐츠 읽기 경험을 다듬고, Electron 위젯에서는 다른 작업 화면 위에서 단축키로 즉시 호출하는 사용 패턴을 검증했습니다. 기술적으로는 D3 기반 트리 시각화·OpenAI 연동·저장 구조·렌더링 레이어를 조합해 질문 생성·분기·복귀·재탐색이 하나의 흐름으로 이어지게 만들었습니다.",
        "architecture": "리포지토리는 `src/`·`electron/`·`server/`·`supabase/`·`api/`·`prompts/`를 중심으로 구성됩니다. `src/` 내부에는 `features/`·`domain/`·`infrastructure/`·`views/`·`components/`·`shared/`·`theme/`가 분리되어 있어 UI 레이어와 도메인 로직·공통 인프라를 한 파일에 몰아넣지 않고 역할별로 나눕니다. `electron/`은 메인 프로세스·프리로드·서비스·트레이·접근성 보조 기능을 담당하며 데스크톱 위젯 레이어를 구성합니다.",
        "highlights": [
            "D3 트리 시각화로 질문과 답변의 분기 구조를 화면에서 바로 탐색",
            "하나의 응답에서 여러 후속 질문을 독립 브랜치로 확장해 컨텍스트 오염 문제를 구조적으로 완화",
            "Electron 위젯 형태를 함께 실험해 다른 작업 중에도 단축키로 호출 가능한 사용 시나리오 검증",
            "웹 버전과 데스크톱 버전 병행 운영으로 학습 도구로서의 접근성과 몰입감 테스트",
            "Markdown·수식·코드 하이라이트 렌더링으로 설명형 학습 콘텐츠 소비 경험 강화",
            "빠른 프로토타이핑 이후 도메인·인프라·기능 단위로 구조를 나누며 유지보수 가능한 형태로 정리",
        ],
        "metrics": [
            ("개발 기간 기준 커밋", "483 commits"),
            ("핵심 문제 정의", "컨텍스트 오염 해결"),
            ("사용자 인터뷰", "20명 중 18명 공감"),
            ("사용 패턴 관찰", "100명 중 82명 AI 학습 활용"),
            ("핵심 인터페이스", "D3 트리 시각화"),
            ("확장 실험", "Electron 위젯 병행"),
        ],
        "stack": [
            "React 18", "JavaScript", "Tailwind CSS", "Framer Motion",
            "D3.js",
            "Electron",
            "Supabase",
            "OpenAI",
            "react-markdown", "KaTeX", "Shiki",
            "Playwright",
        ],
        "tags": ["React", "D3.js", "Electron", "AI UX", "Learning Tools", "Supabase", "Information Architecture", "Prototyping"],
    },
]

HEAD = """<!DOCTYPE html>
<html lang="ko-KR">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>{title} — SL:IT 포트폴리오</title>
<meta content="{desc}" name="description"/>
<link crossorigin="anonymous" href="https://cdn.prod.website-files.com/6893fd49c41afeab4a5ef473/css/letsur-n.webflow.shared.c3da34d10.css" rel="stylesheet" type="text/css"/>
<link href="/kr/assets/slit-shared.css" rel="stylesheet" type="text/css"/>
<link href="/Group%207.png" rel="shortcut icon"/>
<meta content="{title} — SL:IT 포트폴리오" property="og:title"/>
<meta content="{desc}" property="og:description"/>
</head>
<body class="body">
"""

NAV = """
<div class="navbar w-nav" data-animation="default" data-collapse="medium" data-duration="500" id="navbar" role="banner">
  <div class="nav-container w-container">
    <a class="brand w-nav-brand" href="/kr/"><img alt="SL:IT" class="brand-image" loading="lazy" src="/Group%207.png" style="width:128px;height:auto;object-fit:contain" width="128"/></a>
    <nav class="nav-menu w-nav-menu" role="navigation">
      <div class="nav-link-wrap">
        <a class="nav-1depth-link w-inline-block" href="/kr/services/"><div class="nav-menu-label">서비스</div></a>
        <a class="nav-1depth-link w-inline-block" href="/kr/process/"><div class="nav-menu-label">작업 방식</div></a>
        <a class="nav-1depth-link w-inline-block" href="/kr/portfolio/"><div class="nav-menu-label">포트폴리오</div></a>
        <a class="nav-1depth-link w-inline-block" href="/kr/insights/"><div class="nav-menu-label">인사이트</div></a>
        <a class="nav-1depth-link w-inline-block" href="mailto:slit.amazing@gmail.com"><div class="nav-menu-label">문의하기</div></a>
      </div>
    </nav>
    <div class="menu-button w-nav-button"><div class="menu-line-wrap"><div class="menu-line"></div><div class="menu-line"></div><div class="menu-line"></div></div></div>
  </div>
</div>
"""

FOOTER = """
<section class="section">
  <div class="w-layout-blockcontainer container w-container">
    <div class="cta-wrap">
      <div class="cta-header">
        <h2 class="cta-heading">비슷한 구조로 만들 프로젝트가 있나요?</h2>
        <a class="primary-button large w-inline-block" href="mailto:slit.amazing@gmail.com"><div>프로젝트 문의하기</div></a>
      </div>
    </div>
  </div>
</section>

<div class="section gray-10-bg footer space">
  <div class="nav-container w-container">
    <div class="footer">
      <div class="footer-top">
        <div class="footer-logo-wrap"><a class="brand w-nav-brand" href="/kr/"><img alt="" loading="lazy" src="/Group%207.png" style="width:128px;height:auto;object-fit:contain" width="128"/></a></div>
        <div class="footer-sitemap-wrap">
          <div class="footer-sitemap-item">
            <a class="sitemap-link" href="/kr/services/">서비스</a>
            <a class="sitemap-link" href="/kr/process/">작업 방식</a>
            <a class="sitemap-link" href="/kr/portfolio/">포트폴리오</a>
            <a class="sitemap-link" href="/kr/insights/">인사이트</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="footer-copyright-wrap">
          <div class="footer-sitemap-item-copy">
            <a class="sitemap-link" href="/kr/">홈</a>
            <div class="footer-devider"></div>
            <a class="sitemap-link" href="mailto:slit.amazing@gmail.com">이메일 문의</a>
          </div>
          <div class="footer-copyright-left-wrap-2">
            <div class="copryright-link">SL:IT</div>
            <div class="copryright-link">MVP · AI 서비스 · SaaS 개발 에이전시</div>
            <div class="footer-devider t-hidden"></div>
            <div class="copryright-link">문의: slit.amazing@gmail.com</div>
            <div class="footer-devider t-hidden"></div>
            <div class="copryright-link">© SL:IT. All Rights Reserved.</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=6893fd49c41afeab4a5ef473" type="text/javascript"></script>
<script src="https://cdn.prod.website-files.com/6893fd49c41afeab4a5ef473/js/webflow.7a9c4908.c57223fa47f28ecb.js" type="text/javascript"></script>
<script>
(function(){
  var btn = document.querySelector('.menu-button');
  var nav = document.getElementById('navbar');
  if (!btn || !nav) return;
  new MutationObserver(function(){
    nav.classList.toggle('nav-open', btn.classList.contains('w--open'));
  }).observe(btn, {attributes:true, attributeFilter:['class']});
})();
</script>
</body>
</html>
"""


def render(project):
    meta_cells = "".join(
        f'<div><div class="slit-detail-meta-label">{label}</div><div class="slit-detail-meta-value">{value}</div></div>'
        for label, value in project["meta"]
    )
    highlight_items = "".join(f"<li>{item}</li>" for item in project["highlights"])
    stack_items = "".join(f'<span class="slit-stack-item">{item}</span>' for item in project["stack"])
    metric_rows = "".join(
        f"<tr><th>{label}</th><td>{value}</td></tr>" for label, value in project["metrics"]
    )
    tags = " · ".join(project["tags"])

    desc = project["tagline"]

    body = f"""
<section class="slit-hero">
  <div class="w-layout-blockcontainer container w-container">
    <a class="slit-back" href="/kr/portfolio/">← 포트폴리오 전체</a>
    <div class="slit-hero-eyebrow">{project['category']}</div>
    <h1 class="slit-hero-title">{project['title']}</h1>
    <p class="slit-hero-sub">{project['hero_sub']}</p>
  </div>
</section>

<section class="section" style="padding-top:40px">
  <div class="w-layout-blockcontainer container w-container">
    <div class="slit-detail-meta">
      {meta_cells}
    </div>

    <div class="slit-prose">
      <h2>개요</h2>
      <p>{project['overview']}</p>

      <h2>클라이언트 과제</h2>
      <p>{project['challenge']}</p>

      <h2>솔루션</h2>
      <p>{project['solution']}</p>

      <h2>아키텍처</h2>
      <p>{project['architecture']}</p>

      <h2>핵심 구현 하이라이트</h2>
      <ul>
        {highlight_items}
      </ul>

      <h2>성과 지표</h2>
      <table>
        <tbody>
          {metric_rows}
        </tbody>
      </table>

      <h2>기술 스택</h2>
      <div class="slit-stack">
        {stack_items}
      </div>

      <h2>역량 태그</h2>
      <p style="font-size:14px;color:#555">{tags}</p>
    </div>
  </div>
</section>
"""
    return HEAD.format(title=project["title"], desc=desc) + NAV + body + FOOTER


def main():
    for project in PROJECTS:
        out_dir = BASE / project["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        html = render(project)
        (out_dir / "index.html").write_text(html, encoding="utf-8")
        print(f"wrote {out_dir/'index.html'}")


if __name__ == "__main__":
    main()
