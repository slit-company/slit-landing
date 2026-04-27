# Anyon

비개발자와 기업이 아이디어 구상부터 배포까지 한 흐름으로 실행할 수 있게 만든 AI 자동화 개발 플랫폼

## 개요

Anyon은 생성형 AI를 단순 코드 생성 도구가 아니라 실제 서비스 제작 파이프라인으로 확장한 데스크톱 기반 개발 플랫폼이다. 제품 기획, 템플릿 선택, 멀티 에이전트 개발, 외부 서비스 연동, 배포까지 이어지는 흐름을 하나의 제품 경험으로 묶는 데 초점을 맞췄다. 리포지토리 기준으로 2025년 4월 11일부터 2026년 2월 23일까지 1,155개의 커밋이 축적되었고, Electron 기반 앱, 웹 서버 계층, 워커, 템플릿, E2E 테스트, Supabase 연동을 모두 포함한 풀스택 제품으로 운영되었다.

## 클라이언트 과제

기존 AI 코딩 도구는 초안 생성에는 강했지만, 실제 서비스 완성 단계에서는 여러 단절이 있었다. 비개발자에게는 개발 환경 설치, 코드 구조 이해, 외부 API 연결, 배포 설정이 각각 별도의 장벽으로 남았고, 기업 입장에서는 프로토타입을 실제 운영 가능한 산출물로 끌어올리는 과정에서 품질 편차와 반복 비용이 커졌다. 특히 아이디어 검증 속도는 빨라졌지만, 코드 일관성 저하, 배포 오류, 사람 손으로 반복해야 하는 설정 작업이 누적되면서 생산성이 다시 떨어지는 문제가 있었다.

Anyon은 이 간극을 줄이기 위해 설계되었다. 인터뷰 기반으로는 사용자 56명과의 대화에서 설치, 배포, 외부 서비스 설정이 핵심 이탈 구간으로 반복 확인되었고, B2B 인터뷰 12곳 중 7곳에서는 프로젝트 문서 기준 PoC 검토 의향이 확인되었다. 즉, 과제는 단순히 코드를 더 빨리 만드는 것이 아니라, 비개발자와 실무 조직이 실제로 배포 가능한 결과물을 더 안정적으로 만들 수 있는 실행 환경을 만드는 일이었다.

## 솔루션

이 프로젝트에서는 Electron 기반 데스크톱 애플리케이션 위에 React와 TypeScript UI를 구축하고, 서버 계층과 워커 계층을 분리해 기획부터 실행까지 이어지는 end to end 자동화 흐름을 구성했다. 사용자는 앱 안에서 요구사항을 정리하고, 템플릿을 선택하고, 여러 모델 제공자를 연결한 AI 에이전트와 상호작용하며 구현을 진행할 수 있다. 이후 Playwright 자동화와 배포 흐름을 연결해 환경 설정과 검증, 결과 배포까지 한 제품 안에서 이어지도록 설계했다.

구조적으로는 단일 모델 호출 도구가 아니라 멀티 모델, 멀티 런타임, 멀티 채널을 조합한 작업 플랫폼에 가깝다. OpenAI, Anthropic, Bedrock, Google, xAI 계열 SDK와 MCP SDK를 함께 사용해 확장성을 확보했고, 로컬 SQLite와 Supabase를 병행해 데스크톱 앱의 즉시성과 클라우드 연동성을 동시에 챙겼다. 검증 과정에서 확인한 내부 운영 기준으로는 코드 일관성 지표가 34% 개선되었고, 에러율은 41% 낮아졌으며, 평균 배포 시간은 실측 기준 약 3분 수준까지 단축되었다. AI API 비용도 프로젝트 문서 기준 앱 1개당 평균 $13.28 수준으로 집계되었다.

## 기술 스택

