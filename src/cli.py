"""
Command Line Interface for Hybrid Encryption System
Provides user-friendly interface for encrypting and decrypting files
"""

import argparse
import os
import sys
from hybrid_encryption import HybridEncryption

def print_banner():
    """Print application banner"""
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║        SECURE FILE TRANSFER SYSTEM                        ║
    ║        AES-256 + XChaCha20 Hybrid Encryption            ║
    ║                                                           ║
    ║        Central University of Jammu                        ║
    ║        B.Tech CSE (Cyber Security)                        ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """
    print(banner)

def encrypt_command(args):
    """Handle encryption command"""
    input_file = args.file
    output_dir = args.output if args.output else "encrypted"
    
    # Check if file exists
    if not os.path.exists(input_file):
        print(f"✗ Error: File '{input_file}' not found!")
        sys.exit(1)
    
    # Check file size
    file_size = os.path.getsize(input_file)
    print(f"\nFile: {input_file}")
    print(f"Size: {file_size:,} bytes ({file_size / (1024*1024):.2f} MB)")
    
    # Confirm encryption
    if not args.yes:
        confirm = input("\nProceed with encryption? (y/n): ")
        if confirm.lower() != 'y':
            print("Encryption cancelled.")
            sys.exit(0)
    
    # Encrypt
    hybrid = HybridEncryption()
    result = hybrid.encrypt_file(input_file, output_dir)
    
    if result:
        print("\n✓ SUCCESS! File encrypted successfully.")
        print(f"\nTo decrypt this file, use:")
        print(f"  python cli.py decrypt -m {result['metadata_file']}")
        
        if args.save_key:
            key_backup = f"{input_file}.masterkey"
            with open(key_backup, 'w') as f:
                f.write(result['master_key'].hex())
            print(f"\n⚠ Master key saved to: {key_backup}")
            print("  Keep this file SECURE! You need it for decryption.")
    else:
        print("\n✗ FAILED! Encryption failed.")
        sys.exit(1)

def decrypt_command(args):
    """Handle decryption command"""
    metadata_file = args.metadata
    output_dir = args.output if args.output else "decrypted"
    
    # Check if metadata file exists
    if not os.path.exists(metadata_file):
        print(f"✗ Error: Metadata file '{metadata_file}' not found!")
        sys.exit(1)
    
    # Decrypt
    hybrid = HybridEncryption()
    decrypted_file = hybrid.decrypt_file(metadata_file, output_dir)
    
    if decrypted_file:
        print("\n✓ SUCCESS! File decrypted successfully.")
        print(f"\nDecrypted file: {decrypted_file}")
    else:
        print("\n✗ FAILED! Decryption failed.")
        sys.exit(1)

def info_command(args):
    """Display information about the system"""
    print("\n" + "="*60)
    print("HYBRID ENCRYPTION SYSTEM INFORMATION")
    print("="*60)
    print("\nEncryption Methods:")
    print("  • File Content:  AES-256-GCM")
    print("  • Key Protection: XChaCha20-Poly1305")
    print("\nKey Features:")
    print("  • 256-bit encryption keys")
    print("  • 192-bit nonce for XChaCha20 (prevents nonce reuse)")
    print("  • Authenticated encryption (integrity protection)")
    print("  • Two-layer security model")
    print("\nSecurity Benefits:")
    print("  • Addresses AES-GCM nonce reuse vulnerabilities")
    print("  • Hardware acceleration for AES (when available)")
    print("  • Software-optimized XChaCha20 for key protection")
    print("  • Algorithm diversity (defense in depth)")
    print("="*60 + "\n")

def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description='Hybrid Encryption System (AES-256 + XChaCha20)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Encrypt a file:
    python cli.py encrypt -f document.pdf
    
  Encrypt with custom output directory:
    python cli.py encrypt -f document.pdf -o my_encrypted_files
    
  Decrypt a file:
    python cli.py decrypt -m encrypted/document.pdf.meta
    
  Show system information:
    python cli.py info
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Encrypt command
    encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt a file')
    encrypt_parser.add_argument('-f', '--file', required=True, help='File to encrypt')
    encrypt_parser.add_argument('-o', '--output', help='Output directory (default: encrypted)')
    encrypt_parser.add_argument('-y', '--yes', action='store_true', help='Skip confirmation')
    encrypt_parser.add_argument('-s', '--save-key', action='store_true', 
                               help='Save master key to file (for backup)')
    
    # Decrypt command
    decrypt_parser = subparsers.add_parser('decrypt', help='Decrypt a file')
    decrypt_parser.add_argument('-m', '--metadata', required=True, 
                               help='Metadata file (.meta)')
    decrypt_parser.add_argument('-o', '--output', help='Output directory (default: decrypted)')
    
    # Info command
    info_parser = subparsers.add_parser('info', help='Show system information')
    
    args = parser.parse_args()
    
    # Print banner
    print_banner()
    
    # Execute command
    if args.command == 'encrypt':
        encrypt_command(args)
    elif args.command == 'decrypt':
        decrypt_command(args)
    elif args.command == 'info':
        info_command(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
