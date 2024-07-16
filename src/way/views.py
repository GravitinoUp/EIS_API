"""
Views controllers for way app
"""


from fastapi import APIRouter, Depends, status

from src.way.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)
from src.way.schemas import WayCreateSchema, WayGetSchema
from src.way.dependencies import get_way_service, WayRepository
from src.users.utils import oauth2_scheme


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA,
    dependencies=[Depends(oauth2_scheme)]
)


@router.get('/', response_model=WayGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    id: int,
    service: WayRepository = Depends(get_way_service)
):
    item = await service.get_by_id(id)
    return item


@router.post('/', response_model=WayGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    item: WayCreateSchema,
    service: WayRepository = Depends(get_way_service)
):
    item = await service.add(item)
    return item


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    id: int,
    service: WayRepository = Depends(get_way_service)
):
    await service.delete_by_id(id)
    

@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: WayRepository = Depends(get_way_service)
):
    items = await service.get_all(limit, offset)
    return items
    