"""
Database models of way app
"""

# you need to import Base from [project_name].database 


from sqlalchemy import Column, Integer, String
from src.database import Base


class Way(Base):
    __tablename__ = "way"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    