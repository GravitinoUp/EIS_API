"""
plans schemas
"""

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from typing import List


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
    uuid: UUID


class PlanBaseSchema(BaseModel):
    created_at: datetime
    year: int
    status: str
    
    
class PlanCreateSchema(PlanBaseSchema):
    purchases: List[PurchaseCreateSchema]
    
    
class PlanGetSchema(PlanBaseSchema):
    uuid: UUID
    purchases: List[PurchaseGetSchema]