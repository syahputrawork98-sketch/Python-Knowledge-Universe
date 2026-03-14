# Bab 05: Attributes (Instance vs Class)

Chapter Code: CORE-03-05
Version: Core.Fundamentals.03.00
Last Updated: 2026-03-14
Status: Draft

> **Deskripsi Singkat**: Memahami perbedaan antara data yang dimiliki oleh masing-masing objek (Instance Attribute) dan data yang dibagi bersama oleh semua objek dalam satu cetak biru (Class Attribute).

## 1. Analogi (Pendekatan Konsep)

### Analogi Singkat
> "**Instance Attribute** adalah isi tas masing-masing petualang (beda orang, beda isi), sedangkan **Class Attribute** adalah nama Server atau cuaca di dunia game tersebut (semua petualang merasakan hal yang sama)."

### Analogi Panjang / Cerita (Dunia MMORPG)
Bayangkan sebuah game **RPG Online**.
1. **Instance Attribute (Equipment)**: Setiap pemain (objek) punya `nama`, `level`, dan `pedang` yang berbeda-beda. Jika "Pemain A" menaikkan levelnya, "Pemain B" tidak ikut naik level. Data ini unik dan "menempel" pada objek melalui `self`.
2. **Class Attribute (Dunia)**: Semua pemain berada di server yang sama, misal `server = "Asia-1"`. Jika admin mengubah nama server menjadi "Global-Oceania", maka secara otomatis informasi server di profil "Pemain A" dan "Pemain B" akan berubah. Data ini didefinisikan langsung di dalam class (di luar `__init__`) dan dibagi bersama.

## 2. Istilah Kunci (Key Terms)

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| Instance Attribute | Variabel yang didefinisikan di dalam `__init__` menggunakan `self`. Unik tiap objek. | `self.hp = 100` |
| Class Attribute | Variabel yang didefinisikan langsung di dalam class. Dibagi oleh semua objek. | `game_version = "1.0"` |
| Namespace | "Ruang" tempat Python menyimpan variabel agar tidak saling bertabrakan. | `obj.__dict__` |
| Overriding | Keadaan di mana objek membuat instance attribute dengan nama yang sama dengan class attribute. | `self.server = "Private"` |

## 3. Konsep Utama

### Instance Attribute
Dibuat di dalam constructor. Atribut ini adalah alasan mengapa kita bisa punya banyak objek berbeda dari satu class.
```python
class Hero:
    def __init__(self, nama):
        self.nama = nama  # Tiap Hero punya nama beda
```

### Class Attribute
Didefinisikan tepat di bawah baris `class`. Sangat berguna untuk menyimpan konstanta atau data yang memang harus sama untuk semua instance.
```python
class Hero:
    dunia = "Zubat-Land"  # Semua Hero tinggal di sini
```

### Hati-hati dengan List/Dict!
**Peringatan Keras**: Jangan gunakan tipe data yang bisa berubah (*mutable*) seperti List atau Dictionary sebagai Class Attribute jika Anda berniat mengubahnya untuk tiap objek. Mereka akan saling "terkontaminasi".
```python
class Hero:
    inventory = []  # SALAH! Jika Hero A ambil item, Hero B juga punya item itu.
```
*Solusi: Selalu letakkan list/dict kosong di dalam `__init__`.*

## 4. Visualisasi Analogi

*(Aset Visual SVG sedang dalam pengembangan)*

## 5. Peringatan / Jebakan Umum (Gotchas)
- **Bersembunyi di Balik Nama**: Jika Anda memiliki Class Attribute `x = 10` dan Anda menjalankan `obj.x = 20`, Python akan membuat Instance Attribute baru bernama `x` untuk objek tersebut. Class Attribute aslinya tetap `10` untuk objek lainnya. Ini disebut *Shadowing*.
- **Efisiensi Memori**: Class Attribute jauh lebih hemat memori karena datanya hanya disimpan satu kali di satu tempat, bukan di setiap unit objek.

## 6. Referensi Kode Praktik
Contoh perbandingan atribut tersedia di folder `examples/`:
- `01_instance_vs_class.py`: Demonstrasi bagaimana perubahan class attribute memengaruhi semua objek.

## 7. Latihan (Validasi)
- [ ] Buat Class `Mobil` dengan class attribute `roda = 4`.
- [ ] Buat instance attribute `warna` dan `merk`.
- [ ] Buat 2 objek mobil, lalu coba ubah jumlah `roda` pada salah satu objek (Shadowing). Apa yang terjadi pada objek mobil satunya?
- [ ] Ubah jumlah `roda` langsung melalui nama Class (`Mobil.roda = 6`). Lihat efeknya pada semua objek yang belum terkena *shadowing*.
