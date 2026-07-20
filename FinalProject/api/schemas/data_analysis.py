from pydantic import BaseModel
from datetime import datetime


class DataAnalysisBase(BaseModel):
    report_name: str
    metric: str
    value: float


class DataAnalysisCreate(DataAnalysisBase):
    pass

class DataAnalysisResponse(DataAnalysisBase):
    id: int
    generated_at: datetime

    class Config:
        from_attributes = True

class DataAnalysisUpdate(BaseModel):
    report_name: str | None = None
    metric: str | None = None
    value: float | None = None