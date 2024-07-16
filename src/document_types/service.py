"""
document_types app service and repository
"""

from uuid import UUID
from sqlalchemy.exc import IntegrityError

from src.document_types.schemas import DocumentTypeCreateSchema
from src.document_types.models import DocumentType
from src.exceptions import NotFoundException, ConflictException
from src.abstract_repository import SQLAlchemyRepository, AbstractRepository


# define your service here and rename if it's necessary
# WARNING: if this sevice doesn't work with DB,
# you may implement only your own service

class DocumentTypeRepository(SQLAlchemyRepository):
    model = DocumentType


class DocumentTypeService:
    def __init__(self, repository: AbstractRepository):
        self.repo: AbstractRepository = repository()

    async def get_all(self, limit: int, offset: int):
        if document_type := await self.repo.get_all(limit, offset):
            return document_type
        raise NotFoundException()

    async def get_by_uuid(self, uuid: UUID):
        if document_type := await self.repo.get_by_uuid(uuid):
            return document_type
        raise NotFoundException()

    async def delete_by_uuid(self, uuid: UUID):
        if document_type := await self.repo.delete_by_uuid(uuid):
            return document_type
        raise NotFoundException()
        
    async def create(self, tech_task: DocumentTypeCreateSchema):
        document_type_dict = tech_task.model_dump()
        try:
            new_document_type = await self.repo.add(document_type_dict)
            return new_document_type
        except IntegrityError:
            raise ConflictException()