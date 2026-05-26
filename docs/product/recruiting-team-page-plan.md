# SL:IT Recruiting / Team Portfolio Page Plan

**Date:** 2026-05-25  
**Source repo:** `/Users/slit/opensource/slit-company-slit-landing`  
**Source content:** Google Drive `Recova/06_브랜드_콘텐츠/포트폴리오/SLIT_포트폴리오_웹사이트_콘텐츠.md` and section docs under `팀_포트폴리오_내용_확정용/`.

## 1. One-line intent

기존 SL:IT 랜딩페이지의 흑백·굵은 타이포·카드형 디자인을 유지하면서, 채용 후보자에게 “SL:IT은 Treedi → Anyon → Recova로 문제를 좁혀온 작은 AI-native 팀이고, 지금 합류하면 고객 미팅/IR/제품 설명에 바로 쓰이는 결과물을 함께 만든다”는 메시지를 전달하는 별도 팀 소개/채용 페이지를 만든다.

## 2. Target user / actor

- **Primary user:** 포트폴리오를 쌓고 싶은 디자이너, 브랜드/제품 설명/IR 장표를 함께 만들 수 있는 초기 합류 후보자.
- **Secondary user:** AI 제품을 실제 운영 흐름까지 보고 싶은 빌더, 프론트/프로덕트/오퍼레이션 성향의 초기 팀 후보자.
- **Internal operator:** 도현님/SL:IT 팀이 채용 제안, DM, 소개 링크로 공유.

## 3. Core positioning

기존 메인 랜딩은 고객/의뢰자 대상이다. 새 페이지는 채용 후보자 대상이다. 따라서 기존 메인의 “MVP·AI 서비스·SaaS 개발 에이전시” 메시지를 그대로 반복하지 않는다.

새 페이지의 중심 문장은 다음 쪽이 맞다.

> 레거시 산업에 AI를 넣는 작은 팀

보조 문장은 다음 방향으로 정리한다.

> SL:IT은 Treedi와 Anyon을 거치며 빠르게 만들고, 고객을 만나고, 틀린 가정을 좁혀왔다. 지금은 Recova를 중심으로 렌탈·구독 미수금 회수 업무의 AI voice follow-up workflow를 만들고 있다.

## 4. Route / navigation recommendation

Recommended route:

```txt
/kr/team/
```

Alternative routes:

```txt
/kr/join/
/kr/careers/
```

Recommendation: `/kr/team/` first. 이유는 현재 콘텐츠가 단순 구인 공고보다 “팀 포트폴리오 + 합류 설득”에 가깝기 때문이다. 이후 실제 포지션 공고가 생기면 `/kr/careers/`로 분리할 수 있다.

Navigation changes:

- 기존 상단 메뉴에 `팀` 또는 `팀 합류` 추가.
- 기존 `문의하기` CTA는 유지하되, 팀 페이지 내부 CTA는 `팀에 합류하기` 또는 `대화 시작하기`로 변경.

## 5. Page structure

### Section 1. Hero — 레거시 산업에 AI를 넣는 작은 팀

**Goal:** 첫 화면에서 고객용 랜딩이 아니라 채용/팀 소개 페이지임을 명확히 한다.

Copy direction:

```txt
레거시 산업에 AI를 넣는 작은 팀

SL:IT은 두 명이 움직이는 AI-native 팀입니다. Treedi와 Anyon을 거치며 빠르게 만들고, 고객을 만나고, 틀린 가정을 좁혀왔습니다.
지금은 Recova를 중심으로 렌탈·구독 미수금 회수 업무의 AI voice follow-up workflow를 만들고 있습니다.
```

CTA:

- Primary: `합류 대화 시작하기`
- Secondary: `팀 여정 보기`

Design:

- 기존 `/kr/` hero의 큰 한글 타이포 유지.
- 흰/베이지 톤 배경 + 검정 CTA.
- 우측 또는 하단에 추상 워크플로우 비주얼: `문자/결제링크 → AI 전화 → 납부 예정일/지연 사유 → 상담원 handoff → 기록`.

### Section 2. Team — 지금은 두 명이 움직입니다

**Goal:** 완성된 조직이 아니라, 작은 팀에서 큰 범위를 맡는다는 사실을 솔직하게 보여준다.

Copy source:

- `04_창업자와_팀.md`

Content:

- 전도현: CEO. 제품 방향, 고객 개발, 사업 전략, 실행 총괄.
- 한지상: CMO. 시장 메시지, 브랜드, 고객 커뮤니케이션, 성장/콘텐츠.
- 핵심 메시지: “지금 들어오는 사람은 완성된 시스템에 합류하는 게 아니라 시스템을 같이 만드는 자리에 들어온다.”

Design:

