"""
Database models of purchase_steps app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4
from sqlalchemy import UUID, Column, String

from src.database import Base


class PurchaseStep(Base):
    __tablename__ = "purchase_step"
    
    uuid = Column(UUID, primary_key=True, default=uuid4)
    name = Column(String)