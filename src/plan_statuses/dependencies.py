"""
FastAPI dependencies for the app plan_statuses
"""

# define your dependencies here
from src.plan_statuses.service import  PlanStatusService, PlanStatusRepository

def get_plan_status_service():
    return PlanStatusService(PlanStatusRepository)