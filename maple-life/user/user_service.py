from datetime import datetime, timedelta
import bcrypt
import jwt
import werkzeug.exceptions as http_exceptions
from flask import current_app

from user.domain.user import User
from user.dto.login_response import LoginResponse
from user.dto.user_info_response import UserInfoResponse


class UserService:
    def __init__(self, db):
        self.db = db

    def __hash_password(self, password):
        return bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())

    def __create_jwt(self, user_id):
        payload = {"user_id": user_id, "exp": datetime.utcnow() + timedelta(days=7)}
        return jwt.encode(payload, current_app.config["JWT_SECRET"], "HS256")

    def __validate_user(self, email):
        if User.find_by_email(email) is None:
            raise http_exceptions.NotFound(f"이메일, 혹은 비밀번호가 잘못되었습니다")

    def __validate_password(self, password, hashed_password):
        is_valid = bcrypt.checkpw(
            password.encode("utf-8"), hashed_password.encode("utf-8")
        )
        if not is_valid:
            raise http_exceptions.BadRequest("이메일, 혹은 비밀번호가 잘못되었습니다")

    def __authorize_user(self, g_user_id, user_id):
        if g_user_id != user_id:
            raise http_exceptions.BadRequest("권한이 없습니다")

    def create_new_user(self, request):
        email = request["email"]

        if User.find_by_email(email) is not None:
            raise http_exceptions.BadRequest(f"이메일{email} 사용자가 이미 존재합니다")

        new_user = User(
            email=email,
            username=request["username"],
            hashed_password=self.__hash_password(request["password"]),
            accumulated_task_time=0,
        )

        self.db.session.add(new_user)
        self.db.session.commit()

    def login(self, request):
        email = request["email"]
        password = request["password"]

        self.__validate_user(email)
        user = User.find_by_email(email)
        self.__validate_password(password, user.hashed_password)

        return LoginResponse(user.user_id, self.__create_jwt(user.user_id))

    def get_user(self, user_id):
        user = User.find_by_id(user_id)
        return UserInfoResponse.of(user)

    def change_username(self, g_user_id, user_id, new_username):
        self.__authorize_user(g_user_id, user_id)
        user = User.find_by_id(user_id)
        user.username = new_username
        self.db.session.commit()
        return UserInfoResponse.of(user)
