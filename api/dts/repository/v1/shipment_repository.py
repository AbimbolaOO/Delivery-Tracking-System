from sqlalchemy.orm import Session

from dts.models.v1 import Shipment


class ShipmentRepositiory:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data):
        query = Shipment(**data)
        self._session.add(query)
        return query

    def get(self, filter):
        return Shipment.query.filter_by(**filter)

    def update(self, *, filter, data):
        query = Shipment.query.filter_by(**filter)
        if query == None:
            return None
        query.update(data)
        return query

    def delete(self, filter):
        query = self.get(filter)
        if query.first() == None:
            return False
        query.delete()
        return True
