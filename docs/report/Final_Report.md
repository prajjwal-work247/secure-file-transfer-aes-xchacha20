# PROJECT REPORT

## SECURE FILE ENCRYPTION SYSTEM USING AES-256 AND XCHACHA20

---

**SUBMITTED IN PARTIAL FULFILMENT OF THE REQUIREMENTS FOR THE AWARD OF DEGREE OF**

**BACHELOR OF TECHNOLOGY**

**IN**

**COMPUTER SCIENCE & ENGINEERING**

---

**Submitted By:**

**Pragati Raj - Roll No. 22BECCS28**  
**Prajjwal Gupta - Roll No. 22BECCS29**

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

In the contemporary digital landscape, secure file encryption has become essential for protecting sensitive data from unauthorized access and cyber threats. Traditional encryption systems, particularly those relying solely on AES-GCM (Advanced Encryption Standard in Galois/Counter Mode), face operational challenges including strict nonce management requirements and performance limitations in environments lacking hardware acceleration. Nonce reuse in AES-GCM represents a critical vulnerability that can compromise both data confidentiality and integrity.

This project presents a hybrid encryption framework that combines AES-256-GCM for file content encryption with XChaCha20-Poly1305 for encryption key protection. By leveraging XChaCha20's extended 192-bit nonce space—2^96 times larger than standard AES-GCM's 96-bit nonce—the system significantly reduces the probability of nonce collision, thereby mitigating a major operational security risk. The dual-layer architecture provides algorithmic diversity, ensuring that compromise of one encryption layer does not result in total system failure.

The implementation utilizes well-established cryptographic libraries: PyCryptodome (version 3.19.0) for AES operations and PyNaCl (version 1.5.0) for XChaCha20 functionality. Both libraries provide audited, industry-standard implementations, eliminating the risks associated with custom cryptographic code. A command-line interface facilitates user interaction with three primary commands: encrypt, decrypt, and info, providing intuitive access to encryption capabilities without requiring users to manage cryptographic keys manually.

Performance benchmarking conducted on files ranging from 1MB to 100MB demonstrates consistent encryption throughput averaging 87 MB/s and decryption throughput averaging 92 MB/s on standard hardware (AMD Ryzen 5 processor). The system maintains integrity verification through authenticated encryption at both layers, with comprehensive testing confirming 100% accuracy in recovering original files after encryption-decryption cycles.

The project follows an iterative development methodology with modular architecture enabling independent component testing. Version control through Git ensures traceable development history, while comprehensive documentation facilitates future maintenance and enhancement. All test cases passed successfully, validating system correctness, security properties, and performance characteristics.

This work contributes a practical, well-documented implementation addressing real-world challenges in file encryption systems. While not claiming theoretical cryptographic innovation, the project demonstrates effective application of established algorithms in a hybrid architecture that balances compliance requirements (AES for regulatory standards), operational resilience (XChaCha20 for nonce management), and practical performance.

**Keywords:** Hybrid Encryption, AES-256-GCM, XChaCha20-Poly1305, File Security, Nonce Management, Authenticated Encryption, Cryptographic Implementation, Python

---

# ACKNOWLEDGEMENT

We express our sincere gratitude to our project guide, **Mr. Gaurav Thakur**, Assistant Professor, Department of Computer Science & Engineering, Central University of Jammu, for his invaluable guidance, constant encouragement, and unwavering support throughout this project. His insights into cryptographic systems and security engineering significantly enhanced our understanding of applied cryptography and secure software development practices.

We are deeply thankful to **Dr. [HOD Name]**, Head of Department, Computer Science & Engineering, Central University of Jammu, for providing the necessary facilities, infrastructure, and academic environment that enabled successful project completion. His vision for integrating practical skills with theoretical knowledge has been instrumental in our learning journey.

We acknowledge the faculty members of the Department of Computer Science & Engineering for their academic guidance, constructive feedback during project presentations, and continued support throughout our undergraduate program. Their dedication to quality education has shaped our technical competencies and professional outlook.

We appreciate the open-source community, particularly the maintainers and contributors of PyCryptodome and PyNaCl (libsodium) libraries. Their commitment to providing secure, well-documented, and freely available cryptographic implementations formed the foundation upon which this project was built. The cryptographic community's emphasis on transparency and peer review exemplifies the highest standards of security engineering.

We extend our gratitude to our fellow students and peers who provided valuable suggestions, participated in testing, and offered encouragement during challenging phases of development. Collaborative learning and peer interaction enriched our understanding of complex concepts and problem-solving approaches.

Finally, we express heartfelt appreciation to our families for their unconditional support, patience, and motivation throughout this endeavor. Their encouragement enabled us to dedicate time and effort to this project while maintaining balance in our academic pursuits.

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
| **CHAPTER 1: INTRODUCTION** | **1** |
| 1.1 Project Overview | 2 |
| 1.2 Objectives of Project | 4 |
| 1.3 Problem Formulation | 5 |
| 1.4 Existing System | 7 |
| 1.5 Proposed System | 10 |
| 1.6 Features of the Project | 13 |
| **CHAPTER 2: REQUIREMENT ANALYSIS** | **16** |
| 2.1 Feasibility Study | 17 |
| 2.2 Software Requirement Specification Document | 20 |
| 2.3 SDLC Model Used | 25 |

---

# LIST OF FIGURES

| Fig. No. | Figure Title | Page No. |
|----------|--------------|----------|
| 1.1 | Hybrid Encryption System Architecture | 11 |
| 1.2 | Encryption Process Overview | 12 |
| 2.1 | Iterative Development Model Phases | 27 |

---

# LIST OF TABLES

| Table No. | Table Caption | Page No. |
|-----------|---------------|----------|
| 1.1 | Comparison of Encryption Algorithms | 8 |
| 2.1 | Hardware Requirements | 21 |
| 2.2 | Software Requirements | 22 |
| 2.3 | Functional Requirements | 23 |
| 2.4 | Non-Functional Requirements | 24 |

---

# CHAPTER 1: INTRODUCTION

## 1.1 Project Overview

**Project Category:** Application Development / System Development

The exponential growth of digital data in contemporary society has fundamentally transformed information storage, processing, and transmission paradigms. With the global datasphere projected to exceed 175 zettabytes, ensuring data confidentiality and integrity has become paramount across all sectors—government, healthcare, finance, education, and personal computing. Cloud computing, while offering unprecedented convenience and scalability, introduces significant security challenges as sensitive data traverses networks and resides on third-party infrastructure. Encryption serves as the foundational defense mechanism, providing mathematical guarantees for protecting information from unauthorized access and tampering.

This project develops a secure file encryption system implementing a hybrid cryptographic approach that combines AES-256-GCM (Advanced Encryption Standard in Galois/Counter Mode) for file content encryption with XChaCha20-Poly1305 for encryption key protection. Unlike traditional single-algorithm systems or conventional hybrid schemes employing asymmetric cryptography (RSA/ECC) for key exchange, this system utilizes two complementary symmetric algorithms operating in distinct roles to address specific operational challenges while maintaining cryptographic strength.

The Advanced Encryption Standard, established by NIST (National Institute of Standards and Technology) in 2001, represents the gold standard for symmetric encryption across government, military, and commercial applications globally. AES operates as a block cipher using substitution-permutation networks, providing proven security after decades of cryptanalytic scrutiny. When combined with Galois/Counter Mode, AES delivers both confidentiality (encryption) and integrity (authentication) in a single operation, making it ideal for protecting file content. Hardware acceleration features (AES-NI instructions) present in modern Intel and AMD processors enable multi-gigabyte-per-second throughput, making AES-256-GCM highly efficient for bulk data encryption.

However, AES-GCM implementations face critical operational challenges. The algorithm requires strict adherence to nonce (number used once) uniqueness—each encryption operation using the same key must employ a unique nonce value. Nonce reuse with the same key represents a catastrophic failure mode: attackers can recover authentication keys and potentially decrypt ciphertexts. This vulnerability is not merely theoretical; documented incidents in production TLS implementations and other systems demonstrate real-world risks. Managing nonce uniqueness becomes operationally burdensome, requiring either stateful counters (challenging in distributed systems) or secure random generation with careful probability analysis.

XChaCha20, designed by Daniel J. Bernstein as an extension of the ChaCha20 stream cipher, addresses these operational challenges through an extended nonce space. While standard ChaCha20 uses 96-bit nonces (same as AES-GCM), XChaCha20 extends this to 192 bits—providing 2^96 times more possible nonce values. This extended space dramatically reduces collision probability even under imperfect randomness, enabling safer random nonce generation without state coordination. Combined with the Poly1305 message authentication code, XChaCha20-Poly1305 provides authenticated encryption comparable to AES-GCM while offering superior software performance on platforms lacking hardware acceleration and enhanced operational resilience through larger nonce space.

The hybrid architecture implemented in this project leverages the strengths of both algorithms: AES-256-GCM encrypts file content (benefiting from hardware acceleration where available, maintaining regulatory compliance with FIPS-approved algorithms), while XChaCha20-Poly1305 encrypts the AES encryption key (providing robust key protection with extended nonce space, efficient software performance). This separation of concerns addresses the nonce management challenge—while file content encryption still requires unique nonces, the encryption key encryption operates independently with XChaCha20's larger nonce space providing additional safety margin.

The system is implemented in Python 3.10+, utilizing well-maintained cryptographic libraries: PyCryptodome (version 3.19.0) for AES operations and PyNaCl (version 1.5.0) wrapping libsodium for XChaCha20 functionality. Reliance on established, audited libraries rather than custom cryptographic code represents security best practice, as cryptographic implementation errors frequently introduce vulnerabilities even when underlying algorithms remain secure. The implementation emphasizes correctness, security properties, and usability through comprehensive testing and clear documentation.

A command-line interface provides user access to encryption and decryption capabilities with three primary commands: encrypt (for file encryption), decrypt (for file decryption), and info (for system information display). Automated key generation and management eliminate common user errors, while metadata files simplify decryption by packaging all necessary information (encrypted key, file paths, master key) in a single, human-readable JSON format. The interface follows Unix command-line conventions, making it accessible to technical users while remaining suitable for integration into scripts and automated workflows.

**Target Users and Applications:**

The system serves multiple user categories:

1. **Security-conscious professionals** requiring local file encryption without reliance on third-party services
2. **System administrators** needing scriptable encryption for backup and archival workflows
3. **Software developers** seeking reference implementations of hybrid encryption systems
4. **Educational institutions** demonstrating applied cryptography concepts
5. **Researchers** handling sensitive data requiring strong confidentiality protections

**Key Innovation and Contribution:**

While the individual cryptographic algorithms (AES and XChaCha20) are well-established standards, this project's contribution lies in their thoughtful integration to address practical operational challenges. The hybrid approach is not novel in principle (hybrid encryption is common), but the specific combination of two symmetric algorithms in complementary roles—rather than the traditional asymmetric-symmetric pairing—represents a pragmatic engineering solution to documented vulnerabilities in single-algorithm systems. The system prioritizes:

- **Operational resilience** through extended nonce space
- **Performance** through hardware acceleration where available
- **Compliance** through use of NIST-approved algorithms
- **Security** through algorithmic diversity (defense in depth)
- **Usability** through automation and clear interfaces

The project demonstrates that effective security engineering requires balancing theoretical cryptographic strength with operational reality, acknowledging that most security failures result from implementation errors, configuration mistakes, or operational lapses rather than algorithmic weaknesses.

## 1.2 Objectives of Project

This project defines four primary objectives, all of which have been fully implemented and validated through comprehensive testing:

**Objective 1: Design and Implement a Hybrid Encryption Framework Combining AES-256 and XChaCha20**

**Description:** Develop a functional file encryption system that integrates AES-256-GCM for file content encryption with XChaCha20-Poly1305 for encryption key protection, implementing both algorithms correctly according to their specifications and composing them into a cohesive hybrid architecture.

**Specific Goals:**
- Implement AES-256 encryption module using PyCryptodome library with proper nonce generation, authentication tag handling, and error management
- Implement XChaCha20-Poly1305 key encryption module using PyNaCl library with correct master key generation and secure key wrapping
- Integrate both modules into a unified hybrid controller that orchestrates the complete encryption and decryption workflow
- Validate correct operation through unit tests for individual modules and integration tests for the complete system

**Implementation Status:** ✅ **Fully Achieved**

The system successfully implements separate, modular components (`aes_encryption.py`, `xchacha20_encryption.py`) with clear interfaces, integrated through `hybrid_encryption.py`. All modules passed independent testing, and the integrated system correctly encrypts and decrypts files of various sizes with 100% integrity preservation (original and decrypted files match exactly in all test cases).

**Objective 2: Address Nonce Management Vulnerabilities in AES-GCM Through Extended Nonce Space**

**Description:** Mitigate the operational risk of nonce reuse in AES-GCM implementations by employing XChaCha20's extended 192-bit nonce space for the critical key encryption operation, thereby reducing collision probability and enhancing system resilience against nonce management failures.

**Specific Goals:**
- Analyze and document nonce reuse vulnerabilities in traditional AES-GCM deployments
- Implement XChaCha20-Poly1305 with proper utilization of the 192-bit nonce (24 bytes)
- Demonstrate collision probability reduction: XChaCha20's 2^192 nonce space versus AES-GCM's 2^96 space
- Validate nonce uniqueness across multiple encryption operations through statistical testing

**Implementation Status:** ✅ **Fully Achieved**

The system generates cryptographically secure random nonces for both AES (128-bit) and XChaCha20 (192-bit) operations using OS-provided entropy sources. Testing confirms nonce uniqueness across 1000+ encryption operations with no collisions observed. The XChaCha20 implementation correctly utilizes PyNaCl's SecretBox, which automatically generates 192-bit nonces, providing the 2^96 collision probability reduction as designed.

**Objective 3: Develop User-Friendly Command-Line Interface with Automated Key Management**

**Description:** Provide accessible encryption capabilities to users through an intuitive command-line interface that automates cryptographic operations, eliminating the need for manual key generation, storage, and retrieval while maintaining security properties.

**Specific Goals:**
- Implement CLI with three primary commands: encrypt, decrypt, info
- Automate all cryptographic key generation using secure random number generators
- Implement metadata-based decryption that eliminates manual key handling by users
- Provide clear, actionable error messages for common failure scenarios
- Include comprehensive help documentation and usage examples

**Implementation Status:** ✅ **Fully Achieved**

The `cli.py` module implements a complete command-line interface using Python's argparse library. Users can encrypt files with a single command without manually generating keys, decrypt files by referencing metadata files (no manual key input required), and access system information through the info command. Error handling provides meaningful messages for file-not-found, permission-denied, and authentication-failure scenarios.

**Objective 4: Evaluate System Performance and Validate Security Properties Through Comprehensive Testing**

**Description:** Conduct rigorous performance benchmarking across various file sizes and validate security properties including encryption correctness, integrity verification, nonce uniqueness, and key independence through systematic testing.

**Specific Goals:**
- Measure encryption and decryption times for files ranging from 1MB to 100MB
- Calculate throughput (MB/s) and analyze performance characteristics
- Verify data integrity: confirm decrypted files match originals exactly (SHA-256 hash comparison)
- Validate authentication: confirm tampered ciphertext is detected and rejected
- Generate performance visualization graphs for report inclusion
- Document all test cases and results

**Implementation Status:** ✅ **Fully Achieved**

Performance testing suite (`performance_test.py`) benchmarks the system across six file sizes (1, 5, 10, 25, 50, 100 MB), measuring encryption/decryption times and calculating throughput. Results demonstrate consistent performance (encryption: ~87 MB/s, decryption: ~92 MB/s average). Visualization script (`visualize_results.py`) generates six performance graphs using matplotlib. All integrity tests confirm 100% match between original and decrypted files. Authentication tests confirm tampered ciphertext is correctly rejected without outputting plaintext.

**Summary of Objectives Achievement:**

All four objectives have been fully implemented, tested, and validated. The project successfully demonstrates a working hybrid encryption system that addresses identified vulnerabilities in traditional approaches while maintaining practical usability and performance. Documentation, code comments, and comprehensive testing provide evidence of objective completion suitable for academic evaluation and future reference.

## 1.3 Problem Formulation

Secure file encryption systems face a convergence of security, performance, and operational challenges that motivate the hybrid approach implemented in this project. This section formalizes the problem space, identifies specific deficiencies in existing systems, and establishes the rationale for the proposed solution.

**Problem Statement 1: Nonce Reuse Vulnerability in AES-GCM Implementations**

AES in Galois/Counter Mode (AES-GCM) provides authenticated encryption, combining confidentiality and integrity protection in a single operation. However, the algorithm's security critically depends on nonce uniqueness: each encryption operation using the same key must employ a unique nonce value. The requirement is absolute—nonce reuse with the same key enables catastrophic attacks.

**Technical Details of the Vulnerability:**

When AES-GCM reuses a nonce with the same key, the following attack vectors emerge:
1. **Authentication Key Recovery:** Attackers can recover the authentication key (hash subkey H) by analyzing two ciphertexts encrypted with the same key-nonce pair
2. **Plaintext Recovery:** With the authentication key compromised, attackers can recover XOR combinations of plaintexts, and in some cases, complete plaintexts
3. **Forgery:** Attackers can construct valid ciphertexts for arbitrary plaintexts, completely breaking authentication

The Internet Engineering Task Force (IETF) explicitly warns in RFC 5288: "Implementations must ensure that [nonce] values are not repeated for a given key... The security consequences of nonce reuse are severe." Despite this clear guidance, nonce reuse vulnerabilities have appeared in production systems, including widely-deployed TLS implementations, demonstrating the operational difficulty of ensuring nonce uniqueness in real-world deployments.

**Operational Challenges:**

Maintaining nonce uniqueness requires one of three approaches:
1. **Stateful Counters:** Maintain persistent state across all encryption operations, incrementing a counter for each operation. This approach is challenging in distributed systems where multiple nodes may encrypt data, requiring coordination mechanisms that introduce complexity and potential failure modes.
2. **Random Nonces:** Generate random nonces using cryptographically secure random number generators. With AES-GCM's 96-bit nonce space, birthday paradox considerations limit the number of operations before collision probability becomes non-negligible (approximately 2^48 operations for 2^-32 collision probability).
3. **Deterministic Construction:** Construct nonces from message content or associated data. This approach requires careful design to ensure uniqueness and may leak information about plaintext structure.

Each approach introduces operational burden, potential for implementation errors, or security trade-offs. Human error, software bugs, virtual machine cloning, or system failures can result in nonce reuse despite best efforts.

**Problem Statement 2: Performance Heterogeneity Across Computing Platforms**

AES performance varies dramatically between hardware-accelerated and software-only implementations, creating challenges for systems deployed across heterogeneous infrastructure.

**Performance Characteristics:**

Modern Intel and AMD processors include AES-NI (AES New Instructions), dedicated hardware instructions for AES operations that provide:
- **Hardware-accelerated:** 5-10 GB/s throughput (multi-core systems)
- **Software-only:** 50-500 MB/s throughput (depending on implementation quality)

This 10x to 100x performance disparity creates operational challenges:
- Organizations with diverse infrastructure (servers, workstations, mobile devices, IoT sensors) cannot rely on consistent AES performance
- Systems designed for hardware acceleration perform poorly on devices lacking such features
- Mobile devices and embedded systems may lack AES-NI equivalents, experiencing degraded performance

**Problem Statement 3: Single Point of Cryptanalytic Failure**

Exclusive reliance on a single cryptographic algorithm creates systemic risk. While AES has withstood decades of cryptanalytic scrutiny and remains secure against known attacks, prudent security engineering acknowledges uncertainty:

**Risk Factors:**
1. **Cryptanalytic Advances:** Future mathematical breakthroughs could weaken or break AES
2. **Quantum Computing:** Grover's algorithm reduces AES-256 effective security to 128 bits (still considered adequate, but reduced safety margin)
3. **Implementation Vulnerabilities:** Even with algorithmically sound encryption, implementation errors in specific libraries or hardware can introduce vulnerabilities
4. **Side-Channel Attacks:** Timing attacks, power analysis, and electromagnetic emanation analysis can leak information even when algorithms remain secure

The principle of defense in depth suggests employing multiple independent security layers such that compromise of one layer does not result in total system failure. Algorithmic diversity provides insurance against algorithm-specific failures.

**Problem Statement 4: Compliance Requirements Versus Operational Best Practices**

Regulatory frameworks often mandate specific cryptographic standards, creating tension between compliance and operational optimality.

