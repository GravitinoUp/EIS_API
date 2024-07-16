"""
documents schemas
"""

from uuid import UUID
from pydantic import BaseModel


# define your schemas here and rename< which already exists
class DocumentBaseSchema(BaseModel):
    name: str
    document_type_uuid: UUID
    purchase_uuid: UUID
    executor_uuid: UUID
    customer_uuid: UUID
    person_executor_uuid: UUID
    person_customer_uuid: UUID


class DocumentCreateSchema(DocumentBaseSchema):
    ...


class DocumentGetSchema(DocumentBaseSchema):
    uuid: UUID
