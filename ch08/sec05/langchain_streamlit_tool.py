import streamlit as st
import sys

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage

sys.path.append("..")
from langchain_tool_functions import tools, tool_dict

from dotenv import load_dotenv
load_dotenv()


# 모델 초기화
llm = ChatOpenAI(
    model="gpt-5.6-luna",
    use_responses_api=True,
)

# 도구 바인딩
llm_with_tools = llm.bind_tools(tools)


# 사용자의 메시지 처리하기 위한 함수
def get_ai_response(messages):
    response = llm_with_tools.stream(messages)

    gathered = None

    for chunk in response:
        # tool 호출을 위해 전체 chunk를 모음
        if gathered is None:
            gathered = chunk
        else:
            gathered += chunk

        # 실제 텍스트만 화면에 출력
        if chunk.text:
            yield chunk.text

    # 최종 응답의 텍스트만 문자열로 저장
    response_text = gathered.text

    # tool 호출이 있는 경우
    if gathered.tool_calls:
        # Responses API의 content 리스트를 그대로 저장하지 않음
        ai_message = AIMessage(
            content=response_text,
            tool_calls=gathered.tool_calls,
        )

        st.session_state.messages.append(ai_message)

        for tool_call in gathered.tool_calls:
            selected_tool = tool_dict[tool_call["name"]]

            tool_msg = selected_tool.invoke(tool_call)

            st.session_state.messages.append(tool_msg)

            # Tool 실행 결과를 바로 화면에 표시
            with st.expander("🔧 Tool 실행 결과"):
                st.write(tool_msg.content)

        # tool 실행 결과를 다시 모델에게 전달
        for chunk in get_ai_response(st.session_state.messages):
            yield chunk

    else:
        # 일반적인 AI 응답도 문자열만 저장
        st.session_state.messages.append(
            AIMessage(content=response_text)
        )


# Streamlit 앱
st.title("💬 Langchain Chat")


# 스트림릿 session_state에 메시지 저장
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        SystemMessage("너는 사용자를 돕기 위해 최선을 다하는 인공지능 봇."),
        AIMessage("How can I help you?")
    ]


# 스트림릿 화면에 메시지 출력
for msg in st.session_state.messages:
    if msg.content:
        if isinstance(msg, SystemMessage):
            st.chat_message("system").write(msg.content)
        elif isinstance(msg, AIMessage):
            st.chat_message("assistant").write(msg.content)
        elif isinstance(msg, HumanMessage):
            st.chat_message("user").write(msg.content)


# 사용자 입력 처리
if prompt := st.chat_input():
    st.chat_message("user").write(prompt)

    st.session_state.messages.append(HumanMessage(prompt))

    response = get_ai_response(st.session_state["messages"])

    st.chat_message("assistant").write_stream(response)