from task.dto.task_response import TaskResponse


class GetAllTaskResponse:
    def __init__(self, available_task_time, tasks) -> None:
        self.available_task_time = available_task_time
        self.tasks = [TaskResponse.of(task) for task in tasks]
