# Deep Learning Chatbot

## Overview

This project is a **custom chatbot for deep learning** built using **Streamlit, LangChain, FAISS, and Hugging Face models**. It allows users to ask deep learning-related questions and receive responses based on **retrieval-augmented generation (RAG)**.

## Working Principle

1. **Document Processing**
   - Loads deep learning-related PDFs into the system.
   - Extracts text and splits it into manageable chunks.

2. **Vectorization & Storage**
   - Converts text chunks into embeddings using **sentence-transformers/all-MiniLM-L6-v2**.
   - Stores embeddings in a **FAISS vector database** for fast retrieval.

3. **Retrieval & Response Generation**
   - Retrieves relevant text chunks from FAISS when a user asks a question.
   - Uses **Mistral-7B-Instruct-v0.3** from Hugging Face to generate responses.

## Features

✅ **PDF Ingestion** – Loads and processes multiple PDFs.  
✅ **Vector Search** – Uses FAISS for fast text retrieval.  
✅ **LLM-Powered Responses** – Generates intelligent answers using Hugging Face models.  
✅ **Streamlit UI** – Provides an interactive interface with animations and transitions.  

## Requirements

- Python 3.8+
- Streamlit
- LangChain
- FAISS
- Hugging Face Transformers
- Sentence Transformers
- PyPDFLoader

## Sample 

**Interface**
![Chatbot Interface](https://github.com/JoyBiswasgithub/Custom-ChatBot-for-Deep-Learning/blob/main/sample/interface.png)


**Thinking**
![Chatbot Interface](https://github.com/JoyBiswasgithub/Custom-ChatBot-for-Deep-Learning/blob/main/sample/thinking.png)

**Sample Answer**
1. ![Chatbot Interface](https://github.com/JoyBiswasgithub/Custom-ChatBot-for-Deep-Learning/blob/main/sample/textual.png)

2. ![Chatbot Interface](https://github.com/JoyBiswasgithub/Custom-ChatBot-for-Deep-Learning/blob/main/sample/coding.png)

**If Answer Is Not Present In Database**
![Chatbot Interface](https://github.com/JoyBiswasgithub/Custom-ChatBot-for-Deep-Learning/blob/main/sample/interface.png)
