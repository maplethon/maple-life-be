from werkzeug import exceptions as http_exceptions

from task.domain.icon_types import IconTypes
from task.domain.task import Task
from task.domain.task_status import TaskStatus
from task.dto.create_task_response import CreateTaskResponse
from task.dto.task_response import TaskResponse
from task.dto.get_all_task_response import GetAllTaskResponse


class TaskService:
    def __init__(self, db):
        self.db = db

    def __create_task(self, user_id, request):
        return Task(
            task_title=request["task_title"],
            expected_time=request["expected_time"],
            icon=IconTypes[request["icon"]].name,
            status=TaskStatus.DOING.name,
            user_id=user_id,
        )

    def __get_total_task_time(self, tasks):
        return sum([float(task.expected_time) for task in tasks])

    def __get_available_time(self, total_task_time):
        HOURS_IN_DAY = 24
        available_time = HOURS_IN_DAY - total_task_time

        if available_time < 0:
            raise http_exceptions.BadRequest("잔여 작업 시간이 부족합니다")

        return available_time

    def __validate_task(self, user_id, task_id):
        task = Task.find_by_id(task_id)

        if task is None:
            raise http_exceptions.NotFound("존재하지 않는 태스크입니다")

        if task.user_id != user_id:
            raise http_exceptions.BadRequest("권한이 없습니다")

    def save_task(self, user_id, request):
        new_task = self.__create_task(user_id, request)
        self.db.session.add(new_task)

        tasks = Task.get_all_task_by_user(user_id)
        total_task_time = self.__get_total_task_time(tasks)

        try:
            available_task_time = self.__get_available_time(total_task_time)
            self.db.session.commit()
        except http_exceptions.BadRequest as e:
            self.db.session.rollback()
            raise e

        return CreateTaskResponse(available_task_time, TaskResponse.of(new_task))

    def get_all_task(self, user_id):
        tasks = Task.get_all_task_by_user(user_id)
        total_task_time = self.__get_total_task_time(tasks)
        available_time = self.__get_available_time(total_task_time)
        return GetAllTaskResponse(available_time, tasks)

    def update_task(self, user_id, task_id, request):
        self.__validate_task(user_id, task_id)
        task = Task.find_by_id(task_id)
        task.task_title = request["task_title"]
        task.expected_time = request["expected_time"]
        task.icon = request["icon"]

        tasks = Task.get_all_task_by_user(user_id)
        total_task_time = self.__get_total_task_time(tasks)

        try:
            available_task_time = self.__get_available_time(total_task_time)
            self.db.session.commit()
        except http_exceptions.BadRequest as e:
            self.db.session.rollback()
            raise e

        return CreateTaskResponse(available_task_time, TaskResponse.of(task))
