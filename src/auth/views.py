"""
Routes for users app
"""
from fastapi import APIRouter, status, Depends
from typing import Annotated

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.exceptions import UnauthorizedException
from src.auth.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)
from src.auth.schemas import UserCreateSchema
from src.auth.service import UserService
from src.auth.dependencies import get_user_service
from src.auth.utils import decode_jwt, sign_jwt # noqa


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(
    user: Annotated[OAuth2PasswordRequestForm, Depends()],
    service: Annotated[UserService, Depends(get_user_service)],
): 
    if new_user := await service.get_by_data(user.username, user.password):
        return {"access_token": sign_jwt(new_user.uuid), "token_type": "bearer"}
    raise UnauthorizedException


# @router.get("/me", status_code=status.HTTP_200_OK)
# async def about_me(
#     token: Annotated[str, Depends(oauth2_scheme)]
# ):
#     return decode_jwt(token)


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def create_user(
    service: Annotated[UserService, Depends(get_user_service)],
    user: UserCreateSchema
):
    new_user = await service.add(user)
    return {'access_token': sign_jwt(new_user.uuid), 'token_type': 'bearer'}