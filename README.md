# 🎬 YouTube Video Question Answering System (RAG)

A **Retrieval-Augmented Generation (RAG)** based application that enables users to ask questions about a YouTube video and receive **accurate, transcript-grounded answers**. The system ensures that responses are strictly based on the video transcript, preventing hallucinations and maintaining factual reliability.

---

## 📌 Overview

This project extracts transcripts from YouTube videos, converts them into vector embeddings, stores them in a Pinecone vector database, and retrieves relevant context to answer user queries using a Large Language Model (LLM).

The frontend is built using **Streamlit**, while the backend leverages **LangChain**, **OpenAI embeddings**, and **Pinecone** for semantic search.

---

## ✨ Key Features

- 🔗 Input any YouTube video URL
- 📄 Automatically fetch and process English transcripts
- 🧠 Semantic embedding generation using OpenAI
- 🔍 Context retrieval via Pinecone similarity search
- 💬 Natural language Q&A interface
- 🧹 Manual and automatic vector cleanup
- 🚫 No hallucinations – answers only from transcript context

---

## 🏗️ Architecture

```
User (Streamlit)
   │
   ▼
YouTube URL + Question
   │
   ▼
Transcript Extraction
   │
   ▼
Text Cleaning & Chunking
   │
   ▼
Embedding Generation (OpenAI)
   │
   ▼
Vector Storage (Pinecone)
   │
   ▼
Similarity Search (LangChain)
   │
   ▼
LLM Answer Generation
```

---

## 🧰 Technology Stack

| Layer | Tool / Library |
|-----|--------------|
| Frontend | Streamlit |
| Backend | Python |
| LLM | OpenAI GPT |
| Embeddings | text-embedding-3-small |
| Vector DB | Pinecone |
| Orchestration | LangChain |
| Transcript API | YouTube Transcript API |

---

## 📁 Directory Structure

```
.
├── app.py                # Streamlit frontend (root)
├── src/
│   ├── backend/
│   │   ├── langchain_pinecone.py
│   │   ├── similarity_search.py
│   │   ├── transcript_getter.py
│   │   └── yt_chatbot.py
│   └── utill/
│       ├── extracting_videoId.py
│       └── make_para.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🔐 Environment Configuration

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key
OPENAI_API_KEY_EMBEDDING=your_openai_embedding_key
PINECONE_API_KEY=your_pinecone_api_key
```

---

## ⚙️ Installation & Execution

1. **Clone the repository**
```
git clone <repository-url>
cd youtube-video-qa
```

2. **Create virtual environment**
```
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```
pip install -r requirements.txt
```

4. **Run the Streamlit app**
```
streamlit run app.py
```

---

## 🧑‍💻 Usage Guide

1. Paste a valid YouTube video URL
2. Ask a question related to the video content
3. The system will:
   - Generate embeddings (once per session)
   - Retrieve relevant transcript chunks
   - Generate a context-aware answer
4. Ask multiple questions if required
5. Click **Clear Embeddings** when finished

> If the user forgets to clear embeddings, all vectors are **automatically deleted when the app exits**.

---

## 🧹 Vector Lifecycle Management

- ✅ Embeddings are created once per session
- ✅ Manual cleanup button provided
- ✅ Automatic cleanup using `atexit` on app shutdown
- ❌ No persistent or orphan vectors

This ensures efficient Pinecone usage and prevents unnecessary storage costs.

---

## 🧠 Design Principles

- Retrieval-first answering (RAG)
- Strict transcript grounding
- Hallucination-free responses
- Clear separation of frontend and backend
- Minimal coupling and reusable backend logic

If sufficient context is unavailable, the model responds:

> "I don't know."

This behavior is **intentional and correct**.

---

## ⚠️ Limitations

- Requires English subtitles to be available
- Generic transcript sections (outros) may affect retrieval quality
- Single video supported per session

---

## 🔮 Future Enhancements

- Advanced transcript cleaning
- Hybrid retrieval (BM25 + vector search)
- Cross-encoder reranking
- Multi-video context support
- Streaming responses
- User authentication and rate limiting

---

## 📜 License

MIT License

---

## 🙏 Acknowledgements

- OpenAI
- Pinecone
- LangChain
- Streamlit
- YouTube Transcript API

---

This project serves as a **practical, end-to-end implementation of a RAG-based system** and can be extended for production or research use cases.

