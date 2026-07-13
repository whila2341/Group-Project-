from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_items import OrderItem
from .promo_codes import PromoCode
from .payment import Payment
from .order_tracking import OrderTracking
from .customer_feedback import CustomerFeedback


class OrderBase(BaseModel):
    customer_name: str
    phone_number: str
    delivery_or_takeout: str
    delivery_address: Optional[str] = None
    summary: Optional[str] = None


class OrderCreate(OrderBase):
    promo_code_id: Optional[int] = None


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    phone_number: Optional[str] = None
    delivery_or_takeout: Optional[str] = None
    delivery_address: Optional[str] = None
    summary: Optional[str] = None
    promo_code_id: Optional[int] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    promo_code_id: Optional[int] = None
    promo_code: Optional[PromoCode] = None
    order_items: list[OrderItem] = None
    payment: Optional[Payment] = None
    order_tracking: Optional[OrderTracking] = None
    feedback: Optional[CustomerFeedback] = None

    class ConfigDict:
        from_attributes = True
