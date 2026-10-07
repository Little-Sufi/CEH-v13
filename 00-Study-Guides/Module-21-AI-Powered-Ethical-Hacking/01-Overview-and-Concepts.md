# 01. Overview and Concepts — AI-Powered Ethical Hacking

> [!INFO] 📌 **Module Scope & Core Objectives**
> Direct technical extraction from official CEH v13 Syllabus (Module 21). Covers Artificial Intelligence & Machine Learning Fundamentals, OWASP Top 10 for Large Language Models (LLMs), Prompt Injection Attacks (Direct vs Indirect), Model Data Poisoning, Model Inversion & Extraction, Adversarial Machine Learning, RAG Security, and AI System Hardening.

---

## 🧠 1. AI & Machine Learning Threat Architecture

### 1.1 Machine Learning Pipeline & Threat Surface
Machine Learning (ML) systems rely on data collection, feature engineering, model training, and inference API serving.
- **Training Phase Threats**: Data Poisoning, Backdoor Insertion, Supply Chain Poisoning.
- **Inference Phase Threats**: Prompt Injection, Model Extraction (Stealing), Model Inversion (Privacy Leakage), Adversarial Evasion Attacks.

> [!ABSTRACT] 🏛️ **📋 Comprehensive OWASP Top 10 for LLMs Reference Matrix**

| Vulnerability Risk | Category Description | Exploitation Vector | Primary Security Impact |
| :--- | :--- | :--- | :--- |
| **LLM01: Prompt Injection** | Direct / Indirect prompt manipulation | Crafting malicious input prompts (`Ignore previous instructions`) | Bypasses system guardrails / Unauthorised actions |
| **LLM02: Sensitive Info Disclosure**| Model revealing confidential training data | Extracting PII or API keys via prompt probing | Data breach / Regulatory violation |
| **LLM03: Supply Chain Vulnerabilities**| Compromised third-party models/plugins | Malicious HuggingFace weights or PyTorch datasets | Remote Code Execution / System Takeover |
| **LLM04: Data and Model Poisoning**| Tampering with training/fine-tuning datasets| Injecting malicious samples into training corpus | Model bias / Trojanized backdoors |
| **LLM05: Improper Offloading / Plugin**| Insecure LLM plugin/tool execution | Unsanitized LLM parameters passed to shell/DB APIs | Remote Code Execution / SQL Injection |
| **LLM06: Excessive Agency** | Over-privileged LLM tools and integrations | Granting LLM shell or delete permissions | Unauthorized infrastructure modification |

---

## ⚡ 2. Prompt Injection & Adversarial Attack Mechanics

### 2.1 Direct vs Indirect Prompt Injection
- **Direct Prompt Injection (Jailbreaking)**: Attacker directly inputs adversarial prompts into an LLM interface (e.g., `"DAN" / "Do Anything Now"` prompts or system prompt override attempts).
- **Indirect Prompt Injection**: Attacker embeds hidden malicious instructions inside third-party content (e.g., web pages, PDF documents, or emails) that an LLM ingests via Retrieval-Augmented Generation (RAG) or web search plugins.

> [!IMPORTANT] 🔄 **📋 Comprehensive AI Attack Vectors Comparison Matrix**

| Attack Type | Target Component | Execution Mechanism | Primary Countermeasure |
| :--- | :--- | :--- | :--- |
| **Direct Prompt Injection**| System Prompt Boundary | System instruction override prompts | Input Guardrails (NeMo Guardrails) + System/User Prompt Separation |
| **Indirect Prompt Injection**| RAG Context / Web Plugins | Hidden zero-width or white text instructions in web/PDF data | Content Sanitization + Human-in-the-Loop Verification |
| **Model Inversion Attack**| Inference API | Reconstructing private training images via confidence scores | Differential Privacy + Noise Addition |
| **Adversarial Evasion** | Image / Audio Classifier | Adding imperceptible noise perturbations to input samples | Adversarial Training + Input Smoothing |
