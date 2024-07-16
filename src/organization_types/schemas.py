"""
organization_types schemas
"""

from uuid import UUID
from pydantic import BaseModel


# define your schemas here and rename< which already exists
class OrganizationTypeBaseSchema(BaseModel):
    name: str


class OrganizationTypeCreateSchema(OrganizationTypeBaseSchema):
    ...


class OrganizationTypeGetSchema(OrganizationTypeBaseSchema):
    uuid: UUID

