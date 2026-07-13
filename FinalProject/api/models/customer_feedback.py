from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class CustomerFeedback(Base):
    __tablename__ = "customer_feedback"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, unique=True)
    star_rating = Column(Integer, nullable=False)
    written_review = Column(String(1000))

    order = relationship("Order", back_populates="feedback")
