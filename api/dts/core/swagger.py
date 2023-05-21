import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Delivery Management System API",
        "description": "API Endpoints for a Delivery Management System",
        "contact": {
            "yemicompany": "",
            "responsibleDeveloper": "",
            "email": "abimbolaolayemiwhyte@gmail.com",
            "url": "www.yemiGoesToCarbon.com",
        },
        "termsOfService": "www.yemiGoesToCarbon.com",
        "version": "1.0",
    },
    "host": os.environ.get("API_HOST", ""),
    "basePath": "/api/v1/dts/",  # base bash for blueprint registration
    "schemes": ["http", "https"],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": 'JWT Authorization header using the Bearer scheme. Example: "Authorization: Bearer {token}"',
        }
    },
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "api/v1/dts/apispec",
            "route": "/api/v1/dts/apispec.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/api/v1/dts/docs",
    "swagger_ui_bundle_js": "//unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js",
    "swagger_ui_standalone_preset_js": "//unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js",
    "jquery_js": "//unpkg.com/jquery@2.2.4/dist/jquery.min.js",
    "swagger_ui_css": "//unpkg.com/swagger-ui-dist@3/swagger-ui.css",
}
