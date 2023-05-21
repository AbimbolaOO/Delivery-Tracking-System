from flask import request
from flasgger import swag_from

from dts.utils.responses import error_response, success_response
from dts.services.v1.dts_services import DtsService


# TODO:: ADD RATE limiter
@swag_from("/dts/docs/create_shipment.yaml")
def create_shipment():
    data = request.get_json()
    try:
        res_data = DtsService().create_shipment(data)
        return success_response(
            message="Shipment created successfully.",
            data=res_data,
            status_code=201,
        )
    except Exception as e:
        (error,) = e.args
        return error_response(message=error, status_code=400)


@swag_from("/dts/docs/get_shipment.yaml")
def get_shipment():
    waybill_no = request.args.get("waybill_no", type=str)
    try:
        res_data = DtsService().get_shipment(waybill_no)
        return success_response(
            message="Shipment details.",
            data=res_data,
            status_code=200,
        )
    except Exception as e:
        (error,) = e.args
        return error_response(message=error, status_code=400)


@swag_from("/dts/docs/get_full_shipment_data.yaml")
def get_full_shipment_data():
    waybill_no = request.args.get("waybill_no", type=str)
    try:
        res_data = DtsService().get_full_shipment_data(waybill_no)
        return success_response(
            message="Shipment details.",
            data=res_data,
            status_code=200,
        )
    except Exception as e:
        (error,) = e.args
        return error_response(message=error, status_code=400)


@swag_from("/dts/docs/list_shipment.yaml")
def list_shipment():
    is_completed = request.args.get("is_completed", type=str)
    page = request.args.get("page", type=int)
    per_page = request.args.get("per_page", type=int)
    try:
        res_data = DtsService().list_shipments(is_completed, page, per_page)
        return success_response(
            message="List of shipments.",
            data=res_data,
            status_code=200,
        )
    except Exception as e:
        (error,) = e.args
        return error_response(message=error, status_code=400)


@swag_from("/dts/docs/move_shipment.yaml")
def move_shipment(waybill_no):
    data = request.get_json()
    try:
        res_data = DtsService().move_shipment(waybill_no, data)
        return success_response(
            message="List of shipments.",
            data=res_data,
            status_code=200,
        )
    except Exception as e:
        (error,) = e.args
        return error_response(message=error, status_code=400)


@swag_from("/dts/docs/cancel_shipment.yaml")
def cancel_shipment():
    data = request.get_json()
    try:
        res_data = DtsService().cancel_shipment(data)
        return success_response(
            message="Shipment is cancelled.",
            data=res_data,
            status_code=200,
        )
    except Exception as e:
        (error,) = e.args
        return error_response(message=error, status_code=400)


@swag_from("/dts/docs/end_shipment.yaml")
def end_shipment():
    data = request.get_json()
    try:
        DtsService().end_shipment(data)
        return success_response(
            message="Ended Shipment delivery.",
            data=None,
            status_code=200,
        )
    except Exception as e:
        (error,) = e.args
        return error_response(message=error, status_code=400)


@swag_from("/dts/docs/delete_shipment.yaml")
def delete_shipment():
    data = request.get_json()
    try:
        res_data = DtsService().delete_shipment(data)
        return success_response(
            message="",
            data=None,
            status_code=204,
        )
    except Exception as e:
        (error,) = e.args
        return error_response(message=error, status_code=400)
