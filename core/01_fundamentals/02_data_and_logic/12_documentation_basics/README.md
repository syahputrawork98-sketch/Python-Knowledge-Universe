# Bab 12: Documentation Basics

Chapter Code: CORE-02-12
Version: Core.Fundamentals.02.00
Last Updated: 2026-03-14
Status: Draft

> **Deskripsi Singkat**: Mempelajari standar penulisan dokumentasi kode yang profesional agar kode mudah dipahami oleh manusia (termasuk diri sendiri di masa depan) menggunakan *Docstrings* dan *Type Hinting*.

## 1. Analogi (Pendekatan Konsep)

### Analogi Singkat
> "Kode tanpa dokumentasi adalah **mesin tanpa label tombol**: Anda mungkin tahu cara kerjanya sekarang, tapi sebulan lagi (atau bagi orang lain) itu hanyalah kotak hitam yang membingungkan."

### Analogi Panjang / Cerita (Masa Depan)
Bayangkan Anda menulis **Surat untuk Diri Sendiri di Masa Depan**.
Hari ini Anda jenius, Anda tahu persis fungsi `hit_tunj(g, t, a)` itu menghitung tunjangan gaji. Namun enam bulan lagi, Anda lupa apa itu `g, t, a`.
Dokumentasi berupa **Docstrings** adalah surat pendek di atas fungsi yang menjelaskan: "Ini fungsi hitung tunjangan, `g` adalah Gaji, `t` adalah Masa Tugas, `a` adalah Anak." Dengan membaca surat itu, Anda yang "kurang jenius" di masa depan langsung paham seketika.

## 2. Istilah Kunci (Key Terms)

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| Docstring | String literal di awal fungsi/kelas/modul untuk dokumentasi. | `"""Penjelasan"""` |
| Type Hinting | Menambahkan petunjuk tipe data pada variabel atau parameter fungsi. | `age: int` |
| Comment | Catatan pendek untuk menjelaskan "Mengapa" (bukan "Apa") kode dilakukan. | `# Mengatasi bug X` |
| `help()` | Fungsi bawaan Python untuk menampilkan dokumentasi sebuah objek. | `help(print)` |
| PEP 257 | Panduan resmi Python tentang konvensi penulisan Docstring. | - |

## 3. Konsep Utama

### Docstrings
Digunakan di baris pertama setelah definisi fungsi/kelas.
```python
def sapa(nama):
    """Menyapa pengguna dengan nama mereka."""
    print(f"Halo {nama}")

print(sapa.__doc__) # Mengakses dokumentasi
```

### Type Hinting (Modern Python)
Membantu Code Editor (IDE) memberikan saran dan mencegah kesalahan tipe data.
```python
def hitung_luas(p: float, l: float) -> float:
    return p * l
```

### Komentar vs Dokumentasi
- **Dokumentasi (Docstrings)**: Menjelaskan **Apa** fungsinya, apa inputnya, dan apa hasilnya. (Untuk pengguna fungsi).
- **Komentar (#)**: Menjelaskan **Mengapa** kode ditulis dengan cara tertentu, misal trik khusus atau peringatan bug. (Untuk pengembang kode).

## 4. Peringatan / Jebakan Umum (Gotchas)
- **Hindari ini**: Menulis komentar yang menjelaskan hal yang sudah jelas (e.g., `x = 10 # isi x dengan 10`). Kode yang bersih seharusnya "bercerita" sendiri.
- **Ingat bahwa**: Type hinting di Python bersifat **opsional** dan tidak dipaksakan oleh interpreter secara default. Python tetaplah bahasa yang dinamis, namun *type hinting* sangat membantu produktivitas tim.

## 5. Referensi Kode Praktik
Silakan lihat skrip lengkapnya pada direktori `examples/` di dalam bab ini.

```python
def bagi(a: int, b: int) -> float:
    """Membagi a dengan b. Mengembalikan float."""
    return a / b
```
