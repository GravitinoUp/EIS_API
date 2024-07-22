"""
Views controllers for purchases app
"""


from fastapi import APIRouter, status, Depends

from src.purchases.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)

from src.purchases.dependencies import get_purchases_service
from src.purchases.service import PurchaseService
from src.purchases.schemas import PurchaseGetSchema, PurchaseCreateSchema


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA
)


@router.get('/', response_model=PurchaseGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    id: int,
    service: PurchaseService = Depends(get_purchases_service),
):
    item = await service.get_by_id(id)
    return item


@router.get('/status', status_code=status.HTTP_200_OK)
async def get_status(
    id: int,
    service: PurchaseService = Depends(get_purchases_service),
):
    status = await service.get_status_by_id(id)
    return {'status': status}


@router.put('/update_status', status_code=status.HTTP_200_OK)
async def update_status(
    id: int,
    service: PurchaseService = Depends(get_purchases_service),
):
    await service.update_status(id)
    return {'message': 'start updating status'}


@router.put('/', status_code=status.HTTP_200_OK)
async def create_one(
    plan_id: int,
    purchase: PurchaseCreateSchema,
    service: PurchaseService = Depends(get_purchases_service),
):
    purchase = await service.add(purchase, plan_id)
    return purchase


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    id: int,
    service: PurchaseService = Depends(get_purchases_service),
):
    await service.delete(id)


@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: PurchaseService = Depends(get_purchases_service),
):
    items = await service.get_all(limit=limit, offset=offset)
    return items