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

The exponential growth of digital data in the 21st century has fundamentally transformed how individuals and organizations store, process, and transmit information. With the global datasphere projected to reach 175 zettabytes by 2025, the need for robust data security mechanisms has become paramount. Cloud computing, which enables convenient on-demand access to shared computing resources, has emerged as the dominant paradigm for data storage and processing. However, this shift toward cloud-based infrastructure introduces significant security challenges, particularly concerning data confidentiality and integrity during storage and transmission.

Encryption serves as the cornerstone of modern data security, providing mathematical guarantees for protecting sensitive information from unauthorized access. Symmetric encryption algorithms, which use the same key for both encryption and decryption operations, offer the computational efficiency necessary for protecting large volumes of data. The Advanced Encryption Standard (AES), established by the National Institute of Standards and Technology (NIST) in 2001 [1][1], has become the de facto standard for symmetric encryption across government, military, and commercial applications. AES operates as a block cipher, processing data in fixed-size blocks using substitution-permutation networks, and is widely implemented in hardware acceleration features found in modern processors.

Despite its widespread adoption and proven security record, AES implementations face operational challenges that can compromise security in real-world deployments. The Galois/Counter Mode (GCM) of operation, commonly used with AES for authenticated encryption, requires strict adherence to nonce uniqueness—each encryption operation must use a unique nonce value with the same key. Nonce reuse represents a critical vulnerability in AES-GCM, potentially enabling attackers to recover authentication keys and forge authenticated ciphertext. This vulnerability is not merely theoretical; documented incidents in production systems [4][4], including vulnerabilities in widely-used TLS implementations, demonstrate the practical risks associated with nonce management failures.

Furthermore, the performance characteristics of AES-GCM vary significantly across different computing environments. While modern processors equipped with AES-NI (AES New Instructions) achieve exceptional throughput rates exceeding several gigabytes per second, software-only implementations on devices lacking hardware acceleration experience substantially degraded performance. This performance disparity creates challenges for heterogeneous computing environments encompassing traditional servers, mobile devices, and Internet of Things (IoT) sensors, where uniform security policies must be maintained across diverse hardware capabilities.

In response to these challenges, the cryptographic community has developed alternative symmetric ciphers designed for efficient software implementation. ChaCha20, designed by Daniel J. Bernstein [2][2], represents a stream cipher optimized for software performance across various platforms without requiring specialized hardware support. The extended-nonce variant, XChaCha20, addresses nonce management concerns by extending the nonce space from 96 bits to 192 bits, dramatically reducing the probability of nonce collision even under imperfect random number generation. When combined with the Poly1305 message authentication code, XChaCha20-Poly1305 provides authenticated encryption comparable to AES-GCM while offering distinct operational advantages.

The concept of hybrid encryption, combining multiple cryptographic primitives to leverage their respective strengths, has proven effective in addressing complex security requirements. Traditional hybrid encryption schemes typically combine asymmetric algorithms for key exchange with symmetric algorithms for bulk data encryption. However, hybrid approaches can also employ multiple symmetric algorithms in complementary roles, creating defense-in-depth architectures that mitigate algorithm-specific vulnerabilities while optimizing performance characteristics for specific operational contexts. This project explores such an approach, combining AES-256 for file content encryption with XChaCha20-Poly1305 for encryption key protection, thereby addressing the nonce management challenges inherent in pure AES-GCM deployments while maintaining compliance with established cryptographic standards.

This project, developed at Central University of Jammu, implements such a hybrid framework, demonstrating the practical feasibility of combining AES-256-GCM for file encryption with XChaCha20-Poly1305 for key protection. The implementation provides a command-line interface suitable for both interactive use and automated workflows, with comprehensive performance benchmarking across various file sizes to characterize operational behavior.

### 1.2 Motivation

The motivation for this project stems from the practical challenges observed in contemporary file encryption systems and the need for security solutions that balance cryptographic strength with operational resilience. Current encryption implementations, while mathematically sound, often fail due to implementation errors, operational mistakes, or environmental limitations rather than algorithmic weaknesses. The Zoom video conferencing platform's initial encryption implementation, which used AES-128 in ECB mode rather than a secure authenticated encryption mode, exemplifies how implementation choices can undermine theoretical security guarantees. Similarly, numerous TLS implementations have experienced vulnerabilities related to nonce reuse in AES-GCM, demonstrating that even widely-deployed, professionally-maintained systems struggle with correct nonce management.

