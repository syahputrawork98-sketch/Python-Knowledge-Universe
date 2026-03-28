"""
LAB PRACTICAL: Multi-file Package Navigation
Standard: PPM V4 - Gold Standard

Tujuan: Membuktikan alur import (Absolute vs Relative) di dalam paket.
Guna: Membangun proyek skala besar yang terorganisir dengan benar.
"""

# Import dari modul satu paket (Sibling)
from auth import authenticate

def run_main():
    print("=" * 60)
    print("🪄 PACKAGE NAVIGATION LAB")
    print("=" * 60)
    
    user_status = authenticate("Antigravity")
    if user_status:
        print("✅ Access Granted.")

    print("=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    run_main()
