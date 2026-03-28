"""
LAB PRACTICAL: Package Audit
Standard: PPM V4 - Gold Standard

Tujuan: Melakukan audit paket yang terinstal secara programmatik di dalam environment aktif.
Guna: Memverifikasi dependensi tanpa harus keluar dari interpreter Python atau menjalankan terminal.
"""

import sys

# Menggunakan importlib.metadata (Standar sejak Python 3.8+)
try:
    from importlib.metadata import distributions
except ImportError:
    # Fallback untuk versi Python lama (menggunakan pkg_resources jika tersedia)
    distributions = None

def run_package_audit():
    print("=" * 60)
    print("📦 PYTHON PACKAGE AUDIT")
    print("=" * 60)
    print(f"Interpreter: {sys.executable}")
    print("-" * 60)

    if distributions:
        dist_list = list(distributions())
        if not dist_list:
             print("   [INFO]: Tidak ada paket eksternal (pip) yang terinstal.")
        else:
            print(f"{'Package Name':<30} | {'Version':<15}")
            print("-" * 60)
            for dist in sorted(dist_list, key=lambda x: x.metadata['Name'].lower()):
                name = dist.metadata['Name']
                version = dist.version
                print(f"{name:<30} | {version:<15}")
    else:
        print("❌ Error: importlib.metadata tidak tersedia di versi Python ini.")

    print("=" * 60)
    print("✅ Audit Completed.")

if __name__ == "__main__":
    run_package_audit()
