"""
purchase_steps schemas
"""

from uuid import UUID
from pydantic import BaseModel


# define your schemas here and rename< which already exists
class PurchaseStepCreateSchema(BaseModel):
    name: str
    
class PurchcaseStepGetSchema(BaseModel):
    uuid: UUID
