# GitHub Copilot 경험 커스터마이징

_커스텀 지시사항, 프롬프트, 커스텀 에이전트를 활용하여 GitHub Copilot의 동작을 특정 개발 워크플로우에 맞게 커스터마이징합니다._

## 환영합니다

- **대상**: 개발자 및 교육자로서 Copilot의 동작을 특정 워크플로우에 맞게 조정하고 싶은 분
- **배울 내용**: 커스텀 지시사항, 프롬프트, 커스텀 에이전트를 설정하여 특정 사용 사례에 맞게 Copilot을 더 효과적으로 만드는 방법
- **만들 것**: 프로젝트 표준에 따라 일관된 코드를 자동으로 생성하는 지시사항, 프롬프트, 커스텀 에이전트로 구성된 커스터마이즈된 Copilot 설정
- **사전 요구사항**: [GitHub Copilot 시작하기](https://github.com/skills-kr/getting-started-with-github-copilot) 실습
- **소요 시간**: 이 실습은 30분 이내에 완료할 수 있습니다.

이 실습에서 다음을 수행합니다:

1. 저장소 전체 커스텀 지시사항을 설정하여 Copilot에 필수 프로젝트 컨텍스트 제공
1. 특정 파일 유형 및 디렉토리에 대한 맞춤형 커스텀 지시사항 생성
1. 숙제 과제와 같은 일반적인 작업을 위한 재사용 가능한 프롬프트 템플릿 구축
1. 전문화된 워크플로우를 위한 커스텀 에이전트 구성

### 이 실습을 시작하는 방법

실습을 내 계정으로 복사한 뒤, Octocat(Mona)이 첫 번째 레슨을 준비할 때까지 **약 20초** 기다린 후 **페이지를 새로고침**하세요.

[![](https://img.shields.io/badge/실습%20복사-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/new?template_owner=skills-kr&template_name=customize-your-github-copilot-experience&owner=%40me&name=skills-customize-your-github-copilot-experience&description=실습:+GitHub+Copilot+경험+커스터마이징&visibility=public)

<details>
<summary>문제가 있나요? 🤷</summary><br/>

실습을 복사할 때 다음 설정을 권장합니다:

- 소유자(owner)는 개인 계정 또는 조직(organization)을 선택하세요.

- 비공개 저장소는 Actions 사용 시간이 소모되므로 공개 저장소를 만드는 것을 권장합니다.

20초 후에도 실습이 준비되지 않으면 [Actions](../../actions) 탭을 확인하세요.

- 작업이 실행 중인지 확인하세요. 때로는 조금 더 오래 걸릴 수 있습니다.

- 실패한 작업이 표시되면 이슈를 제출해 주세요. 버그를 발견하셨네요! 🐛

</details>

---

> **참고**: 이 실습은 [skills/customize-your-github-copilot-experience](https://github.com/skills/customize-your-github-copilot-experience)를 기반으로 한글화하고, [🏆 GitHub Skills Workshop Dashboard](https://github-skills.studydev.com)와 연계되어 있습니다.

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)
