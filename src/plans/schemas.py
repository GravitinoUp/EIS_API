"""
plans schemas
"""

from datetime import datetime
from pydantic import BaseModel
from typing import List

from src.purchases.schemas import PurchaseCreateSchema, PurchaseGetSchema


class PlanBaseSchema(BaseModel):
    year: int
    
    
class PlanCreateSchema(PlanBaseSchema):
    purchases: List[PurchaseCreateSchema]
    
    
class PlanGetSchema(PlanBaseSchema):
    id: int
    created_at: datetime
    status: str
    version: int
    purchases: List[PurchaseGetSchema]