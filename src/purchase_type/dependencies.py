"""
FastAPI dependencies for the app purchase_type
"""

# define your dependencies here
from src.purchase_type.service import PurchaseTypeRepository, PurchaseTypeService


def get_purchase_type_service():
    return PurchaseTypeService(PurchaseTypeRepository)