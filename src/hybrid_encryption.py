"""
Hybrid Encryption System
Combines AES-256 for file encryption and XChaCha20 for key encryption
"""

import os
import json
from aes_encryption import AESEncryption
from xchacha20_encryption import XChaCha20KeyEncryption

class HybridEncryption:
    def __init__(self):
        self.aes = AESEncryption()
        self.xchacha = XChaCha20KeyEncryption()
        
    def encrypt_file(self, input_file, output_dir="encrypted"):
        """
        Encrypt a file using hybrid approach:
        1. Encrypt file content with AES-256
        2. Encrypt AES key with XChaCha20
        
        Args:
            input_file: Path to file to encrypt
            output_dir: Directory to store encrypted files
            
        Returns:
            dict: Paths to encrypted file and key file
        """
        try:
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            
            # Generate filenames
            base_name = os.path.basename(input_file)
            encrypted_file = os.path.join(output_dir, f"{base_name}.enc")
            key_file = os.path.join(output_dir, f"{base_name}.key")
            metadata_file = os.path.join(output_dir, f"{base_name}.meta")
            
            print(f"\n{'='*60}")
            print(f"HYBRID ENCRYPTION PROCESS")
            print(f"{'='*60}")
            print(f"Input file: {input_file}")
            
            # Step 1: Generate AES key
            print(f"\n[1/4] Generating AES-256 key...")
            aes_key = self.aes.generate_key()
            print(f"✓ AES key generated: {aes_key.hex()[:32]}...")
            
            # Step 2: Encrypt file with AES
            print(f"\n[2/4] Encrypting file with AES-256-GCM...")
            nonce, tag = self.aes.encrypt_file(input_file, encrypted_file, aes_key)
            
            if not nonce:
                raise Exception("AES encryption failed")
            
            # Step 3: Generate XChaCha20 master key
            print(f"\n[3/4] Generating XChaCha20 master key...")
            master_key = self.xchacha.generate_master_key()
            print(f"✓ Master key generated: {master_key.hex()[:32]}...")
            
            # Step 4: Encrypt AES key with XChaCha20
            print(f"\n[4/4] Encrypting AES key with XChaCha20-Poly1305...")
            encrypted_aes_key = self.xchacha.encrypt_key(aes_key, master_key)
            
            if not encrypted_aes_key:
                raise Exception("Key encryption failed")
            
            # Save encrypted AES key
            self.xchacha.save_encrypted_key(encrypted_aes_key, key_file)
            
            # Save metadata
            metadata = {
                "original_filename": base_name,
                "encrypted_file": encrypted_file,
                "key_file": key_file,
                "master_key": master_key.hex(),
                "file_size": os.path.getsize(input_file)
            }
            
            with open(metadata_file, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            print(f"\n{'='*60}")
            print(f"✓✓✓ ENCRYPTION COMPLETED SUCCESSFULLY!")
            print(f"{'='*60}")
            print(f"Encrypted file: {encrypted_file}")
            print(f"Encrypted key:  {key_file}")
            print(f"Metadata:       {metadata_file}")
            print(f"{'='*60}\n")
            
            return {
                "encrypted_file": encrypted_file,
                "key_file": key_file,
                "metadata_file": metadata_file,
                "master_key": master_key
            }
            
        except Exception as e:
            print(f"\n✗✗✗ ENCRYPTION FAILED: {str(e)}")
            return None
    
    def decrypt_file(self, metadata_file, output_dir="decrypted"):
        """
        Decrypt a file using hybrid approach:
        1. Decrypt AES key with XChaCha20
        2. Decrypt file content with AES
        
        Args:
            metadata_file: Path to metadata file
            output_dir: Directory to store decrypted file
            
        Returns:
            str: Path to decrypted file
        """
        try:
            # Create output directory
            os.makedirs(output_dir, exist_ok=True)
            
            print(f"\n{'='*60}")
            print(f"HYBRID DECRYPTION PROCESS")
            print(f"{'='*60}")
            print(f"Metadata file: {metadata_file}")
            
            # Load metadata
            print(f"\n[1/4] Loading metadata...")
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)
            
            encrypted_file = metadata["encrypted_file"]
            key_file = metadata["key_file"]
            master_key = bytes.fromhex(metadata["master_key"])
            original_filename = metadata["original_filename"]
            
            print(f"✓ Metadata loaded")
            print(f"  Original file: {original_filename}")
            
            # Step 2: Load encrypted AES key
            print(f"\n[2/4] Loading encrypted AES key...")
            encrypted_aes_key = self.xchacha.load_encrypted_key(key_file)
            
            if not encrypted_aes_key:
                raise Exception("Failed to load encrypted key")
            
            # Step 3: Decrypt AES key with XChaCha20
            print(f"\n[3/4] Decrypting AES key with XChaCha20...")
            aes_key = self.xchacha.decrypt_key(encrypted_aes_key, master_key)
            
            if not aes_key:
                raise Exception("Key decryption failed")
            
            print(f"✓ AES key decrypted: {aes_key.hex()[:32]}...")
            
            # Step 4: Decrypt file with AES
            print(f"\n[4/4] Decrypting file with AES-256-GCM...")
            decrypted_file = os.path.join(output_dir, original_filename)
            success = self.aes.decrypt_file(encrypted_file, decrypted_file, aes_key)
            
            if not success:
                raise Exception("File decryption failed")
            
            print(f"\n{'='*60}")
            print(f"✓✓✓ DECRYPTION COMPLETED SUCCESSFULLY!")
            print(f"{'='*60}")
            print(f"Decrypted file: {decrypted_file}")
            print(f"{'='*60}\n")
            
            return decrypted_file
            
        except Exception as e:
            print(f"\n✗✗✗ DECRYPTION FAILED: {str(e)}")
            return None


