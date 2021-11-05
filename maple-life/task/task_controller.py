from common.api_response import ApiResponse
from common.utils import login_required
from flask import Blueprint, request, g


def create_task_blueprint(services):
    task_service = services.task_service

    task_bp = Blueprint("task", __name__, url_prefix="/tasks")

    @task_bp.route("", methods=["POST"])
    @login_required
    def save_task():
        return ApiResponse.ok(task_service.save_task(g.user_id, request.json))

    @task_bp.route("", methods=["GET"])
    @login_required
    def get_all_task():
        return ApiResponse.ok(task_service.get_all_task(g.user_id))

    @task_bp.route("/<int:task_id>", methods=["PUT"])
    @login_required
    def update_task(task_id):
        return ApiResponse.ok(
            task_service.update_task(g.user_id, task_id, request.json)
        )

    @task_bp.route("/<int:task_id>/status/done", methods=["PATCH"])
    @login_required
    def complete_task(task_id):
        return ApiResponse.ok(task_service.complete_task(g.user_id, task_id))

    @task_bp.route("/<int:task_id>", methods=["DELETE"])
    @login_required
    def delete_task(task_id):
        return ApiResponse.ok(task_service.delete_task(g.user_id, task_id))

    return task_bp
