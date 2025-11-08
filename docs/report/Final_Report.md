# PROJECT REPORT

## SECURE FILE ENCRYPTION SYSTEM USING AES-256 AND XCHACHA20

---

**SUBMITTED IN PARTIAL FULFILMENT OF THE REQUIREMENTS FOR THE AWARD OF DEGREE OF**

**BACHELOR OF TECHNOLOGY**

**IN**

**COMPUTER SCIENCE & ENGINEERING**

---

**Submitted By:**

**Name:**  
Pragati Raj - Roll No. 22BECCS28  
Prajjwal Gupta - Roll No. 22BECCS29

**Group No. 51**

---

**Under the supervision of**

**Mr. Gaurav Thakur**  
Assistant Professor  
Department of Computer Science & Engineering

---

**DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING**

**CENTRAL UNIVERSITY OF JAMMU**

Rahya-Suchani (Bagla), District Samba-181143, Jammu (J&K)

**November 2025**

---

# ABSTRACT

*(Not more than one page or 500 words)*

In the contemporary digital landscape, where cyber threats escalate alongside our reliance on cloud storage and file sharing, secure file encryption has become essential for protecting sensitive data. Traditional encryption systems, particularly those relying solely on AES-GCM, face operational challenges including nonce management vulnerabilities and performance limitations in non-accelerated environments.

This project presents a hybrid encryption framework that combines Advanced Encryption Standard (AES-256) in Galois/Counter Mode for file content encryption with XChaCha20-Poly1305 for encryption key protection. The system addresses critical nonce reuse vulnerabilities inherent in AES-GCM implementations by leveraging XChaCha20's extended 192-bit nonce space, significantly reducing collision probability even under imperfect randomness conditions.

The implementation utilizes well-established cryptographic libraries—PyCryptodome for AES operations and PyNaCl for XChaCha20 functionality—ensuring security through audited, industry-standard code. A command-line interface provides user-friendly access to encryption and decryption operations, with automated metadata management for seamless key recovery during decryption.

Performance benchmarking conducted across file sizes ranging from 1MB to 100MB demonstrates consistent encryption throughput of [X] MB/s and decryption throughput of [Y] MB/s on standard hardware. The system maintains data integrity through authenticated encryption in both layers, with comprehensive testing validating correct operation across various file types and sizes.

The project follows an iterative development methodology, with modular architecture enabling independent testing and validation of encryption components before integration. Version control through Git ensures traceable development history, while comprehensive documentation facilitates future maintenance and enhancement.

This work contributes a practical, well-documented implementation addressing real-world security concerns in file encryption systems. While not claiming theoretical cryptographic innovation, the project demonstrates effective application of established algorithms in a hybrid architecture that balances security, performance, and operational resilience. The system provides a foundation for future enhancements including network transfer capabilities, graphical user interfaces, and integration with cloud storage platforms.

**Keywords:** Hybrid Encryption, AES-256, XChaCha20, File Security, Nonce Management, Authenticated Encryption, Cryptographic Implementation

---

# ACKNOWLEDGEMENT

We express our sincere gratitude to our project guide, **Mr. Gaurav Thakur**, Assistant Professor, Department of Computer Science & Engineering, Central University of Jammu, for his invaluable guidance, constant encouragement, and support throughout this project. His insights into cryptographic systems and security engineering significantly enhanced our understanding and implementation approach.

We are thankful to **Dr. [HOD Name]**, Head of Department, Computer Science & Engineering, for providing necessary facilities and resources that enabled successful project completion. We also acknowledge the faculty members of the Department of Computer Science & Engineering for their academic guidance and support.

We appreciate the open-source community, particularly the maintainers of PyCryptodome and PyNaCl libraries, whose well-documented, secure implementations formed the foundation of our work.

Finally, we express gratitude to our family and friends for their continuous support and motivation throughout this endeavor.

**Pragati Raj (22BECCS28)**  
**Prajjwal Gupta (22BECCS29)**

---

# TABLE OF CONTENTS

| Contents | Page No. |
|----------|----------|
| Abstract | i |
| Acknowledgement | ii |
| List of Figures | iii |
| List of Tables | iv |
| Table of Contents | v |
| **Chapter 1: Introduction** | **1** |
| 1.1 Project Overview | 2 |
| 1.2 Objectives of Project | 3 |
| 1.3 Problem Formulation | 4 |
| 1.4 Existing System | 5 |
| 1.5 Proposed System | 6 |
| 1.6 Features of the Project | 8 |
| **Chapter 2: Requirement Analysis** | **10** |
| 2.1 Feasibility Study | 11 |
| 2.2 Software Requirement Specification | 13 |
| 2.3 SDLC Model Used | 15 |
| **Chapter 3: System Design** | **17** |
| 3.1 Product Perspective | 18 |
| 3.2 Product Functions | 19 |
| 3.3 User Characteristics | 20 |
| 3.4 Constraints | 21 |
| 3.5 Use Case Model/Flow Chart/DFDs | 22 |
| 3.6 Database Design | 25 |
| 3.7 Table Structure | 26 |
| 3.8 ER Diagrams | 27 |
| 3.9 Assumptions and Dependencies | 28 |
| 3.10 Specific Requirements | 29 |
| **Chapter 4: Development, Implementation and Testing** | **31** |
| 4.1 Introduction to Development Environment | 32 |
| 4.2 Supporting Languages and Tools | 34 |
| 4.3 Implementation of Problem | 36 |
| 4.4 Test Cases | 40 |
| **Chapter 5: Results and Discussions** | **43** |
| 5.1 User Interface Representation | 44 |
| 5.2 Parameters Used for Evaluation | 46 |
| 5.3 Comparative Analysis | 47 |
| 5.4 Project Screenshots with Explanation | 50 |
| **Chapter 6: Conclusion and Future Scope** | **54** |
| 6.1 Conclusion | 55 |
| 6.2 Future Scope | 56 |
| **References** | **57** |
| **Appendix** | **58** |

---

# LIST OF FIGURES

| Fig. No. | Figure Title | Page No. |
|----------|--------------|----------|
| 1.1 | System Architecture Overview | 7 |
| 3.1 | System Architecture Diagram | 18 |
| 3.2 | Encryption Process Flowchart | 22 |
| 3.3 | Decryption Process Flowchart | 23 |
| 3.4 | Data Flow Diagram - Level 0 | 24 |
| 3.5 | Use Case Diagram | 25 |
| 4.1 | Development Environment Setup | 32 |
| 4.2 | Module Interaction Diagram | 37 |
| 5.1 | Command-Line Interface - Info Command | 44 |
| 5.2 | Encryption Process Screenshot | 50 |
| 5.3 | Decryption Process Screenshot | 51 |
| 5.4 | Encryption Time vs File Size | 47 |
| 5.5 | Decryption Time vs File Size | 48 |
| 5.6 | Throughput Comparison | 48 |
| 5.7 | Encryption vs Decryption Time | 49 |
| 5.8 | Performance Summary Table | 49 |

---

# LIST OF TABLES

| Table No. | Table Caption | Page No. |
|-----------|---------------|----------|
| 2.1 | Hardware Requirements | 13 |
| 2.2 | Software Requirements | 14 |
| 3.1 | Functional Requirements | 29 |
| 3.2 | Non-Functional Requirements | 30 |
| 4.1 | Cryptographic Libraries Used | 34 |
| 4.2 | Module Description | 36 |
| 4.3 | Test Case Specifications | 40 |
| 4.4 | Test Results Summary | 42 |
| 5.1 | Performance Benchmarking Results | 46 |
| 5.2 | Comparative Analysis with Existing Systems | 47 |

---

# CHAPTER 1: INTRODUCTION

## 1.1 Project Overview

**Project Category:** Application Development / System Development

This project develops a secure file encryption system implementing a hybrid cryptographic approach that combines AES-256-GCM (Advanced Encryption Standard in Galois/Counter Mode) for file content encryption with XChaCha20-Poly1305 for encryption key protection. The system addresses critical operational challenges in contemporary encryption implementations, particularly nonce management vulnerabilities and performance limitations across heterogeneous computing environments.

The application provides a command-line interface enabling users to encrypt files of arbitrary size, with automated generation and secure storage of encryption keys. The hybrid architecture leverages AES-256 for high-throughput file encryption, benefiting from widespread hardware acceleration support in modern processors, while employing XChaCha20's extended nonce space (192 bits) to mitigate nonce reuse risks during key encryption operations.

Developed using Python 3.10+ with industry-standard cryptographic libraries (PyCryptodome and PyNaCl), the system ensures implementation security through reliance on audited, well-maintained code rather than custom cryptographic primitives. Version control through Git and comprehensive testing validate correct operation and enable collaborative development.

The project demonstrates practical application of cryptographic principles in addressing real-world security requirements, balancing theoretical soundness with operational feasibility. Performance benchmarking across files ranging from 1MB to 100MB characterizes system behavior under various workloads, while integrity verification confirms correct encryption and decryption across all test cases.

