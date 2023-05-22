from sqlalchemy.orm import Session

from dts.models.v1.tracker import Tracker


class TrackerRepositiory:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data):
        query = Tracker(**data)
        self._session.add(query)
        return query

    def get(self, filter):
        return Tracker.query.filter_by(**filter)

    def update(self, *, filter, data):
        query = Tracker.query.filter_by(**filter)
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
