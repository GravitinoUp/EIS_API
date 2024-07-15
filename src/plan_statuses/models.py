"""
Database models of plan_statuses app
"""

# you need to import Base from [project_name].database 
from sqlalchemy import Column, Integer, String

from src.database import Base

class PlanStatus(Base):
    __tablename__ = "plan_status"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)