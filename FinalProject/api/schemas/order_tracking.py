from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class OrderTrackingBase(BaseModel):
    order_number: str
    status: str = "received"
    time_estimation: Optional[int] = None
    arrival_estimation: Optional[datetime] = None


class OrderTrackingCreate(OrderTrackingBase):
    order_id: int


class OrderTrackingUpdate(BaseModel):
    order_number: Optional[str] = None
    status: Optional[str] = None
    time_estimation: Optional[int] = None
    arrival_estimation: Optional[datetime] = None


class OrderTracking(OrderTrackingBase):
    id: int
    order_id: int

    class ConfigDict:
        from_attributes = True
