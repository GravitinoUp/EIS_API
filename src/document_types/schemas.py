"""
document_types schemas
"""

from uuid import UUID
from pydantic import BaseModel


# define your schemas here and rename< which already exists
class DocumentTypeBaseSchema(BaseModel):
    name: str


class DocumentTypeCreateSchema(DocumentTypeBaseSchema):
    ...


class DocumentTypeGetSchema(DocumentTypeBaseSchema):
    uuid: UUID

