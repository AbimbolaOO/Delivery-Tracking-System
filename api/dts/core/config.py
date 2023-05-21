import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    CORS_ALLOW_HEADERS = [
        "Origin",
        "Content-Type",
        "Authorization",
        "authorization",
        "Accept",
    ]
    CORS_EXPOSE_HEADERS = [
        "Origin",
        "Content-Type",
        "Authorization",
        "authorization",
        "Accept",
        "Content-Length",
    ]
    CORS_ORIGINS = "*"
    CORS_METHODS = ["GET", "HEAD", "POST", "OPTIONS", "PUT", "PATCH", "DELETE"]
    CORS_RESOURCES = r"/*"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config_options = {
    "production": ProductionConfig,
    "staging": StagingConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig,
}
