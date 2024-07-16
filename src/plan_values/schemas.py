"""
plan_values schemas
"""

from uuid import UUID
from pydantic import BaseModel


# define your schemas here and rename< which already exists
class PlanValueBaseSchema(BaseModel):
    purchase_uuid: UUID
    year: int
    count: int
    avg_price: float


class PlanValueCreateSchema(PlanValueBaseSchema):
    ...


class PlanValueGetSchema(PlanValueBaseSchema):
    uuid: UUID


class ItemUpdate(PlanValueBaseSchema):
    ...

