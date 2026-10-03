# 사용 uv 환경에서 아래 패키지들 add 필요
# uv add langchain-core pydantic yfinance pytz ddgs youtube-search youtube-transcript-api tabulate

from langchain_core.tools import tool

from pydantic import BaseModel, Field
import yfinance as yf

from datetime import datetime
import pytz

from typing import List

from ddgs import DDGS

from youtube_search import YoutubeSearch
from youtube_transcript_api import YouTubeTranscriptApi


# Pydantic의 데이터 모델 기능을 이용해서 StockHistoryInput이라는 입력 형식을 만들겠다.
class StockHistoryInput(BaseModel):
    ticker: str = Field(..., title="주식 코드", description="주식 코드 (예: AAPL)")
    period: str = Field(..., title="기간", description="주식 데이터 조회 기간 (예: 1d, 1mo, 1y)")


# Pydantic을 이용하지 않는다면:
#"parameters": {
#    "type": "object",
#    "properties": {
#        "ticker": {
#            "type": "string",
#            "description": "..."
#        },
#        "period": {
#            "type": "string",
#            "description": "..."
#        }
#    },
#    "required": ["ticker", "period"]
#}


@tool
def get_yf_stock_history(stock_history_input: StockHistoryInput) -> str:
    """주식 종목의 가격 데이터를 조회하는 함수"""
    stock = yf.Ticker(stock_history_input.ticker)
    history = stock.history(period=stock_history_input.period)
    history_md = history.to_markdown()

    return history_md


@tool # @tool 데코레이터를 사용하여 함수를 도구로 등록
def get_current_time(timezone: str, location: str) -> str:
    """ 현재 시각을 반환하는 함수

    Args:
        timezone (str): 타임존 (예: 'Asia/Seoul') 실제 존재하는 타임존이어야 함
        location (str): 지역명. 타임존이 모든 지명에 대응되지 않기 때문에 이후 llm 답변 생성에 사용됨
    """
    tz = pytz.timezone(timezone)
    now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    location_and_local_time = f'{timezone} ({location}) 현재시각 {now} ' # 타임존, 지역명, 현재시각을 문자열로 반환
    print(location_and_local_time)
    return location_and_local_time


@tool
def get_web_search(query: str, search_period: str) -> str:
    """
    웹 검색을 수행하는 함수.

    Args:
        query: 검색어
        search_period: 검색 기간
    """
    print("-------- WEB SEARCH --------")
    print(query)
    print(search_period)

    try:
        results = DDGS().text(
            query,
            region="kr-kr",
            timelimit=search_period,
            max_results=5
        )

        return str(results)

    except Exception as e:
        print("웹 검색 오류:", e)
        return f"웹 검색 결과를 찾을 수 없습니다. 검색어: {query}"


@tool
def get_youtube_search(query: str) -> List[dict]:
    """
    유튜브 검색을 한 뒤, 영상들의 내용을 반환하는 함수.

    Args:
        query: 검색어

    Returns:
        List[dict]: 검색 결과
    """
    print("-------- YOUTUBE SEARCH --------")
    print(query)

    videos = YoutubeSearch(
        query,
        max_results=5
    ).to_dict()

    # 1시간 이상의 영상은 스킵
    # (59:59가 최대 길이)
    videos = [
        video
        for video in videos
        if len(video["duration"]) <= 5
    ]

    for video in videos:
        video_url = "http://youtube.com" + video["url_suffix"]
        video_id = video["id"]

        video["video_url"] = video_url

        try:
            # YouTube 자막을 직접 가져옴
            transcript = YouTubeTranscriptApi().fetch(
                video_id,
                languages=["ko", "en"]
            )

            video["content"] = " ".join(
                snippet.text
                for snippet in transcript
            )

        except Exception as e:
            print("YouTube 자막 가져오기 오류:", e)
            video["content"] = ""

    return videos


# 도구를 tools 리스트에 추가하고, tool_dict에도 추가
tools = [
    get_current_time,
    get_yf_stock_history,
    get_web_search,
    get_youtube_search
]

tool_dict = {
    "get_current_time": get_current_time,
    "get_yf_stock_history": get_yf_stock_history,
    "get_web_search": get_web_search,
    "get_youtube_search": get_youtube_search
}