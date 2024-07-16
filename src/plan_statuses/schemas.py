"""
plan_statuses schemas
"""

from pydantic import BaseModel


# define your schemas here and rename< which already exists
    
    
class PlanStatusCreateSchema(BaseModel):
    name: str
    
    
class PlanStatusGetSchema(PlanStatusCreateSchema):
    id: int