"""
Views controllers for currency app
"""


from fastapi import APIRouter, status, Depends

from src.currency.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)
from src.currency.schemas import CurrencyCreateSchema, CurrencyGetSchema
from src.currency.dependencies import get_currency_service, CurrencyService
from src.users.utils import oauth2_scheme


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA,
    dependencies=[Depends(oauth2_scheme)]
)


@router.get('/', response_model=CurrencyGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    code: int,
    service: CurrencyService = Depends(get_currency_service)
):
    currency = await service.get_by_id(code)
    return currency


@router.post('/', response_model=CurrencyGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    currency: CurrencyCreateSchema,
    service: CurrencyService = Depends(get_currency_service)
):
    currency = await service.add(currency)
    return currency


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    code: int,
    service: CurrencyService = Depends(get_currency_service)
):
    await service.delete_by_id(code)
    

@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: CurrencyService = Depends(get_currency_service)
):
    currencies = await service.get_all(limit, offset)
    return currencies
    