"""
branches schemas
"""

from uuid import uuid4, UUID
from pydantic import BaseModel, Field


# define your schemas here and rename< which already exists


class BranchCreateSchema(BaseModel):
    name: str
    address: str = Field(default=None)
    

class BranchGetSchema(BranchCreateSchema):
    uuid: UUID = Field(default_factory=uuid4)
    
    class Config:
        orm_mode = True