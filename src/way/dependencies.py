"""
FastAPI dependencies for the app way
"""

# define your dependencies here
from src.way.service import WayRepository, WayService

def get_way_service():
    return WayService(WayRepository)