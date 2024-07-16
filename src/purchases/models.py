"""
Database models of purchases app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4
from sqlalchemy import Boolean, Column, UUID, DateTime, Integer, Double, String, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class Purchase(Base):
    __tablename__ = "purchase"
    
    uuid = Column(UUID, primary_key=True, default=uuid4)
    plan_uuid = Column(UUID, ForeignKey("plan.uuid"), nullable=False)
    name = Column(String, nullable=False)
    kosgu_uuid = Column(UUID, nullable=False)
    purchase_offer_number = Column(Integer, nullable=True)
    okpd_uuid = Column(UUID, ForeignKey("okpd.uuid"), nullable=False)
    object_name = Column(String, nullable=False)
    okei_id = Column(Integer, ForeignKey("okei.id"), nullable=False)
    result_name = Column(String, nullable=True)
    npa_date = Column(DateTime, nullable=False)
    npa_number = Column(String, nullable=False)
    start_max_price = Column(Double, nullable=False)
    limit_uuid = Column(UUID,  nullable=False)
    purchase_public_discussion = Column(String, nullable=True)
    authorized_instution = Column(String, nullable=True)
    organizer_name = Column(String, nullable=True)
    placement_month = Column(Integer, nullable=True)
    way_id = Column(Integer, ForeignKey("way.id"), nullable=False)
    small_buisness = Column(String, nullable=True)
    price_value = Column(Double, nullable=False)
    savings = Column(Double, nullable=True)
    contract_number = Column(String, nullable=False)
    contract_date = Column(DateTime, nullable=False)
    contragent = Column(String, nullable=True)
    approval_letter = Column(String, nullable=True)
    purchase_type_uuid = Column(UUID, ForeignKey("purchase_type.uuid"), nullable=False)
    initiator_uuid = Column(UUID, ForeignKey("user.uuid"), nullable=False)
    executor_uuid = Column(UUID, ForeignKey("organization.uuid"), nullable=False)
    purchase_id = Column(Integer, nullable=False)
    contract_id =  Column(Integer, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_application_date = Column(DateTime, nullable=False)
    executor_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=False)
    end_price = Column(Double, nullable=False)
    currency_code = Column(String, ForeignKey("currency.code"), nullable=False)
    purchase_step_uuid = Column(UUID, ForeignKey("purchase_step.uuid"), nullable=False)
    delivery_address = Column(String, nullable=True)
    is_organization_fund = Column(Boolean, nullable=True)
    application_enforcement = Column(String, nullable=True)
    is_unilateral_refusion = Column(Boolean, nullable=True)
    contract_enforcement = Column(String, nullable=True)
    quality_gurantee_period = Column(Integer, nullable=True)
    manufacturer_guarantee = Column(Integer, nullable=True)
    warranty_obligations_enforcement = Column(String, nullable=True)
    additionl_info = Column(String, nullable=True)
    
    okpd = relationship("OKPD", foreign_keys=[okpd_uuid])
    okei = relationship("OKEI", foreign_keys=[okei_id])
    way = relationship("Way", foreign_keys=[way_id])
    purchase_type = relationship("PurchaseType", foreign_keys=[purchase_type_uuid])
    initiator = relationship("User", foreign_keys=[initiator_uuid])
    executor = relationship("Organization", foreign_keys=[executor_uuid])
    currency = relationship("Currency", foreign_keys=[currency_code])
    purchase_step =  relationship("PurchaseStep", foreign_keys=[purchase_step_uuid])
    