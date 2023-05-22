import traceback
import logging
import datetime

from dts.utils.responses import error_response


def resource_not_found(e):
    return error_response(message="Page Not Found.", status_code=404)


def too_many_request(e):
    return error_response(message=" Too Many Requests.", status_code=429)


def internal_server_error(e):
    logging.critical(
        f"\n{'='*30} DELIVERY TRACKING SYSTEM :: ERROR :: {datetime.datetime.now()} {'='*30}\n\n {traceback.format_exc()}\n{'='*54} END ERROR {'='*54}\n",
    )
    return error_response(message="Internal Server Error.", status_code=500)
