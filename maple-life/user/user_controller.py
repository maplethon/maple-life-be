from common.api_response import ApiResponse
from flask import Blueprint, request, Response, g

from common.utils import login_required


def create_user_blueprint(services):
    user_service = services.user_service

    user_bp = Blueprint("user", __name__, url_prefix="/users")

    @user_bp.route("/signup", methods=["POST"])
    def signup():
        user_service.create_new_user(request.json)
        return ApiResponse.ok()

    @user_bp.route("/login", methods=["POST"])
    def login():
        return ApiResponse.ok(user_service.login(request.json))

    @user_bp.route("", methods=["GET"])
    @login_required
    def get_user_info():
        return ApiResponse.ok(user_service.get_user(g.user_id))

    @user_bp.route("/<int:user_id>/username", methods=["PATCH"])
    def change_username(user_id):
        new_username = request.json["username"]
        return ApiResponse.ok(user_service.change_username(user_id, new_username))

    return user_bp
