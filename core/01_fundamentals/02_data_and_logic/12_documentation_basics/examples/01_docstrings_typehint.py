# 01_docstrings_typehint.py
"""
Contoh standar penulisan dokumentasi dan type hinting.
"""

def hitung_diskon(harga: int, persen_diskon: float = 0.1) -> float:
    """
    Menghitung harga akhir setelah dipotong diskon.
    
    Args:
        harga (int): Harga asli barang.
        persen_diskon (float): Persentase diskon (0.0 sampai 1.0). Default 0.1 (10%).
        
    Returns:
        float: Harga setelah diskon.
    """
    # Menghitung nominal diskon
    # Kita menggunakan float agar akurat saat pembagian
    nominal = harga * persen_diskon
    return harga - nominal

# Mencoba melihat bantuan
# help(hitung_diskon) 

hasil = hitung_diskon(100000, 0.25)
print(f"Harga bayar: Rp{hasil:.0f}")

# Type hinting pada variabel
konfigurasi: dict = {"debug": True, "timeout": 30}
print(f"Status Debug: {konfigurasi['debug']}")
