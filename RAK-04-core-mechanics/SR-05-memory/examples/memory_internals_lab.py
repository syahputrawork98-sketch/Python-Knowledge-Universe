"""
LAB PRACTICAL: Memory Internals (RefCounts & GC)
Standard: PPM V4 - Gold Standard

Tujuan: Membedah mekanisme manajemen memori CPython secara nyata.
Guna: Mendeteksi dan mencegah kebocoran memori (Memory Leaks).
"""

import sys
import gc
import ctypes

def get_addr(obj):
    return hex(id(obj))

def run_lab():
    print("=" * 60)
    print("🚀 CPYTHON MEMORY INTERNALS LAB")
    print("=" * 60)

    # 1. Reference Counting Determinism
    print("\n1. Reference Counting: Immediate Deallocation")
    class Tracker:
        def __del__(self):
            print("   [DESTRUCTOR] Tracking object is being destroyed NOW.")
            
    def scope_test():
        t = Tracker()
        print(f"   [INFO] Tracker created at {get_addr(t)}")
        print("   [INFO] Leaving scope...")
        
    scope_test() # Refcount zero -> immediate __del__

    # 2. Circular References: The GC Territory
    print("\n2. Circular References: Breaking the Cycle")
    gc.collect() # Clean start
    
    class Node:
        def __init__(self, name):
            self.name = name
            self.next = None
        def __del__(self):
            print(f"   [DESTRUCTOR] Node {self.name} is finally destroyed.")

    a = Node("A")
    b = Node("B")
    a.next = b
    b.next = a # CYCLE CREATED
    
    del a
    del b
    print("   [INFO] a and b deleted from main scope, but refcounts are still 1!")
    
    print("   [ACTION] Manually triggering gc.collect()...")
    collected = gc.collect()
    print(f"   [RESULT] GC collected {collected} unreachable objects.")

    # 3. Real Memory Addresses with ctypes
    print("\n3. Real Memory Inspection (ctypes)")
    x = "Hello Internals"
    addr = id(x)
    # Using ctypes to read directly from memory (DANGEROUS but educational)
    print(f"   [INFO] String 'x' at {hex(addr)}")
    
    # Python object is typically: [refcnt, type_ptr, data...]
    # On 64-bit: 8 bytes for refcnt, 8 bytes for type_ptr
    refcnt_from_mem = ctypes.c_long.from_address(addr).value
    print(f"   [DATA] Refcount read directly from memory: {refcnt_from_mem}")

    print("\n" + "=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    run_lab()
