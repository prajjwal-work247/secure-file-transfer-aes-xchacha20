"""
XChaCha20 Key Encryption Module
Encrypts AES keys using XChaCha20-Poly1305
"""

import nacl.secret
import nacl.utils
from nacl.encoding import Base64Encoder

class XChaCha20KeyEncryption:
    def __init__(self):
        self.key_size = 32  # 256 bits for XChaCha20
        
    def generate_master_key(self):
        """Generate a random 256-bit master key for XChaCha20"""
        return nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
    
    def encrypt_key(self, aes_key, master_key):
        """
        Encrypt an AES key using XChaCha20-Poly1305
        
        Args:
            aes_key: The AES key to encrypt (32 bytes)
            master_key: Master key for XChaCha20 encryption (32 bytes)
            
        Returns:
            encrypted_key: Encrypted key (includes nonce and ciphertext)
        """
        try:
            # Create SecretBox with master key
            box = nacl.secret.SecretBox(master_key)
            
            # Encrypt the AES key (automatically generates nonce)
            encrypted = box.encrypt(aes_key)
            
            print(f"✓ AES key encrypted with XChaCha20")
            print(f"  Nonce size: {nacl.secret.SecretBox.NONCE_SIZE} bytes (192 bits)")
            print(f"  Encrypted key size: {len(encrypted)} bytes")
            
            return encrypted
            
        except Exception as e:
            print(f"✗ Key encryption failed: {str(e)}")
            return None
    
    def decrypt_key(self, encrypted_key, master_key):
        """
        Decrypt an AES key using XChaCha20-Poly1305
        
        Args:
            encrypted_key: The encrypted key data
            master_key: Master key for XChaCha20 decryption (32 bytes)
            
        Returns:
            aes_key: Decrypted AES key (32 bytes)
        """
        try:
            # Create SecretBox with master key
            box = nacl.secret.SecretBox(master_key)
            
            # Decrypt the AES key
            aes_key = box.decrypt(encrypted_key)
            
            print(f"✓ AES key decrypted successfully")
            
            return aes_key
            
        except Exception as e:
            print(f"✗ Key decryption failed: {str(e)}")
            return None
    
    def save_encrypted_key(self, encrypted_key, filename):
        """Save encrypted key to file"""
        try:
            with open(filename, 'wb') as f:
                f.write(encrypted_key)
            print(f"✓ Encrypted key saved to: {filename}")
            return True
        except Exception as e:
            print(f"✗ Failed to save key: {str(e)}")
            return False
    
    def load_encrypted_key(self, filename):
        """Load encrypted key from file"""
        try:
            with open(filename, 'rb') as f:
                encrypted_key = f.read()
            print(f"✓ Encrypted key loaded from: {filename}")
            return encrypted_key
        except Exception as e:
            print(f"✗ Failed to load key: {str(e)}")
            return None


# Test the module
if __name__ == "__main__":
    import os
    
    print("=" * 60)
    print("XChaCha20 Key Encryption Module Test")
    print("=" * 60)
    
    # Initialize
    xchacha = XChaCha20KeyEncryption()
    
    # Generate master key for XChaCha20
    master_key = xchacha.generate_master_key()
    print(f"\n1. Generated XChaCha20 Master Key: {master_key.hex()[:32]}...")
    
    # Simulate an AES key
    from Crypto.Random import get_random_bytes
    aes_key = get_random_bytes(32)
    print(f"\n2. Test AES Key to encrypt: {aes_key.hex()[:32]}...")
    
    # Encrypt the AES key
    print(f"\n3. Encrypting AES key with XChaCha20...")
    encrypted_key = xchacha.encrypt_key(aes_key, master_key)
    
    if encrypted_key:
        # Save to file
        print(f"\n4. Saving encrypted key to file...")
        xchacha.save_encrypted_key(encrypted_key, "test_encrypted_key.bin")
        
        # Load from file
        print(f"\n5. Loading encrypted key from file...")
        loaded_key = xchacha.load_encrypted_key("test_encrypted_key.bin")
        
        # Decrypt
        print(f"\n6. Decrypting AES key...")
        decrypted_key = xchacha.decrypt_key(loaded_key, master_key)
        
        # Verify
        print(f"\n7. Verification:")
        if decrypted_key and decrypted_key == aes_key:
            print("✓✓✓ SUCCESS: Original and decrypted keys match!")
            print(f"    Original:  {aes_key.hex()[:32]}...")
            print(f"    Decrypted: {decrypted_key.hex()[:32]}...")
        else:
            print("✗✗✗ FAILED: Keys don't match!")
        
        # Cleanup
        os.remove("test_encrypted_key.bin")
        
    print("\n" + "=" * 60)
    print("Test Complete")
    print("=" * 60)
