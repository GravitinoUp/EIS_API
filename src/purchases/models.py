"""
Database models of purchases app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4
from sqlalchemy import Column, UUID, DateTime, Integer, Double, String, ForeignKey

from src.database import Base


class Purchase(Base):
    __tablename__ = "purchase"
    
    uuid = Column(UUID, primary_key=True, default=uuid4)
    plan_uuid = Column(UUID, ForeignKey("plan.uuid"), nullable=False)
    name = Column(String, nullable=False)
    kosgu_uuid = Column(UUID, nullable=True)
    purchase_offer_number = Column(Integer, nullable=True)
    okpd_uuid = Column(UUID, ForeignKey("okpd.uuid"), nullable=True)
    object_name = Column(String, nullable=True)
    okei_uuidd = Column(UUID, ForeignKey("okei.uuid"), nullable=True)
    result_name = Column(String, nullable=True)
    npa_date = Column(DateTime, nullable=True)
    npa_number = Column(String, nullable=True)
    start_max_price = Column(Double, nullable=True)
    limit_uuid = Column(UUID,  nullable=True)
    purchase_public_discussion = Column(String, nullable=True)
    authorized_instution = Column(String, nullable=True)
    organizer_name = Column(String, nullable=True)
    placement_month = Column(Integer, nullable=True)
    way_id = Column(Integer, ForeignKey("way.id"), nullable=True)
    small_buisness = Column(String, nullable=True)
    price_value = Column(Double, nullable=True)
    savings = Column(Double, nullable=True)
    contract_number = Column(String, nullable=True)
    contract_date = Column(DateTime, nullable=True)
    contragent = Column(String, nullable=True)
    approval_letter = Column(String, nullable=True)
    purchase_type_uuid =  Column(UUID, ForeignKey("purchase_type.uuid"), nullable=False)
    
    