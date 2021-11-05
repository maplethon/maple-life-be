from flask import g
from werkzeug import exceptions as http_exceptions

from task.domain.icon_types import IconTypes
from task.domain.task import Task
from task.domain.task_status import TaskStatus
from task.dto.create_task_response import CreateTaskResponse
from task.dto.task_info_response import TaskResponse


class TaskService:
    def __init__(self, db):
        self.db = db

    def create_task(self, request):
        new_task = Task(
            task_title=request["task_title"],
            expected_time=request["expected_time"],
            icon=IconTypes[request["icon"]].name,
            status=TaskStatus.DOING.name,
            user_id=g.user_id,
        )
        self.db.session.add(new_task)

        tasks = Task.get_all_task_by_user(g.user_id)
        total_task_time = sum([float(task.expected_time) for task in tasks])

        try:
            available_task_time = self.get_available_time(total_task_time)
            self.db.session.commit()
        except http_exceptions.BadRequest as e:
            self.db.session.rollback()
            raise e

        return CreateTaskResponse(available_task_time, TaskResponse.of(new_task))

    def get_available_time(self, total_task_time):
        HOURS_IN_DAY = 24
        available_time = HOURS_IN_DAY - total_task_time

        if available_time < 0:
            raise http_exceptions.BadRequest("잔여 작업 시간이 부족합니다")

        return available_time
