"""
FastAPI dependencies for the app products
"""

# define your dependencies here
from src.products.service import ProductService, ProductRepository

def get_product_service():
    return ProductService(ProductRepository)