- 2-column role cards.
- 카드에는 얼굴 사진이 없어도 된다. 기존 사이트 디자인에 맞춰 이름/역할/책임영역 중심 카드가 더 안전하다.

### Section 3. Journey — Treedi → Anyon → Recova

**Goal:** 여러 프로젝트 나열이 아니라, 문제를 좁혀온 학습 곡선을 보여준다.

Copy source:

- `01_핵심_서사.md`
- `03_프로젝트_설명.md`

Cards:

1. **Treedi**  
   AI 대화가 길어질수록 문맥이 꼬이는 문제를 트리 구조로 풀려 한 첫 제품 실험. 제작 속도는 증명했지만, 고객이 돈을 내는 문제까지는 못 갔다는 학습.

2. **Anyon**  
   비개발자 창업가가 아이디어를 실제 제품으로 옮기는 과정을 줄이려 한 AI-native 제작 환경. AI보다 “고객 일이 줄어드는가”가 중요하다는 학습.

3. **Recova**  
   문자와 결제링크로 끝나지 않는 미수금 회수 건을 AI가 전화로 follow-up하는 workflow. 납부 예정일, 지연 사유, 상담 필요 여부, 금지 표현, handoff, 기록까지 같이 다루는 현재 초점.

Design:

- 기존 메인의 3단계 카드 구조 재사용.
- 1번 밝은 카드, 2번 회색 카드, 3번 검정 카드로 점점 선명해지는 흐름.
- Recova 카드는 가장 강하게 처리.

### Section 4. Proof — 빈손으로 시작하지 않았습니다

**Goal:** 스펙 자랑이 아니라, 팀이 실제로 움직이고 검증해온 증거를 보여준다.

Copy source:

- `02_증거와_타임라인.md`
- `SLIT_포트폴리오_웹사이트_콘텐츠.md` Proof section

Proof bullets/cards:

- 2025년 9월 SL:IT 결성 이후 Treedi, FAXI, Anyon, Recova로 이어지는 제품 실험.
- 경기 딥테크 대학 창업오디션 대상.
- 성균관대 5개국 연합 AI+X 글로벌 창업경진대회 대상.
- Founder Sprint 선발과 운영 시스템 개발 수주 경험.
- 한양대 캠퍼스타운, 아산 두어스, 성균관대 성창재 등 창업 프로그램/지원사업.
- SPEC 창업 커뮤니티 운영 경험.
- NPL사, 렌탈사, 대형 고객 미팅을 통한 B2B AI 구매 기준과 연동 장벽 학습.

Design:

- 현재 인사이트 카드와 유사한 3-column proof card grid.
- 각 카드 상단 작은 label: `Award`, `Program`, `Customer Learning`, `Community`, `Build`.
- 너무 많은 숫자/수상 나열보다 “이 경험들이 Recova로 수렴한다”는 문장으로 마무리.

### Section 5. Why Recova — 지금 가장 거친 업무로 내려왔습니다

**Goal:** 후보자가 “왜 하필 미수금/레거시/전화인가”를 이해하게 한다.

Copy source:

- `SLIT_포트폴리오_웹사이트_콘텐츠.md` Hero/Journey/Recova
- `02_증거와_타임라인.md` Recova section
- `05_합류_메시지.md` builder section

Core message:

```txt
좋은 데모는 몇 시간 안에도 만들 수 있습니다. 고객사가 맡길 수 있는 제품은 다릅니다.
발신 시간, 본인 확인, 제3자 응답, 금지 표현, 녹취, 상담원 handoff, 실패 로그, QA 기준이 같이 움직여야 합니다.
```

Design:

- 다크 섹션 추천.
- 중앙 큰 문장 + 아래 workflow diagram.
- Diagram nodes: `청구 이후 미해결 건` → `AI voice follow-up` → `납부 예정일/지연 사유 확인` → `위험 표현 차단` → `상담원 handoff` → `기록/QA`.

### Section 6. Design problem — 지금 필요한 일

**Goal:** 디자이너/빌더가 실제로 맡게 될 산출물을 명확히 보여준다.

Copy source:

- `SLIT_포트폴리오_웹사이트_콘텐츠.md` Why this is a design problem / What you will work on
- `05_합류_메시지.md`

Cards:

- Recova 1-pager: 렌탈사/NPL사 담당자가 내부 공유할 수 있는 자료.
- IR/지원사업 장표: 팀 스펙과 Recova 방향이 한 번에 읽히는 자료.
- Recova workflow diagram: 통화 전/중/후, 상담원 handoff, 기록 흐름.
- SL:IT 팀 포트폴리오: Treedi, Anyon, Recova가 흩어진 아이템처럼 보이지 않게 연결.
- B2B AI 브랜드 시스템: 화면, 문서, 음성 업무가 이어지는 서비스 구조.

Design:

