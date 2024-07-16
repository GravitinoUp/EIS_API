"""
Database models of organizations app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4
from sqlalchemy import UUID, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base


class Organization(Base):
    __tablename__ = "organization"

    uuid = Column(UUID, primary_key=True, default=uuid4)
    organization_type_uuid = Column(UUID, ForeignKey('organization_type.uuid'), nullable=False)
    contact_person_uuid = Column(UUID, ForeignKey('user.uuid'), nullable=False)
    full_name = Column(String(50), nullable=False)
    short_name = Column(String(20), nullable=False)
    register_number = Column(Integer, nullable=False, unique=True)
    bic = Column(Integer, nullable=False, unique=True)
    address = Column(String, nullable=False)
    mail_address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    fax = Column(String, nullable=False)
    email = Column(String, nullable=False)
    orgn = Column(String, nullable=False)
    inn = Column(Integer, nullable=False)
    kpp = Column(Integer, nullable=False)
    okpo = Column(Integer, nullable=False)
    region = Column(String, nullable=False)
    additional_info = Column(String, nullable=False)
    web_site = Column(String, nullable=False)

    organization_type = relationship("OrganizationType", foreign_keys=[organization_type_uuid])
    contact_person = relationship("User", foreign_keys=[contact_person_uuid])

    
