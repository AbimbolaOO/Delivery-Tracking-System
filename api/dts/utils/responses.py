import json
from flask import Response, jsonify
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


def error_response(*, message, status_code):
    if type(message) != dict:
        message = str(message)
    return jsonify(status="error", data=None, message=message), status_code


def success_response(*, message, data, status_code):
    response = {
        "status": "success",
        "message": message,
        "data": data,
    }

    return Response(
        mimetype="application/json", response=json.dumps(response), status=status_code
    )
