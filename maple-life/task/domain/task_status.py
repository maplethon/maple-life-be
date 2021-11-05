from enum import Enum, auto
from werkzeug import exceptions


class TaskStatus(Enum):
    DOING = auto()
    DONE = auto()

    def complete(self):
        if self == TaskStatus.DOING:
            return TaskStatus.DONE

        if self == TaskStatus.DONE:
            raise exceptions.BadRequest("이미 완료된 태스크입니다")
