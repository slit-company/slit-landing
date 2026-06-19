# Lyla

채팅, 규칙, 메모리, 루틴, 푸시, 전화까지 하나의 제품 경험으로 묶은 AI 개인 비서 시스템

## 개요

Lyla는 프론트 제품 리포지토리와 Lyla-backend를 결합해 운영하는 AI 개인 비서 제품이다. 사용자는 하나의 연속된 대화 경험으로 인식하지만, 내부적으로는 채팅, 규칙 실행, 메모리 관리, 관계 단계 판단, 루틴 추적, 푸시 알림, 전화 채널이 분리된 구조로 작동한다. 프론트 리포지토리 기준 개발 기간은 2026년 3월 20일부터 2026년 4월 20일까지이며, 백엔드는 2026년 3월 24일 기준 초기 서버 골격이 잡혀 있다. 이 프로젝트는 단순 챗봇이 아니라, 사용자의 하루 운영을 지속적으로 보조하는 멀티 채널 개인 비서 제품을 목표로 한다.

## 클라이언트 과제

개인 비서형 제품은 채팅만 자연스럽다고 끝나지 않는다. 사용자가 기억, 선호, 루틴, 관계 맥락을 기대하는 동시에, 실제로는 정해진 시각의 알림, 조용한 시간대 통제, 전화 기반 깨우기, 작업 리마인드, 반복 규칙 실행까지 안정적으로 돌아가야 한다. 즉 문제는 좋은 답변 생성 하나가 아니라, 대화 경험과 운영 자동화를 같은 제품 안에서 신뢰성 있게 연결하는 일이었다. 특히 푸시와 전화처럼 사용자를 먼저 깨우는 채널은 감사 가능성과 명시적 제어가 함께 설계돼야 했다.

## 솔루션

Lyla는 사용자에게는 하나의 연속된 스레드처럼 보이지만, 시스템 내부에서는 에피소드 단위 대화 처리, 규칙 기반 실행, 구조화된 메모리, 채널별 런타임을 조합하는 아키텍처로 설계했다. 프론트 리포지토리에서는 채팅 경험, 제품 문서, 프로토타입, 성장 실험 자산을 함께 관리하고, 백엔드에서는 Express와 TypeScript 기반 API, Supabase 저장소, OpenAI와 Anthropic 연동, node-cron 스케줄러, Zod 검증 계층을 운영한다. 도메인 관점에서는 채팅, 규칙, 메모리, 관계 단계, 루틴, 푸시, 전화가 모두 동일한 사용자 상태를 공유하도록 설계해, 한 채널에서 생성된 맥락이 다른 채널에서도 일관되게 작동하도록 만들었다.

## 기술 스택

| 영역 | 사용 기술 |
| --- | --- |
| Frontend | Lyla 프론트 제품 리포지토리, Xcode 기반 iOS 앱 구조 |
| Backend / Runtime | Express, TypeScript |
| Data | Supabase, PostgreSQL |
| AI | OpenAI, Anthropic |
| Automation / Scheduling | node-cron, Expo Push Notification API |
| Validation / Ops | Zod, SSE 스트리밍, 아키텍처 문서 체계 |

## 아키텍처

프론트 리포지토리는 `architecture/`, `technical/`, `frontend/`, `backend/`, `scripts/`, `prototypes/`, `viral/`, `design/` 구조로 정리되어 있어 제품 설계, 구현 문서, 실험 자산을 한곳에서 관리한다. 백엔드는 `src/routes`, `src/services`, `src/db`, `src/jobs`, `src/lib`, `src/middleware`로 분리되어 있으며, 채팅 SSE 스트리밍, 전화 라우트, 푸시 테스트, 캘린더와 스케줄 API를 각각 독립된 계층으로 다룬다. `services/`에는 LLM client, context composer, memory composer, memory extractor, relationship stage, tool executor, episode manager가 들어 있어 대화와 메모리 흐름을 서비스 레벨에서 분리하고, `db/queries`와 `jobs/`는 도메인 쿼리와 정기 실행 작업을 담당한다. 이 구조는 사용자에게는 하나의 비서처럼 보이지만, 내부적으로는 채팅, 규칙 실행, 메모리, 푸시, 전화가 서로 간섭하지 않도록 경계를 세운 아키텍처다.

## 핵심 구현 하이라이트

- 채팅, 규칙, 메모리, 관계 단계, 루틴, 푸시, 전화 도메인을 하나의 제품 모델 안에서 통합
- 사용자에게는 하나의 연속된 스레드처럼 보이도록 설계하면서 내부적으로는 에피소드, 메모리, 실행 로그를 분리
- `routes/`와 `services/` 계층을 분리해 채팅 SSE, 전화, 규칙, 메모리, 프로필, 캘린더, 스케줄 기능을 독립적으로 관리
- OpenAI와 Anthropic 이중 LLM 경로를 두고, 컨텍스트 조합과 메모리 추출 로직을 서비스 레이어로 정리
- node-cron 기반 스케줄러와 조용한 시간대 필터를 붙여 루틴, 리마인드, 에스컬레이션, 리뷰 흐름을 자동화
- Expo Push Notification API와 전화 채널을 함께 다뤄, 앱 안팎의 리마인드 경험을 하나의 제품으로 연결

## 성과 지표

| 지표 | 내용 |
| --- | --- |
| 프론트 개발 기간 | 2026-03-20 ~ 2026-04-20 |
| 백엔드 개발 기준 | 2026-03-24 |
| 백엔드 핵심 스택 | Express, TypeScript, Supabase, OpenAI, Anthropic, node-cron, Zod |
| 통합 채널 | 채팅, 푸시, 전화 |
| 핵심 도메인 | 규칙, 메모리, 관계 단계, 루틴, 스케줄, 프로필 |

## 역량 태그

`AI Assistant Product` `Express` `TypeScript` `Supabase` `Memory Systems` `Notification Architecture` `Voice Channel Design` `Multi Channel UX`
