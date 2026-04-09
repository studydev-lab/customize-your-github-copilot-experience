## 단계 2: 파일별 지시사항

일반 프로젝트 지시사항이 준비되었으니, 과제에만 관련된 더 구체적인 서식 규칙이 필요하다는 것을 깨달았습니다. 저장소 전체 지시사항은 일반적인 코딩 표준에 잘 작동하지만, 모든 채팅 메시지에 포함되는 상세한 과제 구조 요구사항으로 그것들을 복잡하게 만들고 싶지 않습니다.

모든 과제가 같은 패턴과 구조를 따르도록 하여 학생들에게 일관된 경험을 제공하고 싶지만, 이러한 규칙은 과제 파일을 작업할 때만 적용되어야 합니다.

### 📖 이론: 커스텀 지시사항 파일

지시사항 파일(`*.instructions.md`)은 프로젝트의 특정 파일이나 디렉토리에 대한 맞춤형 가이드를 Copilot에 제공합니다.

모든 곳에 적용되는 저장소 전체 지시사항과 달리, 이 파일들은 [프론트매터](https://jekyllrb.com/docs/front-matter/)의 `applyTo` 필드에서 [글로브 구문](https://code.visualstudio.com/docs/editor/glob-patterns)을 사용하여 특정 파일을 대상으로 합니다. 이렇게 하면 해당 패턴과 일치하는 파일에서 작업할 때 지시사항이 자동으로 적용됩니다. 또는 Copilot Chat의 **Add Context** 버튼을 사용하여 수동으로 지시사항을 첨부할 수 있습니다.

Visual Studio Code는 기본적으로 `.github/instructions/` 디렉토리에서 `*.instructions.md` 파일을 [검색](vscode://settings/chat.instructionsFilesLocations)합니다.

> [!TIP]
> 지시사항은 작업이 **어떻게** 수행되어야 하는지에 초점을 맞춰야 합니다 - 코드베이스의 해당 부분에서 사용되는 가이드라인, 표준, 규칙을 설명합니다

자세한 내용은 [VS Code 문서: 커스텀 지시사항](https://code.visualstudio.com/docs/copilot/copilot-customization#_custom-instructions) 페이지를 참조하세요.

### ⌨️ 활동: 과제별 지시사항 만들기

이제 과제 파일이 일관된 구조와 서식을 따르도록 맞춤형 지시사항을 만들어 봅시다.

1. 먼저 기존 과제 템플릿을 살펴봅시다. `templates/assignment-template.md`를 열어 모든 과제가 따라야 할 구조를 확인합니다.

1. 다음과 같은 새 파일을 생성합니다:

   ```text
   .github/instructions/assignments.instructions.md
   ```


1. 다음 내용을 추가하여 과제 서식 표준을 정의합니다. `assignments` 디렉토리의 마크다운(`.md`) 파일에 대한 모든 채팅 요청에 자동으로 적용됩니다.

   ```markdown
   ---
   applyTo: "assignments/**/*.md"
   ---

   # Assignment Markdown Structure Guidelines

   All assignment markdown files should follow these guidelines:

   ## 1. Template Usage

   - Assignment markdown files must follow the structure in [`templates/assignment-template.md`](../../templates/assignment-template.md).
   - The assignment must be created as a `README.md` file
   - Do not remove or skip required sections from the template.

   ## 2. Section Guidance

   The section headers should reflect the structure in the template, including the exact icon usage.

   - **Title**: Replace `[Assignment Title]` with a short, descriptive name (e.g., `Python Basics`, `Loops and Conditionals`, `Functions and Modules`).
   - **Objective**: Write 1-2 sentences summarizing what the student will learn or accomplish. Focus on the main skills or concepts.
   - **Tasks**: For each task:
      - Use a specific, action-oriented task name
      - In the Description, clearly state what the student must do.
      - In Requirements, use bullet points to list the expected outcomes or features. Be specific and measurable
      - Provide example input/output in code blocks if helpful.

   Do not include extra sections unless explicitly specified.
   ```

### ⌨️ 활동: 과제 지시사항 테스트하기

1. VS Code에서 `assignments/games-in-python/README.md` 파일을 엽니다. 이 과제는 여러분이 교사로서 설정한 모든 규칙과 일치하지 않습니다.

1. 이 과제 파일의 현재 구조를 검토해 보세요. 이전에 살펴본 템플릿 구조와 어떻게 다른지 확인합니다. **Site Preview** 탭에서 현재 어떻게 보이는지도 확인할 수 있습니다.

1. 과제 파일을 열어둔 상태에서, `Agent` 모드의 Copilot에게 과제 구조를 업데이트해 달라고 요청합니다:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Update this assignment file to follow the project standards and template structure
   > ```

1. Copilot이 일반 프로젝트 지시사항과 과제별 지시사항 파일을 어떻게 참조하는지 관찰합니다.

   <img width="492" height="376" alt="Copilot 채팅에서 첨부된 참조를 보여주는 스크린샷" src="https://github.com/user-attachments/assets/dbf26be3-5940-4619-af4e-0a4380f16494" />

1. 제안된 변경 사항을 원본 파일 구조와 비교하여 Copilot이 지시사항을 어떻게 적용했는지 확인합니다. 제안된 변경 사항을 적용하고 업데이트된 과제가 **Site Preview**에서 어떻게 보이는지 확인합니다.

1. 두 파일 모두 `main` 브랜치에 커밋하고 변경 사항을 GitHub에 푸시합니다.

   - `.github/instructions/assignments.instructions.md`
   - `assignments/games-in-python/README.md`

1. Mona가 다음 단계를 준비할 때까지 기다리세요!

<details>
<summary>문제가 있나요? 🤷</summary><br/>

- 두 파일 모두 `main` 브랜치에 커밋했는지 확인하세요:
  - `.github/instructions/assignments.instructions.md`
  - `assignments/games-in-python/README.md`

</details>
