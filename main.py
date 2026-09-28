from backend.document_generator import generate_document


def create_legal_document(document_type, details):
    return generate_document(document_type, details)