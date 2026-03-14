class Hewan:
    """Parent Class (Base)"""
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara...")

class Kucing(Hewan):
    """Child Class (Derived)"""
    def bersuara(self):
        # Method Overriding: Versi Kucing lebih spesifik
        print(f"{self.nama} mengeong: Meow! Meow!")

class Anjing(Hewan):
    """Child Class (Derived)"""
    def bersuara(self):
        # Method Overriding
        print(f"{self.nama} menggonggong: Woof! Woof!")

# --- EKSEKUSI ---
generic_animal = Hewan("Makhluk")
muezza = Kucing("Muezza")
doggo = Anjing("Doggo")

generic_animal.bersuara()
muezza.bersuara()
doggo.bersuara()
