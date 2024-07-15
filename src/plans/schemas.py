"""
plans schemas
"""

from uuid import uuid4, UUID
from pydantic import BaseModel, Field
from datetime import datetime

# define your schemas here and rename< which already exists


class PlanCreateSchema(BaseModel):
    version: str 
    year: int
    number: int
    created_at: datetime
    updated_at: datetime 
    
    branch_uuid: UUID = Field(default_factory=uuid4) 
    status_id: int
    
    
class PlanGetSchema(PlanCreateSchema):
    uuid: UUID = Field(default_factory=uuid4)
    
    class Config:
        orm_mode = True
    