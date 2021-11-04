from common.api_response import ApiResponse
from flask import Blueprint, request, Response

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

    @user_bp.route("/<int:user_id>", methods=["GET"])
    @login_required
    def gerUserInfo(user_id):
        return ApiResponse.ok(user_service.getUser(user_id))

    return user_bp
