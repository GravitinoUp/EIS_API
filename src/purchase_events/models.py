"""
Database models of purchase_events app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4
from sqlalchemy import UUID, Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from src.database import Base


class PurchaseEvent(Base):
    __tablename__ = "purchase_event"
    
    uuid = Column(UUID, primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    purchase_uuid = Column(UUID, ForeignKey("purchase.uuid"), nullable=False)
    user_uuid = Column(UUID, ForeignKey("user.uuid"), nullable=False)   
    
    purchase = relationship("Purchase", foreign_keys=[purchase_uuid])
    user = relationship("User", foreign_keys=[user_uuid])