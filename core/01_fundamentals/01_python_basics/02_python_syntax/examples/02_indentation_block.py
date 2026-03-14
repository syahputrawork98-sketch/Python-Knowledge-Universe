# 02_indentation_block.py
# Berkaitan dengan lekukan Visual 4 spasi untuk membedakan
# mana yang Atasan dan mana yang Bawahan (Anak Buah).

batas_umur = 18

print("--- Pengecekan Umur Pengunjung ---")

umur = 20

# Di sini terjadi pengecekan. Python mulai masuk ke Blok bersyarat jika nilainya True.
if umur >= batas_umur:
    # PERHATIKAN 4 SPASI DI KIRI!
    # Semua yang masuk ke dalam sejauh 4 spasi adalah "Anak Buah" dari 'if'
    print("[✓] Selamat datang kembali, Tuan.")
    print("[✓] Silakan masuk ke dalam.")

# Spasi KEMBALI HILANG atau kembali rata lurus ke baris utama:
# Ini menandakan bahwa blok 'if' telah berakhir total.
# Sehingga instruksi di bawah ini TIDAK LAGI menjadi syarat apapun.
print("Pemeriksaan usai.")
