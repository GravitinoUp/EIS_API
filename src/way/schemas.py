"""
way schemas
"""

from pydantic import BaseModel


# define your schemas here and rename< which already exists
class WayCreateSchema(BaseModel):
    name: str
    

class WayGetSchema(BaseModel):
    id: int