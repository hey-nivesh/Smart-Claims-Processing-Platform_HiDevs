# data_loader.py
import os
from langchain.document_loaders import PyPDFLoader, TextLoader, WebBaseLoader
from langchain.document_loaders import UnstructuredFileLoader
import requests
from bs4 import BeautifulSoup

class DataLoader:
    def __init__(self):
        self.documents = []
    
    def load_text_file(self, file_path):
        """Load text files"""
        loader = TextLoader(file_path)
        docs = loader.load()
        self.documents.extend(docs)
        return docs
    
    def load_pdf(self, file_path):
        """Load PDF files"""
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        self.documents.extend(docs)
        return docs
    
    def load_web_content(self, url):
        """Load web content"""
        try:
            loader = WebBaseLoader(url)
            docs = loader.load()
            self.documents.extend(docs)
            return docs
        except Exception as e:
            print(f"Error loading web content: {e}")
            return []
    
    def load_multiple_sources(self, sources):
        """Load from multiple sources"""
        all_docs = []
        for source in sources:
            if source['type'] == 'text':
                docs = self.load_text_file(source['path'])
            elif source['type'] == 'pdf':
                docs = self.load_pdf(source['path'])
            elif source['type'] == 'web':
                docs = self.load_web_content(source['url'])
            all_docs.extend(docs)
        return all_docs