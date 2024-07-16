"""
tech_tasks schemas
"""

from uuid import UUID
from pydantic import BaseModel


# define your schemas here and rename< which already exists
class TechTaskBaseSchema(BaseModel):
    purchase_uuid: UUID
    data_json: dict


class TechTaskCreateSchema(TechTaskBaseSchema):
    ...


class TechTaskGetSchema(TechTaskBaseSchema):
    uuid: UUID


