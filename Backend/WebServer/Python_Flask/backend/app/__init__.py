from flask import Flask
from app.controllers.user_controller import user_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Register blueprints
    app.register_blueprint(user_blueprint, url_prefix="/api/users")

    return app
