"""
LAB PRACTICAL: Object Anatomy (PyObject & RefCounts)
Standard: PPM V4 - Gold Standard

Tujuan: Membedah struktur objek di level C (CPython).
Guna: Memahami pola penggunaan memori dan siklus hidup objek.
"""

import sys
import ctypes

def get_address(obj):
    """Utility to get memory address as a hex string."""
    return hex(id(obj))

def run_lab():
    print("=" * 60)
    print("🚀 CPYTHON OBJECT ANATOMY LAB")
    print("=" * 60)

    # 1. Identity & Memory Address
    print("\n1. Identity (Pointer to PyObject)")
    x = [1, 2, 3]
    y = x
    print(f"   [DATA] x = {x}")
    print(f"   [ADDR] Address of x: {get_address(x)}")
    print(f"   [ADDR] Address of y: {get_address(y)}")
    print(f"   [INFO] y points to the SAME PyObject as x? {x is y}")

    # 2. Reference Counting (ob_refcnt)
    print("\n2. Reference Counting (ob_refcnt)")
    # getrefcount typically returns 1 higher than actual count 
    # because the function call itself holds a temporary reference.
    count = sys.getrefcount(x)
    print(f"   [REFC] Current refcount for x: {count - 1} (Excl. temp call)")
    
    z = [x, x, x] # List holding 3 references to x
    count_after = sys.getrefcount(x)
    print(f"   [REFC] Refcount after adding to list z: {count_after - 1}")

    # 3. Object Header Size (PyObject_HEAD)
    print("\n3. Object Header Size (Memory Overhead)")
    empty_list = []
    small_int = 42
    large_int = 10**100
    
    # sys.getsizeof() includes the object header + data
    print(f"   [SIZE] Empty List: {sys.getsizeof(empty_list)} bytes")
    print(f"   [SIZE] Small Int (42): {sys.getsizeof(small_int)} bytes")
    print(f"   [SIZE] Large Int (10^100): {sys.getsizeof(large_int)} bytes")

    # 4. Small Integer Caching (CPython Optimization)
    print("\n4. CPython Optimization: Small Int Caching (-5 to 256)")
    a = 256
    b = 256
    print(f"   [TEST] a = 256, b = 256 -> 'a is b'? {a is b} (Cached)")
    
    c = 257
    d = 257
    print(f"   [TEST] c = 257, d = 257 -> 'c is d'? {c is d} (Not Cached - New PyObject)")

    print("\n" + "=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    run_lab()
