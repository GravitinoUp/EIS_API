"""
Views controllers for purchase_products app
"""


from uuid import UUID
from fastapi import APIRouter, Depends, status

from src.purchase_products.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)
from src.purchase_products.schemas import PurchaseProductSchema
from src.purchase_products.dependencies import get_purchase_product_service, PurchaseProductService
from src.auth.utils import oauth2_scheme


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA,
    dependencies=[Depends(oauth2_scheme)]
)


@router.get('/', response_model=PurchaseProductSchema, status_code=status.HTTP_200_OK)
async def get_one(
    uuid: UUID,
    service: PurchaseProductService = Depends(get_purchase_product_service)
):
    item = await service.get_by_uuid(uuid)
    return item


@router.post('/', response_model=PurchaseProductSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    item: PurchaseProductSchema,
    service: PurchaseProductService = Depends(get_purchase_product_service)
):
    item = await service.add(item)
    return item


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    uuid: UUID,
    service: PurchaseProductService = Depends(get_purchase_product_service)
):
    await service.delete_by_uuid(uuid)
    

@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: PurchaseProductService = Depends(get_purchase_product_service)
):
    items = await service.get_all(limit, offset)
    return items
    