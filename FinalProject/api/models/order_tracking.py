from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class OrderTracking(Base):
    __tablename__ = "order_tracking"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, unique=True)
    order_number = Column(String(50), nullable=False, unique=True, index=True)
    status = Column(String(20), nullable=False, server_default="received")
    time_estimation = Column(Integer)
    arrival_estimation = Column(DATETIME)

    order = relationship("Order", back_populates="order_tracking")
