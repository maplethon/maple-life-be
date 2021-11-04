from common.api_response import ApiResponse
from flask import Blueprint, request


def create_task_blueprint(services):
    task_service = services.task_service

    task_bp = Blueprint("task", __name__, url_prefix="/tasks")

    return task_bp
