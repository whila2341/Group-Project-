from pydantic import BaseModel
from datetime import datetime

class PromoCodeBase(BaseModel):
    promo_code: str
    discount: int
    expiration_date: datetime

class PromoCodeCreate(PromoCodeBase):
    pass


class PromoCodeResponse(PromoCodeBase):
    id: int
    updated_at: datetime

    class Config:
        from_attributes = True
