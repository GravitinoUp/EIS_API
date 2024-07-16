"""
tech_tasks app service and repository
"""
from uuid import UUID
from sqlalchemy.exc import IntegrityError

from src.exceptions import ConflictException, NotFoundException
from src.abstract_repository import SQLAlchemyRepository, AbstractRepository
from src.documents.models import Document
from src.documents.schemas import DocumentCreateSchema


# define your service here and rename if it's necessary
# WARNING: if this sevice doesn't work with DB,
# you may implement only your own service

class DocumentRepository(SQLAlchemyRepository):
    model = Document


class DocumentService:
    def __init__(self, repository: AbstractRepository):
        self.repo: AbstractRepository = repository()

    async def get_all(self, limit: int, offset: int):
        if document := await self.repo.get_all(limit, offset):
            return document
        raise NotFoundException()

    async def get_by_uuid(self, uuid: UUID):
        if document := await self.repo.get_by_uuid(uuid):
            return document
        raise NotFoundException()

    async def delete_by_uuid(self, uuid: UUID):
        if document := await self.repo.delete_by_uuid(uuid):
            return document
        raise NotFoundException()
        
    async def create(self, document: DocumentCreateSchema):
        document_dict = document.model_dump()
        try:
            document_task = await self.repo.add(document_dict)
            return document_task
        except IntegrityError:
            raise ConflictException()