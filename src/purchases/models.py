"""
Database models of purchases app
"""
 
from sqlalchemy import BIGINT, Column, Double, Enum, Integer, String

from src.database import Base, generate_unique_id


class Purchase(Base):
    __tablename__ = "purchases"
    
    id = Column(BIGINT, primary_key=True, default=generate_unique_id)
    year = Column(Integer, nullable=False)
    status = Column(
        Enum('На публикации', 'Опубликован', 'Не опубликован', name="status"), 
        nullable=False,
        default='На публикации'
    )
    expense_type_code = Column(Integer, nullable=False)
    okpd2 = Column(String(30), nullable=False)
    
    expense_total = Column(Double, nullable=False)
    expense_first_year = Column(Double, nullable=False)
    expense_second_year = Column(Double, nullable=False)
    expense_third_year = Column(Double, nullable=False)
    expense_next_years = Column(Double, nullable=False)
    
    organization_name = Column(String, nullable=True)
    organization_inn = Column(String, nullable=True)
    organization_kpp = Column(String, nullable=True)
    organization_okpo = Column(String, nullable=True)