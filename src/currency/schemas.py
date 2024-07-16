"""
currency schemas
"""

from pydantic import BaseModel


# define your schemas here and rename< which already exists
class CurrencyCreateSchema(BaseModel):
    name: str
    
    
class CurrencyGetSchema(CurrencyCreateSchema):
    code: int