**Target Users:** Security-conscious individuals, organizations requiring secure file storage, developers seeking reference implementations of hybrid encryption systems, and educational institutions teaching applied cryptography.

**Key Innovation:** While individual components (AES and XChaCha20) are well-established, the project's contribution lies in their thoughtful integration to address specific operational challenges—namely nonce management in AES-GCM—while maintaining standards compliance and achieving practical performance characteristics.

## 1.2 Objectives of Project

The primary objectives of this project are clearly defined and fully implemented:

**Objective 1: Design and Implement a Hybrid Encryption Framework**

To develop a functional file encryption system combining AES-256-GCM for file content encryption with XChaCha20-Poly1305 for key encryption. This objective encompasses:
- Implementation of modular encryption components with clear interfaces
- Integration of components into a cohesive hybrid system
- Validation of correct cryptographic operation through comprehensive testing

**Implementation Status:** Fully achieved. The system implements separate modules for AES encryption (`aes_encryption.py`), XChaCha20 key encryption (`xchacha20_encryption.py`), and hybrid system integration (`hybrid_encryption.py`), with all modules tested independently and in integrated operation.

**Objective 2: Address Nonce Management Vulnerabilities**

To mitigate nonce reuse vulnerabilities inherent in AES-GCM implementations by employing XChaCha20's extended 192-bit nonce space for key encryption. This objective includes:
- Analysis of nonce reuse risks in traditional AES-GCM deployments
- Implementation of XChaCha20-Poly1305 with proper nonce generation
- Demonstration of reduced collision probability through extended nonce space

**Implementation Status:** Fully achieved. The system generates cryptographically secure random nonces for both AES and XChaCha20 operations, with XChaCha20's 192-bit nonce providing 2^96 times larger nonce space than standard AES-GCM, dramatically reducing collision probability.

**Objective 3: Develop User-Friendly Interface and Automation**

To provide accessible encryption capabilities through a command-line interface with automated key management and metadata handling. This objective encompasses:
- CLI implementation with intuitive commands (encrypt, decrypt, info)
- Automated generation and secure storage of encryption keys
- Metadata management for seamless decryption without manual key handling

**Implementation Status:** Fully achieved. The CLI (`cli.py`) provides three primary commands with clear usage patterns, automated key generation and encryption, and metadata-based decryption that eliminates manual key management for end users.

**Objective 4: Evaluate Performance Characteristics and Validate Security Properties**

To conduct comprehensive performance benchmarking across various file sizes and validate security properties through testing. This objective includes:
- Performance measurement (encryption/decryption time, throughput)
- Integrity verification confirming correct operation
- Comparative analysis with single-algorithm approaches where feasible

**Implementation Status:** Fully achieved. Performance testing across 1MB to 100MB files demonstrates consistent throughput, with all test cases confirming perfect integrity (original and decrypted files match exactly). Visualization tools generate graphs for performance analysis included in this report.

## 1.3 Problem Formulation

Contemporary file encryption systems face a convergence of security, performance, and operational challenges that motivate this project's hybrid approach.

**Problem 1: Nonce Reuse Vulnerability in AES-GCM**

AES in Galois/Counter Mode requires a unique nonce for each encryption operation using the same key. Nonce reuse represents a catastrophic failure mode: when the same nonce encrypts multiple plaintexts with the same key, attackers can recover XOR combinations of plaintexts and potentially extract authentication keys. The IETF explicitly warns that "implementations must ensure that [nonce] values are not repeated for a given key" and notes that "the security consequences of nonce reuse are severe."

This requirement creates operational burden: systems must maintain state across encryption operations, implement robust random number generation, or employ counters with guaranteed uniqueness. In distributed systems, coordinating nonce uniqueness across multiple nodes introduces additional complexity. Human error, software bugs, or system failures can lead to nonce reuse, compromising security despite algorithmically sound encryption.

**Problem 2: Performance Heterogeneity Across Computing Platforms**

AES performance varies dramatically between hardware-accelerated and software-only implementations. Modern Intel and AMD processors with AES-NI achieve multi-gigabyte-per-second throughput, while software implementations on processors lacking such instructions experience 10x to 100x performance degradation. This disparity creates challenges for systems spanning diverse hardware:
- High-performance servers with AES-NI
- General-purpose workstations with varying capabilities  
- Mobile devices with ARM processors (some with crypto extensions, some without)
- IoT devices and embedded systems with limited computational resources

Organizations requiring uniform security policies across heterogeneous infrastructure must either accept degraded performance on some platforms or implement platform-specific optimizations, increasing complexity and testing burden.

**Problem 3: Algorithm Agility and Defense in Depth**

Exclusive reliance on a single cryptographic algorithm creates systemic risk. While AES remains secure against known attacks after decades of scrutiny, prudent security engineering acknowledges possibilities of future cryptanalytic breakthroughs or implementation vulnerabilities. The principle of defense in depth suggests employing multiple independent security layers such that compromise of one layer does not result in total system failure.

**Problem 4: Compliance Requirements and Operational Reality**

Regulatory frameworks often mandate specific cryptographic standards. FIPS 140-2, governing U.S. federal agency cryptography, explicitly approves AES but not ChaCha20. Organizations cannot simply abandon AES for operationally superior alternatives without violating compliance requirements. This creates tension between regulatory mandates and operational best practices.

**Proposed Solution Approach**

This project addresses these challenges through a hybrid encryption architecture:

1. **Layered Security:** File content encrypted with AES-256-GCM (addressing compliance requirements, leveraging hardware acceleration where available)

2. **Enhanced Key Protection:** AES keys encrypted with XChaCha20-Poly1305, providing 192-bit nonce space that dramatically reduces collision probability even under imperfect randomness

3. **Algorithmic Diversity:** Two independent encryption algorithms provide defense in depth; compromise of one does not compromise the entire system

4. **Practical Performance:** Hardware-accelerated AES provides high throughput for bulk data; XChaCha20 operates efficiently in software for small key encryption operations

This approach acknowledges that most security failures result from operational issues rather than algorithmic weaknesses, designing a system that mitigates common implementation pitfalls while maintaining cryptographic soundness.

## 1.4 Existing System

Current approaches to file encryption fall into several categories, each with distinct characteristics and limitations relevant to this project's motivation.

**Single-Algorithm Approaches (AES-Only Systems)**

Many existing file encryption tools employ AES exclusively, typically in GCM or CBC mode with separate authentication. Examples include:

- **VeraCrypt:** Implements AES-256 in XTS mode for full-disk encryption, with cascading options for multiple algorithms
- **BitLocker:** Microsoft's Windows encryption using AES-128 or AES-256 in XTS mode
- **GPG/PGP:** Uses AES (among other algorithms) for symmetric encryption of message contents

**Characteristics:**
- Mature, well-tested implementations with extensive deployment history
- Hardware acceleration support on modern platforms yields excellent performance
- Compliance with regulatory standards (FIPS 140-2, etc.)
- Widespread compatibility and standardization

**Limitations:**
- Nonce management burden remains with application developers
- Performance degradation on platforms lacking hardware acceleration
- Single point of cryptanalytic failure (all security depends on AES)
- Documented vulnerabilities when nonce reuse occurs in GCM mode

**ChaCha20-Based Systems**

Modern systems increasingly adopt ChaCha20-Poly1305, particularly in contexts where software performance matters:

- **WireGuard VPN:** Uses ChaCha20-Poly1305 as primary cipher suite
- **TLS 1.3:** Includes ChaCha20-Poly1305 as mandatory-to-implement cipher suite
- **Signal Protocol:** Uses ChaCha20 variant for message encryption

**Characteristics:**
- Excellent software performance across diverse platforms
- Large nonce space reduces management burden
- Resistance to timing attacks in software implementations
- Growing adoption in modern protocols

**Limitations:**
- Not FIPS 140-2 approved (regulatory compliance issues)
- Less hardware acceleration support than AES
- Newer algorithm with shorter cryptanalytic history than AES

**Traditional Hybrid Encryption (RSA + AES)**

Standard hybrid encryption combines asymmetric algorithms for key exchange with symmetric algorithms for bulk encryption:

- **GPG/PGP:** RSA or ECC for key encryption, AES for message encryption
- **S/MIME:** Similar approach for email encryption
- **TLS/SSL:** Handshake with RSA/ECDH, session encryption with AES or ChaCha20

**Characteristics:**
- Solves key distribution problem through public-key cryptography
- Enables secure communication without prior shared secrets
- Well-understood and widely deployed

**Limitations:**
- Asymmetric operations significantly slower than symmetric
- Larger keys required for equivalent security levels
- Complexity of public key infrastructure (PKI) management
- Vulnerability to quantum computing attacks (RSA, ECC)

**Commercial File Encryption Tools**

Various commercial tools provide file-level encryption:

- **AxCrypt:** AES-256 file encryption with key management
- **7-Zip with encryption:** AES-256 in CBC mode for archive encryption
- **Proprietary cloud storage encryption:** Provider-specific implementations

**Limitations Common to Existing Systems:**

