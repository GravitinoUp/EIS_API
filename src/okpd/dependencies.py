"""
FastAPI dependencies for the app okpd
"""

# define your dependencies here
from src.okpd.service import OKPDRepository, OKPDService


def get_okpd_service():
    return OKPDService(OKPDRepository)