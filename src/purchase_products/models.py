"""
Database models of purchase_products app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4
from sqlalchemy import UUID, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from src.database import Base

class PurchaseProduct(Base):
    __tablename__ = 'purchase_product'
    
    purchase_uuid = Column(UUID, primary_key=True, default=uuid4)
    product_uuid = Column(UUID, ForeignKey('product.uuid'), primary_key=True)
    quantity = Column(Integer, nullable=False)

    product = relationship('Product', foreign_keys=[product_uuid])
