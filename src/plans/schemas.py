"""
plans schemas
"""

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from typing import List, Optional

from src.purchases.schemas import PurchaseCreateSchema, PurchaseGetSchema


class PlanBaseSchema(BaseModel):
    year: int
    
    
class PlanCreateSchema(PlanBaseSchema):
    purchases: List[PurchaseCreateSchema]
    
    
class PlanGetSchema(PlanBaseSchema):
    id: int
    created_at: datetime
    status: str
    purchases: List[PurchaseGetSchema]