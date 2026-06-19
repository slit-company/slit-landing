# Founder Sprint

배치 운영, 스타트업 관리, 팀 협업, 진행 상황 추적을 하나의 웹으로 통합한 운영 자동화 시스템

## 개요

Founder Sprint는 founder-sprint-workspace 기반으로 구축한 배치 운영 자동화 웹이다. 엑셀러레이팅 프로그램에서 반복적으로 발생하는 배치 관리, 스타트업 정보 정리, 팀 단위 운영, 주간 진행 상황 추적, 공지와 피드백 흐름을 제품 안에 통합하는 데 목적이 있었다. 리포지토리 기준 개발 기간은 2026년 1월 21일부터 2026년 4월 10일까지다. 이 프로젝트는 외주 매출 500만원으로 연결된 실운영형 구축 사례이자, 운영 조직이 스프레드시트와 수작업을 줄이고 자체 프로세스를 웹 기반으로 옮긴 사례다.

## 클라이언트 과제

배치 프로그램은 배치 수가 누적될수록 참여 스타트업, 팀원, 멘토, Q&A, 과제, 세션, 이벤트, 오피스아워 기록이 빠르게 늘어난다. 기존처럼 문서와 스프레드시트 중심으로 운영하면 데이터가 분산되고, 담당자 변경 시 히스토리 추적이 어려워지며, 매주 반복되는 안내와 업데이트 업무가 누적된다. 클라이언트가 필요로 한 것은 단순 소개 사이트가 아니라, 배치 운영에 필요한 실무 흐름을 하나의 웹에서 관리할 수 있는 운영 시스템이었다.

## 솔루션

이 프로젝트에서는 Next.js 기반 메인 운영 앱에 Prisma, Supabase, 이메일 발송, 캘린더 연동, 예외 추적, E2E 검증 체계를 결합해 장기 운영 가능한 관리자형 웹을 구축했다. 프로그램 운영에 필요한 배치, 사용자 권한, 스타트업 활동, 질문과 답변, 과제 제출, 오피스아워, 세션, 피드 기능을 하나의 제품 안에서 다룰 수 있게 구성했다. 워크스페이스에는 핵심 서비스가 들어간 `founder-sprint/`와 별도 프론트 자산을 위한 `outsome-react/`가 함께 배치되어 있어, 운영 제품과 주변 웹 자산을 분리 관리할 수 있다. 결과적으로 운영진은 배치와 팀, 진행 현황을 지속적으로 추적할 수 있고, 반복 업무는 자동화된 시스템 위에서 처리할 수 있게 됐다.

## 기술 스택

| 영역 | 사용 기술 |
| --- | --- |
| Frontend | Next.js, React, TypeScript, Tailwind CSS |
| Backend / Runtime | Next.js App Router, Server Actions |
| Data | Prisma, PostgreSQL, Supabase |
| Automation / Integration | Nodemailer, Google APIs |
| Observability / Testing | Sentry, Playwright |

## 아키텍처

워크스페이스는 `founder-sprint/`와 `outsome-react/`로 나뉘며, 실제 운영 기능은 `founder-sprint/`에 집중되어 있다. `founder-sprint/prisma`는 데이터 모델을 관리하고, `src/app`은 인증 영역과 대시보드 영역을 분리해 관리자, 멘토, 참여자 흐름을 화면 단에서 구분한다. `src/actions`, `src/lib`, `src/components`, `src/types`는 서버 액션, 인증 및 메일 유틸리티, 공통 UI, 타입 정의를 분리해 기능 확장과 유지보수를 쉽게 한다. 루트의 `next.config.ts`에는 Sentry 연동과 운영 설정이, `playwright.config.ts`에는 E2E 검증 체계가 배치되어 있어 배포와 테스트 흐름이 코드베이스 수준에서 함께 관리된다. `outsome-react/`는 별도 프론트 자산을 분리한 보조 레이어로, 운영 제품과 주변 웹 산출물을 섞지 않도록 구조를 정리한다.

## 핵심 구현 하이라이트

- 배치, 스타트업, 팀, 진행 상황 관리 기능을 하나의 웹 제품으로 통합
- 질문 답변, 과제, 세션, 오피스아워, 이벤트, 커뮤니티 피드까지 프로그램 운영 핵심 흐름을 구조화
- Prisma 스키마와 Supabase 기반 데이터 계층으로 역할, 배치, 활동 이력을 일관되게 관리
- Nodemailer와 Google APIs를 활용해 초대와 일정 관련 운영 업무를 자동화
- `next.config.ts`와 Sentry 설정으로 운영 환경 예외 추적 기반을 마련
- `playwright.config.ts`와 `e2e/` 디렉터리로 실제 사용자 플로우 검증 체계를 포함

## 성과 지표

| 지표 | 내용 |
| --- | --- |
| 개발 기간 | 2026-01-21 ~ 2026-04-10 |
| 워크스페이스 구조 | `founder-sprint/`, `outsome-react/`, `prisma`, `next.config.ts`, `playwright.config.ts` |
| 운영 범위 | 배치, 스타트업, 팀, 진행 상황 관리 웹 |
| 외주 성과 | 외주 매출 500만원 |
| 운영 가치 | 반복 운영 업무를 줄이는 운영 자동화 시스템 구축 |

## 역량 태그

`Next.js` `TypeScript` `Prisma` `Supabase` `Operations Platform` `Workflow Automation` `Playwright` `B2B SaaS Delivery`
