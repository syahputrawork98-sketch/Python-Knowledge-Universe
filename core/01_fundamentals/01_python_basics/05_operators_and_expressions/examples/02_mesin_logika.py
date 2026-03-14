# 02_mesin_logika.py
# Demonstrasi nyata penggunaan operator perbandingan dan logika
# serta bukti efisiensi 'Short-Circuit' Python.

print("=== SISTEM SELEKSI PENERIMAAN BEASISWA ===")

# Data Mahasiswa
nilai_ujian = 85
absensi_persen = 90
memiliki_rekomendasi = False

print(f"Data: Nilai={nilai_ujian}, Absen={absensi_persen}%, Rekomendasi={memiliki_rekomendasi}")

# 1. Operator Perbandingan (Comparison) menghasilkan Boolean
is_nilai_cukup = nilai_ujian >= 80
is_absen_rajin = absensi_persen > 75

# 2. Operator Logika 'and' (Semua syarat harus True)
lulus_jalur_akademik = is_nilai_cukup and is_absen_rajin

# 3. Operator Logika 'or' (Salah satu cukup)
lulus_akhir = lulus_jalur_akademik or memiliki_rekomendasi

print(f"\nStatus Akademik: {'LULUS' if lulus_jalur_akademik else 'GAGAL'}")
print(f"Keputusan Akhir : {'DITERIMA' if lulus_akhir else 'DITOLAK'}")

print("\n--- Eksperimen Sihir Short-Circuit ---")

def fungsi_rahasia():
    print(">> Mesin Kanan Dijalankan! (Boros Energi)")
    return True

print("Test 1: True or fungsi_rahasia()")
# Karena kiri sudah True, 'or' tidak akan mengeksekusi kanan
True or fungsi_rahasia()
print("(Tidak ada pesan rahasia di atas? Itu karena Short-Circuit or)")

print("\nTest 2: False and fungsi_rahasia()")
# Karena kiri sudah False, 'and' tidak akan mengeksekusi kanan
False and fungsi_rahasia()
print("(Masih sunyi? Itu karena Short-Circuit and)")

print("\nTest 3: True and fungsi_rahasia()")
# Karena kiri True, 'and' WAJIB cek kanan untuk kepastian
True and fungsi_rahasia()
