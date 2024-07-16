"""
plans schemas
"""

from uuid import uuid4, UUID
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# define your schemas here and rename< which already exists


class PlanCreateSchema(BaseModel):
    version:  Optional[str] = "1.0"
    year: int
    number: int
    created_at: datetime
    updated_at: datetime 
    
    branch_uuid: UUID = Field(default_factory=uuid4) 
    status_id: int = Field(default=1, ge=1)
    
    
class PlanGetSchema(PlanCreateSchema):
    uuid: UUID = Field(default_factory=uuid4)
    