class Pizza:
    """Simulasi Toko Pizza untuk memahami tipe-tipe method."""
    
    toko = "Pizza Universe"  # Class Attribute
    
    def __init__(self, rasa, diameter):
        self.rasa = rasa        # Instance Attribute
        self.diameter = diameter

    # 1. Instance Method: Butuh akses ke data pizza spesifik (self)
    def deskripsi(self):
        print(f"Pizza {self.rasa} dengan ukuran {self.diameter}cm dari {self.toko}.")

    # 2. Class Method: Mengakses/mengubah data Toko (cls)
    @classmethod
    def ganti_nama_toko(cls, nama_baru):
        cls.toko = nama_baru
        print(f"[LOG] Nama toko berganti menjadi: {cls.toko}")

    # 3. Static Method: Fungsi bantuan murni, tidak butuh data internal
    @staticmethod
    def validasi_topping(topping):
        topping_tersedia = ["Keju", "Daging", "Jamur"]
        return topping in topping_tersedia

# --- EKSEKUSI ---

# Membuat pizza
my_pizza = Pizza("Margherita", 30)

# Panggil Instance Method
my_pizza.deskripsi()

# Panggil Static Method (Bisa lewat Class langsung)
print(f"Apakah Nanas tersedia? {Pizza.validasi_topping('Nanas')}")
print(f"Apakah Keju tersedia? {Pizza.validasi_topping('Keju')}")

# Panggil Class Method (Efeknya ke seluruh objek)
Pizza.ganti_nama_toko("Antigravity Pizza")
my_pizza.deskripsi() # Perhatikan nama toko berubah otomatis
