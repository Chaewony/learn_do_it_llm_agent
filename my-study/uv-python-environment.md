# UV와 챕터별 Python 개발 환경 구성

책의 실습을 진행하면서 각 챕터마다 독립적인 Python 가상 환경을 구성했습니다.

## 📁 프로젝트 구조

각 챕터에서 사용하는 패키지와 실행 환경을 독립적으로 관리합니다.

```text
chaewony/
├── .env                  # OpenAI API Key
├── .python-version       # 공통 Python 3.12
│
├── ch01/
│   ├── .venv/            # ch01 전용 가상환경
│   ├── pyproject.toml    # ch01 의존성 관리
│   ├── uv.lock           # 의존성 버전 고정
│   └── src.ipynb
│
├── ch02/
│   ├── .venv/            # ch02 전용 가상환경
│   ├── pyproject.toml
│   ├── uv.lock
│   └── src.ipynb
│
├── ch03/
│   ├── .venv/            # ch03 전용 가상환경
│   ├── pyproject.toml
│   ├── uv.lock
│   └── src.ipynb
│
└── ...
```

---

## 🛠️ UV를 사용한 환경 구성

각 챕터를 하나의 독립적인 Python 프로젝트로 구성하기 위해 `uv init --bare`를 사용했습니다.

```bash
uv init --bare
```

이후 각 챕터에 필요한 패키지만 해당 챕터의 환경에 추가합니다.

```bash
uv add {package}
```

이를 통해 챕터마다 필요한 의존성을 독립적으로 관리할 수 있습니다.

---

## 📦 Python 패키지 구분

Python에서 사용하는 모든 모듈을 설치해야 하는 것은 아닙니다.

### 표준 라이브러리

Python에 기본적으로 포함되어 있기 때문에 별도의 설치가 필요하지 않습니다.

```text
표준 라이브러리
├── pprint
├── os
├── json
└── pathlib
```

### 외부 패키지

Python에 기본적으로 포함되어 있지 않으므로 필요한 경우 `uv add`를 사용해 설치합니다.

```text
외부 패키지
├── openai           → uv add openai
├── python-dotenv   → uv add python-dotenv
└── streamlit       → uv add streamlit
```

### 💡 구분하는 방법

```text
Python에 기본 포함
        ↓
    표준 라이브러리
        ↓
     설치할 필요 없음

Python에 기본 포함되지 않음
        ↓
      외부 패키지
        ↓
      uv add 필요
```

---

## 🔐 환경 변수 관리

OpenAI API Key와 같은 민감한 정보는 코드에 직접 작성하지 않고 `.env` 파일에서 관리합니다.

```text
.env
```

```env
OPENAI_API_KEY=...
```

`.env` 파일은 Git에 업로드하지 않도록 `.gitignore`에 등록합니다.

```gitignore
.env
```

---

## 💻 실행 환경

VS Code에서 Jupyter Notebook을 사용하기 위해 다음 확장 프로그램을 설치했습니다.

* Python
* Jupyter

Notebook에서 셀을 실행할 때 **Select Kernel**을 통해 각 챕터의 `.venv`를 선택합니다.

```text
src.ipynb
    ↓
Select Kernel
    ↓
ch03/.venv
    ↓
ch03의 Python 환경에서 실행
```

따라서 각 챕터의 Notebook은 해당 챕터에서 관리하는 Python 환경과 패키지를 사용하게 됩니다.

---

## 🤔 왜 챕터별 가상 환경을 사용하는가?

모든 챕터에서 하나의 가상 환경을 사용하는 대신 챕터별로 환경을 분리하면 각 실습에 필요한 패키지를 독립적으로 관리할 수 있습니다.

```text
공통 Python 버전
       │
       ├── ch01/.venv
       │      └── ch01 의존성
       │
       ├── ch02/.venv
       │      └── ch02 의존성
       │
       ├── ch03/.venv
       │      └── ch03 의존성
       │
       └── ...
```

특정 챕터에서 패키지 버전이나 의존성이 달라지더라도 다른 챕터의 실행 환경에 영향을 주지 않는다는 장점이 있습니다.

---

## 📌 정리

이번 환경 구성을 통해 다음 내용을 학습했습니다.

* `uv`를 이용한 Python 프로젝트 초기화
* `uv add`를 이용한 외부 패키지 관리
* 표준 라이브러리와 외부 패키지의 차이
* `pyproject.toml`과 `uv.lock`을 이용한 의존성 관리
* 챕터별 Python 가상 환경 구성
* VS Code에서 Jupyter와 가상 환경 연결
* `.env`를 이용한 API Key 관리
