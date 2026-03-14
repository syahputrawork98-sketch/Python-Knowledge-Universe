# 01_name_binding.py
# File ini mendemonstrasikan bagaimana fungsi id() menelanjangi 
# fakta bahwa Variabel adalah penempel label pada alamat memori.

print("--- Menyelidiki Gudang Label ---\n")

x = 55
print("Koki membuat variabel 'x' menunjuk ke nilai:", x)
print("Alamat Asli x di Memori: ", id(x))
print()

# Menambahkan alias stiker baru ke arah yang persis sama.
y = x
print("Koki memanggil perintah instruksi 'y = x'")
print("Alamat Asli y di Memori: ", id(y))
print()

print("Perhatikan angka panjang di atas!")
print("ID dari x dan y adalah PERSIS SAMA. Mereka menunjuk ke alamat gudang yang satu jua.")

print("\n--- Kejadian Mutasi ---\n")
# Merubah Stiker y 
y = 100
print("Koki memanggil instruksi penggantian 'y = 100'")
print("Mari kita Cek stiker y dan stiker x sekarang:")
print(f"Stiker Y merujuk ke Nilai: {y} | ID barunya: {id(y)}")
print(f"Stiker X MERUJUK ke Nilai: {x} | ID lamanya (tetap aman): {id(x)}")
