class CreateTaskResponse:
    def __init__(self, available_task_time, task_info_response) -> None:
        self.available_task_time = available_task_time
        self.task = task_info_response
