from datetime import datetime
from typing import Optional
from pydantic import BaseModel, computed_field
from datetime import datetime, timedelta

class OrderTrackingBase(BaseModel):
    # order_number: str
    status: str = "received"
    estimated_minutes: Optional[int] = None

class OrderTrackingCreate(OrderTrackingBase):
    order_id: int

class OrderTrackingUpdate(BaseModel):
    # order_number: Optional[str] = None
    status: Optional[str] = None
    estimated_minutes: Optional[int] = None


class OrderTracking(OrderTrackingBase):
    id: int
    order_id: int
    order_time: datetime

    @computed_field
    @property
    def ready_time(self) -> Optional[datetime]:
        if self.estimated_minutes is None:
            return None
        return self.order_time + timedelta(minutes=self.estimated_minutes)

    class ConfigDict:
        from_attributes = True
