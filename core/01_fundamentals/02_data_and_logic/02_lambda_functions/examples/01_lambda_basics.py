# 01_lambda_basics.py
"""
Contoh penggunaan fungsi Lambda untuk operasi sederhana.
"""

# 1. Lambda Dasar
kuadrat = lambda x: x ** 2
print(f"Kuadrat dari 5: {kuadrat(5)}")

# 2. Lambda dengan banyak argumen
tambah = lambda a, b, c: a + b + c
print(f"Hasil tambah 10, 20, 30: {tambah(10, 20, 30)}")

# 3. Lambda di dalam fungsi Map
angka = [1, 2, 3, 4, 5]
angka_kuadrat = list(map(lambda x: x**2, angka))
print(f"List kuadrat: {angka_kuadrat}")

# 4. Lambda untuk Filter
angka_genap = list(filter(lambda x: x % 2 == 0, angka))
print(f"Angka genap: {angka_genap}")
