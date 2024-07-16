"""
users schemas
"""
from pydantic import BaseModel, Field

    
class UserSchema(BaseModel):
    email: str
    username: str
    phone_number: str
    full_name: str
    role_id: int = Field(default=1)


class UserCreateSchema(UserSchema):
    password: str
