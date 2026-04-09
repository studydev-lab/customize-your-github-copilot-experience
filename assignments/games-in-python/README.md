
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

이 과제에서는 Python 문자열, 반복문, 조건문, 사용자 입력을 활용해 고전적인 Hangman 게임을 구현합니다.
학생은 게임 상태를 추적하고, 정답 여부에 따라 게임을 종료하는 로직을 완성하게 됩니다.

## 📝 Tasks

### 🛠️ Build Core Game Flow

#### Description
미리 정의된 단어 목록에서 임의의 단어를 선택하고, 플레이어가 한 글자씩 추측할 수 있는 기본 게임 흐름을 구현하세요.

#### Requirements
Completed program should:

- 단어 목록(리스트)을 코드에 포함하고 게임 시작 시 임의의 단어 1개를 선택해야 합니다.
- 사용자가 글자를 입력할 때마다 현재 단어 진행 상태를 `_ _ _` 형식으로 출력해야 합니다.
- 이미 입력한 글자를 다시 입력한 경우 이를 안내하고 게임 상태를 유지해야 합니다.


### 🛠️ Add Win/Lose Rules and Feedback

#### Description
오답 횟수를 관리하고, 정답을 모두 맞췄는지 또는 기회를 모두 소진했는지에 따라 게임을 종료하며 결과 메시지를 출력하세요.

#### Requirements
Completed program should:

- 남은 오답 가능 횟수를 숫자로 추적하고 매 턴마다 표시해야 합니다.
- 단어의 모든 글자를 맞추면 승리 메시지를 출력하고 게임을 종료해야 합니다.
- 오답 가능 횟수가 0이 되면 패배 메시지와 정답 단어를 출력하고 게임을 종료해야 합니다.
