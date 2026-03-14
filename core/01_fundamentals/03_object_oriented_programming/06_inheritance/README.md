# Bab 06: Inheritance (Pewarisan)

Chapter Code: CORE-03-06
Version: Core.Fundamentals.03.00
Last Updated: 2026-03-14
Status: Draft

> **Deskripsi Singkat**: Mempelajari cara membuat class baru berdasarkan class yang sudah ada. Konsep ini memungkinkan kita "mewariskan" kemampuan dan data dari Parent ke Child tanpa harus menulis ulang kode dari nol.

## 1. Analogi (Pendekatan Konsep)

### Analogi Singkat
> "**Inheritance** adalah evolusi teknologi, seperti **Telepon Kabel** (Parent) yang mewariskan fungsi 'menelepon' ke **Smartphone** (Child). Smartphone tidak perlu menemukan cara menelepon lagi, ia cukup menambah fitur 'kamera' dan 'internet'."

### Analogi Panjang / Cerita (Silsilah Kendaraan)
Bayangkan sebuah pabrik kendaraan bernama **Global Motors**.
1. **Parent Class (Kendaraan Umum)**: Mereka membuat desain dasar kendaraan yang punya `mesin` dan fungsi `jalan()`. Semua kendaraan pasti punya dua hal ini.
2. **Child Class (Mobil Balap)**: Saat ingin membuat mobil balap, mereka tidak membuat desain dari nol. Mereka mengambil desain **Kendaraan Umum**, lalu menambah fitur `nitro()` dan mengubah fungsi `jalan()` agar jauh lebih cepat.
3. **`super()` (Telepon ke Markas)**: Saat mobil balap dinyalakan, ia tetap butuh prosedur starter mesin dari desain aslinya. Ia menggunakan fungsi `super()` untuk memanggil instruksi orisinal dari "orang tuanya" sebelum menjalankan fitur tambahannya sendiri.

## 2. Istilah Kunci (Key Terms)

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| Parent / Base Class | Class asal yang mewariskan kode. | `class Kendaraan:` |
| Child / Derived Class | Class baru yang menerima warisan. | `class Mobil(Kendaraan):` |
| Method Overriding | Menulis ulang method milik Parent di dalam Child agar perilakunya berubah. | `def jalan(self):` |
| `super()` | Fungsi untuk memanggil method milik Parent Class dari dalam Child Class. | `super().__init__()` |

## 3. Konsep Utama

### Cara Melakukan Pewarisan
Cukup masukkan nama Parent Class di dalam kurung saat mendefinisikan class baru.
```python
class Parent:
    def sapa(self):
        print("Halo dari Orang Tua")

class Child(Parent):
    pass # Child otomatis punya method sapa()
```

### Menggunakan `super()`
Sangat penting digunakan di dalam `__init__` agar atribut milik Parent tetap terinisialisasi dengan benar.
```python
class Smartphone(Phone):
    def __init__(self, merk, OS):
        super().__init__(merk) # Panggil init milik Phone
        self.OS = OS
```

### Method Overriding
Jika Parent punya method `suara()` dan Child juga punya `suara()`, maka yang akan dijalankan adalah versi milik Child. Versi Parent "ditimpa" atau dimodifikasi.

## 4. Visualisasi Analogi

*(Aset Visual SVG sedang dalam pengembangan)*

## 5. Peringatan / Jebakan Umum (Gotchas)
- **Lupa `super()`**: Jika Anda menimpa `__init__` tanpa memanggil `super().__init__()`, maka atribut yang seharusnya ada di Parent Class (seperti merk atau id) tidak akan pernah dibuat. Objek Anda akan "cacat".
- **Fragile Base Class**: Berhati-hatilah mengubah Parent Class. Karena jika Parent rusak, seluruh Child Class yang jumlahnya mungkin puluhan juga akan ikut rusak.

## 6. Referensi Kode Praktik
Contoh pewarisan tersedia di folder `examples/`:
- `01_basic_inheritance.py`: Kasus sederhana pewarisan hewan.
- `02_super_function.py`: Penggunaan `super()` untuk mengembangkan fitur secara bertingkat.

## 7. Latihan (Validasi)
- [ ] Buat Class `Karyawan` dengan atribut `nama` dan `gaji`.
- [ ] Buat Child Class `Manager` yang mewarisi `Karyawan`.
- [ ] Gunakan `super()` untuk mengisi `nama` dan `gaji`, lalu tambahkan atribut baru `tunjangan` khusus untuk Manager.
- [ ] Override method `tampilkan_gaji()` agar Manager menampilkan Gaji + Tunjangan.
