# ๐ ๋ฉ์ดํ ๋ผ์ดํ

> 2020๋ ๊ธฐ๋ถ์ฅ์ ๋ก ๋ณ์์ ์ฐพ์ ํ์ ์ค z์ธ๋ 16.8%๋ก ๋์์ก์ต๋๋ค. โ๋ธ์ธ์ ๋ณโ์ด๋ผ๊ณ  ๋ถ๋ฆฌ๋ ์ฐ์ธ์ฆ์ด ์คํ๋ ค โ์ ์์ด์ ๋ณโ์ด ๋ ๊ฒ์ธ๋ฐ์. ๊ทธ๋์ ์ ํฌ๋ ๋ฎ์์ง z์ธ๋์ ์์กด๊ฐ์ ๋์ฌ๋ณด๋๋ฐ ๋์์ ์ฃผ๊ณ  ์ถ์ด ํด๋น ์๋น์ค๋ฅผ ๊ธฐํํ์ต๋๋ค. ์ ํฌ ์๋น์ค๋ ๋ชฉํ์ ์์ ์๊ฐ์ ์ค์ ํ๊ณ  ์๋ฃํ์ฌ ๊ฒฝํ์น๋ฅผ ์์ต๋๋ค. ๊ฒฝํ์น๊ฐ ์์ผ์๋ก ์๋ผ๋๋ ๋จํ๋๋ฌด๋ฅผ ๋ณด๋ฉฐ ๋ชฉํ๋ฅผ ๋ฌ์ฑํ ์์ ์ ์นญ์ฐฌํด๋ณด์ธ์.

# ๐ ๊ธฐ์  ์คํ

- **ํ๋ก ํธ์๋** : ๋ฆฌ์กํธ
- **๋ฐฑ์๋** : ํ๋ผ์คํฌ
- **๋ฐ์ดํฐ๋ฒ ์ด์ค** : MySQL
- **์ธํ๋ผ**: AWS RDS, Synology NAS, Firebase, Github action


# ๊ฐ๋ฐ ํ๊ฒฝ ์ค์ 

## ํ์ ์์กด์ฑ
  - Python 3.6 ์ด์

## ํ๋ก์ ํธ ํด๋ก  ๋ฐ ๊ฐ์ํ๊ฒฝ ์ค์ 
```bash
$ git clone https://github.com/maplethon/maple-life-be
$ cd maple-life-be
$ python3 -m venv virtualenv
$ source ./virtualenv/bin/activate
$ pip install -r requirements.txt
```

## `.env` ํ์ผ ์์ฑ
- ํ๋ก์ ํธ ๋ฃจํธ ๋๋ ํ ๋ฆฌ (`/maple-life-be`)์ ์์ฑ 
- ํ์ ํ๊ฒฝ๋ณ์
```bash
FLASK_APP=maple-life/app.py
FLASK_ENV=development
APP_CONFIG_FILE=common/config/development.py

DB_HOST=
DB_USER=
DB_PASSWORD=

JWT_SECRET=
```

## ์คํ
```bash
$ flask run --host=0.0.0.0 
```


