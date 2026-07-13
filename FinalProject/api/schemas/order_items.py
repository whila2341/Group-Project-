from typing import Optional
from pydantic import BaseModel
from .menu_items import MenuItem


class OrderItemBase(BaseModel):
    quantity: int = 1


class OrderItemCreate(OrderItemBase):
    order_id: int
    menu_item_id: int


class OrderItemUpdate(BaseModel):
    order_id: Optional[int] = None
    menu_item_id: Optional[int] = None
    quantity: Optional[int] = None


class OrderItem(OrderItemBase):
    id: int
    order_id: int
    menu_item: MenuItem = None

    class ConfigDict:
        from_attributes = True
