import json
from dts.models.v1 import Shipment, Tracker

BASE_PATH = "/api/v1/dts"


def test_create_shipment():
    data = {
        "ecommerce_company": "Lookingcompany",
        "reciepient_address": "26, Ayugy street orile Ijesha",
        "reciepient_email": "looking@gmail.com",
        "reciepient_name": "Ramson Gordon",
        "reciepient_phone": "+2348119997732",
        "waybill_no": "NG009050890001",
    }
    shipment = Shipment(**data)

    assert shipment.ecommerce_company == "Lookingcompany"
    assert shipment.reciepient_address == "26, Ayugy street orile Ijesha"
    assert shipment.reciepient_email == "looking@gmail.com"
    assert shipment.reciepient_name == "Ramson Gordon"
    assert shipment.reciepient_phone == "+2348119997732"
    assert shipment.waybill_no == "NG009050890001"


def test_get_shipment(client):
    response = client.get(f"{BASE_PATH}/shipment/?waybill_no=NG019050895900")
    res = json.loads(response.data.decode("utf-8"))

    assert "YemiIfeCorp" in res.get("data").values()
    assert "26, Ayugy street orile Ijesha" in res.get("data").values()
    assert "yemiifecorp@gmail.com" in res.get("data").values()
    assert "+2348119997733" in res.get("data").values()
    assert res.get("message") == "Shipment details."
    assert res.get("status") == "success"
    assert response.status_code == 200


def test_list_shipment(client):
    response = client.get(f"{BASE_PATH}/shipments/?is_completed=false")
    res = json.loads(response.data.decode("utf-8"))

    assert len(res.get("data")) == 3
    assert res.get("message") == "List of shipments."
    assert res.get("status") == "success"
    assert response.status_code == 200


def test_get_full_shipment_data(client):
    response = client.get(f"{BASE_PATH}/shipment-info/?waybill_no=NG019050895900")
    res = json.loads(response.data.decode("utf-8"))

    assert res.get("message") == "Shipment details."
    assert res.get("status") == "success"
    assert response.status_code == 200


def test_move_shipment():
    data = {
        "dispatcher_name": "Yemi Yellow",
        "location": "23, Ajao estate warehouse",
        "package_status": "PICKED_UP",
    }
    tracker = Tracker(**data)

    assert tracker.dispatcher_name == "Yemi Yellow"
    assert tracker.location == "23, Ajao estate warehouse"
    assert tracker.package_status == "PICKED_UP"


def test_cancel_shipment(client):
    data = {"waybill_no": "NG019050895901"}
    response = client.put(f"{BASE_PATH}/cancel-shipment/", json=data)
    res = json.loads(response.data.decode("utf-8"))

    assert "26, Ayugy street orile Ijesha" in res.get("data").values()
    assert "looking@gmail.com" in res.get("data").values()
    assert "Ramson Gordon" in res.get("data").values()
    assert "+2348119997732" in res.get("data").values()
    assert "NG019050895901" in res.get("data").values()
    assert res.get("message") == "Shipment is cancelled."
    assert res.get("status") == "success"
    assert response.status_code == 200


def test_end_shipment(client):
    data = {"waybill_no": "NG019000895900"}
    response = client.put(f"{BASE_PATH}/end-shipment/", json=data)
    res = json.loads(response.data.decode("utf-8"))

    assert res.get("data") == None
    assert res.get("message") == "Ended Shipment delivery."
    assert res.get("status") == "success"
    assert response.status_code == 200


def test_delete_shipment(client):
    data = {"waybill_no": "NG019000895900"}
    response = client.delete(f"{BASE_PATH}/shipment/", json=data)

    assert response.status_code == 204
