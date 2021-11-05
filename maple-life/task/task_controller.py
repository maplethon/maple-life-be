from common.api_response import ApiResponse
from common.utils import login_required
from flask import Blueprint, request


def create_task_blueprint(services):
    task_service = services.task_service

    task_bp = Blueprint("task", __name__, url_prefix="/tasks")

    @task_bp.route("", methods=["POST"])
    @login_required
    def create_task():
        return ApiResponse.ok(task_service.create_task(request.json))

    return task_bp
