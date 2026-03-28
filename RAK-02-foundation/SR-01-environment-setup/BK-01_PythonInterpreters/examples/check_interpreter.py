"""
LAB PRACTICAL: Environment Audit
Standard: PPM V4 - Gold Standard

Tujuan: Memverifikasi indentitas, versi, dan lokasi biner dari interpreter Python yang sedang aktif. 
Guna: Memastikan apakah interpreter berjalan dalam mode global atau isolasi venv.
"""

import sys
import os
import platform

def audit_environment():
    print("=" * 50)
    print("🐍 PYTHON ENVIRONMENT AUDIT")
    print("=" * 50)

    # 1. Lokasi Biner (Paling Krusial)
    print(f"[Binary Location] : {sys.executable}")
    
    # 2. Versi Python
    print(f"[Python Version ] : {sys.version.split()[0]} ({platform.system()})")
    
    # 3. Status Isolasi (Virtual Env)
    # Jika venv aktif, sys.prefix biasanya berbeda dari sys.base_prefix.
    is_venv = sys.prefix != sys.base_prefix
    status = "Isolated (Virtual Env)" if is_venv else "Global (System)"
    print(f"[Execution Mode ] : {status}")

    print("\n[Audit Paths (sys.path)]:")
    for i, path in enumerate(sys.path, 1):
        if path: # Abaikan empty path (current dir)
             print(f" {i:02d}. {path}")

    print("=" * 50)
    print("✅ Audit Completed.")

if __name__ == "__main__":
    audit_environment()
