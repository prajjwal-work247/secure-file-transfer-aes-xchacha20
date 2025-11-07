# SECURE FILE ENCRYPTION SYSTEM USING AES-256 AND XCHACHA20

## A Project Report

Submitted in partial fulfillment of the requirements for the award of degree of

**BACHELOR OF TECHNOLOGY**

in

**COMPUTER SCIENCE & ENGINEERING (CYBER SECURITY)**

---

**Submitted By:**

Pragati Raj (22BECCS28)  
Prajjwal Gupta (22BECCS29)  
Group No. 51

**Under the supervision of:**

Mr. Gaurav Thakur  
Assistant Professor  
Department of Computer Science & Engineering

**CENTRAL UNIVERSITY OF JAMMU**  
Rahya-Suchani (Bagla), District Samba-181143, Jammu (J&K)

November 2025

---

## CERTIFICATE

This is to certify that the project entitled "**Secure File Encryption System using AES-256 and XChaCha20**" submitted by **Pragati Raj (22BECCS28)** and **Prajjwal Gupta (22BECCS29)** in partial fulfillment of the requirements for the award of Bachelor of Technology in Computer Science & Engineering (Cyber Security) at Central University of Jammu is a bonafide record of work carried out by them under my supervision and guidance.

**Project Guide:**  
Mr. Gaurav Thakur  
Assistant Professor  
Department of CSE

**HOD:**  
Dr. [Name]  
Head of Department  
Department of CSE

Date: ___________

---

## ACKNOWLEDGEMENT

We would like to express our sincere gratitude to our project guide, **Mr. Gaurav Thakur**, Assistant Professor, Department of Computer Science & Engineering, Central University of Jammu, for his valuable guidance, constant encouragement, and support throughout the duration of this project.

We are thankful to **Dr. [HOD Name]**, Head of Department, Computer Science & Engineering, for providing us with the necessary facilities and resources to complete this project.

We also extend our thanks to all faculty members of the Department of Computer Science & Engineering for their support and cooperation.

Finally, we are grateful to our family and friends for their continuous support and motivation.

**Pragati Raj (22BECCS28)**  
**Prajjwal Gupta (22BECCS29)**

---

## ABSTRACT

In the contemporary digital landscape, where cyber threats escalate alongside our reliance on cloud storage and file sharing, secure file encryption has become a cornerstone of digital safety. Traditional encryption systems, particularly those relying solely on AES-GCM, face challenges including performance inefficiencies with large files and critical vulnerabilities such as nonce reuse that can compromise entire security protocols.

This project presents a hybrid encryption framework that combines Advanced Encryption Standard (AES-256) for file content encryption with XChaCha20-Poly1305 for encryption key protection. The system addresses the nonce management challenges inherent in AES-GCM by leveraging XChaCha20's extended 192-bit nonce space, significantly reducing the risk of nonce collision attacks.

The implementation demonstrates a practical approach to secure file encryption, utilizing well-established cryptographic libraries (PyCryptodome and PyNaCl) to ensure reliability and security. Performance benchmarking conducted on files ranging from 1MB to 100MB shows consistent throughput of approximately [X] MB/s for encryption and [Y] MB/s for decryption, validating the system's efficiency for real-world applications.

The project provides a command-line interface for ease of use and includes comprehensive testing to verify both security properties and performance characteristics. While not claiming theoretical innovation, this work contributes a practical, well-documented implementation that addresses real-world security concerns in file encryption systems.

**Keywords:** Hybrid Encryption, AES-256, XChaCha20, File Security, Nonce Management, Cryptographic Implementation

---

## TABLE OF CONTENTS

