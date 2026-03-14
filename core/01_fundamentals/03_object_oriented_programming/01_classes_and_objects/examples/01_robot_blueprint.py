class Robot:
    """Blueprint untuk menciptakan robot sederhana."""
    
    def __init__(self, nama, warna):
        # Atribut Instance (Milik tiap robot)
        self.nama = nama
        self.warna = warna
        self.baterai = 100
    
    def sambutan(self):
        """Metode untuk robot memperkenalkan diri."""
        print(f"Halo! Nama saya {self.nama}. Warna saya {self.warna}. Baterai: {self.baterai}%")
    
    def jalan(self, jarak):
        """Metode untuk melakukan aksi tertentu."""
        biaya = jarak * 2
        if self.baterai >= biaya:
            self.baterai -= biaya
            print(f"{self.nama} berjalan sejauh {jarak} meter. Baterai tersisa: {self.baterai}%")
        else:
            print(f"Maaf, baterai {self.nama} tidak cukup untuk berjalan.")

# --- Penggunaan ---

# 1. Instansiasi (Menciptakan Objek)
robo_merah = Robot("Robo-A", "Merah")
robo_biru = Robot("Robo-B", "Biru")

# 2. Akses Atribut
print(f"Robot 1: {robo_merah.nama}")

# 3. Panggil Method
robo_merah.sambutan()
robo_merah.jalan(10)

robo_biru.sambutan()
robo_biru.jalan(5)
