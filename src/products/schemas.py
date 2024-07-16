"""
products schemas
"""

from uuid import UUID
from pydantic import BaseModel


# define your schemas here and rename< which already exists
class ProductCreateSchema(BaseModel):
    name: str
    okei_id: int
    price: float
    

class ProductGetSchema(ProductCreateSchema):
    uuid: UUID