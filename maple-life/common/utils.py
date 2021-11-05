from functools import wraps
from flask import request, current_app, g
import jwt
from werkzeug.datastructures import Authorization
import werkzeug.exceptions as http_exceptions


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        PREFIX = "Bearer "
        authroization = request.headers.get("Authorization")

        if not authroization.startswith(PREFIX):
            raise http_exceptions.BadRequest("토큰 포멧이 잘못되었습니다")

        access_token = authroization.replace(PREFIX, "")

        try:
            payload = jwt.decode(
                access_token, current_app.config["JWT_SECRET"], "HS256"
            )
        except jwt.ExpiredSignatureError:
            raise http_exceptions.BadRequest("토크이 만료되었습니다")
        except jwt.InvalidTokenError:
            raise http_exceptions.BadRequest("토큰이 잘못되었습니다")

        g.user_id = payload["user_id"]
        return f(*args, **kwargs)

    return decorated_function
