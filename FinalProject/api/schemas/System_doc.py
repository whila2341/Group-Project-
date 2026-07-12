from pydantic import BaseModel
from datetime import datetime


class SystemDocumentationBase(BaseModel):
    title: str
    category: str
    content: str


class SystemDocumentationCreate(SystemDocumentationBase):
    pass


class SystemDocumentationResponse(SystemDocumentationBase):
    id: int
    updated_at: datetime

    class Config:
        from_attributes = True