# 02_mutable_aliasing.py
# Berkaitan dengan obyek Lembek (Papan Tulis) yang sangat rentan
# terhadap modifikasi tanpa sengaja jika menggunakan nama alias.

print("--- Data Kelompok: Tim Alfa ---")
tim_alfa = ["Budi", "Andi", "Siti"]
print("Anggota Tim Alfa:", tim_alfa)

print("\n--- Kejadian Aliasing ---")
print("Kita perintahkan 'tim_beta = tim_alfa', artinya Stiker Beta")
print("kini ditempelkan pada papan absen yang sama persis.")
tim_beta = tim_alfa

print("Sekarang kita tambahkan 'Joko' melalui tim_BETA...")
tim_beta.append("Joko")

# Perhatikan keanehan di bawah ini
print("\nHasilnya:")
print("Tim Beta :", tim_beta)
print("Tim Alfa :", tim_alfa, "   <-- KAGET! Kenapa Alfa juga ketambahan Joko?")
print("Penjelasan: Karena Alfa dan Beta adalah nama alias untuk papan absen yang sama!\n")


print("--- Solusi: Menggunakan COPY ---")
print("Sekarang kita buat Grup Charlie menggunakan salinan bersih.")
print("Perintah: 'tim_charlie = tim_alfa.copy()'\n")
tim_charlie = tim_alfa.copy()

print("Kita tambahkan 'Tono' ke dalam tim_CHARLIE...")
tim_charlie.append("Tono")

print("Hasilnya:")
print("Tim Charlie:", tim_charlie)
print("Tim Alfa   :", tim_alfa, "   <-- Aman! Alfa tidak tercemar Tono.")
