from langchain_core.tools import tool

from pydantic import BaseModel, Field
import yfinance as yf

from datetime import datetime
import pytz

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

# 도구를 tools 리스트에 추가하고, tool_dict에도 추가
tools = [get_current_time, get_yf_stock_history]
tool_dict = {"get_current_time": get_current_time, "get_yf_stock_history": get_yf_stock_history}