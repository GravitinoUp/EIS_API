"""
FastAPI dependencies for the app branches
"""

# define your dependencies here
from src.branches.service import BranchRepository, BranchService


def get_branch_service():
    return BranchService(BranchRepository)