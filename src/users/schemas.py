"""
users schemas
"""
from pydantic import BaseModel

    
class UserSchema(BaseModel):
    email: str
    username: str


class UserCreateSchema(UserSchema):
    password: str
