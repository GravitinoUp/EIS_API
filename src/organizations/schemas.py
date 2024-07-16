"""
organizations schemas
"""

from uuid import UUID
from pydantic import BaseModel


# define your schemas here and rename< which already exists
class OrganizationBaseSchema(BaseModel):
    organization_type_uuid: UUID
    contact_person_uuid: UUID
    full_name: str
    short_name: str
    register_number: int
    bic: int
    address: str
    mail_address: str
    phone: str
    fax: str
    email: str
    orgn: str
    inn: int
    kpp: int
    okpo: int
    region: str
    additional_info: str
    web_site: str


class OrganizationCreateSchema(OrganizationBaseSchema):
    ...


class OrganizationGetSchema(OrganizationBaseSchema):
    uuid: UUID


class ItemUpdate(OrganizationBaseSchema):
    ...
