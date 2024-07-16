"""
FastAPI dependencies for the app tech_tasks
"""

from src.tech_tasks.service import TechTaskRepository, TechTaskService


def get_tech_task_service():
    return TechTaskService(TechTaskRepository())