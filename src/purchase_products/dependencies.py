"""
FastAPI dependencies for the app purchase_products
"""

# define your dependencies here
from src.purchase_products.service import PurchaseProductRepository, PurchaseProductService


def get_purchase_product_service():
    return PurchaseProductService(PurchaseProductRepository)