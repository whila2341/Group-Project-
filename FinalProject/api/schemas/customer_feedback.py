from typing import Optional
from pydantic import BaseModel, Field


class CustomerFeedbackBase(BaseModel):
    star_rating: int = Field(ge=1, le=5)
    written_review: Optional[str] = None


class CustomerFeedbackCreate(CustomerFeedbackBase):
    order_id: int


class CustomerFeedbackUpdate(BaseModel):
    star_rating: Optional[int] = Field(default=None, ge=1, le=5)
    written_review: Optional[str] = None


class CustomerFeedback(CustomerFeedbackBase):
    id: int
    order_id: int

    class ConfigDict:
        from_attributes = True
