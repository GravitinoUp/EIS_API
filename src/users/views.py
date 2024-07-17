"""
Routes for users app
"""
from fastapi import APIRouter, status, Depends
from typing import Annotated

from fastapi.security import OAuth2PasswordRequestForm

from src.exceptions import UnauthorizedException
from src.users.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)
from src.users.dependencies import get_user_service
from src.users.schemas import UserCreateSchema
from src.users.service import UserService
from src.users.utils import sign_jwt


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA,
)

@router.post("/login", status_code=status.HTTP_200_OK)
async def login(
    user: Annotated[OAuth2PasswordRequestForm, Depends()],
    service: Annotated[UserService, Depends(get_user_service)],
): 
    if new_user := await service.get_by_data(user.username, user.password):
        return {"access_token": sign_jwt(new_user.uuid), "token_type": "bearer"}
    raise UnauthorizedException


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def create_user(
    service: Annotated[UserService, Depends(get_user_service)],
    user: UserCreateSchema
):
    new_user = await service.add(user)
    return {'access_token': sign_jwt(new_user.uuid), 'token_type': 'bearer'}