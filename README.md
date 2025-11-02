# Secure File Transfer using AES and XChaCha20

A hybrid encryption framework for secure file transfer combining AES-256 and XChaCha20 algorithms.

## Team Members
- Pragati Raj (22BECCS28)
- Prajjwal Gupta (22BECCS29)

## Project Guide
Mr. Gaurav Thakur, Assistant Professor  
Department of Computer Science & Engineering  
Central University of Jammu

## Features
- AES-256-GCM for file encryption
- XChaCha20-Poly1305 for key encryption
- Hybrid encryption model addressing nonce reuse vulnerabilities

## Installation
bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/secure-file-transfer-aes-xchacha20.git
cd secure-file-transfer-aes-xchacha20

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt


## Usage

### Encrypt a File
bash
python src/cli.py encrypt -f document.pdf


### Decrypt a File
bash
python src/cli.py decrypt -m encrypted/document.pdf.meta


### Show System Information
bash
python src/cli.py info


## Project Structure

├── src/
│   ├── aes_encryption.py       # AES-256 encryption module
│   ├── xchacha20_encryption.py # XChaCha20 key encryption
│   ├── hybrid_encryption.py    # Hybrid system integration
│   └── cli.py                  # Command-line interface
├── docs/                        # Documentation
├── tests/                       # Test files
├── requirements.txt             # Python dependencies
└── README.md                    # This file


## Testing
All modules include built-in tests:
bash
python src/aes_encryption.py
python src/xchacha20_encryption.py
python src/hybrid_encryption.py
