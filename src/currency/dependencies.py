"""
FastAPI dependencies for the app currency
"""

# define your dependencies here
from src.currency.service import CurrencyService, CurrencyRepository

def get_currency_service() -> CurrencyService:
    return  CurrencyService(CurrencyRepository)