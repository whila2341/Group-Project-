from typing import Optional
from pydantic import BaseModel


class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    ingredients: Optional[str] = None
    calories: Optional[int] = None
    price: float


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    ingredients: Optional[str] = None
    calories: Optional[int] = None
    price: Optional[float] = None


class MenuItem(MenuItemBase):
    id: int

    class ConfigDict:
        from_attributes = True
