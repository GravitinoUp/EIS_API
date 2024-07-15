"""
Database models of plans app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4
from src.database import Base

from datetime import datetime
from sqlalchemy import UUID, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Plan(Base):
    __tablename__ = "plan"

    uuid = Column(UUID, primary_key=True, default=uuid4)
    number = Column(Integer, nullable=True)
    version = Column(String, nullable=True, default="1.0")
    year = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=True)
    
    branch_uuid = Column(UUID, ForeignKey('branch.uuid'), nullable=False)
    status_id = Column(Integer, ForeignKey('plan_status.id'), nullable=False)

    status = relationship("PlanStatus", backref="plan")
    branch = relationship("Branch", backref="plan")
    