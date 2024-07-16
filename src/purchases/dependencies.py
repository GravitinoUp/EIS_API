"""
FastAPI dependencies for the app purchases
"""

# define your dependencies here
from src.purchases.service import PurchaseRepository, PurchaseService


def get_purchase_service():
    return PurchaseService(PurchaseRepository)