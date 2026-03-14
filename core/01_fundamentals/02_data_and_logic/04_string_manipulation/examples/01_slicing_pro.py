# 01_slicing_pro.py
"""
Demonstrasi teknik Slicing dan Indexing pada String.
"""

teks = "Python Knowledge Universe"

# 1. Indexing Dasar
print(f"Karakter pertama: {teks[0]}")
print(f"Karakter terakhir: {teks[-1]}")

# 2. Slicing Standar [start:stop]
print(f"Kata pertama: {teks[0:6]}") # Python
print(f"Tanpa start (dari awal): {teks[:6]}")
print(f"Tanpa stop (sampai akhir): {teks[7:]}")

# 3. Slicing dengan Step [start:stop:step]
print(f"Lompat 2: {teks[::2]}")
print(f"Balik teks: {teks[::-1]}") # Trik populer

# 4. Bukti Immutability
try:
    teks[0] = "J"
except TypeError as e:
    print(f"Error: {e} (String tidak bisa diubah langsung!)")
