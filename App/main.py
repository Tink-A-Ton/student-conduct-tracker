from flask import Flask
from flask_cors import CORS
from .database import init_db
from .config import load_config
from .controllers import setup_jwt
from .views import views


def add_views(app: Flask) -> None:
    for view in views:
        app.register_blueprint(view)


def create_app(overrides={}):
    app = Flask(__name__)
    load_config(app, overrides)
    CORS(app)
    add_views(app)
    init_db(app)
    jwt = setup_jwt(app)

    @jwt.invalid_token_loader
    @jwt.unauthorized_loader
    def custom_unauthorized_response(error):
        return "Unauthorized", 401

    app.app_context().push()
    return app
