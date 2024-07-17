"""
Database models of plans app
"""

# you need to import Base from [project_name].database 
from datetime import datetime
from uuid import uuid4
from sqlalchemy import UUID, Column, Double, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class Plan(Base):
    __tablename__ = "plans"

    uuid = Column(UUID, primary_key=True, default=uuid4)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    year = Column(Integer, nullable=False)
    status = Column(String, nullable=False)


class Purchase(Base):
    __tablename__ = "purchases"
    
    uuid = Column(UUID, primary_key=True, default=uuid4)
    year = Column(Integer, nullable=False)
    expense_type_code = Column(Integer, nullable=False)
    okpd2 = Column(String(30), nullable=False)
    expense_total = Column(Double, nullable=False)
    expense_first_year = Column(Double, nullable=False)
    expense_second_year = Column(Double, nullable=False)
    expense_third_year = Column(Double, nullable=False)
    expense_next_years = Column(Double, nullable=False)
    

class PlanPurchase(Base):
    __tablename__ = "plan_purchases"
    
    plan_uuid = Column(UUID, ForeignKey("plans.uuid"), primary_key=True)
    purchase_uuid = Column(UUID, ForeignKey("purchases.uuid"))
    
    plan = relationship("Plan", foreign_keys=[plan_uuid])
    purchase = relationship("Purchase", foreign_keys=[purchase_uuid])