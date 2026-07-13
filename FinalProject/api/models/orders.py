from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=False)
    delivery_or_takeout = Column(String(20), nullable=False, server_default="takeout")
    delivery_address = Column(String(300))
    summary = Column(String(300))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    promo_code_id = Column(Integer, ForeignKey("promo_codes.id"), nullable=True)

    promo_code = relationship("PromoCode", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")
    payment = relationship("Payment", back_populates="order", uselist=False)
    order_tracking = relationship("OrderTracking", back_populates="order", uselist=False)
    feedback = relationship("CustomerFeedback", back_populates="order", uselist=False)
