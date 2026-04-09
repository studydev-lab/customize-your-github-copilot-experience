## 단계 1: Copilot 지시사항 설정하기

여러분은 Mergington 고등학교의 교사로서 학생들을 위한 숙제 과제와 코딩 연습을 만들고 있습니다. 이러한 과제를 공유하기 위한 정적 웹사이트를 운영하고 있으며, AI 어시스턴트가 일관된 코드 품질과 프로젝트 구조를 보장할 수 있도록 일반적인 표준을 수립하고 싶습니다.

Copilot 지시사항이 도움이 될 수 있다고 들었습니다!

<details>
<summary>웹사이트 스크린샷 📸</summary><br/>

첫 번째 활동에서 이 웹사이트를 실행하게 됩니다!

<img width="600" alt="숙제 웹사이트 스크린샷" src="https://github.com/user-attachments/assets/2383b6e9-64d5-4907-94b3-b67153efb008" />

</details>

### 📖 이론: 저장소 커스텀 지시사항이란?

저장소 커스텀 지시사항은 Copilot에 저장소별 가이드와 선호사항을 제공하여 프로젝트 컨텍스트와 표준을 이해하도록 돕습니다. `.github/copilot-instructions.md` 파일을 생성하면, Copilot의 제안이 프로젝트 규칙과 코딩 표준을 일관되게 따르도록 할 수 있습니다.

전체 지시사항 세트는 저장소에서 Copilot Chat에 제출하는 모든 요청에 자동으로 추가됩니다.

> [!TIP]
> 지시사항은 프로젝트의 "방법"에 초점을 맞춰 짧고 간결하게 유지하세요. 목적, 폴더 구조, 코딩 표준, 주요 도구, 예상 형식 등이 포함될 수 있습니다.

자세한 내용은 [GitHub 문서: 저장소 커스텀 지시사항](https://docs.github.com/en/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) 페이지를 참조하세요.

### ⌨️ 활동: 교육 웹사이트 프로젝트 탐색하기

커스텀 지시사항을 사용하기 전에, 먼저 개발 환경을 설정하고 프로젝트 구조를 탐색해 봅시다.

1. 아래 버튼을 마우스 오른쪽 클릭하여 새 탭에서 **Codespace 생성** 페이지를 엽니다. 기본 설정을 사용하세요.

   [![GitHub Codespaces에서 열기](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. **Repository** 필드가 원본이 아닌 여러분의 복사본인지 확인한 후, 녹색 **Create Codespace** 버튼을 클릭합니다.

   - ✅ 여러분의 복사본: `/{{full_repo_name}}`
   - ❌ 원본: `/skills/customize-your-github-copilot-experience`

1. Visual Studio Code가 브라우저에 로드되고 모든 확장이 설치될 때까지 잠시 기다립니다.

   - **Live Preview** 확장이 활성화되었는지 확인하세요.
   - **Python** 확장이 활성화되었는지 확인하세요.

1. `index.html`을 마우스 오른쪽 클릭하고 **Show Preview**를 선택하여 웹사이트가 작동하는 모습을 확인합니다.

   > ❕ **중요**: 실시간 업데이트를 보려면 미리보기 탭을 열어 두세요. 실습 전체에서 편집을 계속할 것입니다.

1. 프로젝트 구조를 탐색합니다:

   - `assets/` 폴더를 탐색하여 웹사이트 자산(CSS, JavaScript, 이미지)을 확인합니다.
   - `assignments/` 폴더를 살펴보고 기존 과제 형식을 이해합니다.
   - 루트 디렉토리의 `index.html`을 검토하여 메인 웹사이트 구조를 확인합니다.
   - 루트 디렉토리의 `config.json`을 검토하여 과제가 어떻게 설정되어 있는지 확인합니다.

### ⌨️ 활동: 저장소 Copilot 지시사항 생성하기

프로젝트를 탐색했으니, 이제 교육 웹사이트 프로젝트를 Copilot이 이해할 수 있도록 커스텀 지시사항을 만들어 봅시다.

1. VS Code에서 다음과 같은 새 파일을 생성합니다:

   ```text
   .github/copilot-instructions.md
   ``` 

   > ❕ **중요:** 파일 이름이 정확해야 합니다. Copilot이 인식하려면 이 특정 파일 이름이 필요합니다.

1. 다음 내용을 추가하여 Copilot이 프로젝트의 목적, 구조, 요구사항을 이해할 수 있도록 합니다:

   ```markdown
   # Project Description

   This project is an educational website for sharing homework assignments and coding exercises with students. Students can browse, view, and download assignments directly from the portal.

   ## Project Structure

   - [`assignments/`](../assignments/) Each homework assignment is stored in its own subfolder with a consistent structure.
   - [`templates/`](../templates/) Reusable templates for new content
   - [`assets/`](../assets/) Contains the website assets including CSS, JavaScript, images, and configuration files
   - [`index.html`](../index.html) The main website page that serves as a static portal for browsing and viewing assignments. Content is configurable via [`config.json`](../config.json) file to dynamically generate assignment lists and details.

   ## Project Guidelines

   - Maintain consistent styling across all pages
   - Keep file and folder names descriptive and organized

   ## Educational Standards

   When generating content for this project:

   - **Learning-focused**: All content should be designed with clear learning objectives and appropriate difficulty levels
   - **Student-friendly**: Use clear, encouraging language that motivates students
   ```

1. Copilot에게 프로젝트에 대해 질문하여 지시사항을 테스트합니다:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Briefly explain this project to me
   > ```

1. Copilot이 응답에서 커스텀 지시사항을 참조하는 것을 확인합니다.

   <img width="504" height="183" alt="image" src="https://github.com/user-attachments/assets/2214ed9e-c165-4440-a23e-d2d33c0231a9" />

1. `.github/copilot-instructions.md` 파일을 `main` 브랜치에 커밋하고 GitHub에 푸시합니다.

1. Mona가 다음 단계를 준비할 때까지 기다리세요!

<details>
<summary>문제가 있나요? 🤷</summary><br/>

- `.github/copilot-instructions.md` 파일은 `.github` 폴더의 루트에 있어야 합니다
- 변경 사항을 커밋하고 푸시했는지 확인하세요.

</details>
