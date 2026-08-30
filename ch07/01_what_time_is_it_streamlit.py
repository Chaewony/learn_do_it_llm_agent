from gpt_functions import get_current_time, tools
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import streamlit as st


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")  # 환경 변수에서 API 키 가져오기

client = OpenAI(api_key=api_key)  # 오픈AI 클라이언트의 인스턴스 생성


def get_ai_response(messages, tools=None):
    response = client.chat.completions.create(
        model="gpt-5.6-luna",  # 응답 생성에 사용할 모델 지정
        messages=messages,  # 대화 기록을 입력으로 전달
        tools=tools,  # 사용 가능한 도구 목록 전달
        reasoning_effort="none",
    )
    return response  # 생성된 응답 내용 반환


st.title("💬 Chatbot")


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": "너는 사용자를 도와주는 상담사야.",
        },  # 초기 시스템 메시지
    ]


# 기존 대화 출력
for msg in st.session_state.messages:
    if msg["role"] in ["assistant", "user"] and msg.get("content"):
        st.chat_message(msg["role"]).write(msg["content"])


if user_input := st.chat_input():  # ① 사용자 입력 받기

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })  # ① 사용자 메시지를 대화 기록에 추가

    st.chat_message("user").write(user_input)  # ① 사용자 메시지를 브라우저에서도 출력


    # -------------------------
    # 첫 번째 GPT 응답
    # -------------------------

    ai_response = get_ai_response(
        st.session_state.messages,
        tools=tools
    )

    ai_message = ai_response.choices[0].message

    print(ai_message)  # ③ gpt에서 반환되는 값을 파악하기 위해 임시로 추가


    # -------------------------
    # Tool 호출 확인
    # -------------------------

    tool_calls = ai_message.tool_calls  # AI 응답에 포함된 tool_calls를 가져옵니다.

    if tool_calls:  # tool_calls가 있는 경우

        # tool_calls를 가진 assistant 메시지를 먼저 대화 기록에 추가
        st.session_state.messages.append(
            ai_message.model_dump(exclude_none=False)
        )

        for tool_call in tool_calls:

            tool_name = tool_call.function.name  # 실행해야한다고 판단한 함수명 받기

            tool_call_id = tool_call.id  # tool_call 아이디 받기

            arguments = json.loads(
                tool_call.function.arguments
            )  # 문자열을 딕셔너리로 변환


            if tool_name == "get_current_time":  # ⑤ 만약 tool_name이 "get_current_time"이라면

                st.session_state.messages.append({
                    "role": "tool",  # role을 "tool"으로 설정
                    "tool_call_id": tool_call_id,
                    "content": get_current_time(
                        timezone=arguments["timezone"]
                    ),  # 타임존 추가
                })


        # -------------------------
        # Tool 실행 결과를 바탕으로 다시 GPT 응답
        # -------------------------

        ai_response = get_ai_response(
            st.session_state.messages,
            tools=tools
        )

        ai_message = ai_response.choices[0].message


    # -------------------------
    # 최종 AI 응답 저장
    # -------------------------

    if ai_message.content:

        st.session_state.messages.append({
            "role": "assistant",
            "content": ai_message.content
        })  # ③ AI 응답을 대화 기록에 추가합니다.

        print("AI\t: " + ai_message.content)  # AI 응답 출력

        st.chat_message("assistant").write(
            ai_message.content
        )  # 브라우저에 메시지 출력