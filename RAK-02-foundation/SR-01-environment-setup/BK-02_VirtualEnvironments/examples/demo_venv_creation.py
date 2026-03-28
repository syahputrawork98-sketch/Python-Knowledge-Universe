"""
LAB PRACTICAL: Virtual Environment Verification
Standard: PPM V4 - Gold Standard

Tujuan: Memverifikasi apakah interpreter saat ini berjalan dalam isolasi venv.
Guna: Menghindari instalasi paket ke sistem global.
"""

import sys
import os

def check_isolation():
    print("=" * 60)
    print("🛸 VIRTUAL ENVIRONMENT ISOLATION CHECK")
    print("=" * 60)

    # 1. Mendeteksi venv
    # Pada venv, base_prefix adalah lokasi Python asli (global),
    # sementara prefix adalah lokasi venv saat ini.
    has_venv = sys.prefix != sys.base_prefix
    
    if has_venv:
        print("✅ STATUS: ISOLATED (Inside Virtual Environment)")
        print(f"   Venv Path: {sys.prefix}")
        print(f"   Base Path: {sys.base_prefix}")
    else:
        print("❌ STATUS: GLOBAL (No Virtual Environment Active)")
        print(f"   Base Path: {sys.base_prefix}")
        print("\n[PERINGATAN]: Disarankan untuk membuat venv sebelum lanjut.")

    # 2. Instruksi Operasional
    print("\n[OPERATIONAL CHEAT SHEET]:")
    print("  Create  : python -m venv .venv")
    if os.name == 'nt': # Windows
        print("  Activate: .\\.venv\\Scripts\\Activate.ps1 (PowerShell)")
    else: # Unix/macOS
        print("  Activate: source .venv/bin/activate (Bash/Zsh)")
    print("  Exit    : deactivate")

    print("=" * 60)

if __name__ == "__main__":
    check_isolation()
