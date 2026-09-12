# Tool Calling 동작 과정과 LangChain 활용

## 📌 학습 내용

### 1. Tool Calling 동작 과정

LLM이 외부 데이터나 기능을 사용해야 할 경우, 직접 실행하는 것이 아니라 **호출할 Tool과 필요한 인자를 결정하고 Python이 실제 Tool을 실행**한다.

예를 들어 주가 조회는 다음과 같이 동작한다.

```txt
👤 사용자
   │
   │ "테슬라 한 달 전보다 올랐나?"
   ▼
🤖 LLM
   │ tool_call
   │ get_yf_stock_history
   │ ticker=TSLA, period=1mo
   ▼
🐍 Python
   │ Tool 실행
   ▼
📈 yfinance
   │ 주가 데이터 조회
   ▼
📦 ToolMessage
   │ 결과를 messages에 추가
   ▼
🤖 LLM
   │
   ▼
💬 최종 답변
```

### 2. `messages`의 흐름

Tool Calling 과정에서 `messages`에는 각 단계의 결과가 순서대로 저장된다.

```txt
messages

├─ HumanMessage   ← 사용자 질문
├─ AIMessage      ← Tool 호출 요청
│    └─ tool_calls
├─ ToolMessage    ← Tool 실행 결과
└─ AIMessage      ← 최종 답변
```

즉,

```txt
사용자 질문
   ↓
LLM의 Tool 호출 요청
   ↓
Python에서 Tool 실행
   ↓
Tool 결과
   ↓
LLM의 최종 답변
```

의 흐름으로 동작한다.

---

### 3. LangChain을 사용하면?

OpenAI API를 직접 사용할 때는 Tool의 이름, 설명, 매개변수 등을 포함한 **Tool 스키마를 직접 작성**해야 했다.

```txt
Python 함수
   ↓
Tool 스키마 직접 작성
   ↓
OpenAI API
```

LangChain에서는 `@tool`을 사용해 함수를 Tool로 만들고 `bind_tools()`를 통해 LLM에 연결할 수 있다.

```txt
@tool
def get_current_time(...):

   ↓

tools = [get_current_time]

   ↓

llm.bind_tools(tools)

   ↓

LLM
```

따라서 **Tool Calling의 기본 동작 자체가 달라지는 것이 아니라, Tool을 LLM에 연결하고 사용하는 과정이 간단해진다.**

---

## 💡 정리

* **Tool Calling**은 LLM이 필요한 Tool을 선택하고 호출을 요청하는 방식이다.
* 실제 Tool 실행은 Python이 담당하고, 결과는 `ToolMessage`로 다시 LLM에게 전달한다.
* `messages`에는 `HumanMessage → AIMessage → ToolMessage → AIMessage`가 순서대로 쌓인다.
* OpenAI API를 직접 사용할 때는 Tool 스키마를 직접 작성해야 한다.
* **LangChain에서는 `@tool`, `bind_tools()` 등을 이용해 이러한 연결 과정을 간단하게 만들 수 있다.**
