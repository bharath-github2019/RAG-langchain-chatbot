# RAG LangChain Sample

(Disclaimer: ChatGPT generted content)

Project Title

Local RAG-Based Chatbot using LangChain, FAISS, and HuggingFace Embeddings

Project Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot that answers user questions strictly based on the content of provided documents. The system is designed to be cost-efficient, modular, and fully local, avoiding dependency on paid APIs for embeddings and retrieval.

The chatbot ingests PDF documents, converts them into vector embeddings, stores them in a vector database, retrieves relevant document chunks for a user query, and generates context-grounded responses using a language model.

Problem Statement

Large Language Models can hallucinate or provide generic answers when queried directly. This project solves that by grounding responses in verified document data, making the chatbot reliable for use cases such as:

Internal policy Q&A

Employee handbooks

Product documentation

Knowledge-base assistants

System Architecture

User Query
→ Retriever (FAISS vector search)
→ Relevant Document Chunks
→ Prompt with Context
→ Language Model
→ Grounded Answer

Key Components
1. Document Ingestion

PDF files are loaded from a local data/ directory

Documents are split into overlapping text chunks to preserve context

Chunking ensures efficient retrieval and accurate answers

2. Embedding Generation (Local & Free)

Uses HuggingFace sentence-transformer models

Converts text chunks into dense vector embeddings

Eliminates reliance on paid embedding APIs

3. Vector Store

FAISS is used for fast similarity search

All embeddings are stored locally on disk

Supports scalable and low-latency retrieval

4. Retrieval Mechanism

For each user query, relevant document chunks are fetched using cosine similarity

Only the top-k most relevant chunks are passed to the language model

5. Prompt Engineering

The system prompt enforces strict grounding

The model is instructed to answer only from retrieved context

If the answer is not present in the documents, the chatbot responds with “I don’t know”

6. Language Model

Designed to support both:

Cloud-based LLMs (OpenAI)

Fully local LLMs via Ollama (Mistral / LLaMA)

In the final setup, the project runs 100% locally with no API key or billing required
