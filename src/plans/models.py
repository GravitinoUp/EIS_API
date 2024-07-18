"""
Database models of plans app
"""

# you need to import Base from [project_name].database 
from datetime import datetime
from uuid import uuid4
from sqlalchemy import UUID, Column, Double, Enum, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class Plan(Base):
    __tablename__ = "plans"

    uuid = Column(UUID, primary_key=True, default=uuid4)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    year = Column(Integer, nullable=False)
    status = Column(
        Enum('На публикации', 'Опубликован', 'Не опубликован', name="status"), 
        nullable=False,
        default='На публикации'
    )
    

class PlanPurchase(Base):
    __tablename__ = "plan_purchases"
    
    uuid = Column(UUID, primary_key=True, default=uuid4)
    plan_uuid = Column(UUID, ForeignKey("plans.uuid", ondelete='CASCADE'))
    purchase_uuid = Column(UUID, ForeignKey("purchases.uuid", ondelete='CASCADE'))
    
    plan = relationship(
        "Plan", 
        foreign_keys=[plan_uuid], 
        backref="plan_purchases", 
        passive_deletes=True
    )
    purchase = relationship(
        "Purchase", 
        foreign_keys=[purchase_uuid], 
        backref="plan_purchases", 
        passive_deletes=True
    )


# Статусы: на публикации; не опубликован; опубликован; 