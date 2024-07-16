"""
FastAPI dependencies for the app okei
"""

# define your dependencies here
from src.okei.service import OKEIService, OKEIepository


def get_okei_service():
    return OKEIService(OKEIepository)