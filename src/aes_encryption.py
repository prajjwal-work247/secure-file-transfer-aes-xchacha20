"""
AES-256 File Encryption Module
Encrypts files using AES-256 in GCM mode
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

class AESEncryption:
    def __init__(self):
        self.key_size = 32  # 256 bits
        self.nonce_size = 16  # 128 bits for GCM
        
    def generate_key(self):
        """Generate a random 256-bit AES key"""
        return get_random_bytes(self.key_size)
    
    def encrypt_file(self, input_file, output_file, key):
        """
        Encrypt a file using AES-256-GCM
        
        Args:
            input_file: Path to file to encrypt
            output_file: Path to save encrypted file
            key: 32-byte AES key
            
        Returns:
            nonce: The nonce used for encryption
            tag: Authentication tag
        """
        try:
            # Generate random nonce
            nonce = get_random_bytes(self.nonce_size)
            
            # Create cipher
            cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
            
            # Read and encrypt file
            with open(input_file, 'rb') as f_in:
                plaintext = f_in.read()
            
            ciphertext, tag = cipher.encrypt_and_digest(plaintext)
            
            # Write encrypted data
            with open(output_file, 'wb') as f_out:
                f_out.write(nonce)
                f_out.write(tag)
                f_out.write(ciphertext)
            
            print(f"✓ File encrypted successfully: {output_file}")
            return nonce, tag
            
        except Exception as e:
            print(f"✗ Encryption failed: {str(e)}")
            return None, None
    
    def decrypt_file(self, input_file, output_file, key):
        """
        Decrypt a file encrypted with AES-256-GCM
        
        Args:
            input_file: Path to encrypted file
            output_file: Path to save decrypted file
            key: 32-byte AES key
            
        Returns:
            bool: True if decryption successful
        """
        try:
            # Read encrypted file
            with open(input_file, 'rb') as f_in:
                nonce = f_in.read(self.nonce_size)
                tag = f_in.read(16)
                ciphertext = f_in.read()
            
            # Create cipher and decrypt
            cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
            plaintext = cipher.decrypt_and_verify(ciphertext, tag)
            
            # Write decrypted data
            with open(output_file, 'wb') as f_out:
                f_out.write(plaintext)
            
            print(f"✓ File decrypted successfully: {output_file}")
            return True
            
        except Exception as e:
            print(f"✗ Decryption failed: {str(e)}")
            return False


# Test the module
if __name__ == "__main__":
    # Create test file
    test_file = "test_input.txt"
    with open(test_file, 'w') as f:
        f.write("This is a test file for AES encryption. " * 100)
    
    # Initialize AES encryption
    aes = AESEncryption()
    
    # Generate key
    key = aes.generate_key()
    print(f"Generated AES Key: {key.hex()[:32]}...")
    
    # Encrypt
    encrypted_file = "test_encrypted.bin"
    nonce, tag = aes.encrypt_file(test_file, encrypted_file, key)
    
    # Decrypt
    decrypted_file = "test_decrypted.txt"
    success = aes.decrypt_file(encrypted_file, decrypted_file, key)
    
    # Verify
    if success:
        with open(test_file, 'r') as f1, open(decrypted_file, 'r') as f2:
            if f1.read() == f2.read():
                print("\n✓✓✓ VERIFICATION PASSED: Original and decrypted files match!")
            else:
                print("\n✗✗✗ VERIFICATION FAILED: Files don't match!")
    
    # Cleanup
    os.remove(test_file)
    os.remove(encrypted_file)
    os.remove(decrypted_file)