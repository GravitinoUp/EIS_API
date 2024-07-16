"""
Database models of currency app
"""

# you need to import Base from [project_name].database 
from sqlalchemy import Column, Integer, String
from src.database import Base


class Currency(Base):
    __tablename__ = "currency"
    
    code = Column(Integer, primary_key=True)
    name = Column(String)