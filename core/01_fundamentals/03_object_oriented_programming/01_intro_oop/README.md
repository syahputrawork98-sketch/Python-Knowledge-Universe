# Bab 01: Intro to OOP Concept

Chapter Code: CORE-03-01
Version: Core.Fundamentals.03.00
Last Updated: 2026-03-14
Status: Draft

> **Deskripsi Singkat**: Sebelum masuk ke kode, kita perlu memahami MENGAPA kita membutuhkan Pemrograman Berorientasi Objek (OOP) dan bagaimana ia mengubah cara kita memandang data dan fungsi.

## 1. Analogi (Pendekatan Konsep)

### Analogi Singkat
> "Pemrograman Prosedural itu seperti **Daftar Belanja** (langkah demi langkah), sedangkan OOP adalah **Kumpulan Alat Terorganisir** (benda yang punya fungsi sendiri-sendiri)."

### Analogi Panjang / Cerita (Simulasi Kota)
Bayangkan Anda sedang membangun sebuah game **Simulasi Kota**.

- **Cara Prosedural**: Anda memiliki variabel raksasa `posisi_mobil_x`, `posisi_mobil_y`, `posisi_bus_x`, `posisi_bus_y`. Lalu Anda punya fungsi `pindahkan_kendaraan(x, y)`. Semakin banyak kendaraan, kode Anda akan dipenuhi oleh ribuan variabel yang berserakan. Anda harus mengingat kendaraan mana yang menggunakan data mana.
- **Cara OOP**: Anda mendefinisikan sebuah konsep bernama **Kendaraan**. Setiap kendaraan (Mobil, Bus, Motor) adalah "benda" yang membawa datanya sendiri (posisinya) dan kemampuannya sendiri (jalan, berhenti). Anda tidak lagi mengelola ribuan koordinat, Anda mengelola sekelompok "kendaraan" yang tahu cara mengurus diri mereka sendiri.

## 2. Istilah Kunci (Key Terms)

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| Paradigma | Cara pandang atau gaya dalam menulis program. | Prosedural, OOP |
| Procedural | Pemrograman yang berfokus pada urutan instruksi dan fungsi. | Skrip linear |
| OOP | *Object Oriented Programming*, fokus pada "objek" yang menggabungkan data dan perilaku. | `car.drive()` |
| Data | Informasi yang disimpan oleh objek. | `color = "Red"` |
| Behavior | Aksi atau fungsi yang bisa dilakukan oleh objek. | `drive()` |

## 3. Konsep Utama

### Mengapa OOP?
1. **Organisasi**: Mengelompokkan data dan fungsi yang berhubungan ke dalam satu wadah.
2. **Reusability**: Kode yang sudah dibuat bisa digunakan kembali dengan mudah.
3. **Maintainability**: Jika ada kesalahan pada "Mobil", Anda hanya perlu memperbaiki bagian "Mobil", bukan seluruh program.
4. **Scalability**: Memudahkan pembangunan sistem besar yang kompleks.

## 4. Visualisasi Analogi

*(Aset Visual SVG sedang dalam pengembangan)*

## 5. Peringatan / Jebakan Umum (Gotchas)
- **Kapan TIDAK memakai OOP**: Jangan memaksakan OOP untuk skrip sederhana 5 baris yang hanya menghitung angka. Gunakan OOP saat data Anda mulai kompleks dan saling berhubungan.
- **Over-engineering**: Membuat terlalu banyak class yang rumit padahal bisa diselesaikan dengan fungsi sederhana.

## 6. Referensi Kode Praktik
Silakan lihat perbandingan gaya koding di folder `examples/`:
- `01_procedural_vs_oop.py`: Perbandingan nyata antara dua gaya pemrograman.

## 7. Latihan (Validasi)
- [ ] Sebutkan 3 benda di sekitar Anda dan sebutkan 2 Atribut (Data) serta 2 Method (Perilaku) untuk benda tersebut.
- [ ] Mengapa kita tidak menggunakan gaya prosedural untuk membangun software raksasa seperti Instagram atau Windows?
