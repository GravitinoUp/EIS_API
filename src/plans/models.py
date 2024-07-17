"""
Database models of plans app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4
from sqlalchemy import UUID, Column, Double, Integer, String
from src.database import Base


class Plan(Base):
    __tablename__ = "plans"

    uuid = Column(UUID, primary_key=True, default=uuid4)
    year = Column(Integer, nullable=False)
    expense_type_code = Column(Integer, nullable=False)
    okpd2 = Column(String(20), nullable=False)

    expense_total = Column(Double, nullable=False)
    expense_fisrt_year = Column(Double, nullable=False)
    expense_second_year = Column(Double, nullable=False)
    expense_third_year = Column(Double, nullable=False)
    expense_next_years = Column(Double, nullable=False)
