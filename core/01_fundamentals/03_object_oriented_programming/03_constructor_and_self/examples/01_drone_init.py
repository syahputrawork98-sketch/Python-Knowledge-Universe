class Drone:
    """Simulasi inisialisasi Drone menggunakan constructor."""
    
    def __init__(self, model, baterai):
        # self.variable adalah cara menempelkan data ke objek
        self.model = model
        self.baterai = baterai
        print(f"[LOG] Drone model {self.model} telah diaktivasi!")

    def cek_status(self):
        print(f"Status {self.model}: Baterai sisa {self.baterai}%")

# 1. Menyiapkan data awal saat pembuatan (Instantiation)
drone_tempur = Drone("Predator-X", 100)
drone_kargo = Drone("Heavy-Lifter", 85)

# 2. Memanggil method
# Perhatikan bahwa kita tidak memasukkan argumen untuk 'self'
drone_tempur.cek_status()
drone_kargo.cek_status()

# 3. Bukti self bekerja
# drone_tempur.cek_status() secara internal adalah Drone.cek_status(drone_tempur)
