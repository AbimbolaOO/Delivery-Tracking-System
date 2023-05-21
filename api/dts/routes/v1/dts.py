from flask import Blueprint

from dts.controllers.v1.dts_controller import (
    create_shipment,
    get_shipment,
    get_full_shipment_data,
    list_shipment,
    move_shipment,
    cancel_shipment,
    end_shipment,
    delete_shipment,
)

dts = Blueprint("dts", __name__)

dts.post("shipment/")(create_shipment)
dts.get("shipment/")(get_shipment)
dts.get("shipment-info/")(get_full_shipment_data)
dts.get("shipments/")(list_shipment)
dts.post("move-shipment/<waybill_no>")(move_shipment)
dts.put("cancel-shipment/")(cancel_shipment)
dts.put("end-shipment/")(end_shipment)
dts.delete("shipment/")(delete_shipment)
