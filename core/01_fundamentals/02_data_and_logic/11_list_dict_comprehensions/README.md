# Bab 11: List & Dict Comprehensions

Chapter Code: CORE-02-11
Version: Core.Fundamentals.02.00
Last Updated: 2026-03-14
Status: Draft

> **Deskripsi Singkat**: Menulis pembuatan dan transformasi koleksi data (*list, dict, set*) secara ringkas, elegan, dan lebih cepat daripada perulangan biasa.

## 1. Analogi (Pendekatan Konsep)

### Analogi Singkat
> "Comprehension itu seperti **mesin pemilah buah otomatis**: Anda memasukkan satu keranjang buah (data), mesin memutuskkan buah mana yang diambil (filter), lalu mesin langsung menatanya di keranjang baru (list baru)."

### Analogi Panjang / Cerita (Saringan)
Bayangkan Anda memiliki daftar **Nama Peserta** dan ingin mengambil hanya nama yang berakhiran "i".
- **Cara Lama**: Anda mengambil keranjang kosong, melihat nama satu-per-satu, jika berakhiran "i" Anda masukkan ke keranjang. (Sangat manual).
- **Comprehension**: Anda memasang **Saringan Ajaib** di mulut keranjang baru. Saringan itu berkata: "Ambil `nama` dari `daftar` JIKA `nama` diakhiri 'i'". Dalam satu gerakan, keranjang baru terisi.

## 2. Istilah Kunci (Key Terms)

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| Comprehension | Karakteristik sintaks Python untuk membuat koleksi data dari iterabel lain. | `[x for x in data]` |
| Expression | Operasi atau nilai yang akan dimasukkan ke dalam list baru. | `x**2` |
| Filtering | Bagian `if` opsional untuk menyaring data yang memenuhi syarat. | `if x > 10` |
| List Comprehension | Menghasilkan objek `list`. | `[...]` |
| Dict Comprehension | Menghasilkan objek `dict` (pasangan key-value). | `{k:v ...}` |

## 3. Konsep Utama

### List Comprehension
**Sintaks:** `[expression for item in iterable if condition]`
```python
angka = [1, 2, 3, 4]
kuadrat = [x**2 for x in angka] # [1, 4, 9, 16]
genap = [x for x in angka if x % 2 == 0] # [2, 4]
```

### Dict Comprehension
Sangat berguna untuk memetakan atau membalikkan dictionary.
```python
# Membuat dict dari list
nama = ["Budi", "Siti"]
panjang_nama = {n: len(n) for n in nama} # {'Budi': 4, 'Siti': 4}
```

## 4. Peringatan / Jebakan Umum (Gotchas)
- **Hindari ini**: Menulis comprehension yang terlalu panjang dan rumit (misal: ada 3 level nested loop). Jika sulit dibaca, gunakan perulangan `for` biasa. Ingat semboyan: *Readability counts*.
- **Ingat bahwa**: Comprehension mengonsumsi memori secara instan untuk membuat list baru. Untuk data berukuran raksasa, pertimbangkan menggunakan *Generator Expression* `(x for x in ...)` yang akan dibahas di materi Lanjutan.

## 5. Referensi Kode Praktik
Silakan lihat skrip lengkapnya pada direktori `examples/` di dalam bab ini.

```python
# Mentransformasi teks
teks = "python"
kapital = [t.upper() for t in teks] # ['P', 'Y', 'T', 'H', 'O', 'N']
```
