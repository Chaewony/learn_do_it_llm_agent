# 📚 Do it! LLM을 활용한 AI 에이전트 개발 입문

> **『Do it! LLM을 활용한 AI 에이전트 개발 입문』**을 따라가며
> LLM, OpenAI API, Tool Calling, LangChain, AI Agent 등을 학습하고 기록하는 저장소입니다.

단순히 책의 예제를 따라 구현하는 것에서 끝내지 않고,
**직접 궁금했던 내용을 추가로 공부하고 실험하면서 이해한 과정을 기록하는 것**을 목표로 합니다.

---

## 🎯 Study Goal

* LLM의 기본 개념과 API 활용 방법 이해
* LLM을 활용한 다양한 AI 애플리케이션 구현
* Function Calling을 통한 외부 도구 및 데이터 연동
* RAG와 인터넷 검색을 활용한 정보 기반 AI 시스템 구현
* LangChain과 LangGraph를 활용한 에이전트 및 멀티에이전트 시스템 이해
* 로컬 LLM과 임베딩 모델을 활용한 AI 시스템 구축

---

## 📖 Book

**Do it! LLM을 활용한 AI 에이전트 개발 입문**

책의 예제를 직접 구현하며 각 장에서 다루는 개념과 기술을 학습합니다.

### 📌 학습 진행 상황

### 📌 학습 진행 상황

|     Chapter    | 학습 내용                                 | Status |
| :------------: | ------------------------------------- | :----: |
| [Ch02](./ch02) | LLM / OpenAI API 기초                   |    ✅   |
| [Ch03](./ch03) | LLM 애플리케이션 개발                         |    ✅   |
| [Ch04](./ch04) | PDF 문서 전처리 / 텍스트 요약                   |    ✅   |
| [Ch05](./ch05) | 음성 인식 / 화자 분리                         |    ✅   |
| [Ch06](./ch06) | Vision 모델 / 이미지 분석 / TTS              |    ✅   |
| [Ch07](./ch07) | Function Calling / 주식 데이터 활용          |    ✅   |
| [Ch08](./ch08) | LangChain / LCEL / `@tool` / Pydantic |    ✅   |
|      Ch09      | RAG / 문서 기반 질의응답                      |    ⬜   |
|      Ch10      | 인터넷 검색 / 웹·YouTube 활용                 |    ⬜   |
|      Ch11      | 로컬 LLM / DeepSeek / RAG               |    ⬜   |
|      Ch12      | LangGraph / 상태 관리 / 메모리               |    ⬜   |
|      Ch13      | LangGraph 기반 RAG / 멀티에이전트             |    ⬜   |
|      Ch14      | LangGraph 기반 멀티에이전트                   |    ⬜   |
|      Ch15      | 자율적으로 작업하는 멀티에이전트                     |    ⬜   |
|      Ch16      | 로컬 LLM / 임베딩 모델 / AI 서비스 발전           |    ⬜   |



> Status
> ✅ 완료 · 🔄 진행 중 · ⬜ 예정

---

## 🗂️ Repository Structure

```text
learn_do_it_llm_agent/
│
├── ch02/                  # Chapter 02 실습
├── ch03/                  # Chapter 03 실습
├── ...
│
├── my-study/              # 💡 책 내용과 연관하여 공부한 내용
│
├── experiments/           # 🧪 직접 실험하고 확인한 내용
│
└── README.md
```

---

# 💡 My Study

책의 내용을 그대로 따라 하는 것에서 끝내지 않고,
**"왜 이렇게 동작하지?"**, **"이건 어떻게 되는 거지?"** 라는 질문에서 시작한 추가 학습 내용을 정리합니다.

### 📚 Topics
* [UV를 활용한 Python 환경 구성](./my-study/uv-python-environment.md)
* [Hugging Face와 로컬 AI 실행 환경](./my-study/hugging-face.md)
* [AI 모델 및 API 활용 정보 찾아보기](./my-study/ai-model-and-api-study.md)
* [Tool Calling 동작 과정과 LangChain 활용](./my-study/tool-calling-and-langchain.md)

> 학습하면서 새로운 주제가 생길 때마다 추가할 예정입니다.

---

# 🧪 TODO: Experiments

책의 예제를 그대로 사용하는 것이 아니라
**코드를 직접 변경하거나 조건을 바꿔보면서 동작을 확인한 실험**을 기록할 예정입니다.

### Example

```text
Question
   ↓
직접 가설 세우기
   ↓
코드 수정
   ↓
실행 결과 확인
   ↓
원인 분석
   ↓
Conclusion
```

### 🔬 Experiments

| Experiment    | 내용                 | Status |
| ------------- | ------------------ | :----: |
| Experiment 01 | Tool Calling 동작 확인 |    ⬜   |
| Experiment 02 | 여러 Tool 호출 과정 확인   |    ⬜   |
| Experiment 03 | API 방식에 따른 차이 확인   |    ⬜   |

> Status
> ✅ 완료 · 🔄 진행 중 · ⬜ 예정

---

# 📌 Learning Philosophy

> **따라 하는 것보다, 왜 그런지 이해하는 것을 목표로 합니다.**

책의 코드를 그대로 구현하는 것은 학습의 시작입니다.

그 이후

**"왜?" → "직접 확인" → "실험" → "정리"**

의 과정을 거쳐서 단순한 예제 코드를
**내가 설명할 수 있는 코드로 만드는 것**을 목표로 합니다.

---

## 📚 Reference

* 『Do it! LLM을 활용한 AI 에이전트 개발 입문』
* [원저작자 예제 Repository](https://github.com/saintdragon2/gpt_agent_2025_easyspub)

---
