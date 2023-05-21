from dts.repository.v1.shipment_repository import ShipmentRepositiory
from dts.repository.v1.tracker_repository import TrackerRepositiory

# db connection
from dts.core.db import db_session


class UnitOfWork:
    def __init__(self) -> None:
        self.session = db_session()
        self.shipment_repo = ShipmentRepositiory(self.session)
        self.tracker_repository = TrackerRepositiory(self.session)

    def persist_data(self):
        self.session.commit()
