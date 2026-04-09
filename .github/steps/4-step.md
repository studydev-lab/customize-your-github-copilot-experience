## 단계 4: 커스텀 에이전트 만들기

지시사항, 프롬프트, 템플릿이 함께 작동하게 되었으니, 커스터마이징을 한 단계 더 발전시키고 싶습니다. 새로운 과제를 브레인스토밍할 때, 구현보다는 순수하게 아이디어 발굴에 집중하는 전문화된 채팅 경험을 원합니다.

### 📖 이론: 커스텀 에이전트

커스텀 에이전트(`*.agent.md`)는 Copilot의 동작을 근본적으로 변경하여, 특정 도구와 응답 형식, 심지어 고유한 성격을 가진 전문화된 대화 경험을 만듭니다! Copilot Chat 인터페이스의 드롭다운 목록에서 선택할 수 있습니다.

Visual Studio Code는 `.github/agents/` 디렉토리에서 `*.agent.md` 파일을 검색합니다.

> [!TIP]
> 커스텀 에이전트에 대해 자세히 알아보기:
>
> - [VS Code 문서: 커스텀 에이전트](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
> - [GitHub 문서: 커스텀 에이전트 설정](https://docs.github.com/en/copilot/reference/custom-agents-configuration)


### ⌨️ 활동: 과제 브레인스토밍 커스텀 에이전트 만들기

이제 과제 아이디어 브레인스토밍을 위한 전문화된 커스텀 에이전트를 만들어 봅시다.

1. 다음과 같은 새 파일을 생성합니다:

   ```text
   .github/agents/assignment-brainstorming.agent.md
   ```

1. 다음 내용을 추가하여 집중된 브레인스토밍 경험을 만듭니다:

   ```markdown
   ---
   name: assignment-brainstorming
   description: Assignment brainstorming assistant
   tools: ["search", "web"]
   ---

   # 💡 Assignment Brainstorming Assistant

   **BRAINSTORM MODE ACTIVATED** 🚀

   I'm your assignment brainstorming partner for Mergington High School! I analyze your existing curriculum and suggest creative next assignments that build on what your students have already learned.

   ## My Response Style

   Every response follows this format:

   🔍 QUICK SCAN: [Brief analysis of existing assignments]
   💡 IDEA BURST: [3-5 rapid-fire suggestions]
   🎯 NEXT QUESTION: [What I need to know to help more]

   ## Rules

   - ⚡ Keep responses short
   - 🎯 Always end with a specific question
   - 💡 Focus on concepts, not details
   - 🚫 Never write assignment specs
   - 📊 Base ideas on existing curriculum gaps
   ```

### ⌨️ 활동: 브레인스토밍 커스텀 에이전트 테스트하기

1. VS Code에서 Copilot Chat을 엽니다.

1. 에이전트 드롭다운 목록에서 커스텀 에이전트를 선택합니다.

   <img width="379" height="218" alt="copilot 에이전트: 과제 브레인스토밍 에이전트 선택됨" src="https://github.com/user-attachments/assets/4effffa7-b8ef-4830-8050-9c777f9f0189" />

1. 교사가 할 수 있는 질문으로 커스텀 에이전트를 테스트합니다. 다른 응답 형식에 주목하세요!

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > What assignment topics are missing from my current curriculum?
   > ```

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Suggest 3 advanced Python assignments for my students.
   > ```

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > What would be a good follow-up assignment after the data analysis assignment?
   > ```

1. 후속 질문을 하여 커스텀 에이전트가 대화 전체에서 성격을 유지하는 방식을 확인합니다.

1. 새 커스텀 에이전트 파일을 커밋하고 푸시합니다: `.github/agents/assignment-brainstorming.agent.md`

1. Mona가 최종 리뷰를 줄 때까지 기다리세요!

<details>
<summary>문제가 있나요? 🤷</summary><br/>

- 커스텀 에이전트 파일이 `.github/agents/` 디렉토리에 `.agent.md` 확장자로 있는지 확인하세요.
- 커스텀 에이전트는 `@` 멘션이 아닌 채팅 인터페이스 하단의 드롭다운 목록에서 선택합니다.
- 커스텀 에이전트가 드롭다운에 나타나지 않으면, VS Code를 재시작하거나 창을 다시 로드하세요.

</details>
