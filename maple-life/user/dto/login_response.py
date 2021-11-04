class LoginResponse:
    def __init__(self, user_id, jwt) -> None:
        self.user_id = user_id
        self.jwt = jwt
