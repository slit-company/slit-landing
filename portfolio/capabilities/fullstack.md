# 풀스택 웹 · 제품 개발

브랜드 사이트 하나를 만드는 수준이 아니라, 프론트엔드 경험, 백엔드 로직, 데이터 구조, 배포, 관리자 도구까지 하나의 제품으로 묶는 역량입니다. 비개발자 운영팀이 실제로 굴릴 수 있는 실운영형 웹과 SaaS 구조를 반복해서 만들어왔습니다.

## 역량 개요

SL:IT는 화면 제작과 서버 연결을 따로 보지 않습니다. SPEC Web에서는 외부 브랜딩 사이트와 내부 운영 도구를 하나의 Next.js 플랫폼으로 통합했고, Founder Sprint에서는 배치 운영 자동화 웹에 데이터 모델, 권한, 메일, 캘린더 연동, E2E 검증 체계를 붙였습니다. Anyon은 Electron 앱과 웹 서버 계층, 워커, 로컬 DB, 클라우드 연동을 아우르는 풀스택 제품이었고, Wireframe AI는 생성형 UI 서비스에 상태 저장, 샌드박스 실행, 결제 시스템까지 포함한 구조로 발전했습니다.

## 우리가 잘하는 문제 유형

- 외부 고객용 화면과 내부 관리자 화면을 하나의 코드베이스로 관리해야 하는 경우
- 비개발자 운영팀이 직접 콘텐츠와 데이터를 수정해야 하는 경우
- 초기 MVP를 넘어서 인증, 저장, 결제, 운영 로그까지 포함한 제품 구조가 필요한 경우
- 빠르게 만들되 이후 유지보수와 기능 확장을 고려한 레이어 분리가 필요한 경우
- 배포 이후 운영자가 계속 쓰게 될 관리자 도구나 CMS 성격의 기능이 필요한 경우

## 구현 방식

1. 퍼블릭 페이지와 운영 도구를 분리된 경험으로 설계하되, 인증과 데이터 흐름은 하나로 묶습니다.
2. 프론트엔드는 Next.js, React, Tailwind 중심으로 빠르게 만들고, 서버 액션이나 API 계층으로 운영 로직을 붙입니다.
3. 데이터는 Prisma, PostgreSQL, Supabase, SQLite 같은 저장 계층 중 프로젝트에 맞는 조합으로 설계합니다.
4. 관리자 화면, 편집기, 대시보드, 로그 같은 운영 기능을 제품 안에 내장해 개발자 의존도를 낮춥니다.
5. Playwright, Vercel, 예외 추적 도구를 연결해 배포와 검증까지 운영 가능한 상태로 마감합니다.

## 대표 프로젝트 레퍼런스

### SPEC Web

- Next.js 15 App Router와 Supabase를 기반으로 퍼블릭 사이트와 관리자 대시보드를 하나의 플랫폼으로 구성했습니다.
- 비개발자가 직접 콘텐츠를 수정하고 게시할 수 있는 관리 도구, 출석 관리, 과제 운영, 스레드형 로그 시스템을 구축했습니다.
- BlockNote와 Tiptap을 결합해 문서형 콘텐츠 편집 경험도 제품 내부에 넣었습니다.

### Founder Sprint

- 배치, 스타트업, 팀, Q&A, 과제, 세션, 오피스아워, 이벤트, 피드 관리 기능을 하나의 운영 웹으로 통합했습니다.
- Prisma, PostgreSQL, Supabase를 바탕으로 역할과 활동 이력을 일관되게 관리했고, Nodemailer와 Google APIs를 연동해 운영 업무를 자동화했습니다.
- Sentry와 Playwright 설정까지 포함해 실운영을 전제로 한 구조를 정리했습니다.

### Anyon

- Electron 데스크톱 앱, 서버 계층, 워커, 템플릿, Supabase 연동을 함께 운영하는 풀스택 제품을 구축했습니다.
- 로컬 SQLite와 Supabase를 병행해 데스크톱 앱의 즉시성과 클라우드 연동을 동시에 확보했습니다.
- `supabase_admin/`, `vercel_admin/` 같은 인프라 관리 계층을 별도로 두어 운영 기능을 제품에 직접 붙였습니다.

### Wireframe AI

- Next.js 14 기반 프론트엔드에 다중 LLM 생성 흐름, Excalidraw 렌더링, E2B 샌드박스 실행을 연결했습니다.
- Supabase, Upstash, Vercel KV를 조합해 상태와 캐시를 분리 관리했고, Stripe 결제를 붙여 서비스형 구조를 완성했습니다.

## 사용할 기술 예시

- React, Next.js, TypeScript, Tailwind CSS, shadcn/ui, Radix UI
- Node.js, Next.js App Router, Server Actions, Electron IPC
- Prisma, PostgreSQL, Supabase, SQLite, Drizzle ORM, Upstash, Vercel KV
- BlockNote, Tiptap, Monaco Editor, Lexical, Excalidraw
- Vercel, Sentry, Playwright, Vitest
- Stripe, Google APIs, Padlet 연동

## 클라이언트가 얻는 가치

- 소개용 사이트에서 끝나지 않고, 실제 운영에 필요한 관리자 기능까지 한 번에 확보할 수 있습니다.
- 프론트엔드와 백엔드, 데이터, 배포가 같은 설계 안에서 움직여 유지보수 비용이 낮아집니다.
- 비개발자 팀도 직접 운영 가능한 화면과 편집 도구를 확보할 수 있습니다.
- MVP 이후에도 확장 가능한 데이터 구조와 운영 레이어를 초기에 함께 가져갈 수 있습니다.
- 검증과 배포 체계까지 포함해 출시 이후의 시행착오를 줄일 수 있습니다.
