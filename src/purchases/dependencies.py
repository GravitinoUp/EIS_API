"""
FastAPI dependencies for the app purchases
"""

from src.purchases.service import PurchaseService
from src.purchases.repositories import PurchaseRepository
from src.plans.repositories import PlanRepository, PlanPurchaseRepository

# TODO: define your dependencies here
def get_purchases_service():
    return PurchaseService(PurchaseRepository, PlanPurchaseRepository, PlanRepository)