1. **Nonce Management:** Systems using AES-GCM must carefully manage nonce uniqueness; failures lead to catastrophic security breaches

2. **Performance Variability:** Single-algorithm systems perform inconsistently across platforms; AES-only systems slow on non-accelerated hardware, ChaCha20-only systems lack regulatory approval

3. **Lack of Algorithmic Diversity:** Most systems rely exclusively on one algorithm family; cryptanalytic breakthrough or implementation vulnerability affects all users

4. **Complexity vs. Usability Trade-off:** Systems with robust key management often impose complexity burden on users; simple systems may lack security features

**Gap Analysis**

Existing systems generally do not combine symmetric algorithms in complementary roles to address operational challenges while maintaining compliance. Traditional hybrid encryption combines asymmetric and symmetric approaches for key distribution, not for addressing nonce management or performance heterogeneity in symmetric encryption itself.

This project fills this gap by employing two symmetric algorithms—AES for bulk encryption (compliance, hardware acceleration) and XChaCha20 for key encryption (extended nonce space, software performance)—creating a practical system that addresses documented operational challenges in real-world encryption deployments.

## 1.5 Proposed System

This project proposes a hybrid symmetric encryption framework combining AES-256-GCM for file content encryption with XChaCha20-Poly1305 for encryption key protection, implemented as a command-line application with automated key management.

**System Architecture**

The system comprises four primary components:

**1. AES-256-GCM File Encryption Module**
- Encrypts file content using AES-256 in Galois/Counter Mode
- Generates cryptographically secure random 256-bit encryption keys
- Produces 128-bit nonces using system random number generator
- Returns authenticated ciphertext with authentication tag
- Implements PyCryptodome library for audited AES implementation

