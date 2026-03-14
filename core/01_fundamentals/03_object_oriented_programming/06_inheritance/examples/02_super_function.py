class Computer:
    def __init__(self, merk, ram):
        self.merk = merk
        self.ram = ram
        print(f"[BOOT] Menyalakan BIOS {self.merk}...")

    def spek(self):
        print(f"Merk: {self.merk} | RAM: {self.ram}GB")

class Laptop(Computer):
    def __init__(self, merk, ram, baterai):
        # super() memanggil constructor milik Computer
        # sehingga kita tidak perlu menulis self.merk = merk lagi
        super().__init__(merk, ram)
        self.baterai = baterai

    def spek(self):
        # Kita bisa memanggil method parent lalu menambah info baru
        super().spek()
        print(f"Kapasitas Baterai: {self.baterai}mAh")

# --- EKSEKUSI ---
print("--- PC Standar ---")
pc_kantor = Computer("Dell", 8)
pc_kantor.spek()

print("\n--- Laptop Portabel ---")
laptop_kerja = Laptop("MacBook", 16, 5000)
laptop_kerja.spek()
