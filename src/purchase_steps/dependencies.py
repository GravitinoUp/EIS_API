"""
FastAPI dependencies for the app purchase_steps
"""

# define your dependencies here
from src.purchase_steps.service import PurchaseStepService, PurhcaseStepRepository


def get_purchase_step_service():
    return PurchaseStepService(PurhcaseStepRepository)