chaewony/
├── .env                  ← gpt api key
├── .python-version       ← 공통 Python 3.12
│
├── ch01/
│   ├── .venv/             ← ch01 전용 가상환경
│   ├── pyproject.toml
│   ├── uv.lock
│   └── src.ipynb
│
├── ch02/
│   ├── .venv/             ← ch02 전용 가상환경
│   ├── pyproject.toml
│   ├── uv.lock
│   └── src.ipynb
│
└── ch03/
    ├── .venv/             ← ch03 전용 가상환경
    ├── pyproject.toml
    ├── uv.lock
    └── src.ipynb
...

---------
각 챕터 별 uv init --bare 을 한다. ← 챕터별 가상 환경 설정
UV add {package} 가 필요한 경우:

표준 라이브러리
├── pprint       ← 설치 필요 없음
├── os           ← 설치 필요 없음
├── json         ← 설치 필요 없음
└── pathlib      ← 설치 필요 없음

외부 패키지
├── openai       ← uv add openai
├── python-dotenv ← uv add python-dotenv
└── streamlit    ← uv add streamlit

---------

실행 환경:
vscode에서 extension 설치 - pytjon, jupyter

셀 실행 시 Select Kernel 옵션이 생기는데, 
각 챕터별 가상 환경을 사용하게 한다.