# Test the hybrid system
if __name__ == "__main__":
    print("\n" + "="*60)
    print("HYBRID ENCRYPTION SYSTEM TEST")
    print("="*60)
    
    # Create test file
    test_file = "test_document.txt"
    test_content = """
    This is a confidential document for testing the hybrid encryption system.
    
    The system uses:
    1. AES-256-GCM for encrypting file content (fast and efficient)
    2. XChaCha20-Poly1305 for encrypting the AES key (nonce-misuse resistant)
    
    This demonstrates the practical application of combining two strong
    encryption algorithms to create a more robust security system.
    """ * 10  # Make it longer
    
    with open(test_file, 'w') as f:
        f.write(test_content)
    
    file_size = os.path.getsize(test_file)
    print(f"\nTest file created: {test_file} ({file_size} bytes)")
    
    # Initialize hybrid system
    hybrid = HybridEncryption()
    
    # Encrypt
    result = hybrid.encrypt_file(test_file)
    
    if result:
        # Decrypt
        decrypted_file = hybrid.decrypt_file(result["metadata_file"])
        
        if decrypted_file:
            # Verify
            print("="*60)
            print("VERIFICATION")
            print("="*60)
            
            with open(test_file, 'r') as f1, open(decrypted_file, 'r') as f2:
                original = f1.read()
                decrypted = f2.read()
                
                if original == decrypted:
                    print("✓✓✓ VERIFICATION PASSED!")
                    print(f"Original size:  {len(original)} bytes")
                    print(f"Decrypted size: {len(decrypted)} bytes")
                    print(f"Content match:  YES")
                else:
                    print("✗✗✗ VERIFICATION FAILED!")
                    print("Original and decrypted content don't match!")
            
            print("="*60)
            
            # Cleanup
            print("\nCleaning up test files...")
            os.remove(test_file)
            
            # Remove encrypted directory
            import shutil
            if os.path.exists("encrypted"):
                shutil.rmtree("encrypted")
            if os.path.exists("decrypted"):
                shutil.rmtree("decrypted")
            
            print("✓ Cleanup complete")
    
    print("\n" + "="*60)
    print("HYBRID SYSTEM TEST COMPLETE")
    print("="*60 + "\n")