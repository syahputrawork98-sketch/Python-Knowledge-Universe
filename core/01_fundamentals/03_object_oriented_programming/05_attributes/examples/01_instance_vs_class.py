class Karakter:
    """Simulasi karakter game untuk memahami perbedaan atribut."""
    
    # 1. Class Attribute: Shared across ALL characters
    judul_game = "Python Quest"
    versi = "v1.2.0"

    def __init__(self, nama, job):
        # 2. Instance Attribute: Unique to EACH character
        self.nama = nama
        self.job = job
        self.level = 1

    def info(self):
        print(f"[{self.judul_game}] {self.nama} ({self.job}) - Lvl {self.level}")

# --- EKSEKUSI ---

p1 = Karakter("Artdarkman", "Warrior")
p2 = Karakter("Syahputra", "Mage")

print("--- Status Awal ---")
p1.info()
p2.info()

print("\n--- Update Instance (Hanya P1 naik level) ---")
p1.level = 5
p1.info()
p2.info() # P2 tetap level 1

print("\n--- Update Class (Update Versi Game) ---")
Karakter.versi = "v1.3.0"
print(f"P1 melihat versi: {p1.versi}")
print(f"P2 melihat versi: {p2.versi}")

print("\n--- Jebakan Shadowing (P1 pindah game sendiri) ---")
p1.judul_game = "Java Journey" # P1 membuat instance attr baru dengan nama yg sama
p1.info() # Judul berubah
p2.info() # P2 tetap di Python Quest (Class Attr asli)
