import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy import Column, String, DateTime, ForeignKey

from dts.core.db import Base
from dts.utils.commons import Commons


__all__ = ["Tracker"]

SCHEMA = "dts"


class Tracker(Base):
    __table_args__ = {"schema": f"{SCHEMA}"}
    __tablename__ = "tracker"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    shipment_id = Column(
        UUID(as_uuid=True),
        ForeignKey(f"{SCHEMA}.shipment.id", ondelete="CASCADE"),
        nullable=False,
    )
    dispatcher_name = Column(String(255), nullable=False)
    package_status = Column(
        ENUM(
            *Commons.package_status(),
            name="package_status",
        ),
        nullable=False,
    )
    location = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow, default=datetime.utcnow)
