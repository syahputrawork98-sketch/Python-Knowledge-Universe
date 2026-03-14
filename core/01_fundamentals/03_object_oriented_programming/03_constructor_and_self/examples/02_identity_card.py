class KTP:
    """Membuktikan identitas unik objek menggunakan self dan id()."""
    
    def __init__(self, nama):
        self.nama = nama

    def siapa_saya(self):
        # id(self) mengembalikan alamat memori unik objek ini
        print(f"Saya adalah {self.nama} dengan alamat memori: {id(self)}")

# Membuat dua objek dari cetak biru yang sama
orang_1 = KTP("Budi")
orang_2 = KTP("Siti")

print("--- Pembuktian Identitas ---")
orang_1.siapa_saya()
orang_2.siapa_saya()

print("\n--- Kesimpulan ---")
print("Walaupun menggunakan Class yang sama, 'self' memastikan")
print("Python merujuk ke petak memori yang berbeda untuk setiap orang.")