**Specific Constraints:**
- **FIPS 140-2:** U.S. federal agencies must use NIST-approved algorithms; AES is approved, ChaCha20 is not
- **Industry Standards:** Many industries (healthcare, finance) require FIPS-validated cryptographic modules
- **International Regulations:** Different jurisdictions may have varying cryptographic requirements

Organizations cannot simply abandon AES for operationally superior alternatives without violating compliance mandates, even when alternative algorithms offer advantages (better software performance, larger nonce spaces, resistance to certain attack classes).

**Formalized Problem Definition:**

Given the identified challenges, the problem can be formalized as:

**Design and implement a file encryption system that:**
1. Provides confidentiality and integrity protection for files of arbitrary size
2. Mitigates nonce reuse risks through architectural design rather than relying solely on operational discipline
3. Maintains acceptable performance across diverse computing platforms (hardware-accelerated and software-only)
4. Provides algorithmic diversity for defense in depth
5. Satisfies compliance requirements through use of NIST-approved algorithms
6. Remains usable by technical users without requiring cryptographic expertise

**Proposed Solution Approach:**

This project addresses the formalized problem through a hybrid symmetric encryption architecture:

**Layer 1 - File Content Encryption (AES-256-GCM):**
- Encrypt file content with AES-256 in GCM mode
- Benefits: Hardware acceleration where available, FIPS compliance, proven security
- Generate unique random nonces for each file encryption operation

**Layer 2 - Key Protection (XChaCha20-Poly1305):**
- Encrypt AES keys using XChaCha20-Poly1305
- Benefits: Extended 192-bit nonce space (2^96 times larger than AES-GCM), excellent software performance, reduced collision probability
- Provides additional security layer protecting encryption keys

**Rationale:**

This approach acknowledges that most security failures result from operational issues (nonce reuse, key mismanagement, configuration errors) rather than algorithmic weaknesses. By using XChaCha20's extended nonce space for the critical key encryption operation, the system reduces operational risk while maintaining AES for bulk encryption (compliance, performance). The dual-layer design provides defense in depth—compromise of one algorithm does not immediately compromise the entire system.

The solution prioritizes practical security over theoretical purity, recognizing that real-world systems must balance cryptographic strength, performance requirements, regulatory compliance, and operational feasibility.

## 1.4 Existing System

Current approaches to secure file encryption encompass various strategies, each with distinct characteristics, strengths, and limitations. This section analyzes existing systems to establish context for the proposed solution.

**Category 1: Single-Algorithm Symmetric Encryption Systems**

Most existing file encryption tools employ a single symmetric algorithm, typically AES, for all encryption operations.

**Examples:**
- **VeraCrypt:** Open-source disk encryption software implementing AES, Serpent, and Twofish with options for cascading algorithms
- **BitLocker:** Microsoft Windows integrated encryption using AES-128 or AES-256 in XTS mode
- **LUKS (Linux Unified Key Setup):** Standard disk encryption for Linux systems, primarily using AES
- **7-Zip with encryption:** File compression tool offering AES-256 encryption for archives

**Characteristics:**
- Mature, extensively tested implementations with long deployment histories
- Hardware acceleration support yields excellent performance on modern processors (multi-GB/s throughput)
- Compliance with regulatory standards (FIPS 140-2 validated implementations available)
- Widespread compatibility and standardization across platforms and tools
- Well-documented security properties with decades of cryptanalytic review

**Limitations:**
- **Nonce Management Burden:** Developers must carefully implement nonce uniqueness; failures have occurred in production systems
- **Performance Degradation:** Significant performance loss on platforms lacking hardware acceleration (embedded systems, older processors, some ARM architectures)
- **Single Point of Failure:** All security depends on one algorithm; cryptanalytic breakthrough or implementation vulnerability affects entire system
- **Operational Complexity:** Proper key management, nonce handling, and mode selection require expertise

**Table 1.1: Comparison of Encryption Algorithms**

| Algorithm | Key Size | Nonce Size | Hardware Accel | Software Perf | FIPS Status |
|-----------|----------|------------|----------------|---------------|-------------|
| AES-GCM | 128-256 bits | 96 bits | Yes (AES-NI) | Moderate | Approved |
| XChaCha20 | 256 bits | 192 bits | No | Excellent | Not Approved |
| ChaCha20 | 256 bits | 96 bits | No | Excellent | Not Approved |
| Serpent | 128-256 bits | Varies | No | Poor | Not Approved |

**Category 2: ChaCha20-Based Modern Systems**

Newer systems increasingly adopt ChaCha20-Poly1305, particularly in contexts prioritizing software performance.

**Examples:**
- **WireGuard VPN:** Modern VPN protocol using ChaCha20-Poly1305 as primary cipher
- **TLS 1.3:** Mandates ChaCha20-Poly1305 support alongside AES-GCM
- **Signal Protocol:** End-to-end encrypted messaging using ChaCha20
- **OpenSSH:** Supports ChaCha20-Poly1305 for session encryption

**Characteristics:**
- Excellent software performance across diverse platforms (competitive with hardware-accelerated AES)
- Resistance to timing attacks in software implementations (constant-time operations)
- Simple, elegant design reducing implementation error probability
- Growing adoption in modern protocols (TLS 1.3, WireGuard, SSH)

**Limitations:**
- **Regulatory Compliance:** Not FIPS 140-2 approved; organizations under federal mandates cannot use exclusively
- **Limited Hardware Support:** Fewer processors include ChaCha20 acceleration compared to AES
- **Shorter Cryptanalytic History:** While considered secure, ChaCha20 has shorter public scrutiny period than AES (2008 vs 1998/2001)

**Category 3: Traditional Hybrid Encryption (Asymmetric + Symmetric)**

Standard hybrid encryption combines asymmetric algorithms for key exchange with symmetric algorithms for bulk encryption.

**Examples:**
- **GPG/PGP:** RSA or ECC for key encryption, AES/Camellia for message encryption
- **S/MIME:** Similar approach for email encryption
- **TLS/SSL:** RSA or ECDH for handshake, AES or ChaCha20 for session encryption
- **Cloud Storage Encryption:** Some services use RSA for key encapsulation, AES for data

**Characteristics:**
- Solves key distribution problem through public-key cryptography
- Enables secure communication without prior shared secrets
- Well-understood protocol designs with formal security proofs
- Widespread deployment and tool support

**Limitations:**
- **Performance Overhead:** Asymmetric operations 100-1000x slower than symmetric
- **Key Size Growth:** Equivalent security requires larger keys than symmetric (3072-bit RSA ≈ 128-bit symmetric security)
- **PKI Complexity:** Certificate authorities, key distribution, revocation introduce operational complexity
- **Quantum Vulnerability:** RSA and ECC vulnerable to Shor's algorithm; quantum computers threaten long-term security

**Category 4: Commercial File Encryption Tools**

Various commercial and open-source tools provide file-level encryption for individual files or directories.

**Examples:**
- **AxCrypt:** AES-256 file encryption with cloud key management options
- **Boxcryptor:** Cloud storage encryption with AES-256 and RSA key management
- **Cryptomator:** Open-source cloud file encryption using AES with secure key derivation
- **NordLocker:** Commercial file encryption service with proprietary protocols

**Limitations:**
- **Proprietary Protocols:** Some use undisclosed encryption schemes, preventing independent security verification
- **Vendor Lock-in:** Encrypted files may require specific software for decryption, limiting portability
- **Cloud Dependencies:** Some require online services for key management, introducing third-party trust
- **Closed Source:** Proprietary tools cannot be audited, contradicting cryptographic best practices

**Gap Analysis: Deficiencies in Existing Systems**

Analyzing existing systems reveals several gaps that motivate this project:

**Gap 1: Nonce Management Remains Burdensome**

All existing systems using AES-GCM require careful nonce management. While some implement counters or random generation, the operational burden persists. No mainstream system addresses nonce management through architectural design (extended nonce spaces for critical operations).

**Gap 2: Performance Consistency Lacking**

Systems optimized for AES suffer on non-accelerated platforms; systems using ChaCha20 may lack regulatory approval. No hybrid approach leverages both algorithms in complementary roles to achieve consistent performance across platforms while maintaining compliance.

**Gap 3: Limited Algorithmic Diversity in Symmetric Encryption**

Traditional hybrid encryption combines asymmetric and symmetric algorithms for different purposes (key exchange vs data encryption). Few systems employ multiple symmetric algorithms in layered roles to provide defense in depth while avoiding asymmetric encryption overhead.

**Gap 4: Complexity Versus Usability Trade-off**

Systems with robust key management (PKI-based) impose complexity on users. Simple systems with automated key handling may lack security features or transparency. Few systems achieve both strong security and operational simplicity.

**Position of Proposed System:**

The proposed hybrid symmetric encryption system addresses these gaps by:
- Using XChaCha20's extended nonce space for key encryption to mitigate nonce collision risks architecturally
- Combining AES (for compliance and hardware acceleration) with XChaCha20 (for robust key protection and software performance)
- Employing two symmetric algorithms in layered roles (not traditional asymmetric-symmetric hybrid)
- Automating key management while maintaining transparency through open-source implementation
- Focusing on practical operational security rather than purely theoretical optimization

This system occupies a unique position: more sophisticated than single-algorithm tools, yet simpler than full PKI-based solutions; compliant with regulatory standards while incorporating modern cryptographic techniques.

## 1.5 Proposed System

**System Architecture Overview**

The system comprises four primary architectural components operating in a layered design:

**Component 1: AES-256-GCM File Encryption Module**

Responsible for encrypting and decrypting file content using the Advanced Encryption Standard.

**Technical Specifications:**
- **Algorithm:** AES-256 (Rijndael block cipher with 256-bit key)
- **Mode of Operation:** GCM (Galois/Counter Mode) providing authenticated encryption
- **Key Generation:** Cryptographically secure random 256-bit keys via OS entropy source
- **Nonce Generation:** Random 128-bit nonces for each encryption operation
- **Authentication:** 128-bit authentication tags computed over ciphertext
- **Implementation:** PyCryptodome library version 3.19.0
- **Performance:** Hardware acceleration via AES-NI when available

**Functionality:**
- `generate_key()`: Produces 32-byte random encryption keys
- `encrypt_file(input_path, output_path, key)`: Encrypts file content, returns nonce and authentication tag
- `decrypt_file(input_path, output_path, key)`: Decrypts file content with integrity verification

**Component 2: XChaCha20-Poly1305 Key Encryption Module**

Responsible for encrypting AES keys to provide an additional security layer.

**Technical Specifications:**
- **Algorithm:** XChaCha20 stream cipher (extended-nonce variant of ChaCha20)
- **Authentication:** Poly1305 message authentication code
- **Key Size:** 256 bits (32 bytes)
- **Nonce Size:** 192 bits (24 bytes) - extended from standard 96-bit nonces
- **Implementation:** PyNaCl library version 1.5.0 wrapping libsodium
- **Output Size:** Fixed 72 bytes (24-byte nonce + 32-byte encrypted key + 16-byte tag)

**Functionality:**
- `generate_master_key()`: Produces 32-byte XChaCha20 master keys
- `encrypt_key(aes_key, master_key)`: Encrypts AES key, automatically generating nonce
- `decrypt_key(encrypted_key, master_key)`: Decrypts and verifies AES key
- `save_encrypted_key(data, path)`: Writes encrypted key to file
- `load_encrypted_key(path)`: Reads encrypted key from file

**Component 3: Hybrid Integration Controller**

Orchestrates the complete encryption and decryption workflow, coordinating both encryption modules.

**Encryption Workflow:**
1. Generate random 256-bit AES key using secure RNG
2. Encrypt file content with AES-256-GCM, producing encrypted file and authentication tag
3. Generate random 256-bit XChaCha20 master key
4. Encrypt AES key using XChaCha20-Poly1305
5. Create metadata JSON containing: original filename, file paths, master key, file size
6. Save encrypted file (.enc), encrypted key (.key), and metadata (.meta)

**Decryption Workflow:**
1. Load and parse metadata file
2. Extract XChaCha20 master key from metadata
3. Load encrypted AES key from .key file
4. Decrypt AES key using XChaCha20 master key (verify Poly1305 tag)
5. Load encrypted file content
6. Decrypt file using recovered AES key (verify GCM tag)
7. Save decrypted file with original filename
8. Securely erase cryptographic keys from memory

**Security Properties:**
- **Fail-Safe Design:** Authentication failure aborts operation immediately; no unauthenticated data output
- **Key Separation:** AES keys and master keys are cryptographically independent
- **Integrity Verification:** Dual-layer authentication (GCM + Poly1305) detects tampering
- **Automated Cleanup:** Temporary keys cleared from memory after operations

**Component 4: Command-Line Interface**

Provides user-facing interaction through three primary commands.

**Command 1: encrypt**
- **Syntax:** `python cli.py encrypt -f FILE [-o OUTPUT_DIR] [-y] [-s]`
- **Function:** Encrypts specified file using hybrid approach
- **Options:**
  - `-f, --file`: File to encrypt (required)
  - `-o, --output`: Output directory (default: "encrypted")
  - `-y, --yes`: Skip confirmation prompt
  - `-s, --save-key`: Save master key to separate file for backup
- **Output:** Creates .enc, .key, and .meta files

**Command 2: decrypt**
- **Syntax:** `python cli.py decrypt -m METADATA [-o OUTPUT_DIR]`
- **Function:** Decrypts file using metadata reference
- **Options:**
  - `-m, --metadata`: Metadata file path (required)
  - `-o, --output`: Output directory (default: "decrypted")
- **Output:** Restores original file with integrity verification

**Command 3: info**
- **Syntax:** `python cli.py info`
- **Function:** Displays system capabilities and usage information
- **Output:** Algorithm details, security features, usage examples

**Figure 1.1: Hybrid Encryption System Architecture**

```
┌─────────────────────────────────────────────────────┐
│          COMMAND-LINE INTERFACE (CLI)               │
│  Commands: encrypt, decrypt, info                   │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│      HYBRID INTEGRATION CONTROLLER                  │
│  Orchestrates encryption/decryption workflow        │
└──────────┬──────────────────────────┬───────────────┘
           │                          │
           ▼                          ▼
┌──────────────────────┐    ┌──────────────────────┐
│  AES-256-GCM         │    │  XChaCha20-Poly1305  │
│  File Encryption     │    │  Key Encryption      │
│                      │    │                      │
│ • PyCryptodome 3.19  │    │ • PyNaCl 1.5.0       │
│ • 256-bit keys       │    │ • 256-bit keys       │
│ • 128-bit nonces     │    │ • 192-bit nonces     │
│ • Hardware accel     │    │ • Software optimized │
└──────────┬───────────┘    └──────────┬───────────┘
           │                          │
           ▼                          ▼
    ┌────────────┐            ┌────────────┐
    │ Encrypted  │            │ Encrypted  │
    │ File (.enc)│            │ Key (.key) │
    └────────────┘            └────────────┘
           │                          │
           └──────────┬───────────────┘
                      ▼
              ┌──────────────┐
              │  Metadata    │
              │  (.meta)     │
              └──────────────┘
```

**File Format Specifications**

**Encrypted File Format (.enc):**
```
Byte Offset | Content              | Size
------------|----------------------|--------
0-15        | AES-GCM Nonce        | 16 bytes
16-31       | Authentication Tag   | 16 bytes
32-EOF      | Encrypted Content    | Variable
```

**Encrypted Key Format (.key):**
```
Byte Offset | Content              | Size
------------|----------------------|--------
0-23        | XChaCha20 Nonce      | 24 bytes
24-55       | Encrypted AES Key    | 32 bytes
56-71       | Poly1305 Tag         | 16 bytes
Total:                              72 bytes (fixed)
```

**Metadata Format (.meta - JSON):**
```json
{
  "original_filename": "document.pdf",
  "encrypted_file": "encrypted/document.pdf.enc",
  "key_file": "encrypted/document.pdf.key",
  "master_key": "a1b2c3d4e5f6...",
  "file_size": 1048576
}
```

**Technical Implementation Details**

**Programming Language:** Python 3.10+
- Chosen for: extensive library support, rapid development, cross-platform compatibility, strong cryptographic ecosystem

**Cryptographic Libraries:**
- **PyCryptodome:** Pure Python with optional C acceleration; BSD-licensed; regularly maintained
- **PyNaCl:** Python bindings for libsodium (high-performance C library); Apache-licensed

**Key Management Strategy:**
- All keys generated using OS cryptographic random number generators
- AES keys exist only in memory during operations (not stored unencrypted)
- Master keys stored in metadata for user convenience (metadata must be protected)
- Automatic key generation eliminates user error in key creation

**Security Analysis**

**Confidentiality:** 256-bit keys provide ~2^256 security level against brute force (computationally infeasible with current and foreseeable technology)

**Integrity:** Authenticated encryption at both layers detects tampering; modified ciphertext fails authentication and triggers operation abort

**Nonce Collision Resistance:** XChaCha20's 192-bit nonce provides 2^96 times larger space than AES-GCM; collision probability negligible even for billions of operations

**Defense in Depth:** Two independent encryption algorithms; compromise of one does not immediately expose the other layer

**Forward Secrecy (Limited):** Users can delete metadata after securely transmitting master key through separate channel, preventing retroactive decryption if metadata subsequently compromised

**Advantages Over Existing Systems**

1. **Addresses Nonce Reuse Risk:** Extended nonce space for key encryption reduces operational vulnerability
2. **Algorithmic Diversity:** Two encryption algorithms provide defense against algorithm-specific failures
3. **Compliance Maintained:** AES for bulk encryption satisfies FIPS requirements
4. **Performance Balanced:** Hardware acceleration for bulk data, efficient software implementation for key operations
5. **Usability Enhanced:** Automated key management, metadata-based decryption, clear CLI
6. **Transparency Provided:** Open-source implementation enables security auditing

**Limitations and Scope**

The current implementation deliberately excludes certain features to maintain project scope:
- No network file transfer (local encryption only)
- No graphical user interface (CLI only)
- No multi-user access control or shared key management
- No cloud storage integration
- No post-quantum cryptographic algorithms
- Limited to Python runtime environments

These limitations do not diminish core functionality but represent areas for future enhancement.

## 1.6 Features of the Project

This section enumerates specific features implemented in the system, demonstrating functionality and technical capabilities.

**Feature 1: Dual-Layer Hybrid Encryption Architecture**

The system implements two encryption layers with complementary algorithms serving distinct roles.

**Description:**
- **Primary Layer:** AES-256-GCM encrypts file content (leverages hardware acceleration, complies with standards)
- **Secondary Layer:** XChaCha20-Poly1305 encrypts AES keys (extended nonce space, software performance)
- **Independence:** Each layer uses separate keys; compromise of one layer requires additional effort to compromise the other

**Benefit:** Defense in depth through algorithmic diversity; operational resilience through extended nonce space for critical key operations

**Feature 2: Automated Cryptographic Key Generation**

Users need not manually create or handle cryptographic keys.

**Description:**
- System automatically generates all required keys using cryptographically secure random number generators
- OS entropy sources accessed via Python `secrets` module or `os.urandom()`
- Key lengths conform to NIST recommendations (256 bits minimum)
- No user interaction required for key creation

**Benefit:** Eliminates common user errors (weak passwords, insufficient randomness, key reuse); ensures cryptographic strength

**Feature 3: Authenticated Encryption at All Layers**

Both encryption layers provide integrity protection, detecting tampering.

**Description:**
- **AES-GCM:** Galois/Counter Mode computes authentication tag over ciphertext; decryption verifies tag before outputting plaintext
- **XChaCha20-Poly1305:** Poly1305 MAC authenticates encrypted keys
- **Fail-Safe:** Authentication failure causes immediate operation abort without outputting unverified data
- **Constant-Time Comparison:** Tag verification uses timing-attack-resistant comparison

**Benefit:** Protects against active attacks (tampering, forgery); maintains data integrity

**Feature 4: Extended Nonce Space for Enhanced Security**

XChaCha20 employs 192-bit nonces, dramatically larger than standard implementations.

**Description:**
- Standard AES-GCM: 96-bit nonces (2^96 possible values)
- XChaCha20: 192-bit nonces (2^192 possible values)
- Collision probability reduced by factor of 2^96
- Random nonce generation safe even with billions of operations

**Benefit:** Mitigates nonce collision risks; enables stateless operation without counter coordination

**Feature 5: Modular Architecture with Independent Components**

System organized as separate, testable modules with clear interfaces.

**Description:**
- **Module 1:** `aes_encryption.py` - AES operations only
- **Module 2:** `xchacha20_encryption.py` - XChaCha20 operations only
- **Module 3:** `hybrid_encryption.py` - Integration logic
- **Module 4:** `cli.py` - User interface
- Each module includes self-test functionality for validation

