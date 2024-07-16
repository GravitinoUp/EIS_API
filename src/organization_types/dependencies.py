"""
FastAPI dependencies for the app organization_types
"""

# define your dependencies here

from src.organization_types.service import OrganizationTypeService, OrganizationTypeRepository


def get_organization_type_service():
    return OrganizationTypeService(OrganizationTypeRepository())