import streamlit as st

from langchain_openai import ChatOpenAI  # 오픈AI 모델을 사용하는 랭체인 챗봇 클래스
from langchain_core.chat_history import (
    BaseChatMessageHistory,  # 기본 대화 기록 클래스
    InMemoryChatMessageHistory,  # 메모리에 대화 기록을 저장하는 클래스
)
from langchain_core.runnables.history import RunnableWithMessageHistory  # 메시지 기록을 활용해 실행 가능한 wrapper 클래스
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from dotenv import load_dotenv
load_dotenv()

st.title("💬 Chatbot")


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        SystemMessage("너는 사용자의 질문에 친절히 답하는 AI챗봇이다.")
    ]


# 세션별 대화 기록을 저장할 딕셔너리 대신 session_state 사용
if "store" not in st.session_state:
    st.session_state["store"] = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in st.session_state["store"]:
        history = InMemoryChatMessageHistory()

        # 시스템 메시지를 실제 대화 기록에도 추가
        history.add_message(
            SystemMessage("너는 사용자의 질문에 친절히 답하는 AI챗봇이다.")
        )

        st.session_state["store"][session_id] = history

    return st.session_state["store"][session_id]


# 모델 초기화
llm = ChatOpenAI(
    model="gpt-5.6-luna",
    use_responses_api=True,
    output_version="responses/v1",
)


# 메시지 기록을 활용하는 Runnable wrapper
with_message_history = RunnableWithMessageHistory(
    llm,
    get_session_history,
)


config = {
    "configurable": {
        "session_id": "abc2"
    }
}


# 스트림릿 화면에 메시지 출력
for msg in st.session_state.messages:
    if isinstance(msg, SystemMessage):
        st.chat_message("system").write(msg.text)

    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.text)

    elif isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.text)


# 사용자 입력 처리
if prompt := st.chat_input():
    print("user:", prompt)

    # 사용자 메시지 화면에 출력
    st.chat_message("user").write(prompt)

    # 화면 표시용 메시지 저장
    st.session_state.messages.append(
        HumanMessage(prompt)
    )

    # LangChain Message History를 통해 모델 호출
    response = with_message_history.invoke(
        [HumanMessage(prompt)],
        config=config,
    )

    # Responses API에서 실제 텍스트만 가져옴
    msg = response.text

    # 화면 표시용 AI 메시지 저장
    st.session_state.messages.append(
        AIMessage(content=msg)
    )

    # AI 응답 출력
    st.chat_message("assistant").write(msg)

    print("assistant:", msg)