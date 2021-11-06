# maple-life

# 개발 환경 설정

## 필요 의존성
  - Python 3.6 이상

## 프로젝트 클론 및 가상환경 설정
```bash
$ git clone https://github.com/maplethon/maple-life-be
$ cd maple-life-be
$ python3 -m venv virtualenv
$ source ./virtualenv/bin/activate
$ pip install -r requirements.txt
```

## `.env` 파일 작성
- 필요 환경변수
```bash
FLASK_APP=maple-life/app.py
FLASK_ENV=development
APP_CONFIG_FILE=common/config/development.py

DB_HOST=
DB_USER=
DB_PASSWORD=

JWT_SECRET=
```

## 실행
```bash
$ flask run --host=0.0.0.0 
```


