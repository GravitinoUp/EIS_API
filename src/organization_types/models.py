"""
Database models of organization_types app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4

from sqlalchemy import UUID, Column, String
from src.database import Base


class OrganizationType(Base):
    __tablename__ = "organization_type"

    uuid = Column(UUID, primary_key=True, default=uuid4)
    name = Column(String, nullable=False)