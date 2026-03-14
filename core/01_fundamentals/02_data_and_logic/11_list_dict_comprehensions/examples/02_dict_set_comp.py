# 02_dict_set_comp.py
"""
Contoh penggunaan Dict dan Set Comprehension.
"""

# 1. Dict Comprehension
# Memetakan angka ke pangkat tiganya
pangkat_tiga = {x: x**3 for x in range(1, 6)}
print(f"Pangkat Tiga: {pangkat_tiga}")

# Membalikkan Dictionary
kurs = {"USD": 15000, "SGD": 11000}
kurs_terbalik = {v: k for k, v in kurs.items()}
print(f"Kurs Terbalik: {kurs_terbalik}")

# 2. Set Comprehension
# Menghasilkan set unik dari teks
kalimat = "belajar python itu menyenangkan"
huruf_unik = {h for h in kalimat if h != " "}
print(f"Huruf unik (abjad): {sorted(list(huruf_unik))}")
