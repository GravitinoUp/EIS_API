"""
Database models of plans app
"""

# you need to import Base from [project_name].database 
from datetime import datetime

from sqlalchemy import UUID, Column, ForeignKey, Integer, String, DateTime, Double
from sqlalchemy.orm import relationship
from src.database import Base


class Plan(Base):
    __tablename__ = "plan"

    uuid = Column(UUID, primary_key=True)
    status_id = Column(Integer, ForeignKey('plan_status.id'), nullable=False)
    version = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())

    status = relationship("PlanStatus", backref='plan')


class PlanStatus(Base):
    __tablename__ = "plan_status"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class PlanPosition(Base):
    __tablename__ = "plan_position"

    uuid = Column(UUID, nullable=False, primary_key=True)
    plan_uuid = Column(UUID, ForeignKey('plan.uuid'), nullable=False)
    purchase_name = Column(String(50), nullable=False)
    purchase_price = Column(Double, nullable=False)
    purchase_date = Column(DateTime, nullable=False, default=datetime.now())
    user_uuid = Column(UUID, ForeignKey('user.uuid'), nullable=False)
    kosgu = Column(String(50), nullable=False)
    purchase_offer_number = Column(Integer, nullable=False)
    object_name = Column(String(50), nullable=False)
    result_name = Column(String(50), nullable=False)
    npa_date = Column(DateTime, nullable=False, default=datetime.now())
    npa_number = Column(Integer, nullable=False)
    current_year_plan_count = Column(Integer, nullable=False)
    current_year_avg_price = Column(Double, nullable=False)
    first_year_plan_count = Column(Integer, nullable=False)
    first_year_avg_price = Column(Double, nullable=False)
    second_year_plan_count = Column(Integer, nullable=False)
    second_year_avg_price = Column(Double, nullable=False)
    next_years_plan_count = Column(Integer, nullable=False)
    next_years_avg_price = Column(Double, nullable=False)
    start_max_price = Column(Double, nullable=False)
    total_limit = Column(Integer, nullable=False)
    current_year_limit = Column(Integer, nullable=False)
    first_year_limit = Column(Integer, nullable=False)
    second_year_limit = Column(Integer, nullable=False)
    next_years_limit = Column(Integer, nullable=False)
    public_purchase_description = Column(String, nullable=False)
    auth_institution = Column(String, nullable=False)
    organizer_name = Column(String, nullable=False)
    placement_month = Column(Integer, nullable=False)
    way_id = Column(Integer, ForeignKey('way.id'), nullable=False)
    small_business = Column(String, nullable=False)
    initiator = Column(String, nullable=False)
    price_value = Column(Double, nullable=False)
    savings = Column(Double, nullable=False)
    contract_number = Column(Integer, nullable=False)
    contarct_date = Column(DateTime, nullable=False, default=datetime.now())
    contragent = Column(String, nullable=False)
    approval_letter = Column(String, nullable=False)

    plan = relationship("Plan", backref='plan_position')
    user = relationship("User", backref='plan_position')
    way = relationship("Way", backref='plan_position')


class Way(Base):
    __tablename__ = "way"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class PlanEvent(Base):
    __tablename__ = "plan_event"

    uuid = Column(UUID, primary_key=True)
    plan_uuid = Column(UUID, ForeignKey('plan.uuid'), nullable=False)
    user_uuid = Column(UUID, ForeignKey('user.uuid'), nullable=False)
    name = Column(String, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.now())

    user = relationship("User", backref='plan_event')
    plan = relationship("Plan", backref='plan_event')
