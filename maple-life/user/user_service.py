import bcrypt
from user.domain.user import User
from user.dto.login_response import LoginResponse
import werkzeug.exceptions as http_exceptions


class UserService:
    def __init__(self, db):
        self.db = db

    def create_new_user(self, request):
        email = request["email"]
        user_exists = User.query.filter_by(email=email).first() is not None
        if user_exists is True:
            raise http_exceptions.BadRequest(f"이메일{email} 사용자가 이미 존재합니다")

        hashed_password = bcrypt.hashpw(
            request["password"].encode("UTF-8"), bcrypt.gensalt()
        )

        new_user = User(
            email=email,
            username=request["username"],
            hashed_password=hashed_password,
            accumulated_task_time=0,
        )

        self.db.session.add(new_user)
        self.db.session.commit()

    def login(self, request):
        return LoginResponse(1, "sss")
