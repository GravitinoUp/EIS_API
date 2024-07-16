"""
Database models of okei app
"""

# you need to import Base from [project_name].database 
from sqlalchemy import Column, Integer, String

from src.database import Base


class OKEI(Base):
    __tablename__ = 'okei'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    short_name = Column(String, nullable=True)