| 영역 | 사용 기술 |
| --- | --- |
| Desktop / Frontend | Electron, React 19, TypeScript, TanStack Router, TanStack Query, Jotai, Tailwind CSS, Framer Motion |
| Backend / Runtime | Node.js, Next.js 기반 `server/`, Electron IPC, worker scripts |
| Data | Better SQLite3, Drizzle ORM, Supabase |
| AI / Automation | AI SDK, OpenAI, Anthropic, Amazon Bedrock, Google, xAI, MCP SDK, Playwright |
| Editor / Authoring | Monaco Editor, Lexical, React Markdown, Shiki |
| Testing / Tooling | Vitest, Playwright, Storybook, Vite |

## 아키텍처

리포지토리는 `src/`, `server/`, `worker/`, `workers/`, `templates/`, `scaffold/`, `e2e-tests/`, `supabase/`를 축으로 나뉜다. `src/`는 Electron 렌더러와 메인 프로세스를 함께 담는 핵심 애플리케이션 레이어로, `ipc/`, `app/`, `components/`, `db/`, `prompts/`, `supabase_admin/`, `vercel_admin/` 같은 폴더가 제품 기능과 인프라 연동을 분리한다. 데스크톱 앱 내부에서는 보안 경계를 둔 IPC 구조를 통해 UI와 시스템 권한을 분리하고, 사용자 상호작용과 실행 로직이 직접 뒤엉키지 않도록 설계했다.

`server/`는 별도 웹 계층과 서버 사이드 실행을 담당하고, `worker/` 및 `workers/`는 스크린샷, 서비스 워커, 프록시, 보조 실행 로직을 담당하는 비동기 처리 레이어로 동작한다. `templates/`와 여러 `scaffold-*` 디렉터리는 생성 결과의 시작점을 표준화하는 역할을 맡아, 사용자가 만드는 결과물의 구조 편차를 줄인다. `supabase/`는 클라우드 함수와 외부 연동을 관리하고, `e2e-tests/`는 실제 사용자 흐름을 기준으로 제품을 검증한다. 전체적으로는 데스크톱 UI, 서버 실행, 워커 자동화, 템플릿 자산, 배포 연동을 분리해 제품 고도화와 유지보수에 유리한 구조를 만든 아키텍처다.

## 핵심 구현 하이라이트

- Electron 기반 데스크톱 앱 안에 기획, 개발, 배포 흐름을 통합해 도구 전환 비용을 줄임
- 멀티 모델 SDK와 MCP SDK를 결합해 특정 모델 종속성을 낮추고 확장 가능한 AI 실행 계층 구성
- Monaco와 Lexical 기반 편집 환경을 붙여 코드 편집과 문서형 상호작용을 한 제품 안에서 처리
- Playwright 자동화를 활용해 외부 서비스 설정과 배포 전후 검증 흐름을 제품 경험으로 연결
- 템플릿과 스캐폴드 구조를 별도 계층으로 운영해 생성 결과의 품질 편차를 줄이고 재사용성 확보
- Vitest, Playwright, Storybook을 함께 사용해 UI, 로직, 사용자 흐름 검증 체계를 다층으로 구성

## 성과 지표

| 지표 | 내용 |
| --- | --- |
| 개발 기간 기준 커밋 | 1,155 commits |
| 누적 외주 매출 | ₩3,700만 |
| 사용자 검증 | 인터뷰 기반 56명 검증 |
| B2B 검증 | 인터뷰 기반 12곳 검토, 7곳 PoC 의향 확인 |
| 코드 품질 개선 | 내부 운영 기준 코드 일관성 +34%, 에러율 -41% |
| 운영 효율 | 실측 기준 평균 배포 약 3분 |
| 비용 효율 | 프로젝트 문서 기준 AI API 비용 평균 $13.28 |
| 대외 성과 | 수상 2건 |

## 역량 태그

`Electron` `React` `TypeScript` `AI Automation` `Multi-Agent Systems` `Supabase` `Playwright` `Developer Platform`
