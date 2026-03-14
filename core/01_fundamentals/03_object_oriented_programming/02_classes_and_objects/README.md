# Bab 02: Classes and Objects

Chapter Code: CORE-03-02
Version: Core.Fundamentals.03.00
Last Updated: 2026-03-14
Status: Draft

> **Deskripsi Singkat**: Bab ini memperkenalkan paradigma Pemrograman Berorientasi Objek (OOP) dengan memahami bagaimana Class berfungsi sebagai "Cetak Biru" dan Object sebagai "Hasil Produksi" nyata di memori.

## 1. Analogi (Pendekatan Konsep)

### Analogi Singkat
> "Class adalah **Resep Kue** atau **Cetak Biru Arsitek**, sementara Object adalah **Kue Nyata** yang bisa dimakan atau **Rumah Fisik** yang bisa ditempati. Anda tidak bisa memakan Resep, Anda butuh kuenya."

### Analogi Panjang / Cerita (Pabrik Robot Kustom)
Bayangkan Anda adalah pemilik Pabrik Robot.

- **Class (Cetak Biru Robot)**: Sebelum membuat robot, teknisi Anda menggambar denah di atas kertas. Denah ini berisi:
    - **Atribut (Data)**: Apa saja komponennya? (Nama, Warna, Kapasitas Baterai).
    - **Method (Perilaku)**: Apa yang bisa ia lakukan? (`jalan()`, `bicara()`, `isi_ulang()`).
- **Object/Instance (Unit Robot Fisik)**: Saat Anda menekan tombol "Produksi", pabrik mengeluarkan satu robot nyata berdasarkan denah tadi. Robot pertama mungkin bernama "Robo-A" warna Merah. Robot kedua "Robo-B" warna Biru. Keduanya dibuat dari denah yang sama, tapi mereka adalah dua unit berbeda yang berdiri sendiri.
- **`self` (Identitas Diri Robot)**: Bayangkan setiap robot punya chip memori internal yang merujuk ke dirinya sendiri. Saat Anda menyuruh robot "Jalan!", ia harus tahu baterai *milik siapa* yang dikonsumsi. Chip `self` ini memastikan robot tidak salah mengambil data dari robot lain.

## 2. Istilah Kunci (Key Terms)

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| Class | Template atau cetak biru untuk menciptakan objek | `class Robot:` |
| Object / Instance | Wujud nyata yang dibuat dari sebuah Class | `my_robot = Robot()` |
| Attribute | Variabel yang menempel pada objek (data) | `robot.warna = "Merah"` |
| Method | Fungsi yang menempel pada objek (perilaku) | `robot.jalan()` |
| `__init__` | Method khusus untuk inisialisasi awal objek | `def __init__(self):` |
| `self` | Parameter yang merujuk pada instance objek itu sendiri | `self.nama = nama` |

## 3. Konsep Utama

### A. Mendefinisikan Class
Class dimulai dengan kata kunci `class` dan biasanya menggunakan penamaan **PascalCase**.
```python
class Robot:
    def __init__(self, nama, warna):
        self.nama = nama    # Atribut
        self.warna = warna
```

### B. Membuat Object (Instantiation)
Memanggil nama class seperti memanggil fungsi untuk membuat unit baru.
```python
robot1 = Robot("Robo-A", "Merah")
robot2 = Robot("Robo-B", "Biru")
```

### C. Menambahkan Perilaku (Methods)
Method adalah fungsi yang ada di dalam class dan selalu menerima `self` sebagai parameter pertama.
```python
class Robot:
    # ... init ...
    def sambutan(self):
        print(f"Halo, saya {self.nama}!")
```

### D. Mengakses Data
Gunakan tanda titik (`.`) untuk mengakses rahasia atau kemampuan objek.
```python
print(robot1.warna) # "Merah"
robot1.sambutan()   # "Halo, saya Robo-A!"
```

## 4. Visualisasi Analogi

![Big Picture Classes and Objects - The Blueprint and The Unit](assets/01_classes_and_objects.svg)

## 5. Di Balik Layar (Under the Hood)
Saat Anda membuat `robot1 = Robot()`, Python mengalokasikan petak memori baru. Python kemudian secara otomatis memanggil method sakti `__init__`. Menariknya, `robot1.sambutan()` sebenarnya diterjemahkan oleh Python menjadi `Robot.sambutan(robot1)`. Itulah mengapa kita wajib menuliskan `self` di definisi method—itu adalah cara Python "menitipkan" identitas unit robot ke dalam fungsinya.

## 6. Peringatan / Jebakan Umum (Gotchas)
- **Lupa `self`**: Lupa menulis `self` di dalam parameter method akan menyebabkan `TypeError` saat method dipanggil.
- **Class vs Instance Attribute**: Berhati-hatilah mendefinisikan variabel di luar `__init__`. Variabel tersebut akan menjadi milik "Pabrik" (semua unit berbagi data yang sama), bukan milik unit masing-masing.
- **PascalCase**: Pastikan nama Class diawali huruf besar. Meskipun Python tidak melarang huruf kecil, itu adalah standar industri agar tidak tertukar dengan fungsi biasa.

## 7. Referensi Kode Praktik
Simulasi pabrik robot tersedia di folder `examples/`:
- `01_robot_blueprint.py`: Dasar pembuatan class dan objek.
- `02_kucing_digital.py`: Contoh sederhana atribut dan perilaku hewan peliharaan.
- `03_bank_account.py`: Mengelola data saldo dalam satu objek.

## 8. Latihan (Validasi)
- [ ] Buatlah Class `Buku` dengan atribut `judul` dan `penulis`. Buat 2 objek buku berbeda.
- [ ] Tambahkan method `info()` pada Class `Buku` untuk mencetak "Buku [judul] ditulis oleh [penulis]".
- [ ] Buat Class `Mobil` yang punya atribut `bensin`. Tambahkan method `jalan()` yang akan mengurangi bensin setiap kali dipanggil.