- 기존 서비스 페이지의 capability cards 재사용.
- 각 카드에 `Output` 라벨을 붙여 포트폴리오 결과물이 명확히 보이게 한다.

### Section 7. Who fits / Who does not fit

**Goal:** 후보자를 넓게 끌어들이는 게 아니라, 맞는 사람과 안 맞는 사람을 선명하게 가른다.

Fits:

- 포트폴리오에 넣을 진짜 문제를 찾는 사람.
- 작은 팀에서 넓게 맡는 걸 좋아하는 사람.
- 장표, 문서, 제품 설명, 브랜드를 한꺼번에 잡아보고 싶은 사람.
- AI 제품을 예쁘게 포장하는 데서 멈추고 싶지 않은 사람.
- B2B, 운영툴, 세일즈 자료, IR 자료에 관심 있는 사람.
- 빠르게 만들고 바로 피드백 받는 환경을 좋아하는 사람.

Does not fit:

- 정해진 브리프만 받고 싶은 사람.
- 예쁜 비주얼만 만들고 싶은 사람.
- 고객 자료나 IR 장표를 디자인 일로 느끼지 않는 사람.
- 레거시 산업, 돈 문제, 규제 같은 단어가 지루하게 느껴지는 사람.
- 작은 팀의 불확실성을 견디기 어려운 사람.

Design:

- 2-column contrast block.
- Left: light card, `잘 맞는 사람`.
- Right: dark card, `안 맞는 사람`.

### Section 8. Close / CTA — 결과물이 바로 쓰입니다

**Goal:** 지원/대화 행동으로 닫는다.

Copy direction:

```txt
큰 회사 같은 안정성은 없습니다. 대신 결과물이 바로 쓰입니다.
합류하면 만든 자료가 고객 미팅에 들어가고, 장표가 지원사업과 IR에 들어가고, 제품 설명 구조가 Recova의 첫인상을 결정합니다.
```

CTA options:

- `합류 대화 시작하기`
- `slit.amazing@gmail.com으로 연락하기`
- Optional: `포트폴리오/작업물 보내기`

## 6. Visual design constraints

Keep from current landing:

- Black/white/gray mono palette.
- Large bold Korean headings.
- Existing nav/header/footer pattern.
- Wide section spacing.
- 3-card layouts.
- Dark section rhythm.
- Black CTA buttons.
- Minimal card labels and arrows.

Avoid:

- Startup recruiting page cliché: colorful gradients, stock team photos, casual emoji-heavy tone.
- Generic job-board sections before team story.
- Overloading the main customer landing with recruiting content.
- Claiming Recova as a fully mature/live product beyond verified current wording.

## 7. MVP scope

### Must-have

- New static page at `/kr/team/index.html`.
- Header/footer consistent with existing `/kr/` pages.
- Sections: Hero, Team, Journey, Proof, Why Recova, What you will work on, Who fits, CTA.
- Links from top nav or footer to `/kr/team/`.
- Email CTA to `slit.amazing@gmail.com`.
- Mobile responsive enough to match current static site behavior.

### Nice-to-have later

- Separate `/kr/careers/` route for actual open positions.
- Team photos or work-in-progress screenshots, if available.
- Downloadable/linked Recova 1-pager or deck once public-safe.
- English version.

### Explicit non-goals

- Do not redesign the whole landing page.
- Do not turn this into a generic 채용공고 page.
- Do not add an application form unless 도현님 explicitly wants it.
- Do not expose sensitive Recova customer names/details beyond already intended public copy.

## 8. Acceptance criteria

- A first-time candidate understands within 10 seconds that this is a small AI-native team working on Recova.
- The page explains why Treedi/Anyon/Recova are one learning journey, not random projects.
- The page makes the concrete work attractive: sales decks, IR slides, workflow diagrams, product explanation, B2B AI brand system.
- The page preserves current SL:IT visual language.
- The page has one clear contact action.

## 9. Open product decisions

1. CTA wording:
   - A. `합류 대화 시작하기`
   - B. `팀에 문의하기`
   - C. `포트폴리오 보내기`
   - Recommendation: A. 제일 덜 딱딱하고, 초기 팀 합류 맥락에 맞다.

2. Route name:
   - A. `/kr/team/`
   - B. `/kr/join/`
   - C. `/kr/careers/`
   - Recommendation: A now, C later.

3. Main nav label:
   - A. `팀`
   - B. `팀 합류`
   - C. `채용`
   - Recommendation: B if 적극 채용, A if 은근한 소개 페이지.

4. Page tone:
   - A. 격식 있는 회사소개체
   - B. 단단한 서사형 반말/구어체 느낌을 격식체로 정리
   - C. 완전 채용공고체
   - Recommendation: B. 원문 힘을 살리되 외부 웹페이지이므로 문장은 격식체로 정리.
