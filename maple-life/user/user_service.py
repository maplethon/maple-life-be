from datetime import datetime, timezone
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
        payload = {"user_id": user_id, "exp": datetime.now(tz=timezone.utc)}
        return jwt.encode(payload, current_app.config["JWT_SECRET"], "HS256")

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
        user = User.find_by_email(email)

        if user is None:
            raise http_exceptions.NotFound(f"이메일{email} 사용자가 존재하지 않습니다")

        return LoginResponse(user.user_id, self.__create_jwt(user.user_id))

    def getUser(self, user_id):
        user = User.find_by_id(user_id)
        return UserInfoResponse(
            user.user_id, user.username, user.email, user.accumulated_task_time
        )
