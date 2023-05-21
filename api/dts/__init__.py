import os
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

ma = Marshmallow()
cors = CORS()
jwt_manager = JWTManager()
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri=os.environ["REDIS_URI"],
    strategy="fixed-window",
    default_limits=["10 per minute"],
)


# The import is placed below the SQLAlchemy() because of circular referencing
from dts.routes.v1.dts import dts as dts_routes
from dts.core.swagger import swagger_template, swagger_config
from dts.core.config import config_options
from dts.core.db import init_db, db_session
from dts.errors.handlers import (
    resource_not_found,
    internal_server_error,
    too_many_request,
)


def create_app(env_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_options.get(env_name, "development"))
    cors.init_app(app)
    init_db()

    ma.init_app(app)
    jwt_manager.init_app(app)
    limiter.init_app(app)

    Swagger(app, config=swagger_config, template=swagger_template)
    app.register_error_handler(404, resource_not_found)
    app.register_error_handler(429, too_many_request)
    app.register_error_handler(500, internal_server_error)
    app.register_blueprint(dts_routes, url_prefix="/api/v1/dts/")

    # Help to tear down session when the http request is completed
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
