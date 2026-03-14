# 02_praktek_casting.py
# Berkaitan dengan simulasi mengapa Type Casting adalah teknik wajib
# penjinak terminal untuk membangun aplikasi kalkulasi apapun.

print("=== MESIN PERAMAL MASA DEPAN ===")

# AWAS! Fungsi input() selalu merampas ketikan user ke dalam wujud Kertas/String!
# Bahkan jika user mengetik angka 18 sekalipun.
input_usia = input("Berapa usia KTP Anda sekarang? (Ketik Angka Bulat): ")

print("\n[Inspeksi Detektif] Mesin menerima data ini sebagai wujud:", type(input_usia))

# Ini akan GAGAL TOTAL jika kita melewatkan Casting:
# prediksi salah = input_usia + 10  <-- Ini akan melahirkan TypeError!

# SOLUSI: Nyalakan Mesin Penggiling (Type Casting) int()
usia_asli = int(input_usia)
print("[Type Casting] Berhasil menggiling Kertas menjadi Angka Bulat:", type(usia_asli))

# Sekarang komputasi matematika bekerja normal layaknya hukum Fisika
prediksi = usia_asli + 10

print(f"\nPrediksi: 10 Tahun lagi, usia Anda adalah {prediksi} tahun!")
