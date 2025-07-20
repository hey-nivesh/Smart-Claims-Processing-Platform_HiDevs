# ai_engine.py
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage
import os

class AIEngine:
    def __init__(self, groq_api_key):
        self.llm = ChatGroq(
            groq_api_key=groq_api_key,
            model_name="llama3-8b-8192"  # Free Groq model
        )
        self.vectorstore = None
        self.qa_chain = None
    
    def setup_retrieval_chain(self, vectorstore):
        """Setup retrieval QA chain"""
        self.vectorstore = vectorstore
        
        # Custom prompt template
        prompt_template = """
        Use the following pieces of context to answer the question at the end. 
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        
        Context: {context}
        
        Question: {question}
        
        Answer:"""
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=True
        )
        
        return self.qa_chain
    
    def query(self, question):
        """Process query and return answer"""
        if self.qa_chain:
            response = self.qa_chain({"query": question})
            return response['result'], response.get('source_documents', [])
        return "AI engine not properly initialized.", []