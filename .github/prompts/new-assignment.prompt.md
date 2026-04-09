---
agent: agent
description: 새 프로그래밍 숙제를 생성합니다
argument-hint: 과제 상세 정보를 입력하세요
---

# 새 프로그래밍 과제 만들기

목표는 Mergington High School 학생들을 위한 새로운 숙제 과제를 생성하는 것입니다.

## 1단계: 과제 정보 수집

사용자가 아직 제공하지 않았다면, 과제 주제가 무엇인지 질문하세요.

## 2단계: 과제 구조 생성

1. 과제 주제를 기반으로 고유한 이름을 사용해 `assignments` 폴더에 새 디렉터리를 만드세요.
1. 해당 디렉터리에 [assignment-template.md](../../templates/assignment-template.md) 구조를 따르는 `README.md` 파일을 만드세요.
1. README 파일에 과제 세부 내용을 채우세요.
1. (선택) 과제에 필요하면 스타터 코드나 첨부 파일을 추가하고, 같은 과제 폴더에 함께 저장하세요.

## 3단계: 웹사이트 설정 업데이트

[config.json](../../config.json) 웹사이트 설정 파일의 과제 목록을 업데이트해 새 과제를 포함하세요. `dueDate` 필드는 별도 지정이 없으면 현재 날짜 기준 7일 뒤 날짜를 사용하세요.