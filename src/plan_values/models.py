"""
Database models of plan_values app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4
from sqlalchemy import UUID, Column, Double, ForeignKey, Integer
from sqlalchemy.orm import relationship

from src.database import Base


class PlanValue(Base):
    __tablename__ = "plan_value"

    uuid = Column(UUID, primary_key=True, default=uuid4)
    purchase_uuid = Column(UUID, ForeignKey("purchase.uuid"), nullable=False)
    year = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)
    avg_price = Column(Double, nullable=False)

    purchase = relationship("Purchase", backref="plan_value")
