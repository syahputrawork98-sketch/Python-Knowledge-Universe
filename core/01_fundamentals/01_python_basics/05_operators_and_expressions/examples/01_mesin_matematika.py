# 01_mesin_matematika.py
# Laboratorium untuk menguji perbedaan mesin pembagian Python
# dan teknik singkat 'Augmented Assignment'.

print("=== LABORATORIUM MATEMATIKA PYTHON ===")

a = 10
b = 3

print(f"\nBahan Baku: a = {a}, b = {b}")

# 1. True Division (Hasil selalu Float)
hasil_bagi = a / b
print(f"Hasil '/'  (True Division) : {hasil_bagi} | Tipe: {type(hasil_bagi)}")

# 2. Floor Division (Hasil Bulat, membuang desimal)
hasil_floor = a // b
print(f"Hasil '//' (Floor Division): {hasil_floor}   | Tipe: {type(hasil_floor)}")

# 3. Modulo (Sisa Bagi)
sisa = a % b
print(f"Hasil '%'  (Modulo/Sisa)   : {sisa}   | Tipe: {type(sisa)}")

# 4. Pangkat (Exponentiation)
pangkat = a ** b
print(f"Hasil '**' (Pangkat)       : {pangkat}| Tipe: {type(pangkat)}")

print("\n--- Simulasi Kenaikan Skor (Augmented Assignment) ---")
skor = 100
print(f"Skor Awal: {skor}")

# Daripada menulis: skor = skor + 50
skor += 50 
print(f"Setelah skor += 50 : {skor}")

# Mencoba perkalian singkat
skor *= 2
print(f"Setelah skor *= 2  : {skor}")
