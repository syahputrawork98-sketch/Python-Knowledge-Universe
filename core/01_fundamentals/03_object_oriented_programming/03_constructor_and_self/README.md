# Bab 03: Constructor & `self`

Chapter Code: CORE-03-03
Version: Core.Fundamentals.03.00
Last Updated: 2026-03-14
Status: Draft

> **Deskripsi Singkat**: Memahami bagaimana objek "dilahirkan" dengan data awal menggunakan `__init__` dan bagaimana `self` bekerja sebagai jembatan identitas antar method.

## 1. Analogi (Pendekatan Konsep)

### Analogi Singkat
> "`__init__` adalah **Proses Aktivasi** atau **Setting Awal** saat gadget baru dinyalakan, sedangkan `self` adalah **Nama Panggilan Objek** untuk merujuk pada dirinya sendiri di dalam kode."

### Analogi Panjang / Cerita (Sertifikat Kelahiran Digital)
Bayangkan sebuah **Pabrik Boneka Pintar**.
1. **`__init__` (Aktivasi)**: Begitu boneka keluar dari mesin cetak, ia tidak langsung punya nama. Petugas pabrik harus menempelkan label nama, warna baju, dan kapasitas suara. Inilah tugas `__init__`—ia memastikan setiap boneka punya data dasar yang diperlukan sebelum diserahkan ke pembeli.
2. **`self` (Chip Memori Internal)**: Di dalam setiap boneka ada sebuah chip memori yang selalu berkata "Milik SAYA". Jika Anda menekan perutnya untuk berbicara, boneka itu harus tahu suara *milik siapa* yang harus diputar. Tanpa `self`, boneka itu akan bingung dan mencoba memutar suara boneka lain di seberang ruangan. `self` memastikan boneka Robo-1 menggunakan baterai Robo-1, bukan baterai Robo-2.

## 2. Istilah Kunci (Key Terms)

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| Constructor | Method khusus yang dipanggil otomatis saat objek dibuat. | `def __init__(self):` |
| Implicit Parameter | Parameter yang dikirim otomatis oleh Python tanpa kita tulis saat memanggil. | `self` |
| Instance Variable | Variabel yang nilainya unik untuk setiap objek. | `self.nama = "A"` |
| `id()` | Fungsi untuk melihat alamat unik objek di memori. | `id(robot)` |

## 3. Konsep Utama

### Method `__init__`
Ini adalah "Magic Method" yang paling sering digunakan. Ia tidak me-`return` nilai, tugasnya hanya menyiapkan (inisialisasi) data awal.

```python
class Drone:
    def __init__(self, model, baterai):
        self.model = model      # Menyiapkan data model
        self.baterai = baterai  # Menyiapkan data baterai
```

### Rahasia di Balik `self`
Tahukah Anda? Saat Anda memanggil `drone1.terbang()`, Python sebenarnya menjalankan:
`Drone.terbang(drone1)`

Parameter `self` adalah cara kita memberi tahu Python: "Gunakan data milik objek yang sedang memanggil method ini." Itulah alasan mengapa `self` **Wajib** menjadi parameter pertama di setiap method instance.

## 4. Visualisasi Analogi

*(Aset Visual SVG sedang dalam pengembangan)*

## 5. Peringatan / Jebakan Umum (Gotchas)
- **Typo `__init__`**: Sering terjadi penulisan `_init_` (satu underscore). Python tidak akan mengenalkannya sebagai constructor dan data Anda tidak akan terpasang. Wajib **dua** underscore di kiri dan kanan.
- **Lupa `self.variable`**: Jika Anda menulis `nama = n` di dalam `__init__` (tanpa `self.`), variabel tersebut bersifat lokal dan akan langsung "hangus" setelah proses inisialisasi selesai. Gunakan `self.` agar ia menempel permanen pada objek.

## 6. Referensi Kode Praktik
Contoh aktivasi objek tersedia di folder `examples/`:
- `01_drone_init.py`: Dasar penggunaan constructor.
- `02_identity_card.py`: Membuktikan keunikan `self` antar objek berbeda.

## 7. Latihan (Validasi)
- [ ] Buat Class `PemainGame` yang meminta `username` dan `level` saat dibuat.
- [ ] Tambahkan method `status()` yang mencetak "Pemain [username] sekarang berada di level [level]".
- [ ] Buat 3 objek pemain berbeda dan buktikan mereka memiliki data yang tidak tertukar.
