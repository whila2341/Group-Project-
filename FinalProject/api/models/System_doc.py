from sqlalchemy import Column, Integer, String, Text, DATETIME
from datetime import datetime
from ..dependencies.database import Base


class SystemDocumentation(Base):
    __tablename__ = "system_documentation"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    last_updated = Column(DATETIME, nullable=False, default=datetime.utcnow)

    # Functions
    update_document = None
    view_document = None