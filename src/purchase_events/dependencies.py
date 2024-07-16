"""
FastAPI dependencies for the app purchase_events
"""

# define your dependencies here
from src.purchase_events.service import PurchaseEventService, PurchaseEventRepository


def get_purchase_event_service():
    return  PurchaseEventService(PurchaseEventRepository)