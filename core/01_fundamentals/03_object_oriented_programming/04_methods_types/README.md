# Bab 04: Types of Methods

Chapter Code: CORE-03-04
Version: Core.Fundamentals.03.00
Last Updated: 2026-03-14
Status: Draft

> **Deskripsi Singkat**: Tidak semua method diciptakan sama. Bab ini membahas perbedaan antara Instance Method, Class Method, dan Static Method, serta kapan waktu yang tepat untuk menggunakan masing-masing tipe.

## 1. Analogi (Pendekatan Konsep)

### Analogi Singkat
> "**Instance Method** adalah tugas Karyawan (bekerja untuk satu orang), **Class Method** adalah tugas Manajer (mengurus seluruh kantor), dan **Static Method** adalah tugas Konsultan Luar (tidak butuh data kantor, hanya memberi saran teknis)."

### Analogi Panjang / Cerita (Sistem Kepegawaian)
Bayangkan sebuah **Perusahaan IT**.
1. **Instance Method (Karyawan)**: Saat Anda menyuruh karyawan "Tulis Kode!", ia harus tahu laptop *milik siapa* yang dipakai dan proyek *apa* yang ia kerjakan sendiri. Ia butuh `self` untuk mengakses data personalnya.
2. **Class Method (Manajer)**: Manajer tidak peduli detail harian satu karyawan. Ia fokus pada "Perusahaan". Jika Anda bertanya "Berapa total karyawan kita?", Manajer akan melihat data seluruh Perusahaan (`cls`). Ia menggunakan decorator `@classmethod`.
3. **Static Method (Konsultan)**: Perusahaan memanggil konsultan hanya untuk mengecek "Apakah format dokumen ini valid?". Konsultan tidak butuh tahu siapa karyawannya atau berapa total modal perusahaan. Ia hanya menjalankan fungsi logika murni tanpa akses ke data internal. Ia menggunakan decorator `@staticmethod`.

## 2. Istilah Kunci (Key Terms)

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| Instance Method | Method standar yang memiliki akses ke `self` (data objek). | `def work(self):` |
| Class Method | Method yang memiliki akses ke `cls` (data class) menggunakan `@classmethod`. | `def total(cls):` |
| Static Method | Method mandiri yang tidak punya akses ke data objek atau class. | `@staticmethod` |
| `@` (Decorator) | Simbol khusus untuk memodifikasi perilaku fungsi atau method. | `@classmethod` |

## 3. Konsep Utama

### Instance Method
Tipe method yang paling umum. Digunakan untuk aksi yang mengubah atau membaca data unik milik satu objek.
```python
class Robot:
    def greet(self):
        print(f"Halo, saya {self.nama}")
```

### Class Method (`@classmethod`)
Digunakan untuk aksi yang berkaitan dengan "Cetak Biru" itu sendiri, bukan satu unit spesifik. Parameter pertamanya adalah `cls`.
```python
class Robot:
    total_robot = 0
    @classmethod
    def tambah_populasi(cls):
        cls.total_robot += 1
```

### Static Method (`@staticmethod`)
Digunakan untuk fungsi pembantu (*utility*) yang diletakkan di dalam class hanya agar kodenya terorganisir, padahal ia tidak butuh data class atau objek.
```python
class Kalkulator:
    @staticmethod
    def is_prima(n):
        # Logika matematika murni
        pass
```

## 4. Visualisasi Analogi

*(Aset Visual SVG sedang dalam pengembangan)*

## 5. Peringatan / Jebakan Umum (Gotchas)
- **Lupa @**: Jika Anda lupa menulis `@classmethod` tapi menggunakan `cls` sebagai parameter, Python akan menganggapnya sebagai `self` biasa dan program akan error.
- **Kapan pakai Static?**: Jika method Anda sama sekali tidak memanggil `self.sesuatu` atau `cls.sesuatu`, maka method tersebut secara teknis adalah Static Method.

## 6. Referensi Kode Praktik
Contoh perbandingan method tersedia di folder `examples/`:
- `01_method_types.py`: Demonstrasi ketiga tipe method dalam satu class.

## 7. Latihan (Validasi)
- [ ] Buat Class `Bank` dengan atribut class `bunga = 0.05`.
- [ ] Buat Instance Method untuk menabung (mengubah saldo personal).
- [ ] Buat Class Method untuk mengubah nilai bunga bank secara global.
- [ ] Buat Static Method untuk memvalidasi apakah nomor rekening mengandung 10 digit.
