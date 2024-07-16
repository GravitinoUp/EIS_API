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
    purchase_type_uuid = Column(UUID, ForeignKey("purchase_type.uuid"), nullable=False)
    initiator_uuid = Column(UUID, ForeignKey("user.uuid"), nullable=False)
    executor_uuid = Column(UUID, ForeignKey("organization.uuid"), nullable=False)
    purchase_id = Column(Integer, nullable=True)
    contract_id =  Column(Integer, nullable=True)
    start_date = Column(DateTime, nullable=False)
    end_application_date = Column(DateTime, nullable=False)
    executor_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=False)
    end_price = Column(Double, nullable=True)
    currency_code = Column(String, ForeignKey("currency.code"), nullable=False)
    purchase_step_uuid = Column(UUID, ForeignKey("purchase_step.uuid"), nullable=False)
    delivery_address = Column(String, nullable=False)
    is_organization_fund = Column(Boolean, nullable=True)
    application_enforcement = Column(String, nullable=True)
    is_unilateral_refusion = Column(Boolean, nullable=True)
    contract_enforcement = Column(String, nullable=True)
    quality_gurantee_period = Column(Integer, nullable=True)
    manufacturer_guarantee = Column(Integer, nullable=True)
    warranty_obligations_enforcement = Column(String, nullable=True)
    additionl_info = Column(String, nullable=True)
    
    okpd = relationship("OKPD", backref="purchase")
    okei = relationship("OKEI", backref="purchase")
    way = relationship("Way", backref="purchase")
    purchase_type = relationship("PurchaseType", backref="purchase")
    initiator = relationship("User", backref="purchase")
    executor = relationship("Organization", backref="purchase")
    currency = relationship("Currency", backref="purchase")
    purchase_step =  relationship("PurchaseStep", backref="purchase")
    