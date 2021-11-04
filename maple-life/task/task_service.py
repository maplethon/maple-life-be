from task.domain.task import Task


class TaskService:
    def __init__(self, db):
        self.db = db