**Benefit:** Facilitates independent testing, debugging, and future enhancement; enables component reuse

**Feature 6: Command-Line Interface with Multiple Operations**

User-friendly CLI providing three primary commands with Unix-style conventions.

**Description:**
- **encrypt:** Syntax follows standard CLI patterns with flags (-f, -o, -y)
- **decrypt:** Simplified operation requiring only metadata file reference
- **info:** Self-documenting system displaying capabilities and usage
- **Help:** `--help` flag provides comprehensive usage information
- **Error Handling:** Clear, actionable error messages for common failure modes

**Benefit:** Accessible to technical users; scriptable for automation; follows familiar interface patterns

**Feature 7: Metadata-Based Decryption**

Single metadata file contains all information needed for decryption.

**Description:**
- Metadata stored as human-readable JSON
- Contains: original filename, file paths, master key, file size
- Users provide single file for decryption (no manual key management)
- Metadata can be backed up, transmitted, or stored separately from encrypted files

**Benefit:** Simplifies decryption workflow; reduces user error; enables flexible key distribution strategies

**Feature 8: Streaming Encryption for Large Files**

Files processed in chunks to prevent memory exhaustion.

**Description:**
- Chunk-based processing for files exceeding memory capacity
- Constant memory footprint regardless of file size
- Suitable for multi-gigabyte files on systems with limited RAM
- Maintains performance through buffered I/O

**Benefit:** Enables encryption of arbitrarily large files; prevents out-of-memory errors

**Feature 9: Comprehensive Integrity Verification**

All operations validate data integrity through authentication.

**Description:**
- Decryption includes mandatory authentication tag verification
- Tampered ciphertext detected and operation aborted
- No partial or unverified plaintext ever output to user
- Test suite confirms integrity preservation (original and decrypted files match exactly)

**Benefit:** Cryptographic guarantee of data integrity; protects against active attacks

**Feature 10: Cross-Platform Compatibility**

Implementation runs on multiple operating systems without modification.

**Description:**
- **Tested Platforms:** Ubuntu 22.04 (Linux), Windows 11
- **Expected Support:** macOS 10.15+ (Python cross-platform compatibility)
- Same codebase functions across platforms
- Platform-independent file formats enable cross-platform encrypted file exchange

**Benefit:** Wide deployment options; users on different OS can exchange encrypted files

**Feature 11: Performance Benchmarking and Visualization**

System includes comprehensive performance testing infrastructure.

**Description:**
- Automated benchmark suite tests multiple file sizes (1-100 MB)
- Measures: encryption time, decryption time, throughput (MB/s)
- Generates performance graphs using matplotlib (6 visualizations)
- Results stored as JSON for reproducibility
- Verification confirms integrity preservation (SHA-256 hash comparison)

**Benefit:** Provides empirical performance data; enables optimization; validates system behavior

**Feature 12: Version Control and Development Transparency**

Complete development history maintained in Git repository.

**Description:**
- All code committed with descriptive messages
- GitHub repository enables code review and collaboration
- Commit history demonstrates iterative development process
- Issue tracking and documentation maintained

**Benefit:** Transparency enables security auditing; demonstrates learning process; facilitates collaboration

**Feature 13: Open-Source Implementation**

System built entirely with open-source tools and libraries.

**Description:**
- Python runtime (PSF license - open source)
- PyCryptodome (BSD license - permissive)
- PyNaCl (Apache 2.0 license - permissive)
- No proprietary dependencies or closed-source components
- Source code available for inspection, auditing, and modification

**Benefit:** Security through transparency; no vendor lock-in; enables independent verification

**Feature 14: Comprehensive Documentation**

Multiple documentation layers support users and developers.

**Description:**
- Inline code comments explain implementation details
- Function docstrings document parameters and behavior
- README file provides installation and usage instructions
- This comprehensive project report documents design and implementation
- Performance test results and visualizations
- User manual included in appendices

**Benefit:** Supports understanding, maintenance, and future enhancement; facilitates evaluation

**Summary of Key Features:**

The system delivers a complete, functional file encryption solution addressing identified vulnerabilities in existing systems while maintaining usability and performance. Features emphasize security (dual-layer encryption, authentication, extended nonces), usability (automated key management, CLI, metadata-based decryption), and transparency (open source, comprehensive documentation, performance data).

---

# CHAPTER 2: REQUIREMENT ANALYSIS

## 2.1 Feasibility Study

Feasibility analysis evaluates whether the proposed system can be successfully developed and deployed given available resources, technical capabilities, constraints, and time limitations. This section assesses technical, operational, economic, schedule, and legal feasibility.

**2.1.1 Technical Feasibility**

**Question:** Can the system be implemented with available technology, libraries, and team expertise?

**Analysis:**

**Cryptographic Libraries Available:**

Python ecosystem provides mature, well-maintained cryptographic libraries implementing required algorithms:

- **PyCryptodome:** Active development (last update within months), extensive documentation, BSD-licensed, supports AES with all standard modes including GCM
- **PyNaCl:** Wrapper for libsodium (highly-regarded C cryptographic library), Apache-licensed, implements XChaCha20-Poly1305 through simple SecretBox API
- **Security:** Both libraries undergo regular security audits and maintain active user communities reporting vulnerabilities

**Development Environment:**

Required tools freely available across platforms:
- Python interpreter (versions 3.8-3.11 tested and compatible)
- Text editors / IDEs (VS Code, PyCharm, vim - team already familiar)
- Git version control (standard development tool, team experienced)
- Testing frameworks (Python unittest - standard library, no installation required)

**Team Expertise:**

- Both team members completed coursework in: Python programming, data structures, algorithms, computer networks
- Prior projects involved Python development (smaller scope)
- Cryptography concepts covered in Cyber Security curriculum
- Linux/Windows command-line proficiency from system administration coursework

**Algorithm Complexity Managed:**

While cryptographic algorithms internally complex (AES involves substitution-permutation networks, Galois field mathematics; ChaCha20 uses ARX operations), library abstractions hide implementation details. Team needs understanding of:
- Proper API usage (passing correct parameter types, handling return values)
- Key management principles (generation, storage, secure erasure)
- Security properties (authentication, nonce uniqueness requirements)
- NOT required: Low-level algorithm implementation, mathematical proofs, custom cryptographic code

**Integration Challenges:**

Combining two encryption systems requires orchestration but involves well-defined steps:
1. Encrypt file with AES → get encrypted file and key
2. Encrypt key with XChaCha20 → get encrypted key
3. Package outputs → create metadata file
4. Reverse for decryption

No novel protocols, distributed system coordination, or complex concurrent operations required.

**Conclusion:** ✅ **Technically Feasible**

Required libraries exist with good documentation. Team possesses necessary programming skills. Integration complexity within team capabilities. No exotic hardware or software requirements.

**2.1.2 Operational Feasibility**

**Question:** Will the system be usable by target audience in practical scenarios? Does it solve real problems users face?

**Analysis:**

**User Interface Appropriateness:**

- Command-line interface familiar to target users (developers, system administrators, security professionals)
- Three-command structure (encrypt, decrypt, info) minimizes learning curve
- Follows Unix CLI conventions (flags like -f, -o; --help standard)
- Output messages guide users through operations
- Error messages indicate problems and suggest solutions

**Target User Technical Level:**

Primary users are technical professionals comfortable with:
- Command-line operation
- File paths and directory navigation
- Basic encryption concepts (even if not cryptographic experts)
- Following technical documentation

**Key Management Automation:**

Significant usability advantage over systems requiring manual key handling:
- Users need not generate keys manually (error-prone)
- No memorizing or manually entering keys during decryption
- Metadata files simplify operation (single file contains all decryption information)
- Reduces risk of key loss or mismanagement

**Performance Adequacy:**

Benchmarking demonstrates acceptable performance for typical use cases:
- 1MB document: ~0.01 seconds encryption (imperceptible delay)
- 100MB file: ~1.2 seconds encryption (acceptable for most scenarios)
- Throughput ~87 MB/s sufficient for interactive use
- No blocking operations preventing other system use

**Portability Across Systems:**

- Cross-platform operation (Linux, Windows, macOS) enables wide deployment
- Encrypted files transferable between systems without compatibility issues
- Same interface across platforms (no retraining when changing OS)

**Integration Possibilities:**

- CLI suitable for integration into scripts (backup automation, data pipeline encryption)
- Standard input/output conventions enable Unix piping if extended
- Exit codes indicate success/failure for automated error handling

**Limitations for Non-Technical Users:**

Current CLI-only interface may challenge non-technical users:
- No graphical interface (point-and-click simplicity)
- Requires command-line comfort
- Error messages assume technical literacy

However, target audience specification (technical professionals) aligns with CLI design.

**Conclusion:** ✅ **Operationally Feasible for Target Audience**

System usable by intended technical users. Automation reduces error potential. Performance acceptable for practical scenarios. Future GUI could broaden accessibility but current design appropriate for defined user base.

**2.1.3 Economic Feasibility**

**Question:** Is the project economically viable given budget and resource constraints? What are development and deployment costs?

**Analysis:**

**Development Costs: Zero Monetary Cost**

- **Licensing:** All software components open source with permissive licenses (no fees)
- **Development Tools:** Python (free), VS Code (free), Git (free)
- **Libraries:** PyCryptodome (BSD), PyNaCl (Apache) - no licensing costs
- **Cloud Services:** Not required; local development only
- **Hardware:** Team members' existing laptops sufficient; no specialized equipment needed

**Time Investment:**

- Primary cost is team members' time (academic project context)
- Estimated: 200-250 person-hours total across both team members over semester
- No opportunity cost (project required for degree completion)

**Deployment Costs: Minimal**

- End users require only Python runtime and libraries (free downloads)
- No server infrastructure, databases, or cloud services required
- No subscription fees or usage restrictions
- Bandwidth costs minimal (encrypted files similar size to originals; ~32 bytes overhead)

**Maintenance Costs:**

- Dependencies maintained by open-source communities (no support contracts)
- Security updates provided free through library maintainers
- No ongoing operational costs

**Comparative Cost Analysis:**

Alternative approaches and their costs:
- **Commercial encryption tools:** $30-100 per user license (AxCrypt, Boxcryptor)
- **Enterprise solutions:** $1000s for corporate deployments
- **Custom development with proprietary libraries:** Licensing fees + development costs
- **This project:** $0 monetary cost

**Resource Availability:**

- University provides: Internet connectivity, electricity, workspace
- No specialized equipment rental or purchase required
- No external consultant fees or expert hiring

**Conclusion:** ✅ **Economically Feasible - Zero Budget Required**

Project incurs no monetary costs. All resources freely available. Economic constraints do not limit project scope or quality. Academic setting provides time resources for development without financial compensation requirement.

**2.1.4 Schedule Feasibility**

**Question:** Can the project be completed within available timeframe (one semester)? Are milestones achievable?

**Analysis:**

**Available Timeline:**

- Academic semester: ~16 weeks (November 2024 - March 2025)
- Effective development time: ~14 weeks (accounting for exams, holidays)
- Team size: 2 members (enables parallel work)

**Complexity Assessment:**

**Core functionality breakdown:**
1. AES encryption module: ~2 weeks (research, implementation, testing)
2. XChaCha20 module: ~1.5 weeks (similar to AES but simpler API)
3. Integration controller: ~1 week (coordinate modules, metadata handling)
4. CLI interface: ~1 week (argument parsing, user interaction)
5. Performance testing: ~1 week (benchmark suite, graph generation)
6. Documentation: ~2-3 weeks (inline comments, README, report writing)
7. Buffer time: ~3-4 weeks (debugging, refinement, unexpected challenges)

**Total estimated: ~12-13 weeks (within 14-week available time)**

**Parallel Work Opportunities:**

Modular architecture enables simultaneous development:
- **Week 1-2:** Literature review (both), environment setup (both)
- **Week 3-5:** Person 1 develops AES module; Person 2 develops XChaCha20 module (parallel)
- **Week 6-7:** Integration (collaborative)
- **Week 8:** CLI development (Person 2 leads)
- **Week 9-10:** Testing and performance benchmarking (both)
- **Week 11-14:** Documentation and report writing (both)

**Risk Mitigation Factors:**

- **Modular design:** Core functionality deliverable even if advanced features deferred
- **Library dependency:** Not implementing cryptography from scratch (90% time savings)
- **CLI vs GUI:** Command-line interface much faster to implement than graphical interface
- **Iterative approach:** Working system at each milestone; can stop at any viable checkpoint

**Milestone Deliverables:**

- **Month 1:** Individual modules working independently
- **Month 2:** Integrated hybrid system functional
- **Month 3:** CLI complete, performance testing done
- **Month 4:** Documentation complete, report submitted

**Schedule Risks:**

- **Library compatibility issues:** Mitigated by version pinning, early testing
- **Debugging time:** Buffer time allocated (3-4 weeks)
- **Team member unavailability:** Modular design enables independent work
- **Scope creep:** Features clearly defined; "nice-to-haves" explicitly deferred

**Conclusion:** ✅ **Schedule Feasible with Proper Planning**

Timeline realistic for defined scope. Parallel work reduces calendar time. Modular architecture provides flexibility. Buffer time accommodates unexpected challenges. Project deliverable within semester timeframe.

**2.1.5 Legal Feasibility**

**Question:** Are there legal, regulatory, or intellectual property constraints preventing implementation or deployment?

**Analysis:**

**Export Control Regulations:**

**Historical Context:**
- Cryptographic software historically subject to export controls (classified as "munitions")
- U.S. regulations evolved; publicly available cryptographic software generally exempt with notification

**Current Status:**
- Project uses standard, widely-deployed algorithms (AES, ChaCha20)
- Implementation based on publicly available specifications (NIST FIPS 197, IETF RFCs)
- Educational/research use generally protected
- No novel cryptographic techniques that might trigger additional scrutiny

**Relevant Regulations:**
- U.S. Export Administration Regulations (EAR) - exemption for publicly available software
- Wassenaar Arrangement - coordinates export controls but allows public domain cryptography

**Conclusion:** Low risk for academic project using standard algorithms and open-source libraries.

**Patent and Intellectual Property:**

**Algorithm Patents:**
- **AES:** Explicitly patent-free; NIST selected Rijndael partly for lack of patent restrictions
- **ChaCha20:** Designed by Daniel J. Bernstein as public domain algorithm; no patent claims
- **GCM Mode:** NIST-standardized mode; no patent restrictions for implementations following standard
- **Poly1305:** Public domain MAC algorithm; no licensing concerns

**Library Licenses:**
- **PyCryptodome:** BSD 2-Clause License (permissive; allows use, modification, distribution)
- **PyNaCl:** Apache License 2.0 (permissive; includes patent grant protecting users)
- **Python:** Python Software Foundation License (permissive, GPL-compatible)

**License Compatibility:**
- All licenses mutually compatible
- Permits use in academic projects
- Enables future open-source release if desired
- No viral copyleft requirements (unlike GPL for some projects)

**Project Code Ownership:**
- Code developed as academic project (educational purpose)
- No employer IP claims (students, not employees)
- No external funding with IP stipulations

**Conclusion:** No patent obstacles. All dependencies use permissive open-source licenses.

**Regulatory Compliance:**

**Data Protection Regulations:**
- Project provides encryption tool; does not collect/process user data
- GDPR, CCPA, etc. not directly applicable (no data processing service)
- Users responsible for complying with regulations when encrypting their data

**Standards Compliance:**
- AES implementation follows FIPS 197 specification
- No formal FIPS 140-2 validation (requires commercial testing laboratory, costly)
- Algorithms compliant with standards but implementation not certified

**Academic Context Protection:**
- Educational projects generally protected under academic freedom principles
- Research and teaching exemptions in various regulations
- Non-commercial nature reduces regulatory burden

**Ethical Considerations:**

**Dual Use Concerns:**
- Encryption technology can be used for legitimate privacy or concealing illegal activities
- However, encryption is fundamental human right per UN declarations
- Legitimate uses vastly outnumber malicious uses
- Many democracies enshrine encryption rights in law

**Responsible Disclosure:**
- Project documentation includes appropriate use guidance
- No marketing toward malicious use cases
- Emphasis on privacy, security, legitimate data protection

**Transparency:**
- Open-source nature enables security auditing
- No hidden backdoors or intentional weaknesses
- Aligns with cryptographic community values

**Conclusion:** ✅ **Legally Feasible with Standard Academic Protections**

No legal barriers identified for academic project using standard, publicly available algorithms and open-source libraries. Export controls generally exempt publicly available educational software. No patent restrictions. Ethical considerations addressed through responsible development and documentation.

**Overall Feasibility Conclusion:**

All feasibility dimensions indicate project viability:

| Feasibility Type | Assessment | Risk Level |
|------------------|------------|------------|
| Technical | ✅ Feasible | Low |
| Operational | ✅ Feasible | Low |
| Economic | ✅ Feasible | Minimal |
| Schedule | ✅ Feasible | Moderate |
| Legal | ✅ Feasible | Low |

**Overall:** ✅ **PROJECT FEASIBLE**

Primary risks—cryptographic implementation errors—mitigated through use of established libraries. Schedule manageable with modular architecture. Zero monetary cost. Legal environment permissive for educational cryptographic projects. Project appropriate for academic timeframe with two-person team.

## 2.2 Software Requirement Specification Document

This section provides comprehensive requirements specification, defining functional and non-functional requirements, hardware and software needs, and constraints.

**2.2.1 Functional Requirements**

Functional requirements define specific behaviors and operations the system must perform.

**FR1: AES-256-GCM File Encryption**

- **Requirement ID:** FR1
- **Priority:** High (Core functionality)
- **Description:** System shall encrypt files using AES-256 in Galois/Counter Mode
- **Input:** File path (any readable file), optional output directory
- **Processing:**
  1. Validate file exists and is readable
  2. Generate 256-bit random encryption key using cryptographically secure RNG
  3. Generate 128-bit random nonce (unique for each operation)
  4. Read file content (streaming for large files)
  5. Encrypt content with AES-256-GCM
  6. Compute authentication tag over ciphertext
- **Output:** Encrypted file containing: nonce (16 bytes) + tag (16 bytes) + ciphertext
- **Success Criteria:** File encrypted successfully, authentication tag generated
- **Failure Handling:** Display error message if file not found, not readable, or encryption fails

**FR2: XChaCha20-Poly1305 Key Encryption**

- **Requirement ID:** FR2
- **Priority:** High (Core functionality)
- **Description:** System shall encrypt AES keys using XChaCha20-Poly1305
- **Input:** AES key (32 bytes exactly), optional output directory
- **Processing:**
  1. Validate input is 32 bytes
  2. Generate 256-bit random master key
  3. Generate 192-bit random nonce
  4. Encrypt AES key with XChaCha20-Poly1305
  5. Compute Poly1305 authentication tag
- **Output:** Fixed-size encrypted key file (72 bytes): nonce (24B) + encrypted key (32B) + tag (16B)
- **Success Criteria:** Key encrypted, authentication tag generated
- **Failure Handling:** Display error if input invalid or encryption fails

**FR3: Metadata Generation and Storage**

- **Requirement ID:** FR3
- **Priority:** High (Required for decryption)
- **Description:** System shall generate metadata files containing decryption information
- **Input:** Original filename, encrypted file path, key file path, master key, file size
- **Processing:**
  1. Create JSON object with required fields
  2. Format with indentation for readability
  3. Write to file with .meta extension
- **Output:** JSON metadata file
- **Success Criteria:** Valid JSON file created with all required fields
- **Failure Handling:** Error if unable to write file

**FR4: File Decryption with Integrity Verification**

- **Requirement ID:** FR4
- **Priority:** High (Core functionality)
- **Description:** System shall decrypt files using metadata, verifying integrity at both layers
- **Input:** Metadata file path, optional output directory
- **Processing:**
  1. Load and parse metadata (validate JSON format)
  2. Extract master key from metadata
  3. Load encrypted AES key from .key file
  4. Decrypt AES key using XChaCha20 master key
  5. Verify Poly1305 authentication tag; abort if invalid
  6. Load encrypted file from .enc file
  7. Decrypt file using recovered AES key
  8. Verify GCM authentication tag; abort if invalid
  9. Write decrypted content only if both tags valid
- **Output:** Decrypted file with original filename
- **Success Criteria:** File decrypted, both authentication tags verified, output matches original
- **Failure Handling:** If any tag invalid, display error and DO NOT output plaintext

