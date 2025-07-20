# text_splitter.py
from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextChunker:
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )
    
    def split_documents(self, documents):
        """Split documents into chunks"""
        texts = self.text_splitter.split_documents(documents)
        return texts