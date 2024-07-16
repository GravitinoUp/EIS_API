"""
Database models of purchase_type app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4
from sqlalchemy import UUID, Column, String

from src.database import Base


class PurchaseType(Base):
    __tablename__ = 'purchase_type'
    
    uuid = Column(UUID, primary_key=True, default=uuid4)
    name = Column(String, nullable=False)