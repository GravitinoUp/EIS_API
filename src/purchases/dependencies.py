"""
FastAPI dependencies for the app purchases
"""

from src.purchases.service import PurchaseService, PurchaseRepository

# TODO: define your dependencies here
def get_purchases_service():
    return PurchaseService(PurchaseRepository)