"""
Views controllers for tech_tasks app
"""


from uuid import UUID
from fastapi import APIRouter, Depends, status

from src.documents.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)
from src.documents.schemas import DocumentCreateSchema, DocumentGetSchema
from src.users.utils import oauth2_scheme
from src.documents.dependencies import get_document_service
from src.documents.service import DocumentService


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA,
    dependencies=[Depends(oauth2_scheme)],

)


@router.get('/', response_model=DocumentGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    uuid: UUID,
    service: DocumentService = Depends(get_document_service)
):
    document = await service.get_by_uuid(uuid)
    return document


@router.post('/', response_model=DocumentGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    document: DocumentCreateSchema,
    service: DocumentService = Depends(get_document_service)
):
    new_document = await service.create(document)
    return new_document


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    uuid: UUID,
    service: DocumentService = Depends(get_document_service)
):
    await service.delete_by_uuid(uuid)


@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: DocumentService = Depends(get_document_service)
):
    document = await service.get_all(limit, offset)
    return document