1. [INTRODUCTION](#1-introduction)
   - 1.1 Background
   - 1.2 Motivation
   - 1.3 Problem Statement
   - 1.4 Objectives
   - 1.5 Project Scope
   - 1.6 Organization of Report

2. [LITERATURE REVIEW](#2-literature-review)
   - 2.1 Symmetric Encryption Fundamentals
   - 2.2 Advanced Encryption Standard (AES)
   - 2.3 ChaCha20 and XChaCha20
   - 2.4 Hybrid Encryption Approaches
   - 2.5 Existing Systems and Solutions
   - 2.6 Research Gap

3. [SYSTEM ANALYSIS](#3-system-analysis)
   - 3.1 Existing System
   - 3.2 Problems with Existing System
   - 3.3 Proposed System
   - 3.4 Advantages of Proposed System
   - 3.5 Feasibility Study

4. [SYSTEM DESIGN](#4-system-design)
   - 4.1 System Architecture
   - 4.2 Data Flow Diagrams
   - 4.3 Module Description
   - 4.4 Algorithm Design
   - 4.5 Database Design (if applicable)

5. [IMPLEMENTATION](#5-implementation)
   - 5.1 Development Environment
   - 5.2 Technologies Used
   - 5.3 Module Implementation
   - 5.4 Code Snippets
   - 5.5 Testing

6. [RESULTS AND ANALYSIS](#6-results-and-analysis)
   - 6.1 Performance Metrics
   - 6.2 Benchmark Results
   - 6.3 Security Analysis
   - 6.4 Comparative Analysis
   - 6.5 Discussion

7. [CONCLUSION AND FUTURE WORK](#7-conclusion-and-future-work)
   - 7.1 Summary
   - 7.2 Contributions
   - 7.3 Limitations
   - 7.4 Future Enhancements

8. [REFERENCES](#8-references)

9. [APPENDICES](#9-appendices)
   - Appendix A: Source Code
   - Appendix B: Test Cases
   - Appendix C: User Manual

---

## 1. INTRODUCTION

### 1.1 Background

[Write 2-3 paragraphs about the importance of file encryption in modern computing, cloud storage, and cybersecurity. Mention rising cyber threats, data breaches, and regulatory requirements.]

### 1.2 Motivation

[Explain why you chose this project. Discuss the practical need for secure file encryption, the limitations of current approaches, and how your project addresses these needs.]

### 1.3 Problem Statement

Current file encryption systems face several critical challenges:

1. **Nonce Management in AES-GCM:** The requirement for unique nonces in each encryption operation creates vulnerability. A single instance of nonce reuse can lead to catastrophic security failures, including potential recovery of authentication keys and compromise of encrypted data integrity.

2. **Performance Bottlenecks:** In environments lacking hardware acceleration (AES-NI), traditional AES-GCM implementations suffer from reduced throughput and increased CPU usage, making them impractical for resource-constrained devices.

3. **Key Distribution Complexity:** Traditional hybrid systems using asymmetric encryption (RSA) for key encapsulation suffer from computational overhead and vulnerability concerns as key sizes increase.

This project addresses these challenges through a hybrid encryption framework that combines AES-256 for file content encryption with XChaCha20-Poly1305 for key protection, providing enhanced security and improved operational characteristics.

### 1.4 Objectives

The primary objectives of this project are:

1. To conduct a comprehensive literature review on symmetric encryption algorithms, including AES and XChaCha20, and their application in secure file systems.

2. To design and implement a hybrid encryption model integrating AES-256 for file content encryption and XChaCha20 for encryption key protection.

3. To develop a user-friendly command-line interface for file encryption and decryption operations.

4. To evaluate the system's performance across various file sizes and analyze throughput characteristics.

5. To validate the security properties of the implementation and verify data integrity throughout the encryption-decryption cycle.

### 1.5 Project Scope

**In Scope:**
- Implementation of AES-256-GCM encryption for file content
- Implementation of XChaCha20-Poly1305 for key encryption
- Hybrid system integration
- Command-line interface
- Performance benchmarking
- Security analysis and testing

**Out of Scope:**
- Network file transfer implementation
- Graphical user interface (GUI)
- Cloud storage integration
- Multi-user access control
- Key distribution protocols
- Post-quantum cryptography

### 1.6 Organization of Report

[Briefly describe what each chapter contains]

---

## 2. LITERATURE REVIEW

[TO BE FILLED: Research on AES, XChaCha20, hybrid encryption, nonce reuse attacks, etc.]

### 2.1 Symmetric Encryption Fundamentals

[Define symmetric encryption, explain how it works, discuss advantages and use cases]

### 2.2 Advanced Encryption Standard (AES)

[History, design principles, AES modes (especially GCM), performance characteristics, hardware acceleration]

### 2.3 ChaCha20 and XChaCha20

[Origin, design by Bernstein, advantages over AES, nonce extension in XChaCha20, use in modern protocols]

### 2.4 Hybrid Encryption Approaches

[Discuss existing hybrid schemes, why combining algorithms provides security benefits]

### 2.5 Existing Systems and Solutions

[Review current file encryption tools: VeraCrypt, GPG, BitLocker, etc.]

### 2.6 Research Gap

[Identify what existing systems don't address that your project does]

---

## 3. SYSTEM ANALYSIS

### 3.1 Existing System

[Describe current approaches to file encryption, focus on AES-GCM-only systems]

### 3.2 Problems with Existing System

1. **Nonce Reuse Vulnerability**
2. **Performance Dependencies**
3. **Key Management Complexity**

### 3.3 Proposed System

[Describe your hybrid approach in detail]

### 3.4 Advantages of Proposed System

1. Enhanced nonce management
2. Algorithmic diversity
3. Performance optimization
4. Simplified key protection

### 3.5 Feasibility Study

**Technical Feasibility:** [Libraries available, algorithms well-documented]  
**Operational Feasibility:** [Easy to use, practical]  
**Economic Feasibility:** [Free tools, no cost]

---

## 4. SYSTEM DESIGN

### 4.1 System Architecture

[INSERT ARCHITECTURE DIAGRAM]

```
┌──────────────────────────────────────────────┐
│           User Interface (CLI)               │
└────────────────┬─────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────┐
│       Hybrid Encryption Controller           │
└────────┬────────────────────────┬────────────┘
         │                        │
         ▼                        ▼
┌────────────────┐      ┌────────────────────┐
│  AES-256-GCM   │      │ XChaCha20-Poly1305 │
│  File Encrypt  │      │  Key Encryption    │
└────────────────┘      └────────────────────┘
```

### 4.2 Data Flow Diagrams

**Encryption Flow:**
1. User provides input file
2. System generates random AES-256 key
3. File encrypted with AES-256-GCM
4. XChaCha20 master key generated
5. AES key encrypted with XChaCha20
6. Encrypted file, encrypted key, and metadata saved

**Decryption Flow:**
1. User provides metadata file
2. System loads encrypted AES key
3. AES key decrypted using XChaCha20 master key
4. File decrypted using recovered AES key
5. Decrypted file saved

### 4.3 Module Description

**Module 1: AES Encryption Module**
- Purpose: Encrypt/decrypt file content
- Input: File path, encryption key
- Output: Encrypted file
- Algorithm: AES-256-GCM

**Module 2: XChaCha20 Key Encryption Module**
- Purpose: Encrypt/decrypt AES keys
- Input: AES key, master key
- Output: Encrypted key
- Algorithm: XChaCha20-Poly1305

**Module 3: Hybrid Encryption Controller**
- Purpose: Coordinate encryption process
- Integrates AES and XChaCha20 modules

**Module 4: Command-Line Interface**
- Purpose: User interaction
- Commands: encrypt, decrypt, info

### 4.4 Algorithm Design

[Provide pseudocode or flowcharts for main operations]

### 4.5 Database Design

[Not applicable for this project - mention that all data stored as files]

---

## 5. IMPLEMENTATION

### 5.1 Development Environment

- **Operating System:** Ubuntu 22.04 / Windows 11
- **Programming Language:** Python 3.10+
- **IDE:** Visual Studio Code
- **Version Control:** Git, GitHub
- **Libraries:** PyCryptodome 3.19.0, PyNaCl 1.5.0, Matplotlib 3.7.1

### 5.2 Technologies Used

[Describe each technology and why it was chosen]

### 5.3 Module Implementation

[Describe how each module was implemented]

### 5.4 Code Snippets

[Include key code sections with explanations]

### 5.5 Testing

**Unit Testing:** [Each module tested independently]  
**Integration Testing:** [Modules tested together]  
**Performance Testing:** [Benchmarked across file sizes]

---

## 6. RESULTS AND ANALYSIS

### 6.1 Performance Metrics

[Define metrics: encryption time, decryption time, throughput]

### 6.2 Benchmark Results

[INSERT PERFORMANCE GRAPHS]

**Table: Performance Results**

| File Size (MB) | Encryption Time (s) | Decryption Time (s) | Throughput (MB/s) |
|----------------|---------------------|---------------------|-------------------|
| 1              | [X]                 | [Y]                 | [Z]               |
| 5              | [X]                 | [Y]                 | [Z]               |
| 10             | [X]                 | [Y]                 | [Z]               |
| 25             | [X]                 | [Y]                 | [Z]               |
| 50             | [X]                 | [Y]                 | [Z]               |
| 100            | [X]                 | [Y]                 | [Z]               |

### 6.3 Security Analysis

[Discuss nonce management, key sizes, authentication]

### 6.4 Comparative Analysis

[Compare with pure AES or pure ChaCha20 if possible]

### 6.5 Discussion

[Interpret results, explain findings]

---

## 7. CONCLUSION AND FUTURE WORK

### 7.1 Summary

[Summarize what was accomplished]

### 7.2 Contributions

[List key contributions of your project]

### 7.3 Limitations

[Be honest about limitations]

### 7.4 Future Enhancements

- Network file transfer implementation
- Graphical user interface
- Cloud storage integration
- Mobile application
- Post-quantum cryptographic algorithms

---

## 8. REFERENCES

[1] J. Daemen and V. Rijmen, The design of Rijndael: AES - the advanced encryption standard. Berlin: Springer, 2002.

[2] Y. Nir and A. Langley, "ChaCha20 and Poly1305 for IETF Protocols," RFC 7539, May 2015.

[Continue with all 10 references from your synopsis...]

---

## 9. APPENDICES

### Appendix A: Source Code

[Include full source code or link to GitHub repository]

### Appendix B: Test Cases

[Document test cases and results]

### Appendix C: User Manual

[Step-by-step guide for using the system]

---

**END OF REPORT**
