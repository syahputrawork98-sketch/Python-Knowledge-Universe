"""
LAB PRACTICAL: sys.path & Import Explorer
Standard: PPM V4 - Gold Standard

Tujuan: Memahami mekanisme resolusi import (Search Mechanics).
Guna: Mendebug kesalahan 'ModuleNotFoundError' dan memahami silsilah modul.
"""

import sys
import os

def audit_import_environment():
    print("=" * 60)
    print("🌍 INTERNAL AUDIT: Python Import System")
    print("=" * 60)

    # 1. Inspecting sys.path (Search locations)
    print("Audit 1: Checking Search Paths (sys.path)")
    for i, path in enumerate(sys.path, 1):
        # Mark the current script directory
        is_cwd = "[CWD]" if path == os.getcwd() or path == "" else ""
        print(f"   [{i}] {path} {is_cwd}")

    print("\nAudit 2: Checking Module Cache (sys.modules)")
    # Just show first 5 loaded modules for brevity
    cached_names = list(sys.modules.keys())[:5]
    print(f"   First 5 cached modules: {cached_names}")
    print(f"   Total modules currently cached: {len(sys.modules)}")

    print("\nAudit 3: Tracing Module Location")
    try:
        import math
        import json
        
        # Displaying metadata from built-in vs standard library
        print(f"   Module 'math' (Built-in) : {math}")
        print(f"   Module 'json' (Library)  : {json.__file__}")
        
    except ImportError as e:
        print(f"   ❌ Error: {e}")

    print("=" * 60)
    print("✅ Audit Completed.")

if __name__ == "__main__":
    audit_import_environment()
