class TaskResponse:
    def __init__(self, task_id, task_title, expected_time, status, icon) -> None:
        self.task_id = task_id
        self.task_title = task_title
        self.expected_time = expected_time
        self.status = status
        self.icon = icon

    @staticmethod
    def of(task):
        return TaskResponse(
            task.task_id,
            task.task_title,
            float(task.expected_time),
            task.status,
            task.icon,
        )
