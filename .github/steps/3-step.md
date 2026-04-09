## 단계 3: 재사용 가능한 프롬프트 구축하기

과제에 대한 지시사항을 수립했으니, 이제 새로운 과제 만들기를 간소화하고 싶습니다.

과제를 만드는 것은 반복적인 작업이며 여러 단계를 포함합니다 - 재사용 가능한 프롬프트에 완벽한 시나리오입니다!

- 과제 생성
- 새 과제를 로드하도록 웹사이트 설정 업데이트

### 📖 이론: 프롬프트 파일

프롬프트 파일(`*.prompt.md`)은 프로젝트에서 일반적이고 유용한 작업을 간소화하기 위한 재사용 가능한 프롬프트입니다. Copilot Chat에서 슬래시 명령(`/`)을 사용하여 선택할 수 있습니다.

프롬프트 파일 위치를 기준으로 마크다운 스타일 링크를 사용하여 다른 워크스페이스 파일, 프롬프트 파일, 또는 지시사항 파일을 참조할 수 있습니다.

Visual Studio Code는 기본적으로 `.github/prompts/` 디렉토리에서 `*.prompt.md` 파일을 [검색](vscode://settings/chat.promptFilesLocations)합니다.

> [!TIP]
> 반복 가능한 작업과 워크플로우를 정의하려면 프롬프트 파일을 사용하세요.
>
> 프롬프트를 작성할 때 **무엇**을 해야 하는지에 초점을 맞추세요. **어떻게**에 대해서는 지시사항을 참조할 수 있습니다.

자세한 내용은 [VS Code 문서: 프롬프트 파일](https://code.visualstudio.com/docs/copilot/copilot-customization#_prompt-files-experimental) 페이지를 참조하세요.

### ⌨️ 활동: 과제 프롬프트 만들기

이제 전체 과제 생성 프로세스를 자동화하는 재사용 가능한 프롬프트를 만들어 봅시다. 과제를 만드는 것은 매번 같은 패턴을 따르는 여러 반복적인 단계를 포함하므로 프롬프트 파일에 완벽한 사례입니다 - 자동화의 이점을 얻을 수 있는 정확한 종류의 워크플로우입니다.

1. 다음과 같은 새 파일을 생성합니다:

   ```text
   .github/prompts/new-assignment.prompt.md
   ```

1. 다음 내용을 추가하여 포괄적인 과제 생성 프롬프트를 만듭니다:

   ```markdown
   ---
   agent: agent
   description: Create a new programming homework assignment
   argument-hint: Provide assignment details
   ---

   # Create New Programming Assignment

   Your goal is to generate a new homework assignment for the Mergington High School students.

   ## Step 1: Gather Assignment Information

   If not already provided by the user, ask what the assignment will be about.

   ## Step 2: Create Assignment Structure

   1. Create a new directory in the `assignments` folder with a unique name based on the assignment topic
   1. Create a new file in the directory named `README.md` with the structure from the [assignment-template.md](../../templates/assignment-template.md) file
   1. Fill out the assignment details in the README file
   1. (Optional) Add starter code or attachments if the assignment needs them - add these files to the same assignment folder

   ## Step 3: Update Website Configuration

   Update the assignments list in [config.json](../../config.json) website configuration file to include the new assignment. For the dueDate field, use the current date plus 7 days unless specified otherwise.
   ```

### ⌨️ 활동: 과제 프롬프트 테스트하기

1. VS Code에서 Copilot Chat을 열고 `Agent` 모드인지 확인합니다.

1. 채팅 입력에 `/new-assignment`를 입력하여 프롬프트를 실행합니다. 2가지 방법이 있습니다:

   - 설명 없이 `/new-assignment`만 입력합니다. Copilot이 과제가 무엇에 관한 것인지 물어볼 것입니다.
   - 주제를 직접 포함합니다: `/new-assignment Building REST APIs with FastAPI framework`

      <details>
      <summary>💡 과제 주제 아이디어</summary>

      ```text
      Python Text Processing - working with strings, file I/O, and text manipulation
      ```

      ```text
      Data Structures in Python - lists, dictionaries, sets, and tuples
      ```

      ```text
      Python Data Visualization - using matplotlib or plotly for charts and graphs
      ```

      ```text
      Building REST APIs with FastAPI framework
      ```

      ```text
      Statistics with Python - data analysis and statistical calculations using pandas and numpy
      ```

      </details>

1. 웹사이트 미리보기의 과제 목록에 새 과제가 나타나는지 확인합니다.

   <details>
   <summary>과제가 보이지 않나요? 🔍</summary>

   다음 항목을 확인하세요:

   - 페이지를 새로고침합니다.
   - `assignments/`에 새 디렉토리가 생성되었습니다.
   - `config.json` 파일이 새 과제로 업데이트 되었습니다.

   </details>

1. 생성된 과제 내용이 수립된 규칙들과 일치하는지 검토합니다.

1. 변경 사항을 커밋하고 푸시합니다:

   - 새 프롬프트 파일: `.github/prompts/new-assignment.prompt.md`
   - 생성된 과제 디렉토리와 파일들.
   - 업데이트된 `config.json` 설정.

1. Mona가 다음 단계를 준비할 때까지 기다리세요!

<details>
<summary>문제가 있나요? 🤷</summary><br/>

- 프롬프트 파일이 `.github/prompts/` 디렉토리에 `.prompt.md` 확장자로 있는지 확인하세요.

</details>
