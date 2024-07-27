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


@router.get('/{id}', response_model=PurchaseGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    id: int,
    service: PurchaseService = Depends(get_purchases_service),
):
    """
    Получение закупки по id.
    """
    item = await service.get_by_id(id)
    return item


@router.get('/{id}/status', status_code=status.HTTP_200_OK)
async def get_status(
    id: int,
    service: PurchaseService = Depends(get_purchases_service),
):
    """
    Получение статуса закупки по id.
    """
    status = await service.get_status_by_id(id)
    return {'status': status}


@router.put('/{id}/status', status_code=status.HTTP_200_OK)
async def update_status(
    id: int,
    service: PurchaseService = Depends(get_purchases_service),
):
    """
    Запуск обновления статуса закупки по id.
    """
    await service.update_status(id)
    return {'message': 'start updating status'}


@router.post('/{plan_id}/', status_code=status.HTTP_200_OK)
async def create_one(
    plan_id: int,
    purchase: PurchaseCreateSchema,
    service: PurchaseService = Depends(get_purchases_service),
):
    """
    Добавление закупки в план-график по id плана.
    """
    purchase = await service.add(purchase, plan_id)
    return purchase


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    id: int,
    service: PurchaseService = Depends(get_purchases_service),
):
    """
    Удаление закупки по id из плана-графика и таблицы с закупками
    """
    await service.delete(id)


@router.get('', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: PurchaseService = Depends(get_purchases_service),
):
    """
    Получение всех закупок с лимитом (limit) и сдвигом (offset).
    """
    items = await service.get_all(limit=limit, offset=offset)
    return items