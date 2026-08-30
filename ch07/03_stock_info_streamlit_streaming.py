from gpt_functions import get_current_time, tools, get_yf_stock_info, get_yf_stock_history, get_yf_stock_recommendations
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import streamlit as st
from collections import defaultdict

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")  # 환경 변수에서 API 키 가져오기

client = OpenAI(api_key=api_key)  # 오픈AI 클라이언트의 인스턴스 생성


# -------------------------
# Tool Call 변환 함수
# -------------------------

def tool_list_to_tool_obj(tools):
    # 기본 값을 가진 딕셔너리 초기화
    tool_calls_dict = defaultdict(
        lambda: {
            "id": None,
            "function": {
                "arguments": "",
                "name": None
            },
            "type": "function"
        }
    )

    # 도구(함수) 호출을 반복하여 처리
    for tool_call in tools:

        # id가 None이 아닌 경우 설정
        if tool_call.id is not None:
            tool_calls_dict[tool_call.index]["id"] = tool_call.id

        # 함수 이름이 None이 아닌 경우 설정
        if tool_call.function.name is not None:
            tool_calls_dict[tool_call.index]["function"]["name"] = (
                tool_call.function.name
            )

        # 인수 추가
        if tool_call.function.arguments:
            tool_calls_dict[tool_call.index]["function"]["arguments"] += (
                tool_call.function.arguments
            )

        # 타입이 None이 아닌 경우 설정
        if tool_call.type is not None:
            tool_calls_dict[tool_call.index]["type"] = tool_call.type

    # 딕셔너리를 리스트로 변환
    tool_calls_list = list(tool_calls_dict.values())

    return {"tool_calls": tool_calls_list}


# -------------------------
# GPT 응답 함수
# -------------------------

def get_ai_response(messages, tools=None, stream=True):
    response = client.chat.completions.create(
        model="gpt-5.6-luna",  # 응답 생성에 사용할 모델을 지정합니다.
        stream=stream,  # (1) 스트리밍 출력을 위해 설정
        messages=messages,  # 대화 기록을 입력으로 전달합니다.
        tools=tools,  # 사용 가능한 도구 목록을 전달합니다.
        reasoning_effort="none",  # tool 사용 시 reasoning 비활성화
    )

    if stream:
        for chunk in response:
            yield chunk  # 생성된 응답의 내용을 yield로 순차적으로 반환합니다.
    else:
        return response


# -------------------------
# Streamlit 화면
# -------------------------

st.title("💬 Chatbot")


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": "너는 사용자를 도와주는 상담사야."
        },  # 초기 시스템 메시지
    ]


# -------------------------
# 기존 대화 출력
# -------------------------

for msg in st.session_state.messages:

    if msg["role"] in ["assistant", "user"] and msg.get("content"):
        st.chat_message(msg["role"]).write(msg["content"])


# -------------------------
# 사용자 입력
# -------------------------

if user_input := st.chat_input():  # 사용자 입력 받기

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })  # 사용자 메시지를 대화 기록에 추가

    st.chat_message("user").write(
        user_input
    )  # 사용자 메시지를 브라우저에서도 출력


    # -------------------------
    # 첫 번째 GPT 응답
    # -------------------------

    ai_response = get_ai_response(
        st.session_state.messages,
        tools=tools
    )


    # 스트리밍 결과를 저장하기 위한 변수
    content = ""
    tool_calls_chunk = []


    # -------------------------
    # 첫 번째 GPT 스트리밍
    # -------------------------

    with st.chat_message("assistant"):

        message_placeholder = st.empty()

        for chunk in ai_response:

            # 일반 텍스트 추출
            if chunk.choices[0].delta.content:

                content_chunk = chunk.choices[0].delta.content

                print(
                    content_chunk,
                    end=""
                )  # 터미널에 줄바꿈 없이 이어서 출력

                content += content_chunk

                message_placeholder.markdown(
                    content
                )  # 스트림릿 챗 메시지에 마크다운으로 출력


            # tool_calls가 있는 경우
            if chunk.choices[0].delta.tool_calls:

                tool_calls_chunk += (
                    chunk.choices[0].delta.tool_calls
                )

        tool_obj = tool_list_to_tool_obj(tool_calls_chunk)
        tool_calls = tool_obj["tool_calls"]

        if len(tool_calls) > 0:
            print(tool_calls)
            tool_call_msg = [tool_call["function"] for tool_call in tool_calls]
            st.write(tool_call_msg)
    

    print("\n=========== tool_calls")
    print(tool_calls)

    print("\n=========== content")
    print(content)


    # -------------------------
    # Tool 호출 처리
    # -------------------------

    if tool_calls:

        # tool_calls를 가진 assistant 메시지를 먼저 저장
        st.session_state.messages.append({
            "role": "assistant",
            "content": content if content else None,
            "tool_calls": tool_calls,
        })


        # 각 tool 실행
        for tool_call in tool_calls:

            tool_name = tool_call["function"]["name"]
            # 실행해야한다고 판단한 함수명 받기

            tool_call_id = tool_call["id"]
            # 함수 아이디 받기

            arguments = json.loads(
                tool_call["function"]["arguments"]
            )
            # 문자열을 딕셔너리로 변환


            # -------------------------
            # 현재 시간 함수
            # -------------------------

            if tool_name == "get_current_time":

                func_result = get_current_time(
                    timezone=arguments["timezone"]
                )


            # -------------------------
            # 주식 정보 함수
            # -------------------------

            elif tool_name == "get_yf_stock_info":

                func_result = get_yf_stock_info(
                    ticker=arguments["ticker"]
                )


            # -------------------------
            # 주식 히스토리 함수
            # -------------------------

            elif tool_name == "get_yf_stock_history":

                func_result = get_yf_stock_history(
                    ticker=arguments["ticker"],
                    period=arguments["period"]
                )


            # -------------------------
            # 주식 추천 함수
            # -------------------------

            elif tool_name == "get_yf_stock_recommendations":

                func_result = get_yf_stock_recommendations(
                    ticker=arguments["ticker"]
                )


            else:
                continue


            # Tool 실행 결과를 대화 기록에 추가
            st.session_state.messages.append({
                "role": "tool",  # role을 "tool"으로 설정
                "tool_call_id": tool_call_id,
                "content": func_result,
            })


        # -------------------------
        # Tool 결과를 바탕으로 다시 GPT 응답
        # -------------------------

        ai_response = get_ai_response(
            st.session_state.messages,
            tools=tools
        )


        content = ""


        # -------------------------
        # 최종 GPT 스트리밍
        # -------------------------

        with st.chat_message("assistant"):

            message_placeholder = st.empty()

            for chunk in ai_response:

                content_chunk = chunk.choices[0].delta.content

                if content_chunk:

                    print(
                        content_chunk,
                        end=""
                    )

                    content += content_chunk

                    message_placeholder.markdown(
                        content
                    )


    # -------------------------
    # 최종 AI 응답 저장
    # -------------------------

    if content:

        st.session_state.messages.append({
            "role": "assistant",
            "content": content
        })  # AI 응답을 대화 기록에 추가합니다.

        print(
            "\nAI\t: " + content
        )  # AI 응답 출력