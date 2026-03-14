# main.py
"""
Contoh menjalankan kode dari struktur package.
"""
from auth import login, services

print("--- Menjalankan Package Demo ---")

# Memanggil lewat __init__.py (shorthand)
login("artdarkman")

# Memanggil lewat modul langsung
services.logout()
