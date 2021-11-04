import os

DB = {
    "host": os.getenv("DB_HOST"),
    "port": 3306,
    "database": "maplelife",
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8&collation=utf8_general_ci"

SQLALCHEMY_TRACK_MODIFICATIONS = False
