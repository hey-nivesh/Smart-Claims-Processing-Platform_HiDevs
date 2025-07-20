# app.py
import streamlit as st
import os
from dotenv import load_dotenv
from data_loader import DataLoader
from data_preprocessor import DataPreprocessor
from text_splitter import TextChunker
from vector_store import VectorStore
from ai_engine import AIEngine

# Load environment variables
load_dotenv()

def main():
    st.set_page_config(
        page_title="Gen AI Knowledge Assistant",
        page_icon="🤖",
        layout="wide"
    )
    
    st.title("🤖 Gen AI Knowledge Assistant")
    st.markdown("Upload documents and ask questions!")
    
    # Sidebar for configuration
    st.sidebar.header("Configuration")
    
    # API Key input
    groq_api_key = st.sidebar.text_input(
        "Enter Groq API Key", 
        type="password",
        help="Get your free API key from https://groq.com"
    )
    
    if not groq_api_key:
        st.warning("Please enter your Groq API key in the sidebar.")
        return
    
    # Initialize session state
    if 'vectorstore' not in st.session_state:
        st.session_state.vectorstore = None
    if 'ai_engine' not in st.session_state:
        st.session_state.ai_engine = None
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # File upload section
    st.header("📁 Document Upload")
    uploaded_files = st.file_uploader(
        "Choose files", 
        accept_multiple_files=True,
        type=['txt', 'pdf']
    )
    
    # Web URL input
    web_urls = st.text_area(
        "Enter web URLs (one per line):",
        height=100
    )
    
    if st.button("Process Documents"):
        if uploaded_files or web_urls.strip():
            with st.spinner("Processing documents..."):
                # Initialize components
                data_loader = DataLoader()
                preprocessor = DataPreprocessor()
                chunker = TextChunker()
                vector_store = VectorStore()
                
                # Load documents
                all_docs = []
                
                # Process uploaded files
                for file in uploaded_files:
                    # Save uploaded file temporarily
                    with open(f"temp_{file.name}", "wb") as f:
                        f.write(file.getbuffer())
                    
                    if file.name.endswith('.txt'):
                        docs = data_loader.load_text_file(f"temp_{file.name}")
                    elif file.name.endswith('.pdf'):
                        docs = data_loader.load_pdf(f"temp_{file.name}")
                    
                    all_docs.extend(docs)
                    os.remove(f"temp_{file.name}")  # Clean up
                
                # Process web URLs
                if web_urls.strip():
                    urls = [url.strip() for url in web_urls.split('\n') if url.strip()]
                    for url in urls:
                        docs = data_loader.load_web_content(url)
                        all_docs.extend(docs)
                
                if all_docs:
                    # Preprocess documents
                    processed_docs = preprocessor.preprocess_documents(all_docs)
                    
                    # Split into chunks
                    chunks = chunker.split_documents(processed_docs)
                    
                    # Create vector store
                    vectorstore = vector_store.create_vectorstore(chunks)
                    st.session_state.vectorstore = vectorstore
                    
                    # Initialize AI engine
                    ai_engine = AIEngine(groq_api_key)
                    ai_engine.setup_retrieval_chain(vectorstore)
                    st.session_state.ai_engine = ai_engine
                    
                    st.success(f"✅ Processed {len(chunks)} document chunks successfully!")
                else:
                    st.error("No documents were loaded. Please check your files or URLs.")
    
    # Chat interface
    st.header("💬 Ask Questions")
    
    if st.session_state.vectorstore and st.session_state.ai_engine:
        # Display chat history
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.chat_message("user").write(message["content"])
            else:
                st.chat_message("assistant").write(message["content"])
        
        # Query input
        if prompt := st.chat_input("Ask a question about your documents..."):
            # Add user message to chat history
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            
            # Get AI response
            with st.spinner("Thinking..."):
                answer, sources = st.session_state.ai_engine.query(prompt)
            
            # Add AI response to chat history
            st.session_state.chat_history.append({"role": "assistant", "content": answer})
            st.chat_message("assistant").write(answer)
            
            # Show sources if available
            if sources:
                with st.expander("📚 Sources"):
                    for i, source in enumerate(sources):
                        st.write(f"**Source {i+1}:**")
                        st.write(source.page_content[:500] + "...")
                        st.write("---")
    
    else:
        st.info("👆 Please upload and process documents first to start asking questions.")

if __name__ == "__main__":
    main()