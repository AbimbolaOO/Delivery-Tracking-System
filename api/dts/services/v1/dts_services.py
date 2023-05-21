from marshmallow.exceptions import ValidationError

from dts.uow.v1.uow import UnitOfWork
from dts.schema.v1.shipment_schema import (
    ShipmentSchema,
    ShipmentWaybillNoSchema,
    ShipmentAndTrackingDataSchema,
)
from dts.schema.v1.tracker_schema import TrackerSchema

shipment_schema = ShipmentSchema()
tracker_schema = TrackerSchema()
shipment_waybill_no_schema = ShipmentWaybillNoSchema()
shipment_and_tracking_data_schema = ShipmentAndTrackingDataSchema()


class DtsService:
    def __init__(self) -> None:
        self.uow = UnitOfWork()

    def create_shipment(self, data):
        try:
            deserialized_data = shipment_schema.load(data)
        except ValidationError as e:
            raise Exception(e.messages)

        try:
            query = self.uow.shipment_repo.create(deserialized_data)
            self.uow.persist_data()
        except Exception as e:
            raise Exception("Ship with waybill no already exist.")

        return shipment_schema.dump(query)

    def get_shipment(self, waybill_no):
        query = self.uow.shipment_repo.get({"waybill_no": waybill_no}).first()
        if query == None:
            raise Exception("Invalid waybill number.")

        return shipment_schema.dump(query)

    def get_full_shipment_data(self, waybill_no):
        query = self.uow.shipment_repo.get({"waybill_no": waybill_no}).first()
        if query == None:
            raise Exception("Invalid waybill number.")

        return shipment_and_tracking_data_schema.dump(query)

    def list_shipments(self, is_completed, page, per_page):
        if page != None and per_page:
            query = (
                self.uow.shipment_repo.get({"is_completed": is_completed})
                .limit(per_page)
                .offset(page * per_page)
            )
        else:
            query = self.uow.shipment_repo.get({"is_completed": is_completed}).all()

        if query == None:
            raise Exception("Invalid data provided.")

        return shipment_schema.dump(query, many=True)

    def move_shipment(self, waybill_no, data):
        try:
            deserialized_data = tracker_schema.load(data)
        except ValidationError as e:
            raise Exception(e.messages)

        query = self.uow.shipment_repo.get({"waybill_no": waybill_no}).first()
        if query == None:
            raise Exception("Invalid waybill number.")

        try:
            query = self.uow.tracker_repository.create(
                {**deserialized_data, "shipment_id": query.id}
            )
            self.uow.persist_data()
        except Exception as e:
            (error,) = e.args
            raise Exception(error)

        return tracker_schema.dump(query)

    def cancel_shipment(self, data):
        try:
            deserialized_data = shipment_waybill_no_schema.load(data)
        except ValidationError as e:
            raise Exception(e.messages)

        query = self.uow.shipment_repo.get(
            {"waybill_no": deserialized_data.get("waybill_no"), "is_cancelled": False}
        ).first()

        if query == None:
            raise Exception("Order can't be cancelled.")

        query = self.uow.shipment_repo.update(
            filter={"waybill_no": deserialized_data.get("waybill_no")},
            data={"is_cancelled": True},
        ).first()

        self.uow.persist_data()

        return shipment_schema.dump(query)

    def end_shipment(self, data):
        try:
            deserialized_data = shipment_waybill_no_schema.load(data)
        except ValidationError as e:
            raise Exception(e.messages)

        query = self.uow.shipment_repo.get(
            {"waybill_no": deserialized_data.get("waybill_no")}
        ).first()

        if query == None:
            raise Exception("Invalid waybill number.")

        if query.is_cancelled:
            raise Exception("Invalid action delivery already cancelled.")

        if query.is_completed:
            raise Exception("Delivery already marked completed.")

        query.is_completed = True

        tracker_query = query.tracker.first()
        if tracker_query == None:
            raise Exception("Can't end shipment, it was never moved.")

        query.tracker.first().package_status = "DELIVERED"
        self.uow.persist_data()

    def delete_shipment(self, data):
        try:
            deserialized_data = shipment_waybill_no_schema.load(data)
        except ValidationError as e:
            raise Exception(e.messages)

        query = self.uow.shipment_repo.delete(
            {"waybill_no": deserialized_data.get("waybill_no")}
        )
        self.uow.persist_data()
        if not query:
            raise Exception("Invalid waybill number.")
