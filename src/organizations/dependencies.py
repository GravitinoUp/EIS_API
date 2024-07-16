"""
FastAPI dependencies for the app organizations
"""

# define your dependencies here
from src.organizations.service import OrganizationRepository, OrganizationService


def get_organization_service():
    return OrganizationService(OrganizationRepository())