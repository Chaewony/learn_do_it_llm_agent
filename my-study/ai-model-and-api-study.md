# AI 모델 및 API 활용 정보 찾아보기

## 📌 학습 내용

LLM을 공부하면서 여러 모델과 API를 직접 사용해 보고,
모델별 지원 기능과 가격, API 변경사항 등을 확인하기 위해 관련 정보를 찾아보았다.

### 1. OpenAI API 가격 확인

OpenAI API를 사용할 때 모델마다 입력/출력 토큰 가격이 다르기 때문에
모델을 선택하기 전에 가격 정보를 확인할 필요가 있다.

- [OpenAI API Pricing](https://developers.openai.com/api/docs/pricing)

가격 페이지에서 모델별 입력 및 출력 비용을 확인할 수 있다.

---

### 2. OpenAI API 변경사항 확인

OpenAI API를 공부하면서 기존 API 사용 방식과 현재 API 사용 방식이
어떻게 달라졌는지 확인했다.

특히 기존 Chat Completions API에서 Responses API로 변경되는 과정과
마이그레이션 방법을 확인했다.

- [Migrate to Responses](https://developers.openai.com/api/docs/guides/migrate-to-responses)

API를 사용할 때 단순히 예제 코드를 따라가는 것뿐만 아니라,
현재 공식 문서에서 권장하는 방식이 무엇인지 확인하는 것이 중요하다는 것을 알게 되었다.

---

### 3. Can I Run?

사용하려는 AI 모델을 현재 사용 중인 PC에서 실행할 수 있는지 확인하기 위해
`Can I Run?` 사이트를 찾아보았다.

- [Can I Run?](https://www.canirun.ai/)

모델을 직접 실행하기 전에 필요한 GPU나 VRAM 등의 하드웨어 조건을 확인하는 데 활용할 수 있다.

특히 로컬에서 LLM을 실행할 때는 모델의 크기뿐만 아니라
내 PC의 GPU와 VRAM이 해당 모델을 실행할 수 있는지도 확인해야 한다.

---

### 4. OpenAI 모델별 지원 기능 확인

OpenAI는 모델마다 지원하는 기능과 사용 가능한 API가 다르기 때문에
모델을 사용할 때 모델 페이지에서 지원 기능을 확인할 수 있다.

- [OpenAI Models](https://developers.openai.com/api/docs/models/all)

모델 페이지에서 해당 모델의 지원 기능과 API 관련 정보를 확인할 수 있다.

따라서 새로운 모델을 사용할 때는 단순히 모델 이름만 확인하는 것이 아니라
내가 사용하려는 기능을 해당 모델이 지원하는지도 확인해야 한다.

---

### 5. Ollama 모델 확인

Ollama에서 사용할 수 있는 다양한 로컬 모델을 확인하기 위해
Ollama Library를 찾아보았다.

- [Ollama Library](https://ollama.com/library)

Ollama Library에서는 다양한 모델을 확인할 수 있으며,
모델마다 크기와 특징 등이 다르기 때문에 로컬 환경에서 사용할 모델을 선택할 때 참고할 수 있다.

OpenAI처럼 API를 통해 모델을 사용하는 경우와 달리,
Ollama에서는 내 PC에서 직접 모델을 실행하기 때문에
PC의 하드웨어 사양과 모델 크기를 함께 고려해야 한다.

---

## 💡 정리

- AI 모델을 선택할 때는 **가격, 지원 기능, 실행 환경**을 함께 확인해야 한다.
- OpenAI는 공식 문서를 통해 **현재 권장되는 API 사용 방식**을 확인할 수 있다.
- 로컬 LLM은 모델 크기뿐만 아니라 **GPU와 VRAM 등의 하드웨어 조건**도 확인해야 한다.
- OpenAI와 Ollama 모두 모델마다 지원하는 기능과 특징이 다르므로 모델 페이지를 직접 확인하는 것이 좋다.
- AI를 공부하면서 새로운 모델이나 API를 사용할 때 **공식 문서를 직접 찾아보고 현재 사용 가능한 기능을 확인하는 습관**이 중요하다는 것을 알게 되었다.