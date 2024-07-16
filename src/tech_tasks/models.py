"""
Database models of tech_tasks app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4
from sqlalchemy import JSON, UUID, Column, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class TechTask(Base):
    __tablename__ = "technical_task"

    uuid = Column(UUID, primary_key=True, default=uuid4)
    purchase_uuid = Column(UUID, ForeignKey('purchase.uuid'), nullable=False)
    data_json = Column(JSON, nullable=False)

    purchase = relationship("Purchase", foreign_keys=[purchase_uuid])