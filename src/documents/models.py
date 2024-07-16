"""
Database models of documents app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4
from sqlalchemy import UUID, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from src.database import Base


class Document(Base):
    __tablename__ = 'document'

    uuid = Column(UUID, primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    document_type_uuid = Column(UUID, ForeignKey('document_type.uuid'), nullable=False)
    purchase_uuid = Column(UUID, ForeignKey('purchase.uuid'), nullable=False)
    executor_uuid = Column(UUID, ForeignKey('organization.uuid'), nullable=False)
    customer_uuid = Column(UUID, ForeignKey('organization.uuid'), nullable=False)
    person_executor_uuid = Column(UUID, ForeignKey('user.uuid'), nullable=False)
    person_customer_uuid = Column(UUID, ForeignKey('user.uuid'), nullable=False)
    
    document_type = relationship('DocumentType', foreign_keys=[document_type_uuid])
    purchase = relationship('Purchase', foreign_keys=[purchase_uuid])
    executor =  relationship('Organization', foreign_keys=[executor_uuid])
    customer =  relationship('Organization', foreign_keys=[customer_uuid])
    person_executor =  relationship('User', foreign_keys=[person_executor_uuid])
    person_customer =  relationship('User', foreign_keys=[person_customer_uuid])