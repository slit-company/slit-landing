# 기술 스택

프로젝트 전반에서 반복적으로 사용한 기술만 추려, 어떤 문제를 어떤 스택으로 풀었는지 중심으로 정리했다. 빈도가 높은 핵심 스택부터 앞에 배치했고, 각 항목에는 실제 사용 프로젝트를 함께 적었다.

## Frontend

- **React**: 데스크톱 앱 UI부터 운영형 웹, 개발 도구 인터페이스까지 가장 반복적으로 사용한 기본 프레임워크. 사용 프로젝트: Anyon, TREEDI, Founder Sprint, Nexus ACP
- **Next.js**: 퍼블릭 사이트와 관리자 기능, 생성형 UI, 운영형 웹을 한 코드베이스로 묶을 때 주로 선택한 프레임워크. 사용 프로젝트: SPEC Web, Wireframe AI, Founder Sprint, Anyon
- **TypeScript**: 프론트와 서버를 같은 언어로 묶어 제품 복잡도가 커져도 구조를 유지하는 데 사용. 사용 프로젝트: Anyon, SPEC Web, Nexus ACP, Founder Sprint, Lyla, LawTeam TSS
- **Tailwind CSS**: 빠른 프로토타이핑과 운영 제품 UI를 모두 빠르게 정리할 때 반복 사용. 사용 프로젝트: Anyon, TREEDI, SPEC Web, Wireframe AI, Nexus ACP, Founder Sprint
- **Radix UI**: 생산성 높은 UI 조합과 접근성 기반 컴포넌트 구성이 필요할 때 사용. 사용 프로젝트: Wireframe AI, Nexus ACP

## Backend / Runtime

- **Node.js**: 웹 서버, 워커, 자동화 스크립트, 배포 흐름을 받치는 기본 런타임으로 사용. 사용 프로젝트: Anyon
- **Next.js App Router**: 프론트와 운영 로직, 서버 액션, 인증 흐름을 함께 다루는 풀스택 구조에 활용. 사용 프로젝트: SPEC Web, Founder Sprint
- **Express**: 채팅, 메모리, 규칙 실행, 전화 채널처럼 실시간 API와 멀티 채널 로직이 필요한 백엔드에 사용. 사용 프로젝트: Lyla
- **Electron**: 웹 기술 스택으로 데스크톱 앱과 위젯을 만들어 AI 제품 경험을 로컬 실행 환경까지 확장할 때 사용. 사용 프로젝트: Anyon, TREEDI
- **Tauri**: 네이티브 배포 효율과 웹 기술 생산성을 함께 가져가야 하는 데스크톱 개발 도구에 사용. 사용 프로젝트: Nexus ACP

## Database / Infra

- **Supabase**: 인증, 데이터 저장, 운영 기능을 한 번에 묶는 백엔드 베이스로 가장 자주 사용. 사용 프로젝트: Anyon, TREEDI, SPEC Web, Wireframe AI, Founder Sprint, Lyla
- **PostgreSQL**: 장기 운영형 서비스와 관리자 시스템, 데이터 마이그레이션이 필요한 구조에서 사용. 사용 프로젝트: Nexus ACP, Founder Sprint, Lyla
- **SQLite**: 로컬 앱의 즉시성과 경량 저장이 중요한 데스크톱 환경에서 사용. 사용 프로젝트: Anyon, Nexus ACP
- **Prisma**: 운영 데이터 모델을 명시적으로 관리하고 관리자형 웹의 변경 비용을 낮추기 위해 사용. 사용 프로젝트: Founder Sprint

## AI / LLM / Agent

- **OpenAI**: 가장 반복적으로 쓴 기본 LLM 계열. 학습 인터페이스, 개인 비서, 생성형 UI, 자동화 플랫폼 전반에 사용. 사용 프로젝트: Anyon, TREEDI, Lyla
- **Anthropic**: OpenAI와 함께 멀티 모델 전략을 구성하거나 개인 비서형 제품의 대체 경로를 확보할 때 사용. 사용 프로젝트: Anyon, Lyla
- **Amazon Bedrock**: 특정 모델 종속성을 줄이고 멀티 모델 확장성을 확보하기 위해 사용. 사용 프로젝트: Anyon
- **Google AI**: 멀티 모델 플랫폼에서 모델 공급자 선택 폭을 넓히기 위해 사용. 사용 프로젝트: Anyon
- **MCP SDK**: 외부 도구와 에이전트 실행 환경을 연결하는 프로토콜 계층으로 사용. 사용 프로젝트: Anyon
- **Vercel AI SDK**: 다중 LLM 선택과 생성형 UI 흐름을 빠르게 제품화하는 데 사용. 사용 프로젝트: Wireframe AI

## Automation / Integration

- **node-cron**: 루틴, 리마인드, 스케줄 작업처럼 시간 기반 자동 실행이 필요한 기능에 사용. 사용 프로젝트: Lyla
- **Stripe**: 생성형 프로토타이핑 서비스를 실제 과금 가능한 제품으로 연결할 때 사용. 사용 프로젝트: Wireframe AI
- **E2B**: 생성 결과를 안전한 샌드박스에서 실행하고 검증하는 환경으로 사용. 사용 프로젝트: Wireframe AI
- **Excalidraw**: 자연어로 만든 결과를 바로 와이어프레임과 프로토타입 형태로 보여주는 렌더링 계층으로 사용. 사용 프로젝트: Wireframe AI

## Testing / Quality

- **Playwright**: E2E 테스트뿐 아니라 외부 서비스 설정 자동화와 실제 사용자 흐름 검증까지 맡긴 핵심 도구. 사용 프로젝트: Anyon, TREEDI, SPEC Web, Founder Sprint
- **Storybook**: UI 단위 검토와 컴포넌트 품질 확인을 위한 기준 환경으로 사용. 사용 프로젝트: Anyon
- **Vitest**: 제품 로직과 UI 레이어를 빠르게 검증하는 테스트 러너로 사용. 사용 프로젝트: Anyon
- **Sentry**: 운영 중 예외를 추적하고 관리자형 웹의 장애 대응 속도를 높이기 위해 사용. 사용 프로젝트: Founder Sprint

## Deployment / Operations

- **Vercel**: Next.js 기반 서비스와 운영형 웹을 빠르게 배포하고 실서비스 반영 속도를 높이는 배포 플랫폼으로 사용. 사용 프로젝트: SPEC Web, Wireframe AI
