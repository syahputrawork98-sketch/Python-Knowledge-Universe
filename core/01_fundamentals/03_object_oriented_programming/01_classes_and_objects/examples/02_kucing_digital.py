class Kucing:
    def __init__(self, nama, ras):
        self.nama = nama
        self.ras = ras
        self.lapar = True
    
    def bersuara(self):
        print(f"{self.nama} berkata: Meooow!")
    
    def makan(self):
        if self.lapar:
            print(f"{self.nama} sedang makan ikan...")
            self.lapar = False
        else:
            print(f"{self.nama} sudah kenyang.")

# --- Penggunaan ---
kitty = Kucing("Kitty", "Persia")
kitty.bersuara()
kitty.makan()
kitty.makan()
