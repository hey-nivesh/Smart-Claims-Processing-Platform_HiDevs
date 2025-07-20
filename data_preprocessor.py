# data_preprocessor.py
import re
from typing import List

class DataPreprocessor:
    def __init__(self):
        pass
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters but keep punctuation
        text = re.sub(r'[^\w\s.,!?-]', '', text)
        # Strip leading/trailing whitespace
        text = text.strip()
        return text
    
    def preprocess_documents(self, documents):
        """Preprocess all documents"""
        processed_docs = []
        for doc in documents:
            cleaned_content = self.clean_text(doc.page_content)
            doc.page_content = cleaned_content
            processed_docs.append(doc)
        return processed_docs