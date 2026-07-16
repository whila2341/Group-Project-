from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base
from datetime import datetime
from datetime import timedelta

class OrderTracking(Base):
    __tablename__ = "order_tracking"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, unique=True)
    # order_number = Column(String(50), nullable=False, unique=True, index=True)
    #   We probably don't need a separate number from id
    status = Column(String(20), nullable=False, server_default="received")
    order_time = Column(DATETIME, default=datetime.now)
    # ready_time = Column(DATETIME)
    estimated_minutes = Column(Integer)

    order = relationship("Order", back_populates="order_tracking")
