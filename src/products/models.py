"""
Database models of products app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4
from sqlalchemy import UUID, Column, Double, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base


class Product(Base):
    __tablename__ = "product"
    
    uuid = Column(UUID, primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    price = Column(Double, nullable=False)
    okei_id = Column(Integer, ForeignKey("okei.id"), nullable=False)
    
    okei = relationship("OKEI", foreign_keys=[okei_id])