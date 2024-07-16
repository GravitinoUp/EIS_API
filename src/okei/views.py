"""
Views controllers for okei app
"""


from fastapi import APIRouter, Depends, status

from src.okei.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)
from src.okei.schemas import OKEICreateSchema, OKEIGetSchema
from src.okei.dependencies import get_okei_service, OKEIService
from src.users.utils import oauth2_scheme

router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA,
    dependencies=[Depends(oauth2_scheme)]
)


@router.get('/', response_model=OKEIGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    code: int,
    service: OKEIService = Depends(get_okei_service)
):
    item = await service.get_by_id(code)
    return item


@router.post('/', response_model=OKEIGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    okei: OKEICreateSchema,
    service: OKEIService = Depends(get_okei_service)
):
    item = await service.add(okei)
    return item


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    id: int,
    service: OKEIService = Depends(get_okei_service)
):
    await service.delete_by_id(id)
    

@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: OKEIService = Depends(get_okei_service)
):
    items = await service.get_all(limit, offset)
    return items
    