**FR5: Command-Line Argument Parsing**

- **Requirement ID:** FR5
- **Priority:** Medium (Usability)
- **Description:** System shall parse and validate command-line arguments
- **Commands:**
  - **encrypt:** `-f FILE [-o OUTPUT] [-y] [-s]`
  - **decrypt:** `-m METADATA [-o OUTPUT]`
  - **info:** No arguments
- **Processing:**
  1. Parse arguments using argparse library
  2. Validate required arguments present
  3. Apply default values for optional arguments
  4. Validate file paths exist (for input files)
- **Output:** Parsed arguments passed to appropriate function
- **Success Criteria:** Arguments correctly parsed and validated
- **Failure Handling:** Display usage help if arguments invalid

**FR6: Automated Key Generation**

- **Requirement ID:** FR6
- **Priority:** High (Security requirement)
- **Description:** System shall automatically generate cryptographically secure random keys
- **Input:** None (automatic operation)
- **Processing:**
  1. Access OS random number generator (os.urandom() or secrets module)
  2. Generate requested number of random bytes (32 for keys)
  3. Return key material
- **Output:** 256-bit (32-byte) random key
- **Success Criteria:** Key generated with sufficient entropy
- **Failure Handling:** Error if RNG unavailable (should never occur on modern OS)

**FR7: Error Handling and User Feedback**

- **Requirement ID:** FR7
- **Priority:** Medium (Robustness)
- **Description:** System shall handle errors gracefully with informative messages
- **Error Scenarios:**
  - File not found
  - Permission denied
  - Authentication failure (tampering)
  - Invalid metadata format
  - Insufficient disk space
- **Processing:**
  1. Catch exceptions at appropriate levels
  2. Format error message with problem description and suggested action
  3. Display to user via console output
  4. Exit with appropriate error code
- **Output:** Error message to stderr, non-zero exit code
- **Success Criteria:** Errors handled without crashes, messages actionable

**FR8: Integrity Verification Testing**

- **Requirement ID:** FR8
- **Priority:** High (Validation)
- **Description:** System shall verify that decrypted files match originals exactly
- **Input:** Original file, decrypted file
- **Processing:**
  1. Compute SHA-256 hash of original file
  2. Compute SHA-256 hash of decrypted file
  3. Compare hashes using constant-time comparison
- **Output:** Pass/fail indication
- **Success Criteria:** Hashes match (files identical)
- **Failure Handling:** Report integrity failure if hashes differ

**Table 2.3: Functional Requirements Summary**

| Requirement ID | Description | Priority | Status |
|----------------|-------------|----------|--------|
| FR1 | AES-256-GCM file encryption | High | Implemented |
| FR2 | XChaCha20 key encryption | High | Implemented |
| FR3 | Metadata generation | High | Implemented |
| FR4 | File decryption with verification | High | Implemented |
| FR5 | CLI argument parsing | Medium | Implemented |
| FR6 | Automated key generation | High | Implemented |
| FR7 | Error handling | Medium | Implemented |
| FR8 | Integrity verification | High | Implemented |

**2.2.2 Non-Functional Requirements**

Non-functional requirements define system qualities, constraints, and characteristics.

**NFR1: Performance Requirements**

- **Requirement ID:** NFR1
- **Description:** System shall meet specified performance thresholds
- **Metrics:**
  - Encryption throughput: ≥ 50 MB/s on standard hardware (Intel i5/AMD Ryzen 5 equivalent, 8GB RAM)
  - Decryption throughput: ≥ 50 MB/s (similar to encryption)
  - Memory usage: ≤ 500 MB peak for any file size (streaming implementation)
  - Startup time: ≤ 2 seconds from command invocation to first output
  - Small file overhead: 1KB file encrypted in ≤ 100ms
- **Measurement:** Python time module, average of multiple runs
- **Justification:** Performance must be adequate for interactive use; users unwilling to wait minutes for moderate-size files

**NFR2: Security Requirements**

- **Requirement ID:** NFR2
- **Description:** System shall implement cryptographic best practices
- **Specifications:**
  - Use cryptographically secure random number generators (os.urandom() or secrets module)
  - Employ authenticated encryption at all layers (no encryption without authentication)
  - Verify authentication tags before outputting plaintext (fail-safe design)
  - Use minimum 256-bit keys (NIST recommendations for long-term security)
  - Never store keys in plaintext (encrypt before any persistent storage)
  - Employ constant-time comparison for authentication tags (prevent timing attacks)
- **Validation:** Code review, security testing with tampered ciphertext
- **Justification:** Cryptographic systems fail catastrophically from small errors; strict security requirements prevent vulnerabilities

**NFR3: Reliability Requirements**

- **Requirement ID:** NFR3
- **Description:** System shall produce consistent, correct results
- **Specifications:**
  - Decrypted files shall match originals with 100% accuracy (bitwise identical)
  - Operations shall be deterministic given same keys/nonces
  - System shall handle interruptions gracefully (no data corruption)
  - Temporary files shall be cleaned up after operations
- **Measurement:** Hash comparison (SHA-256), repeated operation testing
- **Justification:** Encryption system that corrupts data worse than no encryption; perfect reliability required

**NFR4: Usability Requirements**

- **Requirement ID:** NFR4
- **Description:** System shall be accessible to target users (technical professionals)
- **Specifications:**
  - Command syntax follows standard CLI conventions (Unix-style flags)
  - Help messages clearly explain usage with examples
  - Error messages indicate problem cause and resolution steps
  - Operations complete with clear success/failure indication
  - Confirmation prompts prevent accidental data overwriting
- **Measurement:** User testing, error message clarity assessment
- **Justification:** Unusable security tools often abandoned or misused, compromising security

**NFR5: Portability Requirements**

- **Requirement ID:** NFR5
- **Description:** System shall run on multiple operating systems
- **Specifications:**
  - Support Linux (Ubuntu 20.04+), Windows (10+), macOS (10.15+)
  - Use cross-platform Python libraries only
  - Handle platform-specific path separators (/ vs \)
  - Binary file handling correct on all platforms
  - Support Unicode filenames (UTF-8 encoding)
- **Testing:** Run on Linux and Windows; verify encrypted files decrypt on both
- **Justification:** Users employ diverse systems; cross-platform compatibility essential

**NFR6: Maintainability Requirements**

- **Requirement ID:** NFR6
- **Description:** System shall be maintainable and extensible
- **Specifications:**
  - Code follows PEP 8 style guidelines (Python style standard)
  - Functions include docstrings explaining purpose, parameters, returns
  - Modules loosely coupled (low dependencies between components)
  - Version control maintains complete development history
  - Comprehensive documentation (inline comments, README, report)
- **Measurement:** Code review, documentation completeness check
- **Justification:** Academic project may require future modifications; maintainability facilitates extensions

**NFR7: Compliance Requirements**

- **Requirement ID:** NFR7
- **Description:** System shall use standardized cryptographic algorithms
- **Specifications:**
  - AES implementation conforms to FIPS 197 specification
  - GCM mode follows NIST SP 800-38D
  - ChaCha20 conforms to RFC 8439
  - Key sizes meet NIST recommendations (256-bit minimum)
  - No custom cryptographic primitives (use established libraries)
- **Validation:** Library documentation review, specification comparison
- **Justification:** Custom cryptography prone to vulnerabilities; standards ensure peer review and correctness

**Table 2.4: Non-Functional Requirements Summary**

| Requirement ID | Category | Description | Priority |
|----------------|----------|-------------|----------|
| NFR1 | Performance | Throughput ≥50 MB/s, memory ≤500 MB | High |
| NFR2 | Security | Cryptographic best practices | Critical |
| NFR3 | Reliability | 100% accuracy, graceful failures | High |
| NFR4 | Usability | Clear interface, helpful errors | Medium |
| NFR5 | Portability | Cross-platform compatibility | Medium |
| NFR6 | Maintainability | Clean code, documentation | Medium |
| NFR7 | Compliance | Standard algorithms | High |

**2.2.3 Hardware Requirements**

**Table 2.1: Hardware Requirements**

| Component | Minimum Specification | Recommended Specification |
|-----------|----------------------|---------------------------|
| **Processor** | Any modern CPU (x86-64 or ARM) | Intel Core i5 / AMD Ryzen 5 or better |
| **RAM** | 512 MB available | 2 GB available |
| **Storage** | 100 MB for software + space for encrypted files | 1 GB (for software, test files, results) |
| **Network** | Not required (local operation) | Internet for initial library download |
| **Display** | Text-capable terminal | Any (CLI operates in terminal) |

**Rationale for Requirements:**
- **Processor:** Pure Python implementation runs on any architecture; hardware acceleration (AES-NI) beneficial but not required
- **RAM:** Streaming implementation prevents proportional memory growth with file size; 512MB sufficient for moderate files
- **Storage:** Encrypted files approximately same size as originals (32-byte overhead negligible)
- **Network:** System operates offline; network needed only for initial pip install of dependencies

**2.2.4 Software Requirements**

**Table 2.2: Software Requirements**

| Component | Specification | Purpose |
|-----------|---------------|---------|
| **Operating System** | Linux (Ubuntu 20.04+), Windows 10+, macOS 10.15+ | Platform for execution |
| **Python Runtime** | Version 3.8 or higher (3.10+ recommended) | Interpreter for application code |
| **PyCryptodome** | Version 3.19.0 (exact version pinned) | AES-256-GCM implementation |
| **PyNaCl** | Version 1.5.0 (exact version pinned) | XChaCha20-Poly1305 implementation |
| **Matplotlib** | Version 3.7.1 (for visualization) | Performance graph generation |
| **Git** | Version 2.0+ (development only) | Version control |

**Installation Process:**

```bash
# Step 1: Install Python 3.10+
# (Platform-specific: apt/brew/installer)

# Step 2: Create virtual environment
python3 -m venv venv

# Step 3: Activate virtual environment
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Step 4: Install dependencies
pip install -r requirements.txt
```

**requirements.txt Contents:**
```
pycryptodome==3.19.0
PyNaCl==1.5.0
matplotlib==3.7.1
```

**Dependency Rationale:**
- **Version pinning:** Specific versions ensure reproducibility; prevents breaking changes from updates
- **Minimal dependencies:** Only essential libraries included; reduces attack surface and installation complexity
- **Permissive licenses:** All dependencies use BSD, Apache, or similar licenses permitting free use

## 2.3 SDLC Model Used

**Selected Model: Iterative Development with Incremental Delivery**

This project employs an iterative development approach combining elements of incremental and agile methodologies. The model was selected for its suitability to cryptographic software development, academic project constraints, and two-person team dynamics.

**2.3.1 Model Overview and Rationale**

**Iterative Development Characteristics:**

The iterative model divides development into multiple iterations (typically 1-3 weeks each), with each iteration producing a working increment of the system. Unlike waterfall development where each phase must complete before the next begins, iterations allow refinement based on testing feedback and evolving understanding.

**Why Iterative Model for This Project:**

1. **Risk Mitigation:** Cryptographic systems require careful validation; iterative development with continuous testing reduces risk of fundamental design flaws discovered late in development

2. **Feedback Integration:** Each iteration produces working software enabling immediate testing and evaluation; findings inform subsequent iterations

3. **Incremental Complexity:** System built from simple, validated components (individual encryption modules) toward complex integrated system; each stage builds on tested foundation

4. **Team Collaboration:** Two-person team benefits from parallel development of independent modules (early iterations), then collaboration on integration (later iterations)

5. **Academic Constraints:** Iterative model accommodates semester timeline with clear milestones; regular deliverables provide progress visibility for evaluation

6. **Learning Curve:** Team learning cryptographic APIs and best practices during development; iterative approach allows incorporating lessons learned from early iterations into later work

**Rejected Alternative Models:**

**Waterfall Model:** Rejected due to inflexibility; cryptographic systems often require design adjustments based on testing; waterfall's sequential nature prevents iteration

**Pure Agile/Scrum:** Rejected due to overhead inappropriate for two-person team and lack of continuous customer involvement in academic context; formal sprints, daily standups, and product owner role unnecessary

**Spiral Model:** Rejected as overly complex for single-project, two-person context; extensive risk analysis and prototyping cycles introduce unnecessary overhead given use of established libraries

**Figure 2.1: Iterative Development Model Phases**

```
┌──────────────┐
│ Requirements │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Design    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│Implementation│
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Testing    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Evaluation  │
└──────┬───────┘
       │
       ▼ (Repeat for next iteration)
```

**2.3.2 Development Phases and Iterations**

**Phase 1: Planning and Initial Design (Week 1-2)**

**Activities:**
- Literature review on AES, XChaCha20, hybrid encryption approaches
- Requirements definition (functional and non-functional)
- Feasibility analysis
- High-level architecture design
- Development environment setup (Python, libraries, Git)
- Repository initialization on GitHub

**Deliverables:**
- Project synopsis document
- Architecture diagrams
- Requirements specification
- Configured development environment

**Team Organization:** Both members collaborate on research and planning

**Phase 2: Core Module Development (Week 3-6)**

**Iteration 2.1: AES Encryption Module (Weeks 3-4)**

**Team Member 1 (Pragati) Tasks:**
- Design AES encryption module interface
- Research PyCryptodome API documentation
- Implement file encryption with AES-256-GCM
- Implement file decryption with authentication verification
- Write unit tests for AES operations
- Document module with docstrings

**Deliverables:**
- `aes_encryption.py` with complete functionality
- Unit test suite demonstrating correctness
- Performance measurements (baseline)

**Iteration 2.2: XChaCha20 Key Encryption Module (Weeks 4-5)**

**Team Member 2 (Prajjwal) Tasks:**
- Design XChaCha20 encryption module interface
- Research PyNaCl API documentation
- Implement key encryption with XChaCha20-Poly1305
- Implement key decryption with authentication
- Write unit tests for key encryption operations
- Document module

**Deliverables:**
- `xchacha20_encryption.py` with complete functionality
- Unit test suite
- Nonce size verification tests

**Note:** Iterations 2.1 and 2.2 partially overlap (weeks 4-5), enabling parallel development

**Phase 3: Integration and Hybrid System (Week 6-7)**

**Activities (Both Members Collaborative):**
- Design hybrid system architecture
- Implement integration controller coordinating both modules
- Develop encryption workflow (file → AES → key → XChaCha20)
- Develop decryption workflow (reverse process)
- Implement metadata generation and parsing
- Integration testing with various file types and sizes
- Error handling and edge case testing

**Deliverables:**
- `hybrid_encryption.py` with complete integration
- Integration test suite
- End-to-end functionality validated

**Phase 4: User Interface Development (Week 8-9)**

**Team Member 2 (Prajjwal) Leads:**
- Design command-line interface
- Implement argument parsing with argparse
- Implement encrypt command with validation
- Implement decrypt command
- Implement info command
- Input validation and error messages
- Help documentation

**Team Member 1 (Pragati) Supports:**
- Review CLI design
- Test CLI commands
- Write usage documentation
- Create examples

**Deliverables:**
- `cli.py` with complete interface
- Usage documentation
- Command examples and tutorials

**Phase 5: Performance Testing and Optimization (Week 10-11)**

**Team Member 1 (Pragati) Leads:**
- Design performance test suite
- Implement automated benchmarking across file sizes
- Measure encryption/decryption times
- Calculate throughput metrics
- Identify performance bottlenecks
- Optimize critical paths if necessary

**Team Member 2 (Prajjwal) Supports:**
- Create visualization script for results
- Generate performance graphs with matplotlib
- Analyze results
- Prepare performance analysis section for report

**Deliverables:**
- `performance_test.py` automated benchmark suite
- `visualize_results.py` graph generation
- Performance data (JSON format)
- Six visualization graphs
- Performance analysis documentation

**Phase 6: Documentation and Refinement (Week 12-15)**

**Activities (Both Members):**
- Code cleanup and refactoring
- Comprehensive code documentation (docstrings, comments)
- README file with installation and usage instructions
- Project report writing (this document)
- Final integration testing and validation
- Presentation preparation

**Task Distribution:**
- **Pragati:** Chapters 1, 3, 5 (Introduction, System Design, Results)
- **Prajjwal:** Chapters 2, 4, 6 (Requirements, Implementation, Conclusion)
- **Both:** Abstract, Acknowledgements, References, Appendices

**Deliverables:**
- Complete project report (50-60 pages)
- Polished, documented codebase
- Presentation slides
- Final GitHub repository with complete history

**2.3.3 Development Practices and Tools**

**Version Control Workflow:**

**Branching Strategy:**
- `main` branch for stable, tested code
- `feature/*` branches for new features under development
- Merge to main only after testing and review

**Commit Practices:**
- Frequent commits with descriptive messages (format: "Add feature: description")
- Never commit sensitive data (keys, test credentials)
- `.gitignore` excludes temporary files, venv, __pycache__

**Collaboration:**
- Pull requests for significant changes (enables code review)
- Issues for tracking bugs and feature requests
- GitHub Projects board for task management (optional)

**Testing Strategy:**

**Unit Testing:**
- Each module includes independent test suite
- Python unittest framework (standard library)
- Test cases cover normal operation, edge cases, error conditions
- Run tests after each modification: `python -m unittest discover`

**Integration Testing:**
- End-to-end tests for complete workflows
- Test encrypt-decrypt cycles with various file types
- Verify integrity (SHA-256 hash comparison)
- Test error handling with invalid inputs

**Performance Testing:**
- Automated benchmark suite
- Multiple file sizes (1, 5, 10, 25, 50, 100 MB)
- Multiple iterations for statistical validity
- Results visualization

**Security Testing:**
- Tampered ciphertext rejection tests
- Nonce uniqueness verification
- Key independence validation
- Authentication failure handling

**Code Quality Practices:**

**Style Guidelines:**
- PEP 8 Python style guide compliance
- Consistent naming conventions (snake_case for functions/variables)
- Maximum line length: 100 characters
- Docstrings for all public functions (Google or NumPy style)

**Code Review:**
- Peer review between team members before merging
- Focus areas: security-critical sections, error handling, API design
- Checklist: functionality, readability, documentation, testing

**Documentation:**
- Inline comments for complex logic
- Module-level docstrings explaining purpose
- README with quick-start guide
- This comprehensive report

**2.3.4 Continuous Integration (Informal)**

While formal CI/CD pipelines (GitHub Actions, Travis CI) not implemented for this academic project, informal continuous integration practices adopted:

**Integration Frequency:**
- Code integrated to main branch at least weekly
- Both team members pull latest changes before starting new work
- Conflicts resolved promptly when they arise

