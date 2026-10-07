# 🏛️ CEH v13 Master Vault — Module Architecture & MCQ Template

> [!INFO] 📌 **Template Specification & Visual Standards Overview**
> This file defines the **Standard Operating Procedure (SOP)**, **Exhaustive Technical Explanation Standard**, and **MCQ Question Engine Standard** for all 21 modules in the CEH v13 Master Vault.
> Every future module must strictly adhere to the formatting rules, Obsidian callout color types, table grids, deep paragraph explanations, and MCQ distractor refutation standards specified herein.

---

## 📖 1. CRITICAL MANDATE: 100% EXHAUSTIVE TOPIC EXPLANATIONS

> [!IMPORTANT] 🔥 **FULLY DETAILED TEXTBOOK-GRADE EXPLANATION RULE**
> **Brief summaries or high-level overviews are STRICTLY FORBIDDEN.**
> Every single module note must contain **exhaustive, textbook-grade technical explanations**, covering:
> 
> 1. **Underlying Protocol & System Mechanics**: Explaining down to packet headers, TCP flags, RFC standards, memory spaces, and registry keys.
> 2. **Complete Sub-Topic Coverage**: Explaining every sub-concept, tool parameter option, CLI flag, and attack vector in full detail.
> 3. **Step-by-Step Operational Workflows**: Providing exact step-by-step execution sequences, command examples with full argument breakdowns, and real-world attack scenarios.
> 4. **Defensive Hardening Protocols**: Explaining exact configuration settings, firewall/IDS signature tuning, and architectural mitigations.

---

## 🎨 2. Rich Obsidian Callout Color Palette & Icons

To make notes visually stunning, elegant, and instantly scannable, leverage Obsidian's native callout color themes and distinct icons:

| Callout Syntax | Visual Color Theme | Icon Badge | Primary Target Content |
| :--- | :--- | :---: | :--- |
| `> [!INFO]` | **Vibrant Blue** | 📌 | Module Overview, Scope & Primary Objectives |
| `> [!ABSTRACT]` | **Deep Purple** | 🏛️ | Security Architecture & Theoretical Models |
| `> [!IMPORTANT]` | **Warm Amber / Gold** | 🔄 | Execution Lifecycles, Phases & Process Flows |
| `> [!DANGER]` | **Crimson Red** | 🛡️ | Offensive Attack Vectors, Dorks & Exploits |
| `> [!SHIELD]` | **Emerald Green** | 🏰 | Defensive Countermeasures & Security Hardening |
| `> [!TOOL]` | **Cyan / Electric Teal** | 🛠️ | Command-Line & GUI Software Matrices |
| `> [!WARNING]` | **Bright Orange** | ⚡ | Threat Categories, Vulnerabilities & Risk Taxonomies |
| `> [!TIP]` | **Golden Yellow** | 💡 | High-Yield CEH Exam Tips & Pro Insights |
| `> [!QUESTION]` | **Indigo / Violet** | 📌 | MCQ Exam Scenario Contexts |
| `> [!SUCCESS]-` | **Spring Green (Collapsible)** | 🔑 | MCQ Answer Keys, Deep Dives & Distractor Refutations |

---

## 📊 3. Clean Reference Matrix Table Standard (No Misaligned Charts)

> [!CAUTION] 🚨 **STRICT FORMATTING RULE FOR ALL MODULES**
> **DO NOT USE MERMAID FLOWCHARTS, GRAPHICAL DIAGRAMS, OR HTML DIV CONTAINERS.**
> Graphical structures break Obsidian Live Preview rendering and cause text overflow.
> 
> **ALWAYS NEST CLEAN MARKDOWN GRID TABLES INSIDE COLORED CALLOUT BOXES:**

```markdown
> [!IMPORTANT] 🔄 **📋 Comprehensive [Topic Name] Reference Matrix**

| Step / Phase # | Element / Phase Name | Primary Technical Goals | Core Execution Vectors |
| :---: | :--- | :--- | :--- |
| **Phase 1** | **[Element Name]** | Detailed technical objective | Utility / Command Example |
| **Phase 2** | **[Element Name]** | Detailed technical objective | Utility / Command Example |
```

---

## 📁 4. Standard Module Directory Structure

