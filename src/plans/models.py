"""
Database models of plans app
"""

# you need to import Base from [project_name].database 
from datetime import datetime
from sqlalchemy import UUID, Column, Enum, Integer, DateTime, ForeignKey, BIGINT
from sqlalchemy.orm import relationship

from src.database import Base, generate_unique_id


class Plan(Base):
    __tablename__ = "plans"

    id = Column(BIGINT, primary_key=True, default=generate_unique_id)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    year = Column(Integer, nullable=False)
    status = Column(
        Enum('На публикации', 'Опубликован', 'Не опубликован', name="status"), 
        nullable=False,
        default='На публикации'
    )
    

class PlanPurchase(Base):
    __tablename__ = "plan_purchases"
    
    id = Column(BIGINT, primary_key=True, default=generate_unique_id)
    plan_id = Column(BIGINT, ForeignKey("plans.id", ondelete='CASCADE'))
    purchase_id = Column(BIGINT, ForeignKey("purchases.id", ondelete='CASCADE'))
    
    plan = relationship(
        "Plan", 
        foreign_keys=[plan_id], 
        backref="plan_purchases", 
        passive_deletes=True
    )
    purchase = relationship(
        "Purchase", 
        foreign_keys=[purchase_id], 
        backref="plan_purchases", 
        passive_deletes=True
    )


# Статусы: на публикации; не опубликован; опубликован; 