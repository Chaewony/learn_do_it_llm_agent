import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

with st.sidebar:
    openai_api_key = os.getenv("OPENAI_API_KEY")

    st.markdown(
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    )
    st.markdown(
        "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    )
    st.markdown(
        "[Open in GitHub Codespaces](https://codespaces.new/streamlit/llm-examples?quickstart=1)"
    )

st.title("💬 Chatbot")

# 스트림 릿에서 사용자의 세션 상태를 관리하는 기능
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

# 대화 기록을 웹 브라우저에 출력하는 기능
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 사용자 입력 받는 기능
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    st.chat_message("user").write(prompt)

    response = client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=st.session_state.messages
    )

    msg = response.choices[0].message.content

    st.session_state.messages.append(
        {"role": "assistant", "content": msg}
    )

    st.chat_message("assistant").write(msg)

# pip 설치 대신: uv add "streamlit==1.41.1" (uv로 프로젝트를 관리하고 있으니까)
# 실행: uv run streamlit run 03_streamlit_basic.py
