"""
FastAPI dependencies for the app document_types
"""

# define your dependencies here

from src.document_types.service import DocumentTypeRepository, DocumentTypeService


def get_document_type_service():
    return DocumentTypeService(DocumentTypeRepository())