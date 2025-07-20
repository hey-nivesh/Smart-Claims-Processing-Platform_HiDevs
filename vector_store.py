# vector_store.py
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
import chromadb

class VectorStore:
    def __init__(self):
        # Using free HuggingFace embeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.vectorstore = None
    
    def create_vectorstore(self, texts, persist_directory="./chroma_db"):
        """Create vector store from texts"""
        self.vectorstore = Chroma.from_documents(
            documents=texts,
            embedding=self.embeddings,
            persist_directory=persist_directory
        )
        return self.vectorstore
    
    def load_vectorstore(self, persist_directory="./chroma_db"):
        """Load existing vector store"""
        self.vectorstore = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embeddings
        )
        return self.vectorstore
    
    def similarity_search(self, query, k=3):
        """Search for similar documents"""
        if self.vectorstore:
            return self.vectorstore.similarity_search(query, k=k)
        return []