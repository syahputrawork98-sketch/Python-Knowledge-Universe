# 01_tipe_dan_inspeksi.py
# File ini membuktikan bahwa Python memiliki 5 tipe data bawaan yang fundamental
# dan bagaimana cara menyelidikinya diam-diam menggunakan agen type().

telur = 10                  # int
air_liter = 1.5           # float
pesan = "Halo Koki!"        # str
is_matang = False           # bool
kotak_hampa = None          # NoneType

print("--- Laporan Wujud Bahan Baku ---")
print(f"[{telur}] berwujud: {type(telur)}")
print(f"[{air_liter}] berwujud: {type(air_liter)}")
print(f"[{pesan}] berwujud: {type(pesan)}")
print(f"[{is_matang}] berwujud: {type(is_matang)}")
print(f"[{kotak_hampa}] berwujud: {type(kotak_hampa)}")

print("\n--- Uji Logika Alat Masak ---")
print("Kita coba kalikan telur (int) dengan 2:")
print("Hasil:", telur * 2)

print("\nSekarang kita coba kalikan Kertas Teks (str) tulisan 'Aha' dengan 3:")
print("Hasil:", "Aha" * 3)
print("Penjelasan: String tidak dikali secara matematika, melainkan difoto-kopi berjejer!")
