"""
FastAPI dependencies for the app plan_values
"""

# define your dependencies here
from src.plan_values.service import PlanValueRepository, PlanValueService


def get_plan_value_service():
    return PlanValueService(PlanValueRepository())