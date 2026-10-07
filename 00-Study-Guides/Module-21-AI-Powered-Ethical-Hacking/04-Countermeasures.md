# 04. Countermeasures — AI-Powered Ethical Hacking

> [!SHIELD] 🏰 **Defensive Hardening Standards & Secure Configuration**
> Direct technical extraction from official CEH v13 Syllabus (Module 21). Covers Dual-LLM Architecture, Input/Output Guardrails, Differential Privacy, Model Signing & Integrity, Least Privilege Tool Binding, and Human-in-the-Loop (HITL) Controls.

---

## 🛡️ 1. AI Security Hardening Standards

### 1.1 Technical Defensive Checklist

1. **Implement Input/Output Guardrails**: Use firewall frameworks (e.g., NVIDIA NeMo Guardrails or Llama Guard) to filter toxic, prompt-injecting, or sensitive data disclosures in real time.
2. **Dual-LLM Security Pattern**: Separate untrusted external data processing (untrusted execution LLM) from privileged action execution (trusted controller LLM).
3. **Principle of Least Privilege for Plugins**: Never grant LLMs direct shell execution, unconstrained database access, or unrestricted API delete permissions. Mandate **Human-in-the-Loop (HITL)** approval for high-risk actions.
4. **Differential Privacy & Model Watermarking**: Inject noise during training (Differential Privacy) to prevent Model Inversion data leaks, and cryptographically sign model weights (HuggingFace Model Signatures).

> [!SHIELD] 🏰 **📋 Comprehensive AI Security Hardening Matrix**

| Vulnerability Vector | Insecure Legacy State | Mandatory Hardening Standard |
| :--- | :--- | :--- |
| **Direct Prompt Injection**| Unfiltered raw user prompt input | Input Guardrails (NeMo / Llama Guard) |
| **Indirect RAG Injection** | Untrusted document ingestion directly executed | Dual-LLM Architecture + Content Sanitization |
| **Excessive Agency** | LLM granted raw shell / DB drop access | Least Privilege Tool Scope + Human-in-the-Loop (HITL) |
| **Data Poisoning** | Unvalidated web scraping dataset | Cryptographic Data Lineage Verification + Anomaly Auditing |
