"""
okei schemas
"""

from pydantic import BaseModel
from typing import Optional


# define your schemas here and rename< which already exists
class OKEICreateSchema(BaseModel):
    full_name: str
    short_name: Optional[str] 
    
    
class OKEIGetSchema(OKEICreateSchema):
    id: int