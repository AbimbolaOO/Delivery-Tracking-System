import pytest
from dts import create_app, db_session
from dts.models.v1 import Shipment, Tracker


@pytest.fixture()
def client(scope="function", autouse=True):
    app = create_app("testing")
    shipment_data1 = {
        "ecommerce_company": "Lookingcompany",
        "reciepient_address": "26, Ayugy street orile Ijesha",
        "reciepient_email": "looking@gmail.com",
        "reciepient_name": "Ramson Gordon",
        "reciepient_phone": "+2348119997732",
        "waybill_no": "NG019050895901",
    }
    shipment_data2 = {
        "ecommerce_company": "YemiIfeCorp",
        "reciepient_address": "26, Ayugy street orile Ijesha",
        "reciepient_email": "yemiifecorp@gmail.com",
        "reciepient_name": "Godswill Gordon",
        "reciepient_phone": "+2348119997733",
        "waybill_no": "NG019050895900",
    }

    shipment_data3 = {
        "ecommerce_company": "YemiIfeCorp",
        "reciepient_address": "26, Ayugy street orile Ijesha",
        "reciepient_email": "yemiifecorp@gmail.com",
        "reciepient_name": "Godswill Gordon",
        "reciepient_phone": "+2348119997733",
        "waybill_no": "NG019000895900",
    }

    with app.test_client() as client:
        with app.app_context():
            shipment_1 = Shipment(**shipment_data1)
            shipment_2 = Shipment(**shipment_data2)
            shipment_3 = Shipment(**shipment_data3)
            db_session.add_all([shipment_1, shipment_2, shipment_3])
            db_session.commit()

            tracker_data = {
                "dispatcher_name": "Yemi Yellow",
                "location": "23, Ajao estate warehouse",
                "package_status": "PICKED_UP",
            }
            shipment = Shipment.query.filter_by(waybill_no="NG019000895900").first()
            tracker = Tracker(**{**tracker_data, "shipment_id": shipment.id})
            db_session.add(tracker)
            db_session.commit()

        yield client

    with app.app_context():
        db_session.query(Shipment).delete()
        db_session.commit()
