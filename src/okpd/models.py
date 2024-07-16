"""
Database models of okpd app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4
from sqlalchemy import UUID, Column, String

from src.database import Base


class OKPD(Base):
    __tablename__ = 'okpd'
    
    uuid = Column(UUID,  primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    code = Column(String, nullable=True)
    data = Column(String, nullable=True)