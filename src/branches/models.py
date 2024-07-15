"""
Database models of branches app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4
from sqlalchemy import Column, String, UUID

from src.database import Base

    
class Branch(Base):
    __tablename__ = "branch"
    
    uuid = Column(UUID, primary_key=True,  default=uuid4)
    name = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=True)