**2. XChaCha20-Poly1305 Key Encryption Module**
- Encrypts AES keys using XChaCha20-Poly1305
- Generates 256-bit master keys for XChaCha20
- Utilizes 192-bit nonces (extended from ChaCha20's 96-bit nonce)
- Provides authenticated encryption of key material
- Implements PyNaCl library wrapping libsodium implementation

**3. Hybrid Integration Controller**
- Orchestrates encryption workflow: file → AES encryption → key → XChaCha20 encryption
- Manages metadata generation and storage
- Coordinates decryption process in reverse order
- Handles error conditions and validates integrity
- Implements cleanup and secure key erasure after operations

**4. Command-Line Interface**
- Provides user-facing commands: `encrypt`, `decrypt`, `info`
- Automates key generation and management
- Displays progress and status information
- Formats output for readability
- Implements input validation and error handling

**Operational Workflow**

**Encryption Process:**

1. User invokes: `python cli.py encrypt -f document.pdf`

2. System generates random 256-bit AES key

3. File content encrypted with AES-256-GCM:
   - Random 128-bit nonce generated
   - Content encrypted in streaming fashion
   - Authentication tag computed over ciphertext

4. System generates random 256-bit XChaCha20 master key

5. AES key encrypted with XChaCha20-Poly1305:
   - Random 192-bit nonce generated
   - AES key encrypted as authenticated data
   - Resulting ciphertext includes authentication tag

6. System saves three files:
   - `document.pdf.enc`: Encrypted file content
   - `document.pdf.key`: Encrypted AES key
   - `document.pdf.meta`: JSON metadata containing file information and master key

**Decryption Process:**

1. User invokes: `python cli.py decrypt -m encrypted/document.pdf.meta`

2. System loads metadata file, extracting:
   - Original filename
   - Path to encrypted file
   - Path to encrypted key file
   - XChaCha20 master key

3. Encrypted AES key decrypted using XChaCha20 master key

4. File content decrypted using recovered AES key

5. Decrypted file saved with original filename

6. System verifies integrity through authentication tag validation

**Security Properties**

**Confidentiality:** Both file content and encryption keys protected by strong symmetric ciphers (AES-256, XChaCha20) with 256-bit keys providing ~2^256 security level against brute force

**Integrity:** Authenticated encryption in both layers (GCM, Poly1305) detects tampering; modified ciphertext fails authentication, preventing undetected alterations

**Nonce Management:** XChaCha20's 192-bit nonce provides 2^96 times larger space than standard GCM, reducing collision probability to negligible levels even under birthday bounds

**Key Separation:** Different keys used for file content and key encryption; compromise of one does not directly compromise the other

**Forward Secrecy (Limited):** Master keys stored in metadata; users can delete metadata after secure key distribution for forward secrecy properties

**Technical Specifications**

- **Programming Language:** Python 3.10+
- **AES Implementation:** PyCryptodome 3.19.0 (pure Python with optional C acceleration)
- **XChaCha20 Implementation:** PyNaCl 1.5.0 (wrapping libsodium C library)
- **Key Sizes:** 256 bits (AES), 256 bits (XChaCha20)
- **Nonce Sizes:** 128 bits (AES-GCM), 192 bits (XChaCha20)
- **Operating Systems:** Cross-platform (Linux, Windows, macOS)
- **Dependencies:** Python standard library, PyCryptodome, PyNaCl, Matplotlib (for performance visualization)

**Design Principles**

1. **Modularity:** Independent components enable separate testing and potential reuse

2. **Fail-Safe:** Authentication failures result in immediate operation abort; never return unauthenticated plaintext

3. **Automation:** Users need not manually manage keys; system handles generation, encryption, and storage

4. **Transparency:** Open-source implementation using well-documented libraries; no proprietary or obscure cryptographic code

5. **Performance:** Streaming encryption for large files prevents memory exhaustion; hardware acceleration utilized where available

**Advantages Over Existing Approaches**

- Addresses AES-GCM nonce reuse vulnerability through XChaCha20's extended nonce space
- Maintains AES compliance for regulatory requirements
- Provides algorithmic diversity (defense in depth)
- Achieves practical performance across heterogeneous platforms
- Simplifies key management through automation
- Open implementation enables audit and verification

## 1.6 Features of the Project

This section enumerates the key features implemented in the hybrid encryption system, demonstrating functionality and capability.

**Feature 1: Dual-Layer Hybrid Encryption**

The system implements a two-layer encryption architecture where file content and encryption keys are protected by different algorithms operating in complementary roles. This approach provides:
- **Primary encryption:** AES-256-GCM for file content (fast, hardware-accelerated)
- **Key protection:** XChaCha20-Poly1305 for AES key encryption (large nonce space)
- **Independent security layers:** Compromise of one algorithm does not directly expose the other layer

**Feature 2: Automated Key Generation and Management**

Users need not manually generate or handle cryptographic keys:
- System automatically generates cryptographically secure random keys
- Key generation uses operating system's secure random number generator
- Keys automatically encrypted before storage
- Metadata files store encrypted keys and necessary decryption information
- No plaintext key material exposed to users

**Feature 3: Authenticated Encryption at All Layers**

Both encryption layers provide authentication, ensuring data integrity:
- **AES-GCM:** Galois/Counter Mode provides authenticated encryption; tampering detected during decryption
- **XChaCha20-Poly1305:** Poly1305 MAC authenticates encrypted keys
- Failed authentication results in immediate operation abort
- No unauthenticated data ever returned to user

**Feature 4: Extended Nonce Space for Enhanced Security**

XChaCha20's 192-bit nonce dramatically reduces collision probability:
- Standard AES-GCM: 96-bit nonce (2^96 possible values)
- XChaCha20: 192-bit nonce (2^192 possible values)
- Collision probability reduced by factor of 2^96
- Enables secure random nonce generation without state coordination
- Mitigates risks from imperfect random number generators

**Feature 5: Command-Line Interface with Multiple Operations**

User-friendly CLI providing three primary commands:

**`encrypt` command:**
- Syntax: `python cli.py encrypt -f filename`
- Encrypts specified file
- Generates all keys automatically
- Creates encrypted file, key file, and metadata
- Displays progress and completion status

**`decrypt` command:**
- Syntax: `python cli.py decrypt -m metadata_file`
- Decrypts file using metadata
- Validates integrity during decryption
- Restores original filename
- Reports success or failure

**`info` command:**
- Syntax: `python cli.py info`
- Displays system information
- Shows encryption methods used
- Explains security features
- Provides usage examples

**Feature 6: Streaming Encryption for Large Files**

Files processed in chunks rather than loading entirely into memory:
- Prevents memory exhaustion with large files
- Enables encryption of files exceeding available RAM
- Maintains consistent performance regardless of file size
- Suitable for encrypting multi-gigabyte files

**Feature 7: Comprehensive Metadata Management**

System generates JSON metadata files containing all information needed for decryption:
- Original filename
- Encrypted file path
- Encrypted key file path
- XChaCha20 master key (for key decryption)
- File size information
- Human-readable format for inspection

**Feature 8: Cross-Platform Compatibility**

Implementation runs on multiple operating systems:
- **Linux:** Tested on Ubuntu 22.04
- **Windows:** Compatible with Windows 10/11
- **macOS:** Should function (Python cross-platform)
- Same codebase across platforms
- Platform-independent file formats

**Feature 9: Modular Architecture for Testing and Extension**

System organized as independent, testable modules:
- `aes_encryption.py`: AES operations only
- `xchacha20_encryption.py`: XChaCha20 operations only
- `hybrid_encryption.py`: Integration logic
- `cli.py`: User interface
- Each module includes self-test functionality

**Feature 10: Performance Benchmarking and Visualization**

System includes comprehensive performance testing:
- Benchmarks across multiple file sizes (1MB to 100MB)
- Measures encryption time, decryption time, throughput
- Generates performance graphs automatically
- Provides data for comparative analysis
- Results reproducible and verifiable

**Feature 11: Integrity Verification**

All operations validate data integrity:
- Decryption includes authentication tag verification
- Tampered ciphertext detected and rejected
- Test suite confirms original and decrypted files match exactly
- Cryptographic guarantees of integrity preservation

**Feature 12: Version Control and Development Transparency**

Project developed with full version control:
- Complete Git history documents development process
- All code committed with descriptive messages
- GitHub repository enables code review and collaboration
- Transparent development process demonstrates learning and iteration

**Feature 13: Comprehensive Documentation**

Project includes multiple documentation layers:
- Inline code comments explaining implementation details
- README file with installation and usage instructions
- This comprehensive project report
- Performance test results and graphs
- User manual in appendices

**Feature 14: Open-Source Implementation**

System built entirely with open-source tools and libraries:
- Python interpreter (open source)
- PyCryptodome (open source, BSD-licensed)
- PyNaCl (open source, Apache-licensed)
- No proprietary dependencies
- Code available for audit and verification

---

# CHAPTER 2: REQUIREMENT ANALYSIS

## 2.1 Feasibility Study

Feasibility analysis evaluates whether the proposed system can be successfully developed and deployed given available resources, technical capabilities, and constraints.

**Technical Feasibility**

**Question:** Can the system be implemented with available technology and team expertise?

**Analysis:**

*Cryptographic Libraries:* Python ecosystem provides mature, well-maintained cryptographic libraries (PyCryptodome, PyNaCl) implementing required algorithms. These libraries undergo regular security audits and maintain active development communities. Implementation does not require custom cryptographic code—a significant risk factor eliminated.

*Development Environment:* Project requires only standard development tools: Python interpreter, text editor/IDE, Git for version control. All tools freely available across platforms. Team members have prior Python experience from coursework.

*Algorithm Complexity:* While cryptographic algorithms themselves are mathematically complex, library abstractions hide implementation details. Team needs understanding of proper API usage, key management, and security principles rather than low-level algorithm implementation.

*Integration Challenges:* Combining two encryption systems requires careful orchestration but involves well-defined steps (encrypt file, encrypt key, store metadata). No novel protocols or complex distributed systems coordination required.

**Conclusion:** Technically feasible. Required libraries exist, are well-documented, and team possesses necessary programming skills.

**Operational Feasibility**

**Question:** Will the system be usable by target audience in practical scenarios?

**Analysis:**

*User Interface:* Command-line interface familiar to technical users (developers, system administrators, security professionals). Simple three-command structure (encrypt, decrypt, info) minimizes learning curve. Clear output messages guide users through operations.

*Key Management:* Automated key generation and management eliminates common user errors. Users need not understand cryptographic details; system handles complexity internally. Metadata files simplify decryption—users provide single file rather than coordinating keys manually.

*Performance:* Benchmarking demonstrates acceptable performance for typical file sizes. System processes 100MB files in seconds on standard hardware, sufficient for common use cases (documents, images, moderate-size datasets).

*Portability:* Cross-platform implementation enables deployment on diverse systems without modification. Users on different operating systems can exchange encrypted files.

**Conclusion:** Operationally feasible for target technical audience. Non-technical users would benefit from future GUI implementation.

**Economic Feasibility**

**Question:** Is the project economically viable given budget and resource constraints?

**Analysis:**

*Development Costs:* Zero licensing costs—all software components open source. Development requires only time investment by team members (academic project context).

*Hardware Requirements:* System runs on standard personal computers; no specialized hardware required. Team members' existing laptops sufficient for development and testing.

*Library Costs:* All cryptographic libraries freely available under permissive licenses (BSD, Apache). No subscription fees or usage restrictions.

*Deployment Costs:* End users require only Python runtime and libraries—freely downloadable. No infrastructure costs, no cloud services required.

*Maintenance Costs:* Open-source dependencies maintained by active communities; security updates provided free of charge.

**Conclusion:** Economically feasible with zero monetary cost. Academic setting provides time resources for development.

**Schedule Feasibility**

**Question:** Can the project be completed within available timeframe?

**Analysis:**

*Project Duration:* Academic semester provides approximately 4-5 months for project work. Development planned in iterative phases.

*Complexity Assessment:* Core functionality (encryption/decryption modules) requires ~2-3 weeks. Integration and CLI development ~1-2 weeks. Testing and documentation ~2-3 weeks. Performance benchmarking ~1 week. Buffer time for debugging and refinement ~2-3 weeks.

*Parallel Work:* Two team members enable parallel development (one on AES module, one on XChaCha20 module). Later integration reduces total timeline.

*Risk Mitigation:* Modular architecture allows delivery of core functionality even if advanced features require deferral. Command-line interface simpler than GUI, reducing schedule risk.

**Conclusion:** Schedule feasible with proper task allocation and iterative development approach.

**Legal Feasibility**

**Question:** Are there legal or regulatory constraints preventing implementation or deployment?

**Analysis:**

*Export Controls:* Cryptographic software historically subject to export controls. However, modern regulations generally permit export of publicly available cryptographic software with notification. Project uses standard, widely-deployed algorithms, not novel or classified techniques.

*Patent Issues:* AES and ChaCha20 are patent-free, explicitly designed for unrestricted use. No licensing concerns for algorithm implementation.

*Library Licenses:* PyCryptodome (BSD license) and PyNaCl (Apache license) permit use, modification, and distribution without restrictions beyond attribution requirements.

*Educational Context:* Project developed for academic purposes; educational use generally protected. No commercial deployment planned.

**Conclusion:** No legal barriers identified. Standard open-source licensing applies.

**Overall Feasibility Assessment**

All feasibility dimensions (technical, operational, economic, schedule, legal) indicate project viability. Primary risks—cryptographic implementation errors—mitigated through use of established libraries rather than custom code. Project scope appropriate for academic timeframe with two-person team.

## 2.2 Software Requirement Specification

This section documents functional and non-functional requirements, hardware and software needs, and system constraints.

**Functional Requirements**

Functional requirements define what the system must do—specific behaviors and operations.

**FR1: File Encryption**
- **Description:** System shall encrypt files of arbitrary size using AES-256-GCM
- **Input:** File path, optional output directory
- **Processing:** Generate random AES key, generate random nonce, encrypt file content, generate authentication tag
- **Output:** Encrypted file with .enc extension
- **Priority:** High (core functionality)

**FR2: Key Encryption**
- **Description:** System shall encrypt AES keys using XChaCha20-Poly1305
- **Input:** AES key (32 bytes), optional output directory
- **Processing:** Generate XChaCha20 master key, generate 192-bit nonce, encrypt AES key
- **Output:** Encrypted key file with .key extension
- **Priority:** High (core functionality)

**FR3: Metadata Generation**
- **Description:** System shall generate metadata files containing decryption information
- **Input:** Original filename, encrypted file path, key file path, master key
- **Processing:** Format as JSON, write to file
- **Output:** Metadata file with .meta extension
- **Priority:** High (required for decryption)

**FR4: File Decryption**
- **Description:** System shall decrypt files using metadata
- **Input:** Metadata file path, optional output directory
- **Processing:** Load metadata, decrypt AES key, decrypt file content, verify integrity
- **Output:** Decrypted file with original filename
- **Priority:** High (core functionality)

**FR5: Integrity Verification**
- **Description:** System shall verify data integrity during decryption
- **Input:** Encrypted data, authentication tags
- **Processing:** Validate GCM tag, validate Poly1305 tag
- **Output:** Success/failure indication
- **Priority:** High (security requirement)

**FR6: Command-Line Interface**
- **Description:** System shall provide CLI with encrypt, decrypt, and info commands
- **Input:** Command-line arguments
- **Processing:** Parse arguments, validate inputs, invoke appropriate functions
- **Output:** Formatted text output, status messages
- **Priority:** Medium (usability)

**FR7: Automated Key Generation**
- **Description:** System shall automatically generate cryptographically secure keys
- **Input:** None (automatic)
- **Processing:** Use OS random number generator
- **Output:** 256-bit keys for AES and XChaCha20
- **Priority:** High (security requirement)

**FR8: Error Handling**
- **Description:** System shall handle errors gracefully with informative messages
- **Input:** Various error conditions
- **Processing:** Detect errors, format messages, exit safely
- **Output:** Error messages to console
- **Priority:** Medium (robustness)

**Non-Functional Requirements**

Non-functional requirements define system qualities and constraints.

**NFR1: Performance**
- System shall encrypt/decrypt 100MB files in under 10 seconds on standard hardware (Intel i5 or equivalent)
- Throughput shall exceed 10 MB/s for both encryption and decryption
- Memory usage shall not exceed 500MB regardless of file size (streaming implementation)

**NFR2: Security**
- System shall use cryptographically secure random number generators for all key and nonce generation
- System shall employ authenticated encryption at all layers
- System shall never output unauthenticated plaintext
- Keys shall never be stored in plaintext form accessible to users

**NFR3: Reliability**
- System shall produce identical output for identical input (deterministic given keys/nonces)
- Decrypted files shall match original files with 100% accuracy
- System shall handle interruptions gracefully without corrupting data

**NFR4: Usability**
- Command syntax shall follow standard CLI conventions
- Help messages shall clearly explain usage
- Error messages shall indicate problem cause and resolution steps
- System shall provide progress feedback for operations exceeding 1 second

**NFR5: Portability**
- System shall run on Linux, Windows, and macOS without modification
- System shall work with Python 3.8+ (broad version compatibility)
- Encrypted files shall be platform-independent

**NFR6: Maintainability**
- Code shall follow PEP 8 style guidelines
- Functions shall include docstrings explaining purpose and parameters
- Modules shall be loosely coupled for independent testing
- Version control shall maintain complete development history

**NFR7: Security Compliance**
- AES implementation shall use NIST-standardized algorithm
- Key sizes shall meet current NIST recommendations (256 bits minimum)
- System shall not implement custom cryptographic primitives

**Hardware Requirements**

**Minimum Requirements:**
- **Processor:** Any modern x86-64 or ARM processor
- **RAM:** 512 MB available
- **Storage:** 100 MB for software, additional space for encrypted files
- **Operating System:** Linux (Ubuntu 20.04+), Windows 10+, macOS 10.15+

**Recommended Requirements:**
- **Processor:** Intel Core i5 / AMD Ryzen 5 or equivalent (with AES-NI for optimal performance)
- **RAM:** 2 GB available
- **Storage:** 1 GB for software and test files
- **Operating System:** Ubuntu 22.04 LTS / Windows 11

**Software Requirements**

**Development Environment:**
- **Python:** Version 3.10 or higher
- **IDE/Editor:** Visual Studio Code (recommended) or any text editor
- **Version Control:** Git 2.30+
- **Operating System:** Ubuntu 22.04 LTS (development), Windows 11 (testing)

**Runtime Dependencies:**
- **Python Libraries:**
  - PyCryptodome 3.19.0 (AES implementation)
  - PyNaCl 1.5.0 (XChaCha20 implementation)
  - Matplotlib 3.7.1 (performance visualization)
- **System Libraries:**
  - libsodium (automatically installed with PyNaCl)

**Development Tools:**
- **Testing:** Python unittest framework (standard library)
- **Documentation:** Markdown for README, LaTeX/Word for report
- **Performance Measurement:** Python time module (standard library)

**Installation Commands:**

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install pycryptodome==3.19.0
pip install PyNaCl==1.5.0
pip install matplotlib==3.7.1
```

## 2.3 SDLC Model Used

**Selected Model: Iterative Development with Incremental Delivery**

This project employs an iterative development approach combining elements of incremental and agile methodologies, selected for its suitability to cryptographic software development and academic project constraints.

**Model Overview**

The iterative model divides development into multiple iterations, each producing a working increment of the system. Each iteration includes requirements analysis, design, implementation, testing, and evaluation phases. Unlike waterfall development, iterations allow refinement based on testing feedback and evolving understanding of requirements.

**Phases and Activities**

**Phase 1: Initial Planning and Design (Week 1-2)**

*Activities:*
- Literature review on AES, XChaCha20, and hybrid encryption
- Requirements definition and feasibility study
- High-level architecture design
- Development environment setup
- Git repository initialization

*Deliverables:*
- Project synopsis document
- Architecture diagrams
- Development environment configured

**Phase 2: Core Module Development (Week 3-5)**

*Iteration 2.1: AES Encryption Module*
- Design AES encryption interface
- Implement file encryption with AES-256-GCM
- Implement file decryption
- Unit testing of AES operations
- Performance characterization

*Iteration 2.2: XChaCha20 Key Encryption Module*
- Design XChaCha20 encryption interface
- Implement key encryption functionality
- Implement key decryption
- Unit testing of XChaCha20 operations
- Nonce space analysis

*Deliverables:*
- `aes_encryption.py` with tests
- `xchacha20_encryption.py` with tests
- Test results documentation

**Phase 3: Integration and Hybrid System (Week 6-7)**

*Activities:*
- Design hybrid system architecture
- Implement integration controller
- Coordinate encryption workflow (file → AES → key → XChaCha20)
- Coordinate decryption workflow (reverse order)
- Integration testing
- Error handling and edge case testing

*Deliverables:*
- `hybrid_encryption.py` with integration logic
- Integration test suite
- Validated end-to-end functionality

**Phase 4: User Interface Development (Week 8-9)**

*Activities:*
- Design command-line interface
- Implement encrypt command with argument parsing
- Implement decrypt command
- Implement info command
- Input validation and error messages
- Usage documentation

*Deliverables:*
- `cli.py` with complete interface
- User manual
- Command examples and tutorials

**Phase 5: Performance Testing and Optimization (Week 10-11)**

*Activities:*
- Design performance test suite
- Implement automated benchmarking across file sizes
- Generate performance graphs
- Analyze results and identify bottlenecks
- Optimize critical paths if necessary
- Comparative analysis with baseline systems

*Deliverables:*
- `performance_test.py` script
- Performance data (JSON results)
- Visualization graphs
- Performance analysis report

**Phase 6: Documentation and Refinement (Week 12-14)**

*Activities:*
- Code cleanup and refactoring
- Documentation completion (docstrings, comments)
- Project report writing
- Final testing and validation
- Prepare presentation materials

*Deliverables:*
- Complete project report
- Polished codebase
- Presentation slides
- Final GitHub repository

**Rationale for Model Selection**

**Iterative Approach Benefits:**

1. **Risk Mitigation:** Cryptographic systems require careful validation. Iterative development with continuous testing reduces risk of fundamental design flaws discovered late.

2. **Feedback Integration:** Each iteration produces working software enabling testing and evaluation. Findings inform subsequent iterations.

3. **Incremental Complexity:** System built from simple components (individual encryption modules) toward complex integrated system. Each stage builds on validated foundation.

4. **Team Collaboration:** Two-person team benefits from parallel development of independent modules (Phase 2), then collaboration on integration (Phase 3).

5. **Academic Constraints:** Iterative model accommodates semester timeline with clear milestones. Regular deliverables provide progress visibility.

**Alternative Models Considered and Rejected:**

**Waterfall:** Rejected due to inflexibility. Cryptographic systems often require design adjustments based on testing; waterfall's sequential nature prevents iteration.

**Pure Agile:** Rejected due to lack of formal requirements in academic context. Project requires comprehensive documentation and structured report, not continuous delivery.

**Spiral Model:** Rejected as overly complex for two-person, single-project context. Risk analysis overhead unnecessary given use of established libraries.

**Development Practices**

The following practices support the iterative model:

**Version Control:**
- Git for all source code
- Frequent commits with descriptive messages
- Branching for experimental features
- GitHub for collaboration and backup

**Testing:**
- Unit tests for each module
- Integration tests for combined system
- Performance benchmarks
- Integrity verification tests

**Code Review:**
- Peer review between team members
- Focus on security-critical sections
- Style consistency checks

**Documentation:**
- Inline code comments
- Module-level docstrings
- README with setup instructions
- This comprehensive report

**Continuous Integration (Informal):**
- Frequent builds and tests
- Immediate error detection
- Regression prevention

**Outcome**

The iterative model proved effective for this project. Modular development (Phase 2) enabled parallel work and early validation. Integration (Phase 3) proceeded smoothly due to well-defined module interfaces. CLI development (Phase 4) benefited from working core system. Performance testing (Phase 5) provided data for report. The approach balanced structured planning with flexibility to refine based on learning.

---

# CHAPTER 3: SYSTEM DESIGN

## 3.1 Product Perspective

The hybrid encryption system exists as a standalone command-line application designed to operate independently without external service dependencies. This section positions the system within the broader context of file encryption tools and cryptographic software.

**System Context**

The system operates at the application layer, interfacing with:
- **Operating System:** File system for read/write operations, OS-provided secure random number generation
- **Python Runtime:** Interpreter executes application code
- **Cryptographic Libraries:** PyCryptodome and PyNaCl provide algorithmic implementations
- **User:** Command-line interface for human interaction

**System Independence**

Unlike cloud-based encryption services or networked key management systems, this system:
- Operates entirely on local machine without network requirements
- Requires no external authentication or key servers
- Functions offline (air-gapped environments supported)
- Maintains user control over all cryptographic material
- Avoids third-party trust dependencies

**Design Constraints from External Systems**

**Python Ecosystem:**
- Must conform to Python 3.x syntax and semantics
- Limited to Python-available cryptographic libraries
- Performance characteristics influenced by Python interpreter overhead

**Operating System APIs:**
- File I/O constrained by OS file system capabilities
- Random number generation quality depends on OS entropy sources
- Cross-platform compatibility requires OS-agnostic code

**Cryptographic Libraries:**
- AES implementation provided by PyCryptodome (cannot modify algorithm)
- XChaCha20 implementation provided by PyNaCl wrapping libsodium
- Must use library-provided interfaces and modes

**Standards Compliance:**
- AES follows FIPS 197 specification
- XChaCha20 follows RFC 8439 (ChaCha20) with extended nonce
- GCM and Poly1305 follow NIST and IETF specifications

**Interface with User**

The system presents a command-line interface as the sole user interaction mechanism. Future versions might add GUI or network transfer capabilities, but current scope focuses on local encryption with CLI interaction.

**Position in Encryption Ecosystem**

This system occupies a niche between simple single-algorithm tools and complex enterprise encryption solutions:
- More sophisticated than basic AES-only utilities
- Less complex than full-featured encryption suites with PKI
- Bridges academic cryptographic concepts with practical implementation
- Provides reference implementation for hybrid symmetric encryption

## 3.2 Product Functions

This section enumerates the major functions the system provides to users.

**Function 1: Secure File Encryption**

*Description:* Encrypt files of arbitrary size using hybrid AES-256 + XChaCha20 approach

*Inputs:*
- File path to encrypt
- Optional: output directory

*Processing Steps:*
1. Validate file exists and is readable
2. Generate 256-bit AES key using cryptographically secure RNG
3. Generate 128-bit nonce for AES-GCM
4. Encrypt file content with AES-256-GCM, producing ciphertext and authentication tag
5. Generate 256-bit XChaCha20 master key
6. Generate 192-bit nonce for XChaCha20
7. Encrypt AES key with XChaCha20-Poly1305
8. Generate metadata JSON containing file info and master key
9. Save encrypted file (.enc), encrypted key (.key), and metadata (.meta)

*Outputs:*
- Encrypted file maintaining original size plus overhead (16 bytes GCM tag + 16 bytes nonce)
- Encrypted key file (72 bytes: 32-byte key + 24-byte nonce + 16-byte Poly1305 tag)
- Metadata file (JSON format, human-readable)
- Console status messages indicating success/failure

*Error Conditions:*
- File not found → error message, exit
- Permission denied → error message, exit
- Insufficient disk space → error message, exit
- Encryption library error → error message, exit

**Function 2: Secure File Decryption**

*Description:* Decrypt files using metadata file containing necessary information

*Inputs:*
- Metadata file path (.meta)
- Optional: output directory

*Processing Steps:*
1. Load and parse metadata JSON
2. Validate metadata contains required fields
3. Load encrypted AES key from .key file
4. Load XChaCha20 master key from metadata
5. Decrypt AES key using XChaCha20, verifying Poly1305 tag
6. Load encrypted file content
7. Decrypt file content using AES-256-GCM, verifying GCM tag
8. Save decrypted content with original filename

*Outputs:*
- Decrypted file matching original exactly (bitwise identical)
- Console status messages indicating success/failure

*Error Conditions:*
- Metadata file not found → error message, exit
- Invalid metadata format → error message, exit
- Authentication failure (tampered data) → error message, exit WITHOUT outputting partial plaintext
- Missing encrypted file/key → error message, exit

**Function 3: System Information Display**

*Description:* Provide users with information about encryption system capabilities

*Inputs:* None (command: `python cli.py info`)

*Processing Steps:*
1. Format system information as readable text
2. Display encryption algorithms used
3. Explain key sizes and security properties
4. Show usage examples

*Outputs:*
- Formatted text to console explaining system features

**Function 4: Automated Key Management**

*Description:* Generate, encrypt, and store cryptographic keys automatically

*Inputs:* None (internal function called during encryption)

*Processing:*
1. Generate random bytes using `os.urandom()` or equivalent secure source
2. Verify sufficient entropy available
3. Generate keys of appropriate length (256 bits)
4. Encrypt keys before any persistent storage
5. Include keys in metadata for decryption

*Outputs:*
- Cryptographically secure random keys
- Keys never exposed in plaintext to user

**Function 5: Integrity Verification**

*Description:* Verify data has not been tampered with during storage or transmission

*Inputs:* Encrypted data with authentication tags

*Processing:*
1. During decryption, compute authentication tag over ciphertext
2. Compare computed tag with stored tag (constant-time comparison to prevent timing attacks)
3. Proceed with decryption only if tags match
4. Abort immediately if tags mismatch

*Outputs:*
- Success (tags match) → proceed with decryption
- Failure (tags mismatch) → error message, no plaintext output

**Function 6: Performance Benchmarking**

*Description:* Measure system performance across various file sizes

*Inputs:*
- List of file sizes to test (e.g., 1MB, 10MB, 100MB)

*Processing:*
1. Generate test files of specified sizes
2. Encrypt each file, recording time
3. Decrypt each file, recording time
4. Calculate throughput (MB/s)
5. Verify integrity (original matches decrypted)
6. Store results as JSON
7. Generate visualization graphs

*Outputs:*
- JSON file with performance data
- PNG graphs showing performance characteristics
- Console summary of results

## 3.3 User Characteristics

**Primary User Profile: Technical Professionals**

*Description:* Software developers, system administrators, security researchers, IT professionals

*Characteristics:*
- Comfortable with command-line interfaces
- Basic understanding of encryption concepts (even if not cryptographic experts)
- Familiar with file systems and paths
- Can follow technical documentation
- Likely using Linux or developer-oriented environments

*Needs:*
- Simple encryption without complex setup
- Automated key management
- Cross-platform compatibility
- Verifiable security properties (open source, established algorithms)
- Performance adequate for typical file sizes (documents, source code, databases)

*Usage Patterns:*
- Encrypt sensitive files before storage or transmission
- Integrate into scripts or automated workflows
- Test and verify encryption implementations
- Educational purposes (learning applied cryptography)

**Secondary User Profile: Security-Conscious Individuals**

*Description:* Privacy-aware users, journalists, activists, researchers handling sensitive data

*Characteristics:*
- May lack deep technical expertise
- Prioritize security and privacy
- Willing to use command-line if necessary
- Need reliable, trustworthy encryption
- May operate in adversarial environments

*Needs:*
- Strong encryption without vulnerabilities
- No reliance on third-party services
- Offline operation capability
- Open-source for auditability
- Clear documentation

*Usage Patterns:*
- Protect personal documents
- Encrypt files before cloud upload
- Secure communications data
- Long-term archival encryption

**Tertiary User Profile: Students and Educators**

*Description:* Computer science students, cryptography instructors, academic researchers

*Characteristics:*
- Learning cryptographic concepts and implementations
- Interested in understanding "how it works"
- May lack professional development experience
- Value clear code and documentation
- Need reference implementations for comparison

*Needs:*
- Understandable code structure
- Educational documentation
- Ability to modify and experiment
- Examples of correct cryptographic practices
- Performance data for analysis

*Usage Patterns:*
- Study hybrid encryption implementations
- Compare with other approaches
- Extend for research projects
- Incorporate into coursework

**User Skill Requirements**

*Minimum Skills:*
- Basic command-line operation
- File path understanding
- Ability to install Python and packages
- Following written instructions

*Recommended Skills:*
- Python programming (for code modification)
- Basic cryptography concepts
- Version control (Git) familiarity

**Accessibility Considerations**

Current implementation assumes:
- Users can read English-language documentation
- Users can interact with text-based interfaces
- Users have basic computer literacy

Future enhancements could address:
- GUI for non-technical users
- Internationalization (multiple languages)
- Enhanced error messages for beginners

## 3.4 Constraints

**Technical Constraints**

**TC1: Python Runtime Dependency**
- System requires Python 3.8+ interpreter
- Performance limited by Python overhead (compared to compiled languages)
- Memory management handled by Python garbage collector
- Cannot easily deploy as standalone executable without bundling

**TC2: Library Dependencies**
- Must use PyCryptodome and PyNaCl as provided
- Cannot modify underlying cryptographic implementations
- Dependent on library maintenance and security updates
- Potential compatibility issues with future library versions

**TC3: Platform Limitations**
- Random number generation quality depends on OS entropy source
- File I/O performance varies across operating systems and file systems
- Path handling must accommodate different OS conventions (/ vs \)

**TC4: Memory Constraints**
- While streaming prevents loading entire files, metadata and keys held in memory
- Python interpreter overhead ~50-100MB base memory usage
- Large-scale batch operations limited by available RAM

**TC5: No Hardware Security Module (HSM) Support**
- Keys generated and processed in software only
- No integration with TPM or secure enclaves
- Keys present in process memory during operations

**Design Constraints**

**DC1: Command-Line Interface Only**
- No graphical user interface in current version
- Limits accessibility for non-technical users
- Text-based feedback only

**DC2: Local Operation Only**
- No network transfer capabilities
- No client-server architecture
- Users must manually move encrypted files if needed

**DC3: Metadata Storage Requirement**
- Decryption requires metadata file
- Loss of metadata prevents decryption even with encrypted files
- No key recovery mechanism if metadata lost

**DC4: Single-User Focus**
- No multi-user access control
- No shared key management
- Each encryption operation generates unique keys

**Security Constraints**

**SC1: Key Storage in Metadata**
- XChaCha20 master key stored in metadata file
- Metadata must be protected (file permissions, secure storage)
- Compromise of metadata exposes ability to decrypt keys

**SC2: No Forward Secrecy**
- All information needed for decryption present in metadata
- Past encryptions vulnerable if metadata compromised
- No protocol for key erasure after secure distribution

**SC3: Trust in Libraries**
- Security depends on PyCryptodome and PyNaCl correctness
- Must trust library maintainers and audit processes
- Vulnerabilities in libraries affect this system

**SC4: No Post-Quantum Resistance**
- AES-256 and XChaCha20 vulnerable to quantum attacks (Grover's algorithm reduces effective security to 128 bits)
- No lattice-based or other post-quantum algorithms included
- Future quantum computers threaten long-term confidentiality

**Operational Constraints**

**OC1: Installation Requirements**
- Users must install Python and dependencies
- Requires internet connection for initial pip install
- Some users may face corporate/institutional restrictions on software installation

**OC2: Documentation Language**
- Documentation in English only
- May limit accessibility for non-English speakers

**OC3: No Customer Support**
- Academic project without ongoing support infrastructure
- Users must rely on documentation and open-source community

**OC4: Performance Limitations**
- Python implementation slower than compiled alternatives
- Large file operations may require patience on slow hardware
- No GPU acceleration support

**Regulatory Constraints**

**RC1: Export Control Considerations**
- Cryptographic software subject to various national export controls
- While generally exempt for publicly available software, complexity varies by jurisdiction

**RC2: No Compliance Certification**
- System not FIPS 140-2 validated (libraries may be, but this specific implementation is not)
- Cannot be used in contexts requiring certified cryptographic modules

**Time and Resource Constraints**

**TRC1: Development Timeline**
- Academic semester limits development time
- Features must fit within available timeline
- Some advanced capabilities deferred to future work

**TRC2: Team Size**
- Two-person team limits parallelization
- Testing coverage constrained by available person-hours
- Documentation burden shared between two members

**TRC3: Testing Resources**
- Limited to team members' hardware for testing
- Cannot test across all possible platforms and configurations
- No formal security audit or penetration testing budget

## 3.5 Use Case Model / Flow Charts / DFDs

This section provides visual representations of system functionality and data flow.

### Use Case Diagram

```
                  ┌──────────────────────┐
                  │                      │
                  │    File Encryption   │
                  │       System         │
                  │                      │
                  └──────────────────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
    ┌─────────┐      ┌─────────┐     ┌──────────┐
    │ Encrypt │      │ Decrypt │     │   Info   │
    │  File   │      │  File   │     │  Display │
    └─────────┘      └─────────┘     └──────────┘
          │                │
          │                │
          ▼                ▼
    ┌──────────┐     ┌──────────┐
    │ Generate │     │  Verify  │
    │   Keys   │     │ Integrity│
    └──────────┘     └──────────┘
          │
          ▼
    ┌──────────┐
    │  Encrypt │
    │   Keys   │
    └──────────┘
```

**Actor:** User (person executing CLI commands)

**Use Cases:**

**UC1: Encrypt File**
- **Primary Actor:** User
- **Preconditions:** User has file to encrypt, system installed
- **Main Flow:**
  1. User executes: `python cli.py encrypt -f filename`
  2. System validates file exists
  3. System generates AES key
  4. System encrypts file with AES-256-GCM
  5. System generates XChaCha20 master key
  6. System encrypts AES key with XChaCha20
  7. System saves encrypted file, encrypted key, metadata
  8. System displays success message
- **Postconditions:** Three files created (.enc, .key, .meta)
- **Alternative Flows:**
  - 2a. File not found → display error, exit
  - 4a. Encryption fails → display error, exit
  - 7a. Cannot write files → display error, exit

**UC2: Decrypt File**
- **Primary Actor:** User
- **Preconditions:** User has metadata file from previous encryption
- **Main Flow:**
  1. User executes: `python cli.py decrypt -m metadata_file`
  2. System loads metadata
  3. System loads encrypted key
  4. System decrypts AES key with XChaCha20 master key from metadata
  5. System loads encrypted file
  6. System decrypts file with recovered AES key
  7. System verifies integrity (authentication tags)
  8. System saves decrypted file
  9. System displays success message
- **Postconditions:** Decrypted file created, matches original
- **Alternative Flows:**
  - 2a. Metadata not found/invalid → display error, exit
  - 4a. Key decryption fails (authentication) → display error, exit
  - 6a. File decryption fails (authentication) → display error, NO plaintext output

**UC3: Display System Information**
- **Primary Actor:** User
- **Preconditions:** System installed
- **Main Flow:**
  1. User executes: `python cli.py info`
  2. System displays algorithm information
  3. System displays key sizes and security features
  4. System displays usage examples
- **Postconditions:** User informed about system capabilities

### Encryption Process Flowchart

```
START
  │
  ▼
[User provides filename]
  │
  ▼
<File exists?> ──NO──> [Error: File not found] ──> END
  │ YES
  ▼
[Generate random 256-bit AES key]
  │
  ▼
[Generate random 128-bit nonce]
  │
  ▼
[Encrypt file with AES-256-GCM]
  │
  ▼
[Generate authentication tag]
  │
  ▼
[Save encrypted file (.enc)]
  │
  ▼
[Generate random 256-bit XChaCha20 master key]
  │
  ▼
[Generate random 192-bit nonce]
  │
  ▼
[Encrypt AES key with XChaCha20-Poly1305]
  │
  ▼
[Save encrypted key (.key)]
  │
  ▼
[Create metadata JSON with:]
│ - Original filename
│ - Encrypted file path
│ - Encrypted key path
│ - XChaCha20 master key
  │
  ▼
[Save metadata (.meta)]
  │
  ▼
[Display success message]
  │
  ▼
END
```

### Decryption Process Flowchart

```
START
  │
  ▼
[User provides metadata file]
  │
  ▼
<Metadata exists?> ──NO──> [Error: Metadata not found] ──> END
  │ YES
  ▼
[Parse metadata JSON]
  │
  ▼
<Valid format?> ──NO──> [Error: Invalid metadata] ──> END
  │ YES
  ▼
[Extract XChaCha20 master key]
  │
  ▼
[Load encrypted AES key from .key file]
  │
  ▼
[Decrypt AES key with XChaCha20]
  │
  ▼
<Auth tag valid?> ──NO──> [Error: Key tampered] ──> END
  │ YES
  ▼
[Load encrypted file from .enc file]
  │
  ▼
[Decrypt file with AES-256-GCM]
  │
  ▼
<Auth tag valid?> ──NO──> [Error: File tampered] ──> END
  │ YES
  ▼
[Save decrypted file with original name]
  │
  ▼
[Display success message]
  │
  ▼
END
```

### Data Flow Diagram (Level 0 - Context Diagram)

```
┌──────────────┐
│              │
│     USER     │
│              │
└───────┬──────┘
        │
        │ filename
        ▼
┌────────────────────────────┐
│                            │
│   Hybrid Encryption        │
│   System                   │
│                            │
└───────┬────────────────────┘
        │
        │ encrypted files + metadata
        ▼
┌──────────────┐
│              │
│  File System │
│              │
└──────────────┘
```

### Data Flow Diagram (Level 1 - Detailed)

```
                ┌──────────┐
                │   USER   │
                └─────┬────┘
                      │
                      │ filename + command
                      ▼
             ┌──────────────────┐
             │  CLI Interface   │
             │    (cli.py)      │
             └─────┬──────┬─────┘
                   │      │
    ┌──────────────┘      └──────────────┐
    │                                    │
    │ encrypt command                    │ decrypt command
    ▼                                    ▼
┌──────────────────┐              ┌──────────────────┐
│  Hybrid          │              │  Hybrid          │
│  Encryption      │              │  Decryption      │
│  Controller      │              │  Controller      │
└─────┬──────┬─────┘              └─────┬──────┬─────┘
      │      │                          │      │
      │      └───────────┐              │      └───────────┐
      ▼                  ▼              ▼                  ▼
┌───────────┐      ┌───────────┐ ┌───────────┐      ┌───────────┐
│   AES     │      │ XChaCha20 │ │ XChaCha20 │      │   AES     │
│  Encrypt  │      │  Key      │ │  Key      │      │  Decrypt  │
│  Module   │      │  Encrypt  │ │  Decrypt  │      │  Module   │
└─────┬─────┘      └─────┬─────┘ └─────┬─────┘      └─────┬─────┘
      │                  │              │                  │
      │                  │              │                  │
      └──────────┬───────┘              └──────────┬───────┘
                 │                                 │
                 ▼                                 ▼
           ┌─────────────┐                  ┌─────────────┐
           │ File System │                  │ File System │
           │  (Write)    │                  │   (Read)    │
           └─────────────┘                  └─────────────┘
```

**Data Stores:**
- **Encrypted Files (.enc):** Stores AES-encrypted file content
- **Encrypted Keys (.key):** Stores XChaCha20-encrypted AES keys
- **Metadata (.meta):** Stores JSON with decryption information
- **Original Files:** Input to encryption, output from decryption

**Data Flows:**
1. User → CLI: Command + filename
2. CLI → Hybrid Controller: Validated input
3. Hybrid → AES Module: File content
4. AES Module → File System: Encrypted content + tag
5. Hybrid → XChaCha20 Module: AES key
6. XChaCha20 Module → File System: Encrypted key
7. Hybrid → File System: Metadata JSON

(Decryption flows reverse this process)

## 3.6 Database Design

**Note:** This system does not employ a traditional database (SQL or NoSQL). All data persists as files in the file system. This section documents the file-based storage approach.

**Rationale for File-Based Storage:**
- Simplicity: No database server setup required
- Portability: Encrypted files easily transferred between systems
- Self-contained: Each encryption operation produces standalone artifacts
- User control: Users manage files directly without database abstraction
- No query requirements: System doesn't need complex data retrieval

**File Storage Structure:**

```
project_root/
├── encrypted/          # Default output directory for encrypted files
│   ├── document.pdf.enc
│   ├── document.pdf.key
│   └── document.pdf.meta
├── decrypted/          # Default output directory for decrypted files
│   └── document.pdf
└── results/            # Performance test results
    ├── performance_results_TIMESTAMP.json
    └── graphs/
        ├── encryption_time.png
        └── throughput.png
```

**File Naming Conventions:**
- Encrypted file: `{original_filename}.enc`
- Encrypted key: `{original_filename}.key`
- Metadata: `{original_filename}.meta`
- Decrypted file: `{original_filename}` (restored)

## 3.7 Table Structure

**Metadata File Structure (JSON Format)**

The metadata file serves as the "database record" containing all information needed for decryption.

```json
{
  "original_filename": "document.pdf",
  "encrypted_file": "encrypted/document.pdf.enc",
  "key_file": "encrypted/document.pdf.key",
  "master_key": "a1b2c3d4...",  // hex-encoded 256-bit key
  "file_size": 1048576,          // original file size in bytes
  "timestamp": "2025-11-01T14:30:00Z",
  "version": "1.0"
}
```

**Field Descriptions:**

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| original_filename | string | Original file name before encryption | Non-empty, valid filename |
| encrypted_file | string | Path to .enc file | Valid path, file must exist |
| key_file | string | Path to .key file | Valid path, file must exist |
| master_key | string | Hex-encoded XChaCha20 master key | 64 hex characters (256 bits) |
| file_size | integer | Original file size in bytes | Positive integer |
| timestamp | string | ISO 8601 timestamp of encryption | Valid ISO format (optional) |
| version | string | Metadata format version | Semantic version (optional) |

**Encrypted File Format (.enc)**

Binary format:
```
[16 bytes: AES-GCM nonce]
[16 bytes: AES-GCM authentication tag]
[N bytes: Encrypted file content]
```

**Encrypted Key File Format (.key)**

Binary format produced by PyNaCl SecretBox (XChaCha20-Poly1305):
```
[24 bytes: XChaCha20 nonce]
[32 bytes: Encrypted AES key]
[16 bytes: Poly1305 authentication tag]
Total: 72 bytes fixed size
```

**Performance Results Format (JSON)**

```json
{
  "test_date": "2025-11-01 14:30:00",
  "results": [
    {
      "file_size_mb": 10,
      "encryption_time": 0.123,
      "encryption_throughput": 81.3,
      "decryption_time": 0.118,
      "decryption_throughput": 84.7,
      "total_time": 0.241,
      "integrity_verified": true
    },
    // ... more test results
  ]
}
```

## 3.8 ER Diagrams

**Note:** Traditional Entity-Relationship diagrams apply to relational databases. Since this system uses file-based storage, we present a "File Relationship Diagram" showing how files relate to each other.

```
┌────────────────────┐
│  ORIGINAL FILE     │
│                    │
│ - filename         │
│ - content (bytes)  │
│ - size             │
└──────────┬─────────┘
           │
           │ encrypts to
           │
           ▼
┌────────────────────┐
│  ENCRYPTED FILE    │
│      (.enc)        │
│                    │
│ - nonce (16 bytes) │
│ - tag (16 bytes)   │
│ - ciphertext       │
└────────────────────┘
           │
           │ protected by
           │
           ▼
┌────────────────────┐
│   AES KEY          │
│  (ephemeral)       │
│                    │
│ - 256-bit key      │
└──────────┬─────────┘
           │
           │ encrypted to
           │
           ▼
┌────────────────────┐
│  ENCRYPTED KEY     │
│      (.key)        │
│                    │
│ - nonce (24 bytes) │
│ - encrypted key    │
│ - tag (16 bytes)   │
└────────────────────┘
           │
           │ protected by
           │
           ▼
┌────────────────────┐
│  MASTER KEY        │
│  (in metadata)     │
│                    │
│ - 256-bit key      │
└────────────────────┘
           │
           │ stored in
           │
           ▼
┌────────────────────┐
│   METADATA         │
│    (.meta)         │
│                    │
│ - original_filename│
│ - encrypted_file   │
│ - key_file         │
│ - master_key       │
│ - file_size        │
└────────────────────┘
```

**Relationships:**

1. **ORIGINAL_FILE → ENCRYPTED_FILE** (1:1)
   - One original file produces one encrypted file
   - Encrypted file references original via metadata

2. **ENCRYPTED_FILE → AES_KEY** (1:1)
   - Each encrypted file has unique AES key
   - Key never reused across encryptions

3. **AES_KEY → ENCRYPTED_KEY** (1:1)
   - AES key encrypted before storage
   - Produces fixed-size encrypted key file

4. **ENCRYPTED_KEY → MASTER_KEY** (1:1)
   - Each encrypted key protected by unique master key
   - Master key specific to this encryption operation

5. **MASTER_KEY → METADATA** (1:1)
   - Master key stored in metadata
   - Metadata ties all components together

6. **METADATA → ENCRYPTED_FILE, ENCRYPTED_KEY** (1:many)
   - Metadata references both encrypted file and key
   - Central index for decryption

**File Dependencies:**

```
To Decrypt, Need:
1. METADATA (.meta) ─── contains ───> MASTER_KEY
                    └── points to ──> ENCRYPTED_KEY (.key)
                    └── points to ──> ENCRYPTED_FILE (.enc)

2. ENCRYPTED_KEY + MASTER_KEY ──decrypt──> AES_KEY

3. ENCRYPTED_FILE + AES_KEY ──decrypt──> ORIGINAL_FILE
```

## 3.9 Assumptions and Dependencies

**Assumptions**

**A1: Operating System Provides Secure Randomness**
- Assumption: `os.urandom()` (or equivalent) provides cryptographically secure random bytes
- Justification: Modern operating systems maintain entropy pools; /dev/urandom on Linux, CryptGenRandom on Windows provide adequate randomness
- Risk if violated: Weak keys, predictable nonces, security compromise

**A2: System Clock Reasonably Accurate**
- Assumption: System time approximately correct (for timestamps, not security)
- Justification: Timestamps used for metadata only, not security-critical
- Risk if violated: Misleading timestamps, no security impact

**A3: File System Integrity**
- Assumption: File system correctly stores and retrieves data
- Justification: Modern file systems designed for data integrity
- Risk if violated: Corruption could cause decryption failures, but authentication tags detect tampering

**A4: User Has Appropriate Permissions**
- Assumption: User can read source files, write output files
- Justification: System checks and reports permission errors
- Risk if violated: Operation fails with error message, no security impact

**A5: Python Interpreter Uncompromised**
- Assumption: Python runtime is trustworthy
- Justification: Users install Python from official sources
- Risk if violated: Compromised runtime could leak keys; applies to all Python software

**A6: Cryptographic Libraries Correctly Implemented**
- Assumption: PyCryptodome and PyNaCl provide secure, correct implementations
- Justification: Libraries widely used, regularly audited, maintained by experts
- Risk if violated: Algorithmic vulnerabilities; monitoring library security advisories essential

**A7: Adequate Disk Space Available**
- Assumption: Sufficient disk space for encrypted files (approximately same size as originals)
- Justification: System checks available space before writing
- Risk if violated: Partial writes, operation failure; handled with error messages

**A8: Network Isolation for Security**
- Assumption: For highest security, system operates on network-isolated machines
- Justification: No network code means no network-based attacks (in current version)
- Risk if violated: General malware risks if connected to untrusted networks

**Dependencies**

**External Software Dependencies:**

**D1: Python Runtime (version 3.8+)**
- Dependency Type: Critical
- Purpose: Execute