"""
purchase_type schemas
"""

from uuid import UUID
from pydantic import BaseModel


# define your schemas here and rename< which already exists
class PurchaseTypeCreateSchema(BaseModel):
    name: str
    

class PurchaseTypeGetSchema(PurchaseTypeCreateSchema):
    uuid: UUID