"""
purchase_products schemas
"""

from uuid import UUID
from pydantic import BaseModel


# define your schemas here and rename< which already exists
class PurchaseProductSchema(BaseModel):
    purchase_uuid: UUID
    product_uuid: UUID
    quantity: int