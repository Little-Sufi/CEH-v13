# 05. Course Detailed Notes — AI-Powered Ethical Hacking

> [!ABSTRACT] 🏛️ **Comprehensive Syllabus Notes & Technical Reference**
> Direct technical extraction from official CEH v13 Syllabus (Module 21). Covers Generative AI Vulnerabilities, RAG Architecture Security, and Vector Database Exploitation.

---

## 📌 1. Retrieval-Augmented Generation (RAG) & Vector Database Security

- **RAG Architecture**: Enhances LLMs by retrieving relevant contextual chunks from external vector databases (e.g., Pinecone, Milvus, Chroma) using embedding similarity.
- **Vector Database Injection**: Poisoning vector embeddings or stored document chunks to alter LLM context outputs or trigger indirect prompt injection when retrieved.

> [!INFO] 📋 **Comprehensive AI Model Lifecycle Security Matrix**

| Pipeline Stage | Security Focus | Primary Risk | Mitigation Control |
| :--- | :--- | :--- | :--- |
| **Data Collection** | Data Authenticity | Training Data Poisoning | Hash Verification & Lineage Tracking |
| **Model Fine-Tuning**| Weights Integrity | Supply Chain Trojan Weights | Model Signing (SHA-256) & SHA Checks |
| **Inference Serving**| Endpoint Protection | Prompt Injection / Stealing | Guardrails, Rate-Limiting, HITL |
