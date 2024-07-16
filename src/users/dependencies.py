"""
FastAPI dependencies for the app users
"""

from src.auth.service import UserService, UserRepository


def get_user_service():
    return UserService(UserRepository)

