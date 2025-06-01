from langchain_community.document_loaders import PyPDFLoader
from PyPDF2 import PdfReader

def load_resume(file_path):
    # Load resume content
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    resume_text = "\n".join([page.page_content for page in pages])

    # Detect software used to create the PDF
    software_used = detect_document_software(file_path)

    return resume_text, software_used

def detect_document_software(file_path):
    try:
        reader = PdfReader(file_path)
        metadata = reader.metadata

        if metadata:
            if "/Producer" in metadata:
                return metadata["/Producer"]
            elif "/Creator" in metadata:
                return metadata["/Creator"]
        return "Unknown software"
    except Exception as e:
        return f"Could not determine software ({str(e)})"
