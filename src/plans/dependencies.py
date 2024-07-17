"""
FastAPI dependencies for the app plans
"""

# define your dependencies here
from src.plans.service import PlanRepository, PurchaseRepository, PlanPurchaseRepository, PlanService


def get_plan_service():
    return PlanService(PlanRepository(), PurchaseRepository(), PlanPurchaseRepository())