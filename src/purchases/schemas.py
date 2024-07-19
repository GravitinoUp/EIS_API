"""
purchase schemas
"""

from uuid import UUID
from pydantic import BaseModel


class PurchaseCreateSchema(BaseModel):
    year: int
    expense_type_code: int
    okpd2: int

    expense_total: float
    expense_first_year: float
    expense_second_year: float
    expense_third_year: float
    expense_next_years: float
    
    
class PurchaseGetSchema(PurchaseCreateSchema):
    id: int
    status: str

