import werkzeug.exceptions as http_exceptions
from dotenv import load_dotenv
from flask import Flask
import logging

from common.api_response import ApiResponse
from common.database import db, migrate
from task.task_controller import create_task_blueprint
from task.task_service import TaskService
from user.user_controller import create_user_blueprint
from user.user_service import UserService


def create_app():
    app = Flask(__name__)
    app.config.from_envvar("APP_CONFIG_FILE")

    db.init_app(app)
    migrate.init_app(app, db)

    services = create_services(db)
    create_endpoints(app, services)

    return app


def create_services(db):
    class Services:
        pass

    services = Services
    services.user_service = UserService(db)
    services.task_service = TaskService(db)
    return services


def create_endpoints(app, services):
    app.register_blueprint(create_user_blueprint(services))
    app.register_blueprint(create_task_blueprint(services))

    @app.errorhandler(Exception)
    def handle_server_error(e):
        logging.error(e)
        return ApiResponse.internal_error()

    @app.errorhandler(http_exceptions.BadRequest)
    def handle_bad_request(e):
        logging.error(e)
        return ApiResponse.bad_request()

    @app.route("/ping", methods=["GET"])
    def ping():
        return ApiResponse.ok()
