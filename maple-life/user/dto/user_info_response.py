class UserInfoResponse:
    def __init__(self, user_id, username, email, accumulated_task_time) -> None:
        self.user_id = user_id
        self.username = username
        self.email = email
        self.accumulated_task_time = accumulated_task_time
