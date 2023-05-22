import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref, relationship
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy import Column, String, Boolean, DateTime

from dts.core.db import Base
from dts.utils.commons import Commons

__all__ = ["Shipment"]

SCHEMA = "dts"


class Shipment(Base):
    __table_args__ = {"schema": f"{SCHEMA}"}
    __tablename__ = "shipment"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    waybill_no = Column(String(255), nullable=False, unique=True)
    ecommerce_company = Column(String(255), nullable=False, unique=False)
    reciepient_name = Column(String(255), nullable=False, unique=False)
    reciepient_email = Column(String(255), nullable=False, unique=False)
    reciepient_phone = Column(String(255), nullable=False, unique=False)
    reciepient_address = Column(String(255), nullable=False, unique=False)
    is_completed = Column(Boolean, nullable=False, default=False)
    is_cancelled = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow, default=datetime.utcnow)
    tracker = relationship(
        "Tracker",
        lazy="dynamic",
        backref=backref("shipment", uselist=False, lazy="joined"),
    )
