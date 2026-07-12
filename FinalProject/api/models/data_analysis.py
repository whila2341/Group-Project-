from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME
from datetime import datetime
from ..dependencies.database import Base


class DataAnalysis(Base):
    __tablename__ = "data_analysis"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    report_name = Column(String(100), nullable=False)
    metric = Column(String(100), nullable=False)
    value = Column(DECIMAL(10,2), nullable=False)
    date = Column(DATETIME, nullable=False, default=datetime.utcnow)

    # Functions
    generate_report = None
    view_statistics = None