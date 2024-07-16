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
    person_executor_uuid = Column(UUID, ForeignKey('user.uuid'), nullable=False)
    
    document_type = relationship('DocumentType', backref='document')
    purchase = relationship('Purchase', backref='document')
    executor = relationship('Organization', backref='document')
    customer = relationship('Organization', backref='document')
    person_executor = relationship('User', backref='document')
    person_customer = relationship('User', backref='document')