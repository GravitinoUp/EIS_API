"""
Database models of purchases app
"""

# you need to import Base from [project_name].database 
from uuid import uuid4
from sqlalchemy import UUID, Column, Double, Enum, Integer, String
from src.database import Base


class Purchase(Base):
    __tablename__ = "purchases"
    
    uuid = Column(UUID, primary_key=True, default=uuid4)
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