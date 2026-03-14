# Panduan Struktur (Structure Guide)

Proyek **Python Knowledge Universe** disusun dengan analogi **Perpustakaan** untuk memudahkan navigasi konsep mulai dari yang paling luas hingga yang paling spesifik.

Semua penulisan aturan, kerangka, dan penataan menggunakan **Bahasa Indonesia** sebagai standar.

## Analogi Struktur

Berikut adalah pemetaannya ke dalam direktori:

| Tingkatan | Analogi | Contoh Direktori | Keterangan |
| :--- | :--- | :--- | :--- |
| **Level 1** | **Perpustakaan** | `/` (root) | Seluruh sistem proyek. |
| **Level 2** | **Rak (Shelf)** | `core/`, `specializations/` | Pengelompokan besar antara dasar bahasa (core) dan terapan ekosistem (specializations). |
| **Level 3** | **Sub-Rak (Sub-shelf)** | `core/01_fundamentals/` | Fase pembelajaran atau kategori domain (misal: tahap pemahaman dasar, atau domain data science). |
| **Level 4** | **Buku** | `core/01_fundamentals/01_python_basics/` | Kumpulan topik khusus yang dipelajari utuh. |
| **Level 5** | **Bab (Chapter)** | `01_variables/` | Folder berisi materi spesifik. Di dalamnya terdapat `README.md` (Teks inti), `assets/` (Gambar), dan `examples/` (Kode Python). |

## Aturan Pewajiban `README.md`

Guna memudahkan orientasi (agar pembaca tahu mereka sedang ada di "rak" sebelah mana), **setiap direktori (Rak, Sub-Rak, Buku) WAJIB memiliki file `README.md`**.

- **Di level Rak** (`core/README.md`): Menjelaskan tujuan keseluruhan rak ini.
- **Di level Sub-Rak** (`core/01_fundamentals/README.md`): Menjelaskan fase ini, apa sasarannya, dan buku-buku apa yang ada di dalamnya.
- **Di level Buku** (`.../01_python_basics/README.md`): Bertindak sebagai pengantar materi bab-bab di dalam buku tersebut (Mirip Kata Pengantar / Daftar Isi).

## Konvensi Penamaan

1. **Folder / File (selain `README.md`)**: Penamaan menggunakan *snake_case* dengan awalan angka numerik `01_`, `02_`, dst untuk memastikan urutan pembelajaran (contoh: `01_python_basics`, `01_web_development`).
2. **Konvensi Bab**:
   - Seluruh Bab adalah **sebuah folder**, bukan file Markdown tunggal.
   - Misalnya `01_sejarah_python/`, lalu di dalamnya ditempatkan `README.md` untuk menuliskan teks babnya.
   - Semua gambar, PDF, dll yang dibutuhkan oleh bab tersebut disimpan terpisah di sub-folder `assets/` khusus milik bab tersebut.
   - Sama halnya dengan skrip kode, ia dipisah ke dalam folder `examples/` di dalam bab yang mempergunakannya.

## Templat Buku
Setiap folder Buku baru wajib distrukturkan seperti ini:
```text
<urutan>_<nama_buku>/
|-- README.md        <- Wajib ada. Menjelaskan isi buku (Pengantar/Daftar Isi).
|-- CHANGELOG.md     <- Aturan log & versioning draft(Unreleased).
`-- 01_<nama_bab>/   <- Folder bab
    |-- README.md    <- Berupa materi teks.
    |-- assets/      <- Gambar, diagram untuk bab ini.
    `-- examples/    <- Semua skrip python dari materi bab ini.
```
