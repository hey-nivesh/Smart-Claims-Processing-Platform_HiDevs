# 🤖 Gen AI Knowledge Assistant

A complete Retrieval-Augmented Generation (RAG) solution that allows you to upload documents and ask intelligent questions. Built with LangChain, Streamlit, and free AI models.

![Gen AI Demo](https://img.shields.io/badge/Status-Working-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green)

## 🌟 Features

- **📁 Multi-format Document Support**: Upload PDFs, text files, or provide web URLs
- **🧠 Smart Question Answering**: Get contextual answers with source citations
- **💬 Chat Interface**: Interactive conversation with document memory
- **🔍 Semantic Search**: Find relevant information across large document collections
- **🆓 100% Free**: Uses only free APIs and open-source models
- **⚡ Fast Setup**: Get running in under 5 minutes

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Free Groq API key ([Get it here](https://groq.com))

### Installation

1. **Clone or download this project**
```bash
git clone <your-repo-url>
cd gen-ai-knowledge-assistant
```

2. **Create virtual environment**
```bash
python -m venv venv

# Activate virtual environment:
# For Windows:
venv\Scripts\activate

# For macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
# Upgrade pip first
python -m pip install --upgrade pip setuptools wheel

# Install requirements
pip install -r requirements.txt
```

4. **Get your free Groq API key**
   - Visit [groq.com](https://groq.com)
   - Sign up for free account
   - Copy your API key

### Alternative: Without Virtual Environment (Simplest)

If you want to skip the virtual environment setup:

```bash
# Install directly to your system Python
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

**Note**: Using a virtual environment is recommended to avoid package conflicts.

5. **Run the application**
```bash
streamlit run app.py
```

6. **Open your browser** to `http://localhost:8501`

## 📖 How to Use

### Step 1: Enter API Key
- Paste your Groq API key in the sidebar

### Step 2: Upload Documents
- **Files**: Upload PDF or text files
- **Web URLs**: Paste URLs (one per line) for web content
- Click "Process Documents"

### Step 3: Ask Questions
- Type questions in the chat interface
- Get intelligent answers with source citations
- View source documents used for each answer

## 🏗️ Project Structure

```
gen-ai-knowledge-assistant/
├── app.py                 # Main Streamlit application
├── data_loader.py         # Document loading utilities
├── data_preprocessor.py   # Text cleaning and preprocessing
├── text_splitter.py       # Document chunking logic
├── vector_store.py        # Vector database management
├── ai_engine.py           # AI query processing
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .env                  # Environment variables (optional)
```

## 🛠️ Architecture

```
📄 Documents → 🔧 Preprocessing → ✂️ Chunking → 🧮 Embeddings → 🗄️ Vector DB
                                                                        ↓
🤖 AI Response ← 🔍 Retrieval ← 💭 Query Processing ← 💬 User Question
```

### Components

1. **Data Sources**: Multi-format document ingestion (PDF, text, web)
2. **Preprocessing**: Text cleaning and normalization
3. **Chunking**: Smart document splitting with context preservation
4. **Embeddings**: Semantic vector representations using HuggingFace
5. **Vector Database**: ChromaDB for fast similarity search
6. **AI Engine**: Groq's Llama3 for response generation
7. **UI**: Streamlit chat interface

## 🔧 Configuration

### Environment Variables (Optional)

Create a `.env` file:
```env
GROQ_API_KEY=your_api_key_here
```

### Customization Options

**Chunk Size**: Modify in `text_splitter.py`
```python
TextChunker(chunk_size=1000, chunk_overlap=200)
```

**Retrieval Count**: Adjust in `ai_engine.py`
```python
retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
```

**Embedding Model**: Change in `vector_store.py`
```python
HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
```

## 📊 Supported File Types

| Type | Formats | Description |
|------|---------|-------------|
| **Text** | `.txt` | Plain text files |
| **PDF** | `.pdf` | PDF documents |
| **Web** | URLs | Web pages and articles |

## 🆓 Free Services Used

- **[Groq](https://groq.com)**: Free LLM API (Llama3)
- **[HuggingFace](https://huggingface.co)**: Free embedding models
- **[ChromaDB](https://www.trychroma.com/)**: Open-source vector database
- **[Streamlit](https://streamlit.io)**: Free web app framework

## 🐛 Troubleshooting

### Installation Issues

**setuptools error**:
```bash
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

**Package conflicts**:
```bash
pip install --no-deps -r requirements.txt
```

### Runtime Issues

**API Key Error**:
- Ensure your Groq API key is valid
- Check for extra spaces or characters

**Memory Issues**:
- Reduce chunk size in `text_splitter.py`
- Process fewer documents at once

**Slow Performance**:
- Use smaller embedding models
- Reduce retrieval count (k parameter)

## 🔒 Security & Privacy

- **Local Processing**: Documents processed locally on your machine
- **No Data Storage**: No permanent storage of your documents
- **API Security**: Only queries sent to Groq API, not full documents

## 🚀 Advanced Usage

### Batch Processing
```python
# Process multiple documents
sources = [
    {'type': 'pdf', 'path': 'document1.pdf'},
    {'type': 'web', 'url': 'https://example.com'},
    {'type': 'text', 'path': 'notes.txt'}
]
data_loader.load_multiple_sources(sources)
```

### Custom Prompts
Modify the prompt template in `ai_engine.py`:
```python
prompt_template = """
Your custom instructions here...
Context: {context}
Question: {question}
Answer:"""
```

## 📈 Performance Tips

1. **Optimal Chunk Size**: 500-1500 characters work best
2. **Overlap**: Use 10-20% overlap between chunks
3. **Document Quality**: Clean, well-structured documents give better results
4. **Question Specificity**: Specific questions get better answers

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LangChain**: For the excellent RAG framework
- **Streamlit**: For the beautiful UI framework
- **Groq**: For free access to Llama3
- **HuggingFace**: For open-source embedding models
- **ChromaDB**: For the vector database solution

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/your-repo/discussions)
- 📧 **Email**: your-email@example.com

## 🗺️ Roadmap

- [ ] Support for more file formats (Word, Excel, PowerPoint)
- [ ] Advanced query types (summarization, comparison)
- [ ] Multi-language support
- [ ] API endpoints for integration
- [ ] Docker containerization
- [ ] Cloud deployment templates

---

**Made with ❤️ using free and open-source tools**
