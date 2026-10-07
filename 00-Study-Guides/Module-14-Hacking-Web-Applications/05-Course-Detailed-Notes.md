# 05. Course Detailed Notes — Hacking Web Applications

> [!ABSTRACT] 🏛️ **Comprehensive Syllabus Notes & Technical Reference**
> Direct technical extraction from official CEH v13 Syllabus (Module 14). Covers DOM-based XSS Source/Sink Dataflow, GraphQL Introspection Attacks, and JWT Security Mechanics.

---

## 📌 1. DOM-Based XSS & Web API Security

### 1.1 DOM-Based XSS Source and Sink Architecture
DOM XSS occurs entirely within the browser DOM without server-side reflection.
- **Sources (Tainted Inputs)**: `location.search`, `location.hash`, `document.referrer`, `window.name`.
- **Sinks (Execution Vulnerabilities)**: `eval()`, `document.write()`, `innerHTML`, `setTimeout()`, `element.setAttribute()`.

> [!INFO] 📋 **Comprehensive Web API Protocol Security Comparison Matrix**

| Web API Architecture | Transport Protocol | Schema Specification | Security Vulnerability Vector |
| :--- | :--- | :--- | :--- |
| **REST API** | HTTP / JSON | OpenAPI / Swagger | IDOR, Broken Object Level Auth (BOLA) |
| **SOAP API** | HTTP / XML | WSDL | XML External Entity (XXE) Injection |
| **GraphQL API** | HTTP / JSON | Schema Introspection | Introspection abuse, Batching DoS |
