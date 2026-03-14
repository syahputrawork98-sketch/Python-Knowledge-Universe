# 02_formatting_methods.py
"""
Contoh penggunaan string methods dan f-string.
"""

# 1. Methods Populer
data = "  apple,banana,cherry  "
clean_data = data.strip().split(",")
print(f"List buah: {clean_data}")

gabung = " | ".join(clean_data)
print(f"Gabungan: {gabung}")

# 2. f-string Formatting
nama = "Budi"
skor = 95.5678
tanggal = "2026-03-14"

print(f"--- Rapor ---")
print(f"Nama  : {nama:>10}") # Rata kanan lebar 10
print(f"Skor  : {skor:.2f}")  # 2 angka di belakang koma
print(f"Status: {'LULUS' if skor > 75 else 'GAGAL'}")
