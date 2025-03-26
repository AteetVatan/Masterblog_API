"""Module for App Flask to initialize and handle routes."""
import os

from flask import Flask, redirect, url_for, jsonify, send_from_directory
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_swagger_ui import get_swaggerui_blueprint

from backend.config import Config
from .post_controller import PostController


class AppController:
    """Class for App Flask to initialize and handle routes."""

    def __init__(self, app: Flask):
        self.app = app
        self.limiter = Limiter(get_remote_address,
                               app=self.app,
                               default_limits=Config.LIMITER_DEFAULT_LIMITS)
        post_controller = self.start_post_api()
        self.add_routes(post_controller)
        self.__init__swagger()

    def start_post_api(self):
        """Method to start the blog."""
        post_controller = PostController()
        # register the Post Blueprint with running API.
        self.app.register_blueprint(post_controller.blue_print)
        return post_controller

    def __init__swagger(self):
        """Method to initialize the swagger documentation."""
        swagger_ui_blueprint = get_swaggerui_blueprint(
            Config.SWAGGER_URL,
            Config.API_URL,
            config={
                'app_name': Config.APP_NAME
            }
        )
        self.app.register_blueprint(swagger_ui_blueprint, url_prefix=Config.SWAGGER_URL)

    def add_routes(self, post_controller: PostController):
        """Method to handel HTTP Routes."""

        @self.app.route('/')
        def index():
            """The Index page."""
            end_point = f"{post_controller.blue_print_name}.get_posts"
            return redirect(url_for(end_point))

        @self.app.errorhandler(404)
        def not_found_error():
            """API end point for Not Found Error page."""
            return jsonify({"error": "Not Found"}), 404

        @self.app.errorhandler(405)
        def method_not_allowed_error():
            """API end point for Method is not allowed page."""
            return jsonify({"error": "Method Not Allowed"}), 405

        @self.app.route('/favicon.ico')
        def favicon():
            """API end point for favicon"""
            return send_from_directory(
                os.path.join(self.app.root_path, 'static'),
                'favicon.ico',
                mimetype='image/vnd.microsoft.icon'
            )
