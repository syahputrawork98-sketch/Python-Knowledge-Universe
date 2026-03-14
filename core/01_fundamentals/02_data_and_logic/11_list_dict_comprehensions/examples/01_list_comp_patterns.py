# 01_list_comp_patterns.py
"""
Contoh-contoh pola List Comprehension yang umum digunakan.
"""

angka = range(1, 11)

# 1. Transformasi (Mapping)
# Mengubah angka menjadi string dengan prefiks
label = [f"ID-{x}" for x in angka]
print(f"Labels: {label}")

# 2. Penyaringan (Filtering)
# Hanya mengambil angka kelipatan 3
kelipatan_tiga = [x for x in angka if x % 3 == 0]
print(f"Kelipatan 3: {kelipatan_tiga}")

# 3. Transformasi + Penyaringan
# Kuadrat dari angka ganjil
ganjil_kuadrat = [x**2 for x in angka if x % 2 != 0]
print(f"Ganjil Kuadrat: {ganjil_kuadrat}")

# 4. Nested (Hati-hati, gunakan secukupnya)
matriks = [[1, 2], [3, 4]]
rata = [item for baris in matriks for item in baris]
print(f"Flattening matriks: {rata}")
