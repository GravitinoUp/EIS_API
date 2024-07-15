"""
FastAPI dependencies for the app plans
"""

# define your dependencies here
from src.plans.service import PlanRepository, PlanService


def get_plan_service():
    return PlanService(PlanRepository)