"""
Performance Testing Script for Hybrid Encryption System
Tests encryption/decryption speed across different file sizes
"""

import os
import sys
import time
import json
from datetime import datetime

# Add parent directory to path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from hybrid_encryption import HybridEncryption

class PerformanceTest:
    def __init__(self):
        self.hybrid = HybridEncryption()
        self.results = []
        
    def create_test_file(self, size_mb, filename):
        """Create a test file of specified size"""
        size_bytes = size_mb * 1024 * 1024
        
        print(f"Creating {size_mb}MB test file...")
        with open(filename, 'wb') as f:
            # Write in chunks to avoid memory issues
            chunk_size = 1024 * 1024  # 1MB chunks
            remaining = size_bytes
            
            while remaining > 0:
                write_size = min(chunk_size, remaining)
                f.write(os.urandom(write_size))
                remaining -= write_size
        
        print(f"✓ Created: {filename} ({size_mb}MB)")
        
    def test_encryption(self, filename, file_size_mb):
        """Test encryption performance"""
        print(f"\n{'='*60}")
        print(f"Testing Encryption: {file_size_mb}MB file")
        print(f"{'='*60}")
        
        # Measure encryption time
        start_time = time.time()
        result = self.hybrid.encrypt_file(filename, output_dir="test_encrypted")
        end_time = time.time()
        
        encryption_time = end_time - start_time
        
        if result:
            throughput = file_size_mb / encryption_time if encryption_time > 0 else 0
            print(f"\n✓ Encryption completed in {encryption_time:.3f} seconds")
            print(f"  Throughput: {throughput:.2f} MB/s")
            return encryption_time, throughput, result
        else:
            print(f"\n✗ Encryption failed")
            return None, None, None
    
    def test_decryption(self, metadata_file, file_size_mb):
        """Test decryption performance"""
        print(f"\n{'='*60}")
        print(f"Testing Decryption: {file_size_mb}MB file")
        print(f"{'='*60}")
        
        # Measure decryption time
        start_time = time.time()
        decrypted_file = self.hybrid.decrypt_file(metadata_file, output_dir="test_decrypted")
        end_time = time.time()
        
        decryption_time = end_time - start_time
        
        if decrypted_file:
            throughput = file_size_mb / decryption_time if decryption_time > 0 else 0
            print(f"\n✓ Decryption completed in {decryption_time:.3f} seconds")
            print(f"  Throughput: {throughput:.2f} MB/s")
            return decryption_time, throughput, decrypted_file
        else:
            print(f"\n✗ Decryption failed")
            return None, None, None
    
    def verify_integrity(self, original_file, decrypted_file):
        """Verify decrypted file matches original"""
        print(f"\nVerifying file integrity...")
        
        with open(original_file, 'rb') as f1, open(decrypted_file, 'rb') as f2:
            original_data = f1.read()
            decrypted_data = f2.read()
            
            if original_data == decrypted_data:
                print(f"✓ Integrity verified: Files match perfectly")
                return True
            else:
                print(f"✗ Integrity check failed: Files don't match")
                return False
    
    def run_test_suite(self, file_sizes=[1, 5, 10, 25, 50, 100]):
        """Run complete test suite across different file sizes"""
        
        print("\n" + "="*60)
        print("HYBRID ENCRYPTION PERFORMANCE TEST SUITE")
        print("="*60)
        print(f"Test started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"File sizes to test: {file_sizes} MB")
        print("="*60)
        
        for size_mb in file_sizes:
            test_file = f"test_file_{size_mb}mb.bin"
            
            try:
                # Create test file
                self.create_test_file(size_mb, test_file)
                
                # Test encryption
                enc_time, enc_throughput, enc_result = self.test_encryption(test_file, size_mb)
                
                if not enc_result:
                    print(f"Skipping decryption test for {size_mb}MB (encryption failed)")
                    continue
                
                # Test decryption
                dec_time, dec_throughput, dec_file = self.test_decryption(
                    enc_result["metadata_file"], 
                    size_mb
                )
                
                if not dec_file:
                    print(f"Skipping verification for {size_mb}MB (decryption failed)")
                    continue
                
                # Verify integrity
                integrity_ok = self.verify_integrity(test_file, dec_file)
                
                # Store results
                result = {
                    "file_size_mb": size_mb,
                    "encryption_time": enc_time,
                    "encryption_throughput": enc_throughput,
                    "decryption_time": dec_time,
                    "decryption_throughput": dec_throughput,
                    "total_time": enc_time + dec_time,
                    "integrity_verified": integrity_ok
                }
                
                self.results.append(result)
                
                # Clean up
                os.remove(test_file)
                if os.path.exists(dec_file):
                    os.remove(dec_file)
                
                print(f"\n✓ Test completed for {size_mb}MB file")
                print(f"  Encryption: {enc_time:.3f}s ({enc_throughput:.2f} MB/s)")
                print(f"  Decryption: {dec_time:.3f}s ({dec_throughput:.2f} MB/s)")
                print(f"  Total time: {enc_time + dec_time:.3f}s")
                
            except Exception as e:
                print(f"\n✗ Test failed for {size_mb}MB: {str(e)}")
                continue
        
        # Clean up directories
        self.cleanup()
        
        # Save results
        self.save_results()
        
        # Print summary
        self.print_summary()
    
    def cleanup(self):
        """Clean up test directories"""
        import shutil
        
        for directory in ["test_encrypted", "test_decrypted"]:
            if os.path.exists(directory):
                shutil.rmtree(directory)
    
    def save_results(self):
        """Save results to JSON file"""
        results_dir = "results"
        os.makedirs(results_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = os.path.join(results_dir, f"performance_results_{timestamp}.json")
        
        output = {
            "test_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "results": self.results
        }
        
        with open(filename, 'w') as f:
            json.dump(output, f, indent=2)
        
        print(f"\n✓ Results saved to: {filename}")
        return filename
    
    def print_summary(self):
        """Print test summary"""
        if not self.results:
            print("\n✗ No results to display")
            return
        
        print("\n" + "="*60)
        print("PERFORMANCE TEST SUMMARY")
        print("="*60)
        print(f"{'Size (MB)':<12} {'Enc Time (s)':<15} {'Dec Time (s)':<15} {'Total (s)':<12}")
        print("-"*60)
        
        for result in self.results:
            print(f"{result['file_size_mb']:<12} "
                  f"{result['encryption_time']:<15.3f} "
                  f"{result['decryption_time']:<15.3f} "
                  f"{result['total_time']:<12.3f}")
        
        print("="*60)
        
        # Calculate averages
        avg_enc_throughput = sum(r['encryption_throughput'] for r in self.results) / len(self.results)
        avg_dec_throughput = sum(r['decryption_throughput'] for r in self.results) / len(self.results)
        
        print(f"\nAverage Encryption Throughput: {avg_enc_throughput:.2f} MB/s")
        print(f"Average Decryption Throughput: {avg_dec_throughput:.2f} MB/s")
        print(f"Total Tests: {len(self.results)}")
        print(f"All Integrity Checks: {'✓ PASSED' if all(r['integrity_verified'] for r in self.results) else '✗ FAILED'}")
        print("="*60 + "\n")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("STARTING PERFORMANCE TESTS")
    print("="*60)
    print("\nThis will test encryption/decryption performance")
    print("across multiple file sizes. This may take 5-10 minutes.")
    print("\nFile sizes to test: 1, 5, 10, 25, 50, 100 MB")
    
    # Ask for confirmation
    response = input("\nProceed with tests? (y/n): ")
    
    if response.lower() != 'y':
        print("Tests cancelled.")
        sys.exit(0)
    
    # Run tests
    tester = PerformanceTest()
    
    # For quick testing, use smaller files
    # tester.run_test_suite([1, 5, 10])
    
    # For full testing (takes longer)
    tester.run_test_suite([1, 5, 10, 25, 50, 100])
    
    print("\n" + "="*60)
    print("ALL TESTS COMPLETED")
    print("="*60)
    print("\nNext steps:")
    print("1. Check results/ directory for JSON output")
    print("2. Run visualization script to generate graphs")
    print("="*60 + "\n")