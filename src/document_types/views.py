"""
Views controllers for tech_tasks app
"""


from uuid import UUID
from fastapi import APIRouter, Depends, status

from src.document_types.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)
from src.document_types.schemas import DocumentTypeCreateSchema, DocumentTypeGetSchema
from src.auth.utils import oauth2_scheme
from src.document_types.dependencies import get_document_type_service
from src.document_types.service import DocumentTypeService


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA,
    dependencies=[Depends(oauth2_scheme)],

)


@router.get('/', response_model=DocumentTypeGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    uuid: UUID,
    service: DocumentTypeService = Depends(get_document_type_service)
):
    document_type = await service.get_by_uuid(uuid)
    return document_type


@router.post('/', response_model=DocumentTypeGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    document_type: DocumentTypeCreateSchema,
    service: DocumentTypeService = Depends(get_document_type_service)
):
    new_document_type = await service.create(document_type)
    return new_document_type


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    uuid: UUID,
    service: DocumentTypeService = Depends(get_document_type_service)
):
    await service.delete_by_uuid(uuid)


@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: DocumentTypeService = Depends(get_document_type_service)
):
    document_type = await service.get_all(limit, offset)
    return document_type