The increasing diversity of computing devices amplifies these challenges. Modern secure file sharing scenarios encompass high-performance data centers with dedicated cryptographic accelerators, general-purpose workstations, mobile devices with varying capabilities, and resource-constrained IoT devices. A file encrypted on a server equipped with AES-NI hardware acceleration must remain accessible to a mobile device performing software-only decryption. This heterogeneity demands encryption solutions that perform adequately across the entire spectrum of deployment environments without sacrificing security properties.

Regulatory and compliance requirements further complicate encryption system design. Many industries operate under regulatory frameworks mandating specific cryptographic standards. The Federal Information Processing Standard (FIPS) 140-2, for instance, requires federal agencies to use NIST-approved algorithms, with AES being explicitly approved. Organizations subject to such requirements cannot simply abandon AES in favor of alternative algorithms, regardless of operational advantages those alternatives might offer. This regulatory landscape necessitates hybrid approaches that satisfy compliance requirements while incorporating modern cryptographic techniques that address operational limitations of mandated algorithms.

The principle of algorithmic diversity, analogous to biodiversity in natural ecosystems, provides additional motivation for hybrid encryption approaches. Relying exclusively on a single algorithm creates systemic risk—a breakthrough in cryptanalysis affecting that algorithm compromises all systems dependent upon it. While AES has withstood decades of cryptanalytic scrutiny and remains secure against known attacks, prudent security engineering acknowledges the possibility of future advances in cryptanalysis or quantum computing capabilities. Incorporating algorithmic diversity through hybrid approaches provides insurance against such developments, ensuring that compromise of one algorithm does not result in total system failure.

From a practical implementation perspective, modern cryptographic libraries have matured to the point where combining multiple algorithms introduces minimal development complexity. Well-maintained libraries such as PyCryptodome and PyNaCl provide secure, audited implementations of both AES and XChaCha20, complete with appropriate authenticated encryption modes and secure random number generation. The primary challenge lies not in implementing individual algorithms but in architecting systems that compose these primitives correctly while avoiding common pitfalls such as key reuse, inadequate randomness, or improper error handling.

Educational objectives also motivate this project. Understanding the strengths, weaknesses, and appropriate use cases for different cryptographic algorithms requires hands-on implementation experience. By constructing a hybrid encryption system, this project provides practical insight into key management, mode selection, performance characteristics, and the operational considerations that influence cryptographic system design. The project demonstrates that effective security engineering requires not only knowledge of cryptographic theory but also understanding of implementation challenges, performance trade-offs, and the real-world constraints that shape practical security solutions.

Finally, the project addresses the specific needs of security-conscious users who require file encryption capabilities without relying on third-party services or proprietary solutions. While commercial encryption tools exist, open-source implementations built on well-documented algorithms and libraries provide transparency and auditability—essential properties for security-critical applications. By developing a hybrid encryption framework with clear documentation, comprehensive testing, and performance benchmarking, this project contributes a practical tool that users can deploy with confidence while understanding the security properties and limitations of the implementation.

Developed as part of the B.Tech curriculum in Computer Science and Engineering (Cyber Security) at Central University of Jammu, this project bridges theoretical cryptographic knowledge with practical implementation skills, preparing students for security engineering roles in industry and research.

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

[1] J. Daemen and V. Rijmen, The design of Rijndael : AES - the advanced encryption standard ; with 17 tables. Berlin: Springer, 2002.

[2] Y. Nir and A. Langley, “ChaCha20 and Poly1305 for IETF Protocols,” www.rfc-editor.org, May 2015, doi: https://doi.org/10.17487/RFC7539.

[3] Disadvantage AES-GCM. “Disadvantage AES-GCM.” Cryptography Stack Exchange, 31 July 2014, crypto.stackexchange.com/questions/18420/disadvantage-aes-gcm? Accessed 10 Apr. 2025.

[4] A. Choudhury, D. McGrew, and J. Salowey, “AES Galois Counter Mode (GCM) Cipher Suites for TLS,” Aug. 2008, doi: https://doi.org/10.17487/rfc5288.

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
