"""
branches schemas
"""

from uuid import uuid4, UUID
from pydantic import BaseModel, Field
from typing import Optional


# define your schemas here and rename< which already exists


class BranchCreateSchema(BaseModel):
    name: str
    address: Optional[str]
    

class BranchGetSchema(BranchCreateSchema):
    uuid: UUID = Field(default_factory=uuid4)