**Automated Testing:**
- Test suites run before each commit
- Both members responsible for ensuring tests pass
- Broken tests fixed immediately (don't commit broken code)

**Build Validation:**
- Verify system runs on both team members' machines (Ubuntu + Windows)
- Check dependencies install correctly from requirements.txt
- Test CLI commands function as expected

**2.3.5 Outcome and Lessons Learned**

**Model Effectiveness:**

The iterative development model proved highly effective for this project:

✅ **Risk Mitigation:** Early module development identified library API nuances; adjustments made before extensive integration work

✅ **Incremental Progress:** Working system at each milestone provided confidence and motivation

✅ **Parallel Development:** Modular architecture enabled simultaneous work in Phase 2, reducing calendar time

✅ **Flexibility:** Could adjust priorities when challenges arose (e.g., spending more time on performance optimization after initial benchmarks)

✅ **Testing Integration:** Continuous testing throughout development caught errors early when fixes simpler

**Challenges Encountered:**

⚠️ **Schedule Pressure:** Final weeks (documentation phase) more time-intensive than anticipated; started report writing earlier would reduce stress

⚠️ **Dependency Updates:** PyNaCl minor version update mid-project required testing compatibility; version pinning mitigated risk but highlights dependency management importance

⚠️ **Testing Coverage:** Some edge cases discovered late; more comprehensive test case design upfront would catch issues earlier

**Lessons Learned:**

1. **Modular Design Essential:** Independent modules with clear interfaces dramatically simplified development and testing

2. **Library Reliance Beneficial:** Using established cryptographic libraries saved enormous time and reduced security risk compared to custom implementations

3. **Documentation Ongoing:** Writing documentation continuously (not deferring to end) produces better quality and reduces final phase workload

4. **Performance Testing Early:** Initial performance characterization (Phase 2) helped identify that no major optimization needed; earlier testing could have saved optimization time allocation

5. **Git Proficiency Valuable:** Strong version control skills prevented conflicts and enabled effective collaboration; time invested learning Git early in semester paid dividends

**Applicability to Future Projects:**

The iterative development approach with modular architecture suitable for similar projects:
- Medium complexity (not trivial, not enterprise-scale)
- Well-defined requirements with some flexibility
- Team size 2-4 members
- Timeline: 3-6 months
- Academic or research context

For larger teams or longer timelines, more formal agile practices (sprint planning, retrospectives) would be beneficial. For solo projects, simpler workflow sufficient.

---

# CHAPTER 3: SYSTEM DESIGN

## 3.1 Product Perspective

The hybrid encryption system exists as a standalone command-line application designed to operate independently without external service dependencies. This section positions the system within the broader context of file encryption tools and cryptographic software ecosystems.

**System Context and Positioning**

The system operates at the application layer, interfacing with:

**Operating System Layer:**
- **File System:** Read/write operations for accessing files, creating directories, managing paths
- **Entropy Source:** OS-provided secure random number generation (/dev/urandom on Linux, CryptGenRandom on Windows)
- **Process Management:** Memory allocation, process isolation, standard input/output streams
- **Security Features:** File permissions, access controls (inherited from OS)

**Runtime Environment:**
- **Python Interpreter:** Executes application code, manages memory, provides standard library
- **Virtual Environment:** Isolated Python package environment preventing system-wide conflicts
- **Shell/Terminal:** Command-line interface for user interaction

**External Libraries:**
- **PyCryptodome:** Provides AES algorithm implementation with multiple modes (GCM, CBC, CTR)
- **PyNaCl:** Wraps libsodium C library, provides XChaCha20-Poly1305 through SecretBox API
- **Matplotlib:** Generates performance visualization graphs (optional dependency)

**System Independence Characteristics**

Unlike cloud-based encryption services or networked key management systems, this system:

**Local Operation:**
- Processes all data on local machine without network transmission
- No external authentication servers or key management services
- No cloud storage integration or remote API calls
- Functions in air-gapped environments (offline operation)

**User Control:**
- Users maintain complete control over cryptographic material
- No third-party key escrow or recovery mechanisms
- Encrypted files stored locally under user's file system permissions
- No telemetry, analytics, or usage reporting

**No External Dependencies for Core Functionality:**
- Encryption/decryption operates without internet connectivity
- No licensing servers or activation mechanisms
- No mandatory updates or version checks
- Performance testing and visualization only components requiring matplotlib

**Relationship to Encryption Ecosystem**

**Position Among File Encryption Tools:**

```
┌─────────────────────────────────────────┐
│   Enterprise Solutions                   │
│   (Complex, PKI, Multi-user)            │
│   - Commercial encryption platforms      │
│   - Enterprise key management           │
└─────────────────┬───────────────────────┘
                  │
                  │ (More Complexity)
                  │
┌─────────────────▼───────────────────────┐
│   THIS SYSTEM                           │ ◄── Project Position
│   (Hybrid symmetric, CLI, Automated)    │
│   - Practical security                  │
│   - Operational resilience              │
└─────────────────┬───────────────────────┘
                  │
                  │ (Less Complexity)
                  │
┌─────────────────▼───────────────────────┐
│   Simple Tools                          │
│   (Single algorithm, Manual)            │
│   - Basic AES encryption utilities      │
│   - Simple XOR ciphers                  │
└─────────────────────────────────────────┘
```

The system occupies a middle ground:
- **More sophisticated** than simple single-algorithm utilities (dual-layer security, automated key management)
- **Less complex** than enterprise solutions (no PKI infrastructure, no multi-user coordination, no distributed key management)
- **Focuses on** practical individual/small team use cases with strong security properties

**Design Philosophy and Constraints**

**Minimalism:** Include only essential features; avoid feature bloat that increases attack surface and complexity

**Transparency:** Open-source implementation enables security auditing; no proprietary protocols or hidden functionality

**Standards-Based:** Use well-established algorithms (AES from NIST, ChaCha20 from IETF); avoid novel or experimental cryptography

**Library-Reliant:** Delegate cryptographic operations to audited, maintained libraries; never implement custom cryptographic primitives

**User-Centric:** Design for technical users (developers, administrators) who understand command-line interfaces but shouldn't need deep cryptographic expertise

**Future Integration Possibilities**

While currently standalone, the modular architecture supports potential future integration:

**Network Layer:** Could add socket-based file transfer (sender encrypts, receiver decrypts)

**GUI Wrapper:** Existing modules could be wrapped with graphical interface (PyQt, Tkinter) without changing core logic

**Cloud Integration:** Modules could be integrated with cloud storage APIs (encrypt before upload, decrypt after download)

**Automated Workflows:** CLI design enables integration into backup scripts, data pipelines, CI/CD systems

However, current scope deliberately limited to local encryption to maintain simplicity and security focus.

## 3.2 Product Functions

This section enumerates the major functions the system provides, describing inputs, processing logic, outputs, and relationships between functions.

**Function 1: Secure File Encryption (Hybrid Approach)**

**Function ID:** F1  
**Priority:** Critical (Core functionality)

**Description:** Encrypt files using two-layer hybrid approach combining AES-256-GCM for content and XChaCha20-Poly1305 for key protection.

**Input:**
- File path (string): Path to file requiring encryption
- Output directory (optional string): Destination for encrypted files (default: "encrypted")
- Confirmation flag (optional boolean): Skip user confirmation if set

**Processing Steps:**
1. **Validation:** Check file exists, is readable, size > 0 bytes
2. **Directory Creation:** Create output directory if not exists
3. **AES Key Generation:** Generate 256-bit random key using `os.urandom(32)`
4. **AES Nonce Generation:** Generate 128-bit random nonce using `os.urandom(16)`
5. **File Encryption:** Read file content, encrypt with AES-256-GCM, compute authentication tag
6. **Write Encrypted File:** Save nonce (16B) + tag (16B) + ciphertext to .enc file
7. **Master Key Generation:** Generate 256-bit XChaCha20 master key
8. **Key Encryption:** Encrypt AES key with XChaCha20-Poly1305 (automatically generates 192-bit nonce)
9. **Write Encrypted Key:** Save encrypted key package (72 bytes total) to .key file
10. **Metadata Creation:** Generate JSON with all decryption information
11. **Write Metadata:** Save JSON to .meta file
12. **Status Display:** Output success message with file locations

**Output:**
- Encrypted file (.enc): Original file size + 32 bytes (nonce + tag)
- Encrypted key file (.key): Fixed 72 bytes (nonce + encrypted key + tag)
- Metadata file (.meta): JSON with paths, master key, original filename, file size
- Console messages: Progress indicators and success confirmation

**Success Criteria:**
- All three files created successfully
- File permissions appropriate (readable by owner)
- Metadata JSON valid and parseable

**Error Conditions:**
- File not found → Display error, suggest checking path
- Permission denied → Display error, suggest checking permissions
- Insufficient disk space → Display error, suggest freeing space
- Encryption failure → Display error with library exception details

**Function 2: Secure File Decryption with Integrity Verification**

**Function ID:** F2  
**Priority:** Critical (Core functionality)

**Description:** Decrypt files using metadata reference, verifying authentication at both layers before outputting plaintext.

**Input:**
- Metadata file path (string): Path to .meta file from encryption operation
- Output directory (optional string): Destination for decrypted file (default: "decrypted")

**Processing Steps:**
1. **Load Metadata:** Read and parse JSON metadata file
2. **Validate Metadata:** Check required fields present (original_filename, encrypted_file, key_file, master_key)
3. **Load Encrypted Key:** Read 72-byte encrypted key file
4. **Extract Master Key:** Retrieve XChaCha20 master key from metadata (hex decode)
5. **Decrypt Key:** Use XChaCha20 master key to decrypt AES key
6. **Verify Key Tag:** Poly1305 authentication tag verification (constant-time comparison)
7. **Abort if Key Invalid:** If tag verification fails, display error and exit WITHOUT proceeding
8. **Load Encrypted File:** Read encrypted file (nonce + tag + ciphertext)
9. **Extract Components:** Separate nonce (16B), tag (16B), ciphertext (remainder)
10. **Decrypt File:** Use recovered AES key with extracted nonce to decrypt ciphertext
11. **Verify File Tag:** GCM authentication tag verification
12. **Abort if File Invalid:** If tag verification fails, display error and exit WITHOUT saving plaintext
13. **Write Decrypted File:** Only if both tags valid, save plaintext with original filename
14. **Status Display:** Output success message with file location

**Output:**
- Decrypted file: Exact copy of original (bitwise identical)
- Console messages: Progress indicators and success/failure notification

**Success Criteria:**
- Both authentication tags verify successfully
- Decrypted file matches original exactly (SHA-256 hash comparison in tests)
- Original filename restored

**Error Conditions:**
- Metadata not found → Display error, check file path
- Invalid JSON format → Display error, metadata may be corrupted
- Key authentication failure → Display "Key tampering detected", DO NOT output plaintext
- File authentication failure → Display "File tampering detected", DO NOT output plaintext
- Missing encrypted files → Display error with missing file path

**Critical Security Property:** Function NEVER outputs unauthenticated data. If either authentication tag fails, operation aborts immediately without creating output file.

**Function 3: Automated Cryptographic Key Generation**

**Function ID:** F3  
**Priority:** High (Security requirement)

**Description:** Generate cryptographically secure random keys without user intervention.

**Input:** None (automatic operation, no user-provided data)

**Processing:**
1. **Access OS RNG:** Use `os.urandom()` or Python `secrets` module
2. **Generate Random Bytes:** Request specified number of bytes (32 for 256-bit keys)
3. **Return Key Material:** Provide key as bytes object

**Output:**
- 256-bit (32-byte) random key with sufficient entropy
- No disk storage (key exists only in memory)

**Entropy Source:**
- Linux: /dev/urandom (draws from kernel entropy pool)
- Windows: CryptGenRandom (uses CSPRNG)
- macOS: /dev/urandom (similar to Linux)

**Security Properties:**
- Keys unpredictable (full 256-bit security)
- No patterns or correlations between generated keys
- Sufficient entropy even on systems with limited entropy sources (modern OS maintain entropy pools)

**Success Criteria:**
- Key generation completes without error
- Generated key has full 256-bit randomness

**Error Conditions:**
- OS RNG unavailable (should never occur on supported platforms)
- Insufficient entropy (extremely rare on modern systems; OS blocks until sufficient entropy available)

**Function 4: Metadata Management**

**Function ID:** F4  
**Priority:** High (Required for usability)

**Description:** Create, read, and validate metadata files containing decryption information.

**Subfunction 4a: Metadata Creation**

**Input:**
- Original filename
- Encrypted file path
- Encrypted key file path
- Master key (bytes)
- Original file size

**Processing:**
1. Create dictionary with required fields
2. Convert master key to hex string (for JSON compatibility)
3. Format as JSON with indentation (human-readable)
4. Write to file with .meta extension

**Output:**
- JSON metadata file

**Subfunction 4b: Metadata Loading**

**Input:**
- Metadata file path

**Processing:**
1. Read file contents
2. Parse JSON (validate syntax)
3. Validate required fields present
4. Validate master key is valid hex string (64 characters)
5. Return metadata dictionary

**Output:**
- Parsed metadata as Python dictionary

**Error Handling:**
- JSON parse error → Display "Invalid metadata format"
- Missing fields → Display "Incomplete metadata"
- Invalid hex encoding → Display "Corrupted master key"

**Function 5: Command-Line Interface Operations**

**Function ID:** F5  
**Priority:** Medium (Usability)

**Description:** Provide user-facing commands with argument parsing and validation.

**Subfunction 5a: Encrypt Command**

**Syntax:** `python cli.py encrypt -f FILE [-o OUTPUT] [-y] [-s]`

**Arguments:**
- `-f, --file` (required): File to encrypt
- `-o, --output` (optional): Output directory (default: "encrypted")
- `-y, --yes` (optional): Skip confirmation prompt
- `-s, --save-key` (optional): Save master key to separate backup file

**Processing:**
1. Parse command-line arguments
2. Validate file exists
3. Display file info (name, size)
4. Prompt for confirmation unless -y flag set
5. Call encryption function (F1)
6. Display results

**Subfunction 5b: Decrypt Command**

**Syntax:** `python cli.py decrypt -m METADATA [-o OUTPUT]`

**Arguments:**
- `-m, --metadata` (required): Metadata file path
- `-o, --output` (optional): Output directory (default: "decrypted")

**Processing:**
1. Parse arguments
2. Validate metadata file exists
3. Call decryption function (F2)
4. Display results

**Subfunction 5c: Info Command**

**Syntax:** `python cli.py info`

**Processing:**
1. Display system information banner
2. List encryption methods used
3. Explain key features
4. Show security benefits
5. Provide usage examples

**Output:** Formatted informational text to console

**Function 6: Performance Benchmarking**

**Function ID:** F6  
**Priority:** Low (Evaluation/Documentation)

**Description:** Measure encryption and decryption performance across various file sizes.

**Input:**
- List of file sizes to test (e.g., [1, 5, 10, 25, 50, 100] MB)

**Processing:**
1. For each file size:
   a. Generate test file with random data
   b. Measure encryption time (start to finish)
   c. Measure decryption time
   d. Calculate throughput (file_size / time)
   e. Verify integrity (compare hashes)
   f. Record results
2. Save results as JSON
3. Generate performance graphs (if matplotlib available)

**Output:**
- JSON file with performance data
- PNG graphs (6 visualizations)
- Console summary table

**Metrics Measured:**
- Encryption time (seconds)
- Decryption time (seconds)
- Throughput (MB/s)
- Total processing time
- Memory usage (if monitored)

**Function Relationships and Dependencies**

```
┌────────────────────────────────────────────┐
│         CLI Interface (F5)                 │
│  Entry point for all user interactions    │
└────────┬───────────────────────────────────┘
         │
         ├──────────► encrypt command
         │              │
         │              ▼
         │         ┌────────────────┐
         │         │  F1: Encrypt   │
         │         └───┬────────┬───┘
         │             │        │
         │             ▼        ▼
         │         ┌────┐    ┌────┐
         │         │ F3 │    │ F4 │
         │         │Key │    │Meta│
         │         │Gen │    │Mgmt│
         │         └────┘    └────┘
         │
         ├──────────► decrypt command
         │              │
         │              ▼
         │         ┌────────────────┐
         │         │  F2: Decrypt   │
         │         └───┬────────────┘
         │             │
         │             ▼
         │         ┌────────┐
         │         │   F4   │
         │         │  Meta  │
         │         │  Load  │
         │         └────────┘
         │
         └──────────► info command
                       │
                       ▼
                    (Display info)
```

**Summary of Product Functions:**

The system provides six major functions operating in coordinated fashion to deliver secure file encryption with usability and performance. Core functions (F1, F2) implement cryptographic operations; supporting functions (F3, F4, F5) provide automation, usability, and validation; evaluation function (F6) measures and documents performance characteristics.

## 3.3 User Characteristics

Understanding target users informs design decisions regarding interface complexity, automation level, documentation style, and feature priorities.

**Primary User Profile: Technical Professionals**

**Demographics:**
- **Roles:** Software developers, system administrators, DevOps engineers, security researchers, IT professionals
- **Education:** Bachelor's degree in computer science, information technology, or related technical field; or equivalent practical experience
- **Age Range:** 22-45 (typical for technical professional roles)
- **Geographic Distribution:** Global (cross-platform tool)

**Technical Proficiency:**
- **Command-Line Comfort:** High; daily use of terminal/shell for professional tasks
- **Programming Experience:** Familiar with at least one programming language; understands concepts like variables, functions, file I/O
- **File System Knowledge:** Understands directory structures, absolute/relative paths, file permissions
- **Security Awareness:** Basic understanding of encryption concepts (confidentiality, integrity, authentication); may not be cryptographic experts
- **Operating Systems:** Proficient in Linux, Windows, or macOS

**Behavioral Characteristics:**
- **Problem-Solving Approach:** Analytical; reads documentation; troubleshoots errors systematically
- **Tool Preferences:** Favors open-source tools for transparency and customization
- **Automation Mindset:** Seeks scriptable, automatable solutions for recurring tasks
- **Security Consciousness:** Prioritizes security over convenience; willing to invest time learning secure practices

**Usage Context:**
- **Frequency:** Varies from daily (developers encrypting sensitive code) to weekly (administrators encrypting backups)
- **File Types:** Source code, configuration files, databases, backups, personal documents, research data
- **File Sizes:** Typically 1MB-100MB; occasionally larger (multi-GB database backups)
- **Environment:** Often air-gapped or offline environments for security; sometimes in cloud/virtualized environments

**Needs and Expectations:**
- **Strong Security:** Prioritize cryptographic strength over ease of use
- **Transparency:** Desire to understand what tool does; open-source prerequisite
- **Automation:** Want key management automated (not manual key entry)
- **Reliability:** Expect 100% accuracy; any data corruption unacceptable
- **Performance:** Tolerate seconds for encryption but not minutes for moderate files
- **Documentation:** Need clear, technical documentation with examples
- **Integration:** Value tools that fit into existing workflows (scripts, pipelines)

**Limitations and Assumptions:**
- **Not Cryptographers:** Understand encryption benefits but may not know mathematical details
- **Technical Limitations:** May work on systems without admin privileges (can't install system-wide software)
- **Time Constraints:** Need quick setup; lengthy configuration unacceptable

**Secondary User Profile: Security-Conscious Individuals**

**Demographics:**
- **Roles:** Privacy activists, journalists, researchers, concerned citizens
- **Education:** Varies; may lack formal technical education but highly motivated to protect privacy
- **Technical Proficiency:** Moderate to low; can follow detailed instructions but uncomfortable with command-line

**Characteristics:**
- **Motivation:** Strong privacy concerns; may face threats (surveillance, censorship)
- **Security Priority:** Willing to accept complexity for security
- **Learning Curve:** Will invest time learning if convinced of security value
- **Tool Trust:** Seeks trustworthy tools; open-source important for auditability

**Usage Context:**
- **Frequency:** Occasional; encrypt sensitive documents before sharing
- **File Types:** Personal documents, communications, research materials
- **Environment:** Personal computers; may be in adversarial environments

**Current System Limitations:**
- **CLI Barrier:** Command-line interface challenging for non-technical users
- **Error Messages:** Technical error messages may be confusing

**Future Considerations:**
- GUI wrapper could broaden accessibility to this user group
- Enhanced documentation with step-by-step guides
- Video tutorials demonstrating common operations

**Tertiary User Profile: Students and Educators**

**Demographics:**
- **Roles:** Computer science students, cryptography course instructors, academic researchers
- **Education:** Undergraduate to graduate level in technical fields
- **Technical Proficiency:** Growing; learning programming and security concepts

**Characteristics:**
- **Learning Focus:** Interested in "how it works" more than just functionality
- **Experimentation:** May modify code, test edge cases, explore internals
- **Academic Use:** Course projects, research experiments, educational demonstrations

**Usage Context:**
- **Frequency:** Project-based; intensive use during semester, less frequent otherwise
- **File Types:** Test files, sample data, research datasets
- **Environment:** University labs, personal laptops

**Needs:**
- **Clear Code Structure:** Well-commented, readable code for learning
- **Educational Documentation:** Explanations of cryptographic concepts
- **Modular Design:** Ability to study and modify individual components
- **Performance Data:** Benchmarking results for comparison and analysis

**System Design Implications from User Characteristics:**

**For Primary Users (Technical Professionals):**
- ✅ Command-line interface appropriate (daily terminal users)
- ✅ Unix-style argument conventions (-f, --help) familiar
- ✅ Automated key management removes error-prone manual steps
- ✅ Open-source codebase enables security auditing
- ✅ Modular architecture supports integration into custom workflows

**For Secondary Users (Security-Conscious Individuals):**
- ⚠️ CLI may pose barrier; future GUI could improve accessibility
- ✅ Strong security properties address primary concern
- ✅ Open-source critical for trust
- ⚠️ Additional documentation (beginner-friendly guides) would help

**For Tertiary Users (Students/Educators):**
- ✅ Modular code structure facilitates learning
- ✅ Comprehensive documentation supports educational use
- ✅ Performance benchmarking provides data for analysis
- ✅ Well-commented code explains implementation decisions

**User Skill Requirements:**

**Minimum Skills (Required):**
- Basic command-line operation (cd, ls, running programs)
- Understanding of file paths
- Ability to install Python and packages (following instructions)
- Reading English-language documentation

**Recommended Skills (Beneficial):**
- Python programming (for code modification or integration)
- Basic cryptography concepts (encryption, keys, authentication)
- Git version control (for tracking changes if modifying code)
- JSON format familiarity (for understanding metadata)

**Accessibility Considerations:**

**Current System Assumes:**
- Visual ability (text-based interface)
- English language proficiency
- Basic computer literacy
- Access to supported operating system (Linux, Windows, macOS)

**Not Currently Supported:**
- Screen reader integration (CLI text-only may or may not work well with screen readers depending on implementation)
- Non-English languages (interface and documentation English-only)
- Graphical interface (excludes users uncomfortable with command-line)

**Future Accessibility Enhancements:**
- Internationalization (translate interface and docs)
- GUI wrapper (PyQt/Tkinter) for visual, mouse-driven interaction
- Enhanced error messages with recovery suggestions
- Video tutorials demonstrating common tasks

## 3.4 Constraints

Constraints define boundaries and limitations affecting system design, implementation, and deployment. Understanding constraints ensures realistic expectations and appropriate design decisions.

**3.4.1 Technical Constraints**

**TC1: Python Runtime Dependency**

**Description:** System requires Python 3.8+ interpreter for execution

**Implications:**
- Users must install Python (not universally present on all systems)
- Performance limited by Python's interpreted nature (slower than compiled languages like C/C++ or Rust)
- Memory management handled by Python garbage collector (less control than manual memory management)
- Cannot easily distribute as standalone executable (requires Python runtime or bundling with tools like PyInstaller)

**Mitigation:**
- Python widely available across platforms (free download)
- Performance adequate for target use cases (see benchmarking results)
- Clear installation documentation provided

**TC2: Cryptographic Library Dependencies**

**Description:** System depends on external libraries (PyCryptodome, PyNaCl) for cryptographic operations

**Implications:**
- Cannot modify underlying algorithm implementations
- Dependent on library maintainers for security updates
- Potential compatibility issues with future library versions
- Must trust library implementations (though widely audited)

**Mitigation:**
- Version pinning in requirements.txt ensures reproducibility
- Libraries actively maintained with strong security track records
- Alternative: reimplementing cryptography inadvisable (error-prone, time-intensive)

**TC3: Operating System Dependencies**

**Description:** System relies on OS-provided services (file I/O, random number generation)

**Implications:**
- Random number quality depends on OS entropy source
- File I/O performance varies across file systems (ext4, NTFS, APFS)
- Path handling must accommodate different OS conventions (/ vs \)
- System calls may have platform-specific behaviors

**Mitigation:**
- Use Python's cross-platform abstractions (`os.path`, `pathlib`)
- Modern operating systems provide high-quality entropy sources
- Testing on multiple platforms validates cross-platform compatibility

**TC4: Memory Constraints**

**Description:** System must operate within available RAM

**Implications:**
- Cannot load arbitrarily large files entirely into memory
- Python interpreter and libraries have base memory footprint (~50-100MB)
- Large-scale batch operations limited by available RAM

**Mitigation:**
- Streaming implementation for files prevents proportional memory growth
- Chunk-based processing enables handling files larger than RAM
- System tested with files up to 100MB; larger files supported through streaming

**TC5: No Hardware Security Module (HSM) Support**

**Description:** Keys generated and processed in software only; no integration with dedicated crypto hardware

**Implications:**
- Keys present in process memory during operations (vulnerable to memory dumps, rootkit attacks)
- No secure key storage in tamper-resistant hardware
- Cannot leverage HSM performance acceleration or key isolation

**Justification:**
- HSM integration adds significant complexity
- Academic project scope manageable without HSM
- Software-only approach more accessible (no specialized hardware required)

**Future Enhancement:** HSM support could be added through PKCS#11 interface in future versions

**3.4.2 Design Constraints**

**DC1: Command-Line Interface Only**

**Description:** No graphical user interface provided in current version

**Implications:**
- Excludes users uncomfortable with terminal/command-line
- Text-based feedback only (no visual progress bars, icons, dialogs)
- Requires users to navigate file systems via paths rather than file browsers

**Justification:**
- CLI faster to develop than GUI (time constraint)
- Target users (technical professionals) comfortable with CLI
- CLI more scriptable and automatable than GUI
- Future GUI wrapper possible without changing core modules

**DC2: Local Operation Only**

**Description:** No network file transfer capabilities; encryption and decryption occur on local machine

**Implications:**
- Users must manually transfer encrypted files if sharing (email, cloud upload, USB drive)
- No client-server architecture or peer-to-peer transfer
- Cannot encrypt files remotely or decrypt on different machine without file transfer

**Justification:**
- Network code adds complexity and attack surface
- Local-only design simpler and more secure (no network vulnerabilities)
- Users can combine with existing file transfer tools (scp, rsync, cloud sync)
- Future enhancement possible (socket-based transfer) without core redesign

**DC3: Metadata Storage Requirement**

**Description:** Decryption requires metadata file; loss of metadata prevents decryption

**Implications:**
- Users must protect metadata files (contain master key)
- No key recovery mechanism if metadata lost
- Three files per encryption (file, key, metadata) instead of one

**Justification:**
- Metadata simplifies decryption (no manual key entry)
- JSON format human-readable for inspection
- Users can backup metadata separately or encrypt metadata itself for additional security

**Risk Mitigation:** Documentation emphasizes metadata protection; optional -s flag saves master key to separate backup file

**DC4: Single-User Design**

**Description:** No multi-user access control, shared key management, or collaborative features

**Implications:**
- Each encryption operation generates unique keys (no key sharing between users)
- No user authentication or authorization
- No audit logs or access tracking

**Justification:**
- Academic project scope; multi-user features add significant complexity
- Target use case: individual file encryption, not enterprise document management
- Future enhancement possible (integrate with key management systems)

**3.4.3 Security Constraints**

**SC1: Key Storage in Metadata**

**Description:** XChaCha20 master key stored in metadata file for user convenience

**Implications:**
- Metadata file must be protected (contains key needed for decryption)
- Compromise of metadata enables key recovery and subsequent file decryption
- No separation between "what you have" (encrypted file) and "what you know" (key)

**Risk Assessment:** Moderate risk; mitigated by:
- File system permissions (only owner can read)
- Users can encrypt metadata itself for additional layer
- Users can delete metadata after securely transmitting master key through separate channel

**Alternative Designs Considered:**
- **Password-based key derivation:** Users enter password to derive master key (increases usability burden, weak passwords vulnerable)
- **Separate key file encryption:** Store master key in HSM or secure enclave (requires specialized hardware)

**Current Design Justification:** Balances security and usability for target users (technical professionals who understand need to protect metadata)

**SC2: No Forward Secrecy**

**Description:** All information needed for decryption present in metadata; past encryptions remain decryptable indefinitely

**Implications:**
- If metadata compromised at any time, all past and future encryptions using that key vulnerable
- No automatic key rotation or expiration
- Long-lived keys may accumulate risk over time

**Mitigation:**
- Users should encrypt new files with new keys (system does this automatically for each file)
- Metadata can be deleted after secure key exchange if forward secrecy desired
- Future enhancement: Implement key rotation policies

**SC3: Trust in Cryptographic Libraries**

**Description:** Security depends on correctness of PyCryptodome and PyNaCl implementations

**Implications:**
- Vulnerabilities in libraries affect this system
- Must rely on library maintainers for security patches
- Cannot guarantee security beyond what libraries provide

**Mitigation:**
- Both libraries widely used, regularly audited, and actively maintained
- Vulnerabilities typically patched quickly
- Version pinning allows controlled updates after security review
- Open-source nature enables independent security audits

**SC4: No Post-Quantum Resistance**

**Description:** AES-256 and XChaCha20 vulnerable to quantum attacks (Grover's algorithm)

**Implications:**
- Future quantum computers could reduce effective security from 256 bits to 128 bits (still considered adequate, but reduced margin)
- Long-term confidentiality (30+ years) may be at risk from "harvest now, decrypt later" attacks

**Assessment:**
- 128-bit security adequate for most practical purposes
- Large-scale quantum computers not expected for 10-20+ years
- Post-quantum algorithms not yet standardized (NIST PQC competition ongoing)

**Future Enhancement:** Could integrate post-quantum algorithms (Kyber for key encapsulation, AES remains quantum-resistant at 256-bit level with Grover's algorithm) when standards mature

**3.4.4 Operational Constraints**

**OC1: Installation Requirements**

**Description:** Users must install Python and dependencies before first use

**Implications:**
- Barrier to entry (not double-click executable)
- Requires internet connection for `pip install` (initial setup)
- Corporate/institutional environments may restrict software installation

**Mitigation:**
- Clear installation documentation with step-by-step instructions
- Virtual environments isolate dependencies (don't affect system Python)
- Portable Python distributions available for restricted environments

**OC2: Documentation Language**

**Description:** All documentation, error messages, and interface text in English

**Implications:**
- Excludes non-English speakers
- May limit adoption in non-English-speaking regions

**Future Enhancement:** Internationalization (i18n) support could be added using gettext or similar framework

**OC3: No Customer Support Infrastructure**

**Description:** Academic project without ongoing support, helpdesk, or professional support contracts

**Implications:**
- Users must troubleshoot issues independently
- No guaranteed response to questions or bug reports
- No service-level agreements (SLAs) or uptime guarantees

**Mitigation:**
- Comprehensive documentation reduces support needs
- Open-source nature enables community support
- GitHub Issues provides platform for community problem-solving

**OC4: Performance Limitations**

**Description:** Python implementation slower than compiled alternatives; no GPU acceleration

**Implications:**
- Throughput limited compared to hand-optimized C implementations
- Large file operations may require patience on slow hardware
- No SIMD vectorization or GPU offloading for parallel processing

**Measured Performance:**
- Encryption: ~87 MB/s (acceptable for most use cases)
- Decryption: ~92 MB/s (similar to encryption)
- For comparison: Specialized tools can achieve 1-5 GB/s with hardware acceleration and optimized code

**Assessment:** Performance adequate for target use cases (documents, source code, moderate databases); users needing multi-GB/s throughput should use specialized tools

**3.4.5 Regulatory and Compliance Constraints**

**RC1: Export Control Considerations**

**Description:** Cryptographic software subject to various national export controls

**Implications:**
- Distribution across international borders may require notifications or approvals
- Different countries have varying regulations on encryption strength
- Academic/educational use generally exempt but varies by jurisdiction

**Current Status:**
- Project uses publicly available, widely-deployed algorithms (AES, ChaCha20)
- Open-source educational project generally falls under exemptions
- U.S. Export Administration Regulations (EAR) allow publicly available cryptographic software with notification

**Compliance Approach:**
- No commercial distribution planned (academic project)
- If publishing on GitHub: Public domain software generally exempt
- Users responsible for compliance in their jurisdictions

**RC2: No FIPS 140-2 Validation**

**Description:** Implementation not formally validated by accredited testing laboratory

**Implications:**
- Cannot be used in U.S. federal government contexts requiring FIPS 140-2 validated modules
- Some industries (healthcare, finance) may require FIPS validation for regulated data
- Algorithms comply with FIPS specifications but implementation not certified

**Justification:**
- FIPS validation costs $50,000-$200,000 (prohibitive for academic project)
- Libraries used (PyCryptodome, libsodium) available in FIPS-validated forms separately
- Academic/research use doesn't require validation

**Alternative:** Organizations requiring FIPS compliance can use validated libraries directly or employ validated commercial solutions

**3.4.6 Time and Resource Constraints**

**TRC1: Development Timeline**

**Description:** Academic semester provides fixed development period (~16 weeks)

**Implications:**
- Features must fit within available timeline
- Some desirable features deferred to maintain schedule
- Testing depth limited by time available

**Impact on Design:**
- CLI chosen over GUI (faster development)
- Network features deferred (would require additional 3-4 weeks)
- Focus on core functionality rather than extensive feature set

**TRC2: Team Size**

**Description:** Two-person development team limits parallelization and specialization

**Implications:**
- Limited person-hours for development, testing, documentation
- Cannot simultaneously develop multiple complex features
- Testing coverage constrained by available effort

**Mitigation:**
- Modular architecture enables parallel work on independent modules
- Iterative approach allows focusing on priorities first
- Comprehensive test cases prioritized over exhaustive testing

**TRC3: Testing Resources**

**Description:** Limited hardware for testing across platforms and configurations

**Implications:**
- Cannot test on all possible OS versions, Python versions, hardware configurations
- Performance testing limited to team members' hardware
- No formal security audit or penetration testing budget

**Testing Approach:**
- Focus on primary platforms (Ubuntu 22.04, Windows 11)
- Test with Python 3.10 (other versions expected compatible but not exhaustively tested)
- Use automated unit and integration tests to maximize coverage with available resources

**Constraint Summary Table**

| Category | Constraint | Impact | Mitigation |
|----------|------------|--------|------------|
| Technical | Python dependency | Performance, distribution | Adequate for use case |
| Technical | Library dependencies | Update vulnerability | Version pinning |
| Design | CLI only | User accessibility | Future GUI possible |
| Design | Local operation | No network transfer | Combine with transfer tools |
| Security | Metadata storage | Key protection burden | User responsibility, docs |
| Security | No post-quantum | Long-term vulnerability | Future enhancement |
| Operational | Installation required | Setup complexity | Clear documentation |
| Operational | Performance limits | Slower than C/Rust | Acceptable for target files |
| Regulatory | No FIPS validation | Gov/enterprise limits | Algorithms comply with specs |
| Resource | Time constraint | Feature scope | Focus on core functionality |

**Overall Impact of Constraints:**

Constraints guided design toward:
- **Simplicity:** CLI over GUI, local over networked, automated over manual
- **Security:** Library-based over custom crypto, authenticated encryption mandatory
- **Feasibility:** Features achievable within time/resource limits
- **Extensibility:** Modular design enables future enhancements beyond initial scope

Constraints represent realistic boundaries for academic project; system delivers functional, secure file encryption within defined limitations.

## 3.5 Use Case Model / Flow Charts / DFDs

This section provides visual representations of system functionality through use case diagrams, flowcharts, and data flow diagrams.

**3.5.1 Use Case Diagram**

The following diagram illustrates actors and their interactions with the system:

```
                    ┌─────────────────────┐
                    │                     │
         ┌──────────┤   File Encryption   │◄─────────┐
         │          │      System         │          │
         │          │                     │          │
         │          └─────────────────────┘          │
         │                                           │
    ┌────▼────┐                                 ┌────▼────┐
    │  User   │                                 │   OS    │
    │(Primary)│                                 │ (Actor) │
    └────┬────┘                                 └────┬────┘
         │                                           │
         │    ┌──────────────────────────────┐      │
         ├───►│ UC1: Encrypt File            │      │
         │    │ - Provide file path          │      │
         │    │ - System encrypts with hybrid│      │
         │    │ - Receive encrypted outputs  │      │
         │    └──────────────────────────────┘      │
         │                                           │
         │    ┌──────────────────────────────┐      │
         ├───►│ UC2: Decrypt File            │      │
         │    │ - Provide metadata path      │      │
         │    │ - System verifies & decrypts │      │
         │    │ - Receive original file      │      │
         │    └──────────────────────────────┘      │
         │                                           │
         │    ┌──────────────────────────────┐      │
         ├───►│ UC3: View System Info        │      │
         │    │ - Request information        │      │
         │    │ - Display algorithms, features│     │
         │    └──────────────────────────────┘      │
         │                                           │
         │    ┌──────────────────────────────┐      │
         └───►│ UC4: Benchmark Performance   │      │
              │ - Specify file sizes         │      │
              │ - System measures performance│◄─────┘
              │ - Generate graphs & reports  │ (provides entropy,
              └──────────────────────────────┘  file system access)
```

**Actors:**

1. **User (Primary Actor):** Technical professional initiating encryption/decryption operations
2. **Operating System (Secondary Actor):** Provides file system access, random number generation, process management

**Use Cases:**

**UC1: Encrypt File**
- **Goal:** Encrypt a file using hybrid AES + XChaCha20 approach
- **Preconditions:** User has file to encrypt, system installed and configured
- **Postconditions:** Three files created (.enc, .key, .meta); original file unchanged
- **Main Success Scenario:**
  1. User executes encrypt command with file path
  2. System validates file exists and is readable
  3. System generates AES key and encrypts file
  4. System generates XChaCha20 key and encrypts AES key
  5. System creates metadata with all necessary information
  6. System saves encrypted file, encrypted key, and metadata
  7. System displays success message with file locations
- **Extensions (Error Flows):**
  - 2a. File not found → Display error, suggest checking path, exit
  - 2b. File not readable → Display permission error, exit
  - 3a. Encryption fails → Display library error, exit
  - 6a. Cannot write output → Display disk space/permission error, exit

**UC2: Decrypt File**
- **Goal:** Decrypt a file using metadata reference
- **Preconditions:** User has metadata file from previous encryption
- **Postconditions:** Original file restored; integrity verified
- **Main Success Scenario:**
  1. User executes decrypt command with metadata path
  2. System loads and validates metadata
  3. System loads encrypted key and decrypts using master key from metadata
  4. System verifies key authentication tag (Poly1305)
  5. System loads encrypted file and decrypts using recovered AES key
  6. System verifies file authentication tag (GCM)
  7. System saves decrypted file with original name
  8. System displays success message
- **Extensions (Error Flows):**
  - 2a. Metadata not found → Display error, exit
  - 2b. Invalid JSON format → Display "corrupted metadata" error, exit
  - 4a. Key authentication fails → Display "key tampered" error, DO NOT output plaintext, exit
  - 6a. File authentication fails → Display "file tampered" error, DO NOT output plaintext, exit

**UC3: View System Information**
- **Goal:** Learn about system capabilities and usage
- **Preconditions:** System installed
- **Postconditions:** User informed about algorithms, features, usage
- **Main Success Scenario:**
  1. User executes info command
  2. System displays banner with project information
  3. System lists encryption methods (AES-256-GCM, XChaCha20-Poly1305)
  4. System describes key features (256-bit keys, 192-bit nonces, authentication)
  5. System explains security benefits
  6. System provides usage examples

**UC4: Benchmark Performance**
- **Goal:** Measure and visualize system performance
- **Preconditions:** System installed, matplotlib available (optional)
- **Postconditions:** Performance data recorded, graphs generated
- **Main Success Scenario:**
  1. User executes performance test script
  2. System confirms test parameters (file sizes, iterations)
  3. For each file size:
     a. System generates test file
     b. System measures encryption time
     c. System measures decryption time
     d. System verifies integrity
  4. System saves results as JSON
  5. System generates visualization graphs (if matplotlib available)
  6. System displays summary table

**3.5.2 Encryption Process Flowchart**

```
              START
                │
                ▼
     ┌──────────────────────┐
     │ User: Provide File   │
     │   Path via CLI       │
     └──────────┬───────────┘
                │
                ▼
       ┌────────────────┐
       │ Validate File  │
       │ Exists?        │
       └───┬────────┬───┘
           │        │
          NO       YES
           │        │
           ▼        ▼
    ┌──────────┐  ┌──────────────────────┐
    │  Error:  │  │ Generate Random      │
    │   File   │  │ 256-bit AES Key      │
    │Not Found │  │ (os.urandom(32))     │
    └────┬─────┘  └──────────┬───────────┘
         │                   │
         ▼                   ▼
       EXIT         ┌──────────────────────┐
                    │ Generate Random      │
                    │ 128-bit Nonce        │
                    │ (os.urandom(16))     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Encrypt File with    │
                    │ AES-256-GCM          │
                    │ cipher.encrypt_and_  │
                    │ digest(plaintext)    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Write Encrypted File │
                    │ Format: nonce + tag  │
                    │ + ciphertext         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Generate Random      │
                    │ 256-bit Master Key   │
                    │ for XChaCha20        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Encrypt AES Key      │
                    │ with XChaCha20       │
                    │ (auto 192-bit nonce) │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Write Encrypted Key  │
                    │ (72 bytes fixed)     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Create Metadata JSON │
                    │ - Original filename  │
                    │ - File paths         │
                    │ - Master key (hex)   │
                    │ - File size          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Write Metadata File  │
                    │ (.meta extension)    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Display Success      │
                    │ Message with File    │
                    │ Locations            │
                    └──────────┬───────────┘
                               │
                               ▼
                             EXIT
```

**3.5.3 Decryption Process Flowchart**

```
              START
                │
                ▼
     ┌──────────────────────┐
     │ User: Provide        │
     │ Metadata File Path   │
     └──────────┬───────────┘
                │
                ▼
       ┌────────────────┐
       │ Metadata File  │
       │ Exists?        │
       └───┬────────┬───┘
           │        │
          NO       YES
           │        │
           ▼        ▼
    ┌──────────┐  ┌──────────────────────┐
    │  Error:  │  │ Load & Parse         │
    │Metadata  │  │ Metadata JSON        │
    │Not Found │  └──────────┬───────────┘
    └────┬─────┘             │
         │                   ▼
         ▼            ┌────────────────┐
       EXIT           │ Valid JSON?    │
                      └───┬────────┬───┘
                          │        │
                         NO       YES
                          │        │
                          ▼        ▼
                   ┌──────────┐  ┌──────────────────────┐
                   │  Error:  │  │ Extract Master Key   │
                   │ Invalid  │  │ from Metadata        │
                   │Metadata  │  │ (hex decode)         │
                   └────┬─────┘  └──────────┬───────────┘
                        │                   │
                        ▼                   ▼
                      EXIT         ┌──────────────────────┐
                                   │ Load Encrypted Key   │
                                   │ File (.key)          │
                                   └──────────┬───────────┘
                                              │
                                              ▼
                                   ┌──────────────────────┐
                                   │ Decrypt AES Key      │
                                   │ with XChaCha20       │
                                   │ using Master Key     │
                                   └──────────┬───────────┘
                                              │
                                              ▼
                                   ┌────────────────┐
                                   │ Verify Poly1305│
                                   │ Tag Valid?     │
                                   └───┬────────┬───┘
                                       │        │
                                      NO       YES
                                       │        │
                                       ▼        ▼
                                ┌──────────┐  ┌──────────────────────┐
                                │  Error:  │  │ Load Encrypted File  │
                                │   Key    │  │ Extract: nonce, tag, │
                                │Tampered  │  │ ciphertext           │
                                └────┬─────┘  └──────────┬───────────┘
                                     │                   │
                                     ▼                   ▼
                                   EXIT         ┌──────────────────────┐
                                                │ Decrypt File with    │
                                                │ AES-GCM using        │
                                                │ Recovered Key        │
                                                └──────────┬───────────┘
                                                           │
                                                           ▼
                                                ┌────────────────┐
                                                │ Verify GCM     │
                                                │ Tag Valid?     │
                                                └───┬────────┬───┘
                                                    │        │
                                                   NO       YES
                                                    │        │
                                                    ▼        ▼
                                             ┌──────────┐  ┌──────────────────────┐
                                             │  Error:  │  │ Write Decrypted File │
                                             │   File   │  │ with Original Name   │
                                             │Tampered  │  └──────────┬───────────┘
                                             └────┬─────┘             │
                                                  │                   ▼
                                                  ▼            ┌──────────────────────┐
                                                EXIT           │ Display Success      │
                                                               │ Message              │
                                                               └──────────┬───────────┘
                                                                          │
                                                                          ▼
                                                                        EXIT
```

**Critical Security Decision Points:**
- **Poly1305 Tag Verification:** If key authentication fails, abort immediately without attempting file decryption
- **GCM Tag Verification:** If file authentication fails, abort without writing any plaintext output
- Both checks ensure NO unauthenticated data ever reaches user

**3.5.4 Data Flow Diagram - Level 0 (Context Diagram)**

```
                    ┌───────────────┐
                    │               │
                    │     USER      │
                    │               │
                    └───────┬───────┘
                            │
              ┌─────────────┼─────────────┐
              │             │             │
      filename│    metadata │    command  │
              │             │             │
              ▼             ▼             ▼
    ┌─────────────────────────────────────────┐
    │                                         │
    │     HYBRID FILE ENCRYPTION SYSTEM       │
    │                                         │
    │  • Encrypts files (AES + XChaCha20)    │
    │  • Decrypts files (with verification)   │
    │  • Manages keys automatically           │
    │                                         │
    └──────────┬──────────────────────┬───────┘
               │                      │
               │ encrypted files      │ status messages
               │ + metadata           │ + decrypted files
               ▼                      ▼
    ┌──────────────────┐    ┌──────────────────┐
    │                  │    │                  │
    │   FILE SYSTEM    │    │     CONSOLE      │
    │                  │    │    (stdout)      │
    │  Stores .enc,    │    │  Displays user   │
    │  .key, .meta     │    │   messages       │
    │                  │    │                  │
    └──────────────────┘    └──────────────────┘
```

**External Entities:**
- **User:** Provides commands, file paths; receives feedback
- **File System:** Stores encrypted/decrypted files, metadata
- **Console:** Displays status messages, errors, information

**Data Flows:**
1. User → System: Commands (encrypt/decrypt), file paths
2. System → File System: Write encrypted files, keys, metadata
3. File System → System: Read files for encryption/decryption
4. System → Console: Status messages, errors, results

**3.5.5 Data Flow Diagram - Level 1 (Detailed Process View)**

```
┌──────────┐
│   USER   │
└─────┬────┘
      │
      │ (1) file path + command
      │
      ▼
┌─────────────────────────────────────────┐
│  1.0                                    │
│  COMMAND LINE INTERFACE                 │
│  - Parse arguments                      │
│  - Validate inputs                      │
│  - Route to appropriate process         │
└──────┬──────────────────────┬───────────┘
       │                      │
       │ (2) encrypt request  │ (3) decrypt request
       │                      │
       ▼                      ▼
┌──────────────────┐   ┌──────────────────┐
│  2.0             │   │  3.0             │
│  HYBRID          │   │  HYBRID          │
│  ENCRYPTION      │   │  DECRYPTION      │
│  CONTROLLER      │   │  CONTROLLER      │
└───┬──────────┬───┘   └───┬──────────┬───┘
    │          │           │          │
    │(4) file  │(5) AES    │(6) load  │(7) decrypt
    │content   │key        │enc key   │AES key
    │          │           │          │
    ▼          ▼           ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│  2.1   │ │  2.2   │ │  3.1   │ │  3.2   │
│  AES   │ │XChaCha │ │XChaCha │ │  AES   │
│ Encrypt│ │  Key   │ │  Key   │ │Decrypt │
│ Module │ │ Encrypt│ │ Decrypt│ │ Module │
└────┬───┘ └───┬────┘ └───┬────┘ └────┬───┘
     │         │          │         │
     │(8) enc  │(9) enc   │(10) AES │(11) plain
     │file     │key       │key      │text
     │         │          │         │
     └────┬────┴─────┬────┴────┬────┘
          │          │         │
          ▼          ▼         ▼
     ┌────────────────────────────┐
     │  4.0                       │
     │  FILE SYSTEM INTERFACE     │
     │  - Write encrypted files   │
     │  - Write metadata          │
     │  - Read files for decrypt  │
     └──────────┬─────────────────┘
                │
                │ (12) files written/read
                │
                ▼
         ┌──────────────┐
         │ FILE SYSTEM  │
         │  (Storage)   │
         └──────────────┘
```

**Data Stores:**
- **D1: Encrypted Files (.enc)** - Stores AES-encrypted file content
- **D2: Encrypted Keys (.key)** - Stores XChaCha20-encrypted AES keys
- **D3: Metadata (.meta)** - Stores JSON with decryption information

**Processes:**
- **1.0 CLI Interface:** Parses user commands, validates inputs
- **2.0 Hybrid Encryption Controller:** Orchestrates encryption workflow
- **2.1 AES Encrypt Module:** Encrypts file content
- **2.2 XChaCha20 Key Encrypt:** Encrypts AES keys
- **3.0 Hybrid Decryption Controller:** Orchestrates decryption workflow
- **3.1 XChaCha20 Key Decrypt:** Decrypts AES keys
- **3.2 AES Decrypt Module:** Decrypts file content
- **4.0 File System Interface:** Handles file I/O operations

**Data Flows (Numbered):**
1. User provides file path and command
2. CLI routes encryption request to controller
3. CLI routes decryption request to controller
4. Controller sends file content to AES module
5. Controller sends AES key to XChaCha20 module
6. Controller loads encrypted key for decryption
7. Controller sends encrypted key to XChaCha20 for decryption
8. AES module returns encrypted file
9. XChaCha20 module returns encrypted key
10. XChaCha20 module returns decrypted AES key
11. AES module returns plaintext
12. File system interface writes/reads files

## 3.6 Database Design

**Note:** This system does not employ a traditional database management system (DBMS) such as MySQL, PostgreSQL, or MongoDB. All persistent data storage implemented through file system with structured file formats.

**Rationale for File-Based Storage:**

1. **Simplicity:** No database server installation, configuration, or maintenance required
2. **Portability:** Encrypted files and metadata easily transferred between systems via any file transfer method
3. **Self-Contained:** Each encryption operation produces standalone artifacts requiring no central database
4. **User Control:** Users directly manage files using familiar file system tools (ls, cp, mv, backup utilities)
5. **No Query Requirements:** System doesn't need complex queries, joins, or transactions; simple file read/write sufficient

**File-Based Storage Architecture:**

**Primary Storage Elements:**

1. **Encrypted Files (.enc)**
   - Purpose: Store AES-GCM encrypted file content
   - Format: Binary (nonce + tag + ciphertext)
   - Size: Original file size + 32 bytes overhead
   - Location: User-specified directory (default: encrypted/)

2. **Encrypted Key Files (.key)**
   - Purpose: Store XChaCha20-Poly1305 encrypted AES keys
   - Format: Binary (nonce + encrypted key + tag)
   - Size: Fixed 72 bytes
   - Location: Same directory as encrypted file

3. **Metadata Files (.meta)**
   - Purpose: Store decryption information in human-readable format
   - Format: JSON (UTF-8 encoded text)
   - Size: ~200-500 bytes (depends on path lengths)
   - Location: Same directory as encrypted file

**Alternative Approaches Considered:**

**SQLite Database:**
- **Advantages:** Structured queries, ACID transactions, single-file database
- **Disadvantages:** Additional dependency, unnecessary complexity for simple key-value storage, less portable than plain files
- **Decision:** Rejected; file-based approach simpler for this use case

**NoSQL Document Store (MongoDB, CouchDB):**
- **Advantages:** Schema flexibility, JSON-native
- **Disadvantages:** Requires server process, overkill for local file encryption
- **Decision:** Rejected; too heavy for requirements

**Key-Value Store (Redis, LevelDB):**
- **Advantages:** Fast lookups, simple API
- **Disadvantages:** Another process/dependency, data not human-readable
- **Decision:** Rejected; plain JSON files sufficient

**File Organization Strategy:**

```
project_root/
├── encrypted/                    # Default output for encryption
│   ├── document.pdf.enc          # Encrypted file content
│   ├── document.pdf.key          # Encrypted AES key
│   ├── document.pdf.meta         # Metadata JSON
│   ├── image.jpg.enc
│   ├── image.jpg.key
│   └── image.jpg.meta
├── decrypted/                    # Default output for decryption
│   ├── document.pdf              # Restored original files
│   └── image.jpg
└── results/                      # Performance test results
    ├── performance_results_20241101_143052.json
    └── graphs/
        ├── encryption_time.png
        ├── decryption_time.png
        └── throughput.png
```

**File Naming Conventions:**
- **Encrypted file:** `{original_filename}.enc`
- **Encrypted key:** `{original_filename}.key`
- **Metadata:** `{original_filename}.meta`
- **Decrypted file:** `{original_filename}` (original name restored)

**Advantages of This Approach:**
- Users can see all related files together (same directory, same base name)
- File extensions clearly indicate file type
- Easy to back up (copy entire directory)
- Simple to clean up (delete all files with same base name)
- No database corruption risks

## 3.7 Table Structure

While no relational database exists, metadata files contain structured data analogous to database records. This section documents the "schema" of these structures.

**Metadata File Structure (JSON Format)**

The metadata file serves as a "record" containing all information needed for decryption.

```json
{
  "original_filename": "document.pdf",
  "encrypted_file": "encrypted/document.pdf.enc",
  "key_file": "encrypted/document.pdf.key",
  "master_key": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
  "file_size": 1048576,
  "timestamp": "2024-11-01T14:30:00Z",
  "version": "1.0"
}
```

**Field Specifications:**

| Field Name | Data Type | Length/Format | Required | Description |
|------------|-----------|---------------|----------|-------------|
| original_filename | String | Variable | Yes | Original file name before encryption |
| encrypted_file | String (path) | Variable | Yes | Relative or absolute path to .enc file |
| key_file | String (path) | Variable | Yes | Relative or absolute path to .key file |
| master_key | String (hex) | 64 characters | Yes | Hex-encoded 256-bit XChaCha20 master key |
| file_size | Integer | Positive | Yes | Original file size in bytes |
| timestamp | String (ISO 8601) | Variable | No | Encryption operation timestamp |
| version | String | Semantic version | No | Metadata format version (future compatibility) |

**Field Constraints and Validation:**

**original_filename:**
- Must be non-empty string
- Should be valid filename for target OS
- May contain Unicode characters (UTF-8 encoding)
- Example: `"report_2024.pdf"`, `"数据.txt"` (Chinese characters)

**encrypted_file:**
- Must be valid file path (relative or absolute)
- File must exist at specified location
- Should end with .enc extension (by convention)
- Example: `"encrypted/document.pdf.enc"`, `"/home/user/secure/file.enc"`

**key_file:**
- Must be valid file path
- File must exist and be exactly 72 bytes
- Should end with .key extension
- Example: `"encrypted/document.pdf.key"`

**master_key:**
- Must be exactly 64 hexadecimal characters (0-9, a-f)
- Represents 256-bit (32-byte) key
- Case-insensitive but lowercase preferred
- Example: `"3a7b9f2c1e5d8a6f4c2b9e7d3f5a8c1b2e4d6a8c9f1b3e5d7a9c2f4e6a8b0d1f3"`
- Validation regex: `^[0-9a-fA-F]{64}

**file_size:**
- Must be positive integer (> 0)
- Represents bytes
- Used for validation and informational purposes
- Example: `1048576` (1 MB), `52428800` (50 MB)

**timestamp (optional):**
- ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`
- UTC timezone preferred
- Used for auditing, not security-critical
- Example: `"2024-11-01T14:30:00Z"`

**version (optional):**
- Semantic versioning: `MAJOR.MINOR.PATCH`
- Current version: `"1.0"`
- Enables future format compatibility checking
- Example: `"1.0"`, `"1.1"`

**Encrypted File Structure (.enc - Binary Format)**

Not a "table" but structured binary format:

```
┌─────────────────────────────────────────────┐
│ Byte Offset │ Content          │ Size       │
├─────────────────────────────────────────────┤
│ 0-15        │ AES-GCM Nonce    │ 16 bytes   │
│ 16-31       │ Authentication   │ 16 bytes   │
│             │ Tag (GCM)        │            │
│ 32-EOF      │ Encrypted Content│ Variable   │
└─────────────────────────────────────────────┘
Total Size: Original File Size + 32 bytes
```

**Field Specifications:**

| Field | Type | Size | Description |
|-------|------|------|-------------|
| Nonce | Binary | 16 bytes | Random nonce for AES-GCM (must be unique per encryption) |
| Tag | Binary | 16 bytes | GCM authentication tag computed over ciphertext |
| Ciphertext | Binary | Variable | AES-256 encrypted file content (same size as plaintext) |

**Encrypted Key Structure (.key - Binary Format)**

Fixed-size binary format produced by XChaCha20-Poly1305:

```
┌─────────────────────────────────────────────┐
│ Byte Offset │ Content          │ Size       │
├─────────────────────────────────────────────┤
│ 0-23        │ XChaCha20 Nonce  │ 24 bytes   │
│ 24-55       │ Encrypted AES Key│ 32 bytes   │
│ 56-71       │ Authentication   │ 16 bytes   │
│             │ Tag (Poly1305)   │            │
└─────────────────────────────────────────────┘
Total Size: Fixed 72 bytes
```

**Field Specifications:**

| Field | Type | Size | Description |
|-------|------|------|-------------|
| Nonce | Binary | 24 bytes | Random nonce for XChaCha20 (192 bits) |
| Encrypted Key | Binary | 32 bytes | XChaCha20-encrypted AES key |
| Tag | Binary | 16 bytes | Poly1305 authentication tag |

**Performance Results Structure (JSON Format)**

Performance testing generates structured results:

```json
{
  "test_date": "2024-11-01 14:30:00",
  "results": [
    {
      "file_size_mb": 10,
      "encryption_time": 0.115,
      "encryption_throughput": 87.0,
      "decryption_time": 0.109,
      "decryption_throughput": 91.7,
      "total_time": 0.224,
      "integrity_verified": true
    }
  ]
}
```

**Field Specifications:**

| Field | Type | Description | Units |
|-------|------|-------------|-------|
| test_date | String | Timestamp of test execution | ISO format |
| results | Array | List of test results for different file sizes | - |
| file_size_mb | Float | File size tested | Megabytes |
| encryption_time | Float | Time to encrypt | Seconds |
| encryption_throughput | Float | Encryption speed | MB/s |
| decryption_time | Float | Time to decrypt | Seconds |
| decryption_throughput | Float | Decryption speed | MB/s |
| total_time | Float | Combined encrypt + decrypt time | Seconds |
| integrity_verified | Boolean | SHA-256 hash match confirmed | true/false |

**Data Integrity and Validation**

**Metadata Validation Process:**
1. Parse JSON (validate syntax)
2. Check all required fields present
3. Validate master_key is 64-character hex string
4. Validate file_size is positive integer
5. Validate paths point to existing files (during decryption)
6. Validate timestamp format if present (optional field)

**Example Validation Code:**
```python
def validate_metadata(metadata):
    required_fields = [
        'original_filename', 
        'encrypted_file', 
        'key_file', 
        'master_key', 
        'file_size'
    ]
    
    # Check required fields exist
    for field in required_fields:
        if field not in metadata:
            raise ValueError(f"Missing required field: {field}")
    
    # Validate master_key format
    if not re.match:
        raise ValueError("Invalid master_key format")
    
    # Validate file_size
    if not isinstance(metadata['file_size'], int) or metadata['file_size'] <= 0:
        raise ValueError("Invalid file_size")
    
    return True
```

**Error Handling:**
- **Invalid JSON:** `json.JSONDecodeError` → "Corrupted metadata file"
- **Missing fields:** `KeyError` → "Incomplete metadata"
- **Invalid hex:** `ValueError` → "Invalid master key format"
- **File not found:** `FileNotFoundError` → "Encrypted file missing"

## 3.8 ER Diagrams

Traditional Entity-Relationship diagrams model relational database structures. Since this system uses file-based storage, we present a **File Relationship Diagram** showing how files relate conceptually.

**File Entity-Relationship Model**

```
┌─────────────────────────┐
│   ORIGINAL FILE         │
│   (Entity)              │
│                         │
│ Attributes:             │
│ • filename (PK)         │
│ • content (binary)      │
│ • size (bytes)          │
│ • type (extension)      │
└────────────┬────────────┘
             │
             │ (1:1)
             │ "encrypts to"
             │
             ▼
┌─────────────────────────┐
│   ENCRYPTED FILE        │
│   (.enc file)           │
│                         │
│ Attributes:             │
│ • filepath (PK)         │
│ • nonce (16 bytes)      │
│ • auth_tag (16 bytes)   │
│ • ciphertext (binary)   │
└────────────┬────────────┘
             │
             │ (1:1)
             │ "protected by"
             │
             ▼
┌─────────────────────────┐
│   AES KEY               │
│   (Ephemeral Entity)    │
│                         │
│ Attributes:             │
│ • key_value (32 bytes)  │
│ • algorithm (AES-256)   │
│ • lifetime (in-memory)  │
└────────────┬────────────┘
             │
             │ (1:1)
             │ "encrypted to"
             │
             ▼
┌─────────────────────────┐
│   ENCRYPTED KEY         │
│   (.key file)           │
│                         │
│ Attributes:             │
│ • filepath (PK)         │
│ • nonce (24 bytes)      │
│ • enc_key (32 bytes)    │
│ • auth_tag (16 bytes)   │
│ • size (fixed: 72 bytes)│
└────────────┬────────────┘
             │
             │ (1:1)
             │ "protected by"
             │
             ▼
┌─────────────────────────┐
│   MASTER KEY            │
│   (Stored in Metadata)  │
│                         │
│ Attributes:             │
│ • key_value (32 bytes)  │
│ • algorithm (XChaCha20) │
│ • format (hex string)   │
└────────────┬────────────┘
             │
             │ (1:1)
             │ "stored in"
             │
             ▼
┌─────────────────────────┐
│   METADATA              │
│   (.meta file)          │
│                         │
│ Attributes:             │
│ • filepath (PK)         │
│ • original_filename     │
│ • encrypted_file_path   │
│ • key_file_path         │
│ • master_key (hex)      │
│ • file_size             │
│ • timestamp (optional)  │
│ • version (optional)    │
└─────────────────────────┘
```

**Relationships:**

1. **ORIGINAL_FILE → ENCRYPTED_FILE (1:1)**
   - **Relationship:** "encrypts to"
   - **Cardinality:** One-to-one (one original produces one encrypted file)
   - **Referential Integrity:** Encrypted file references original via metadata
   - **Cascade:** If original deleted, encrypted file becomes orphaned (decryption still possible with metadata)

2. **ENCRYPTED_FILE → AES_KEY (1:1)**
   - **Relationship:** "protected by"
   - **Cardinality:** One-to-one (each encrypted file has unique AES key)
   - **Referential Integrity:** Key never reused across encryptions
   - **Lifecycle:** Key exists only in memory during operation

3. **AES_KEY → ENCRYPTED_KEY (1:1)**
   - **Relationship:** "encrypted to"
   - **Cardinality:** One-to-one (AES key encrypted before storage)
   - **Referential Integrity:** Encrypted key file contains complete key package
   - **Storage:** Persistent (saved to disk as .key file)

4. **ENCRYPTED_KEY → MASTER_KEY (1:1)**
   - **Relationship:** "protected by"
   - **Cardinality:** One-to-one (each encrypted key has unique master key)
   - **Referential Integrity:** Master key specific to this encryption operation
   - **Storage:** Stored in metadata (not separate file)

5. **MASTER_KEY → METADATA (1:1)**
   - **Relationship:** "stored in"
   - **Cardinality:** One-to-one (master key embedded in metadata)
   - **Format:** Hex-encoded string (64 characters)
   - **Purpose:** Enables decryption without separate key management

6. **METADATA → ENCRYPTED_FILE + ENCRYPTED_KEY (1:2)**
   - **Relationship:** "references"
   - **Cardinality:** One-to-many (metadata references both file and key)
   - **Referential Integrity:** Paths stored in metadata must point to existing files
   - **Purpose:** Central index tying all components together

**Dependency Graph for Decryption:**

```
To Successfully Decrypt:

        ┌─────────────┐
        │  METADATA   │ (Required: contains master_key)
        │   (.meta)   │
        └──────┬──────┘
               │
     ┌─────────┴─────────┐
     │                   │
     ▼                   ▼
┌────────────┐    ┌──────────────┐
│ENCRYPTED   │    │  ENCRYPTED   │
│   KEY      │    │    FILE      │
│  (.key)    │    │   (.enc)     │
└─────┬──────┘    └──────┬───────┘
      │                  │
      │ decrypt with     │ decrypt with
      │ master_key       │ recovered AES key
      │                  │
      ▼                  │
┌────────────┐           │
│  AES KEY   │───────────┘
│(in memory) │
└────────────┘
      │
      ▼
┌──────────────┐
│  PLAINTEXT   │
│   (output)   │
└──────────────┘
```

**File Lifecycle Diagram:**

```
ENCRYPTION LIFECYCLE:

[Original File] ──┐
                  │
                  ├──► [Read Content]
                  │           │
                  │           ▼
                  │    [Generate AES Key]
                  │           │
                  │           ▼
                  │    [Encrypt with AES]
                  │           │
                  │           ▼
                  │    [Write .enc file]
                  │           │
                  │           ├──► [Encrypted File Created]
                  │           │
                  │           ▼
                  │    [Generate Master Key]
                  │           │
                  │           ▼
                  │    [Encrypt AES Key]
                  │           │
                  │           ▼
                  │    [Write .key file]
                  │           │
                  │           ├──► [Encrypted Key Created]
                  │           │
                  │           ▼
                  │    [Create Metadata]
                  │           │
                  │           ▼
                  │    [Write .meta file]
                  │           │
                  │           ├──► [Metadata Created]
                  │           │
                  └───────────┴──► [Original File Unchanged]


DECRYPTION LIFECYCLE:

[Metadata File] ──┐
                  │
                  ├──► [Parse JSON]
                  │           │
                  │           ▼
                  │    [Extract Master Key]
                  │           │
                  │           ▼
                  │    [Load .key file]
                  │           │
                  │           ▼
                  │    [Decrypt AES Key]
                  │           │
                  │           ├──► [Verify Poly1305 Tag] ──NO──► [Abort]
                  │           │              │
                  │           │             YES
                  │           │              │
                  │           ▼              │
                  │    [Load .enc file]◄─────┘
                  │           │
                  │           ▼
                  │    [Decrypt Content]
                  │           │
                  │           ├──► [Verify GCM Tag] ──NO──► [Abort]
                  │           │              │
                  │           │             YES
                  │           │              │
                  │           ▼              │
                  │    [Write Plaintext]◄────┘
                  │           │
                  └───────────┴──► [Original File Restored]
```

**Referential Integrity Constraints:**

Since no database enforces referential integrity, application logic must ensure:

1. **Metadata → Encrypted File:** Path in metadata must point to existing .enc file
2. **Metadata → Encrypted Key:** Path in metadata must point to existing .key file
3. **Filename Consistency:** All three files (.enc, .key, .meta) should share same base name
4. **Key File Size:** .key file must be exactly 72 bytes (corrupted if different size)
5. **Metadata Completeness:** All required fields must be present and valid

**Validation performed during decryption:**
```python
def validate_decryption_files(metadata):
    # Check encrypted file exists
    if not os.path.exists(metadata['encrypted_file']):
        raise FileNotFoundError("Encrypted file not found")
    
    # Check key file exists and correct size
    if not os.path.exists(metadata['key_file']):
        raise FileNotFoundError("Key file not found")
    
    key_size = os.path.getsize(metadata['key_file'])
    if key_size != 72:
        raise ValueError(f"Invalid key file size: {key_size} (expected 72)")
    
    return True
```

## 3.9 Assumptions and Dependencies

This section documents assumptions underlying system design and external dependencies that must be satisfied for correct operation.

**3.9.1 Assumptions**

**A1: Operating System Provides Secure Randomness**

**Assumption:** `os.urandom()` or Python `secrets` module provides cryptographically secure random bytes with sufficient entropy.

**Justification:**
- Modern operating systems maintain entropy pools seeded from hardware sources (keyboard/mouse timing, disk I/O timing, hardware RNGs)
- Linux: /dev/urandom draws from kernel entropy pool (CSPRNG)
- Windows: CryptGenRandom uses Windows Cryptographic API
- macOS: Similar to Linux (/dev/urandom)

**Risk if Violated:**
- Predictable keys enable brute-force attacks
- Nonce collisions compromise GCM security
- Complete system security failure

**Mitigation:**
- Use only on supported, modern operating systems (Linux 3.17+, Windows 7+, macOS 10.12+)
- Avoid virtualized environments with poor entropy (check /proc/sys/kernel/random/entropy_avail on Linux)
- Never use `random` module (pseudo-random, not cryptographically secure)

**A2: System Clock Reasonably Accurate**

**Assumption:** System time approximately correct (within hours/days, not years)

**Scope:** Applies only to optional timestamp field in metadata; not security-critical

**Risk if Violated:** Misleading timestamps in metadata; no security impact

**A3: File System Integrity**

**Assumption:** File system correctly stores and retrieves data without corruption

**Justification:** Modern file systems (ext4, NTFS, APFS) designed for data integrity with journaling, checksums

**Risk if Violated:**
- File corruption could cause decryption failures
- Authentication tags detect tampering/corruption (system rejects corrupted data)
- No silent corruption (fails safely)

**Mitigation:**
- Users should employ file system integrity features (ZFS checksums, RAID, backups)
- Authentication tags provide cryptographic integrity verification

**A4: User Has Appropriate File System Permissions**

**Assumption:** User can read source files, write to output directories

**Justification:** System checks permissions and reports errors

**Risk if Violated:** Operations fail with clear error messages (permission denied); no security impact

**A5: Python Interpreter Trustworthy**

**Assumption:** Python runtime not compromised or backdoored

**Justification:** Users install Python from official sources (python.org, OS repositories)

**Risk if Violated:** Compromised runtime could leak keys, modify cryptographic operations; applies to ALL Python software

**Mitigation:**
- Install Python from official sources only
- Verify download signatures/checksums
- Keep Python updated with security patches

**A6: Cryptographic Libraries Correctly Implemented**

**Assumption:** PyCryptodome and PyNaCl provide secure, correct implementations of AES and XChaCha20

**Justification:**
- Both libraries widely used in production systems
- Regular security audits and peer review
- Active maintenance with prompt security updates
- Open-source nature enables independent verification

**Risk if Violated:** Algorithmic vulnerabilities; affects all users of these libraries

**Mitigation:**
- Monitor library security advisories
- Update dependencies when security patches released
- Use specific versions (pinning) to avoid unexpected breaking changes

**A7: Adequate Disk Space Available**

**Assumption:** Sufficient disk space for encrypted files (approximately same size as originals)

**Justification:** System can check available space before operations; OS reports errors if exhausted

**Risk if Violated:** Partial file writes; operations fail with error messages

**Mitigation:**
- Check disk space before operations
- Use temporary files, rename on success (atomic operations)
- Clean up temporary files on failure

**A8: No Active Adversary on Local System**

**Assumption:** Local system not compromised by malware, rootkits, or other attackers with system-level access

**Justification:** If local system compromised, attacker can:
- Read keys from memory during operations
- Modify code or libraries
- Install keyloggers
- Access plaintext files before encryption
- No software-only solution can protect against compromised OS

**Scope:** System protects data at rest (encrypted files) and in transit (if transferred); cannot protect against active attacks on local system

**User Responsibility:** Maintain secure, updated system with antivirus, firewalls, and good security practices

**3.9.2 External Dependencies**

**Software Dependencies:**

**D1: Python Runtime (Version 3.8+)**

**Dependency Type:** Critical (system cannot function without Python)

**Version Requirements:**
- Minimum: Python 3.8 (first version with required features)
- Recommended: Python 3.10+ (tested, stable)
- Maximum tested: Python 3.11 (future versions expected compatible)

**Purpose:** Execute application code, provide standard library

**Availability:** Free download from python.org or OS package managers

**Installation:**
```bash
# Ubuntu/Debian
sudo apt install python3.10

# Windows
# Download installer from python.org

# macOS
brew install python@3.10
```

**Risk:** Python interpreter vulnerabilities affect system

**Mitigation:** Keep Python updated with security patches

**D2: PyCryptodome Library (Version 3.19.0)**

**Dependency Type:** Critical (provides AES implementation)

**Purpose:** AES-256-GCM encryption and decryption

**License:** BSD 2-Clause (permissive open-source)

**Installation:** `pip install pycryptodome==3.19.0`

**Version Pinning Rationale:**
- Ensures reproducibility
- Prevents breaking API changes
- Allows controlled updates after security review

**Sub-Dependencies:**
- C compiler (optional, for performance acceleration)
- Python development headers (for C extension build)

**Alternative:** Falls back to pure Python if C compilation unavailable (slower but functional)

**D3: PyNaCl Library (Version 1.5.0)**

**Dependency Type:** Critical (provides XChaCha20 implementation)

**Purpose:** XChaCha20-Poly1305 authenticated encryption

**License:** Apache 2.0 (permissive open-source)

**Installation:** `pip install PyNaCl==1.5.0`

**Sub-Dependencies:**
- libsodium (C library, automatically bundled with PyNaCl)
- cffi (Python C Foreign Function Interface)

**Advantage:** libsodium widely audited, high-performance C implementation

**D4: Matplotlib Library (Version 3.7.1)**

**Dependency Type:** Optional (only for performance visualization)

**Purpose:** Generate performance graphs (PNG images)

**Installation:** `pip install matplotlib==3.7.1`

**System Works Without:** Core encryption/decryption functions unaffected if matplotlib unavailable

**Sub-Dependencies:**
- NumPy (numerical computing library)
- Various image backends (Pillow, etc.)

**When Required:** Only when running `visualize_results.py` for graph generation

**Operating System Dependencies:**

**D5: Secure Random Number Generator**

**Dependency Type:** Critical (security foundation)

**OS Implementations:**
- **Linux:** /dev/urandom (kernel CSPRNG)
- **Windows:** CryptGenRandom (Windows Crypto API)
- **macOS:** /dev/urandom (similar to Linux)

**Accessed Via:** Python `os.urandom()` or `secrets` module

**Requirement:** Modern OS with properly seeded entropy pool

**Minimum OS Versions:**
- Linux: Kernel 3.17+ (improved /dev/urandom)
- Windows: Windows 7+ (CryptGenRandom available)
- macOS: 10.12+ (Sierra and later)

**D6: File System**

**Dependency Type:** Critical (data persistence)

**Requirements:**
- Support for binary file I/O
- Directory creation and traversal
- File permissions (read/write/execute)

**Compatible File Systems:**
- ext4, ext3, XFS, Btrfs (Linux)
- NTFS, FAT32 (Windows)
- APFS, HFS+ (macOS)

**Features Used:**
- Sequential file read/write
- Random access (for streaming large files)
- Atomic file operations (write to temporary, rename to final)

**D7: Command-Line Shell**

**Dependency Type:** Required (user interaction)

**Compatible Shells:**
- bash, zsh, fish (Linux/macOS)
- cmd.exe, PowerShell (Windows)
- Any terminal emulator with text I/O

**Requirements:**
- Text input/output streams (stdin, stdout, stderr)
- Process execution
- Environment variables
- Exit codes

**Development Tool Dependencies (Not Required for Users):**

**D8: Git (Version 2.0+)**

**Dependency Type:** Development only

**Purpose:** Version control, collaboration

**Users Don't Need:** Git not required to run encryption system

**D9: VS Code / Text Editor**

**Dependency Type:** Development only

**Purpose:** Code editing

**Users Don't Need:** No IDE required to use system

**Dependency Management Strategy:**

**Version Pinning:**
- `requirements.txt` specifies exact versions
- Prevents breaking changes from unexpected updates
- Enables reproducible installations

**Virtual Environments:**
- Isolate project dependencies from system Python
- Prevent conflicts with other Python projects
- Enable side-by-side installations of different versions

**Update Policy:**
- Monitor security advisories for dependencies
- Update to patched versions when vulnerabilities discovered
- Test thoroughly before updating version pins
- Document breaking changes in release notes

**Dependency Risks and Mitigations:**

| Risk | Impact | Mitigation |
|------|--------|------------|
| Library vulnerability | Security compromise | Monitor advisories, update promptly |
| Breaking API change | System fails | Version pinning, controlled updates |
| Dependency unavailable | Cannot install | Mirror dependencies, bundle if needed |
| Incompatible versions | Import errors | Specify exact versions in requirements.txt |
| Supply chain attack | Malicious code | Verify package signatures, use trusted repositories |

**Dependency Tree:**

```
hybrid-encryption-system
├── Python 3.8+ (required)
│   └── Standard Library
├── PyCryptodome 3.19.0 (required)
│   └── [Optional: C compiler for acceleration]
├── PyNaCl 1.5.0 (required)
│   ├── cffi (auto-installed)
│   └── libsodium (bundled)
└── Matplotlib 3.7.1 (optional)
    ├── NumPy (auto-installed)
    └── Pillow (auto-installed)
```

**Installation Verification:**

```bash
# Verify all dependencies installed correctly
python -c "import Crypto; import nacl; print('✓ Core dependencies installed')"
python -c "import matplotlib; print('✓ Optional dependencies installed')"
```

**Contingency Plans:**

**If PyCryptodome unavailable:** Cannot proceed; AES implementation critical

**If PyNaCl unavailable:** Cannot proceed; XChaCha20 implementation critical

**If Matplotlib unavailable:** Performance testing still works; graphs not generated (acceptable degradation)

## 3.10 Specific Requirements

This section provides detailed, testable requirements organized by category.

**3.10.1 Functional Requirements (Detailed Specifications)**

**FR-AES-001: AES Key Generation**
- **Requirement:** System shall generate 256-bit AES keys using cryptographically secure random number generator
- **Input:** None (automatic)
- **Output:** 32-byte random key
- **Source:** `os.urandom(32)` or `secrets.token_bytes(32)`
- **Test:** Generate 1000 keys, verify all 32 bytes, verify all unique
- **Priority:** Critical

**FR-AES-002: AES File Encryption**
- **Requirement:** System shall encrypt files using AES-256 in GCM mode
- **Input:** File path, 32-byte key
- **Processing:** Generate 16-byte nonce, encrypt with AES-GCM, compute 16-byte tag
- **Output:** Encrypted file (nonce + tag + ciphertext)
- **Test:** Encrypt known plaintext, verify ciphertext different, verify tag computed
- **Priority:** Critical

**FR-AES-003: AES File Decryption**
- **Requirement:** System shall decrypt AES-GCM encrypted files with authentication
- **Input:** Encrypted file, 32-byte key
- **Processing:** Extract nonce and tag, decrypt ciphertext, verify tag
- **Output:** Original plaintext if tag valid; error if tag invalid
- **Test:** Decrypt and verify matches original; tamper with tag, verify rejection
- **Priority:** Critical

**FR-XC-001: XChaCha20 Master Key Generation**
- **Requirement:** System shall generate 256-bit XChaCha20 master keys
- **Input:** None (automatic)
- **Output:** 32-byte random key
- **Source:** `nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)`
- **Test:** Generate 1000 keys, verify all 32 bytes, verify all unique
- **Priority:** Critical

**FR-XC-002: XChaCha20 Key Encryption**
- **Requirement:** System shall encrypt AES keys using XChaCha20-Poly1305
- **Input:** 32-byte AES key, 32-byte master key
- **Processing:** Generate 24-byte nonce, encrypt with XChaCha20, compute 16-byte Poly1305 tag
- **Output:** 72-byte encrypted key package
- **Test:** Encrypt key, verify output 72 bytes, verify nonce 24 bytes
- **Priority:** Critical

**FR-XC-003: XChaCha20 Key Decryption**
- **Requirement:** System shall decrypt encrypted keys with authentication
- **Input:** 72-byte encrypted key package, 32-byte master key
- **Processing:** Decrypt using master key, verify Poly1305 tag
- **Output:** Original 32-byte AES key if tag valid; error if invalid
- **Test:** Decrypt and verify matches original; tamper with tag, verify rejection
- **Priority:** Critical

**FR-META-001: Metadata Creation**
- **Requirement:** System shall create JSON metadata with required fields
- **Fields:** original_filename, encrypted_file, key_file, master_key (hex), file_size
- **Format:** Valid JSON with UTF-8 encoding, 2-space indentation
- **Output:** .meta file
- **Test:** Create metadata, parse JSON, verify all fields present and valid
- **Priority:** High

**FR-META-002: Metadata Validation**
- **Requirement:** System shall validate metadata before decryption
- **Checks:** Valid JSON syntax, required fields present, master_key valid hex (64 chars), file_size positive integer
- **Output:** Boolean (valid/invalid) with error message if invalid
- **Test:** Valid metadata passes; missing field fails; invalid hex fails
- **Priority:** High

**FR-CLI-001: Encrypt Command**
- **Requirement:** CLI shall parse encrypt command with arguments
- **Syntax:** `cli.py encrypt -f FILE [-o OUTPUT] [-y] [-s]`
- **Validation:** File exists, output directory writable
- **Output:** Success message with file locations or error message
- **Test:** Valid file encrypts; non-existent file shows error
- **Priority:** Medium

**FR-CLI-002: Decrypt Command**
- **Requirement:** CLI shall parse decrypt command with arguments
- **Syntax:** `cli.py decrypt -m METADATA [-o OUTPUT]`
- **Validation:** Metadata file exists, valid JSON
- **Output:** Success message with decrypted file location or error
- **Test:** Valid metadata decrypts; invalid metadata shows error
- **Priority:** Medium

**FR-CLI-003: Info Command**
- **Requirement:** CLI shall display system information
- **Syntax:** `cli.py info`
- **Output:** Formatted text with algorithms, features, examples
- **Test:** Execute command, verify output contains expected information
- **Priority:** Low

**3.10.2 Performance Requirements (Quantified)**

**PR-001: Encryption Throughput**
- **Requirement:** Encryption throughput shall exceed 50 MB/s on standard hardware
- **Test Hardware:** Intel Core i5 / AMD Ryzen 5, 8GB RAM, SSD
- **Measurement:** Average throughput for 10MB, 50MB, 100MB files
- **Acceptance:** 90% of test runs meet threshold
- **Priority:** Medium

**PR-002: Decryption Throughput**
- **Requirement:** Decryption throughput shall exceed 50 MB/s
- **Measurement:** Same as PR-001
- **Rationale:** Symmetric operations should have similar performance
- **Priority:** Medium