Every module directory in `e:\Obsidian\CEH v13\00-Study-Guides\` must contain exactly the following 7 standardized files:

```text
Module-XX-[Module-Name]/
├── 01-Overview-and-Concepts.md      # Foundational security elements, CIA triad, threat taxonomy & detailed explanations
├── 02-Attack-Techniques.md          # Penetration testing 5-phase lifecycle, Cyber Kill Chain, IoCs, Diamond Model
├── 03-Tools.md                      # Comprehensive command-line & GUI tools reference matrix with full syntax breakdowns
├── 04-Countermeasures.md            # Defense-in-Depth, CTI lifecycles, IR lifecycles & Risk Management formulas
├── 05-Course-Detailed-Notes.md      # Legal frameworks, ISO standards, compliance matrix & syllabus notes
├── 06-MCQ-Practice.md               # Extensive, unlimited scenario-driven exam practice engine (50-100+ questions)
└── 07-Full-PDF-Reference.md         # 100% PDF extracted technical text & syllabus topic mapping
```

---

## 🎯 5. MCQ Question Engine Standard (06-MCQ-Practice.md)

> [!IMPORTANT] 🔥 **UNLIMITED QUESTION COUNT RULE**
> **There is NO LIMIT to the number of practice questions inside `06-MCQ-Practice.md`.**
> Generate extensive, high-volume MCQ question banks (ranging from 50 to 100+ ultra-detailed, scenario-driven exam questions per module) to ensure 100% complete coverage of every single topic, sub-concept, command tool option, and technical edge case in the official CEH v13 PDF syllabus.

---

## 📜 6. PDF Technical Extraction Verification Rule

1. **Zero Generic Content**: Every file must be populated by extracting technical concepts from the corresponding official CEH v13 Module PDF (`CEH_v13__Module_XX_...pdf`).
2. **Complete Coverage**: Must cover all frameworks, legal standards, command examples, and threat taxonomies defined in the syllabus.
3. **Double Blank Line Padding**: Ensure strict blank line spacing before all lists, callouts, and tables for 100% error-free Obsidian Markdown rendering.

---

## 📜 7. Stylish PDF Reference Page Blueprint (07-Full-PDF-Reference.md)

Every `07-Full-PDF-Reference.md` file must be styled into an engaging, interactive study repository:

1. **Hero Banner & Callout**:
   ```markdown
   # 📜 07. Full PDF Reference — [Module Name]

   > [!INFO] 🏛️ **Official CEH v13 PDF Source Master Repository**
   > High-fidelity technical text extraction directly from official CEH v13 Syllabus PDF. Organized into stylish, interactive collapsible page blocks for rapid study reference.
   ```

2. **Syllabus Metadata Reference Matrix Table**:
   ```markdown
   | Metadata Attribute | Syllabus Parameter Value |
   | :--- | :--- |
   | **Course Module** | **Module XX: [Module Name]** |
   | **Source PDF File** | `CEH_v13__Module_XX_[Module_Name].pdf` |
   | **Total Extracted Pages** | `XX Pages` |
   | **Syllabus Standard** | CEH v13 (Certified Ethical Hacker 2026 Edition) |
   | **Extraction Status** | 100% Complete / Verified Text Flow |
   ```

3. **Interactive Collapsible Page Chunks**:
   ```markdown
   > [!NOTE]- 📄 **Pages 1 to 5 Technical Extraction**
   > 
   > ### 📍 Page 1
   >
   > > ```text
   > > [Clean extracted page text]
   > > ```
   ```

---

## 🎯 8. STRICT MODULE CONTENT ALIGNMENT RULE FOR MCQS

> [!CAUTION] 🚨 **STRICT SYLLABUS ALIGNMENT REQUIREMENT**
> 1. **Zero Off-Topic Questions**: 100% of questions in `06-MCQ-Practice.md` MUST test specific concepts, tool parameters, command flags, protocol mechanics, legal statutes, or countermeasures documented in THAT module's `01` through `05` note files and official CEH v13 PDF.
> 2. **Syllabus Mapping**: Questions must directly reference tools, flags, and technical mechanisms specific to the module (e.g., Module 01 tests CIA triad/Kill Chain/laws; Module 02 tests Google Dorks/WHOIS/DNS/Shodan; Module 03 tests Nmap flags/TCP control bits/Hping3/evasion).
> 3. **Distractor Refutations**: Distractor refutations must explain why the incorrect options fail based on the specific technical rules taught in the module.
