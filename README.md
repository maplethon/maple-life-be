# 🍁 메이플 라이프

> 2020년 기분장애로 병원을 찾은 환자 중 z세대 16.8%로 높아졌습니다. ‘노인의 병’이라고 불리던 우울증이 오히려 ‘젊은이의 병’이 된 것인데요. 그래서 저희는 낮아진 z세대의 자존감을 높여보는데 도움을 주고 싶어 해당 서비스를 기획했습니다. 저희 서비스는 목표와 소요 시간을 설정하고 완료하여 경험치를 쌓습니다. 경험치가 쌓일수록 자라나는 단풍나무를 보며 목표를 달성한 자신을 칭찬해보세요.

# 🎆 기술 스택

- **프론트엔드** : 리액트
- **백엔드** : 플라스크
- **데이터베이스** : MySQL
- **인프라**: AWS RDS, Synology NAS, Firebase, Github action


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
- 프로젝트 루트 디렉토리 (`/maple-life-be`)에 작성 
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


