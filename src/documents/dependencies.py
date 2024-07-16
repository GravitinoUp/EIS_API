"""
FastAPI dependencies for the app documents
"""

# define your dependencies here
from src.documents.service import DocumentRepository, DocumentService


def get_document_service():
    return DocumentService(DocumentRepository())