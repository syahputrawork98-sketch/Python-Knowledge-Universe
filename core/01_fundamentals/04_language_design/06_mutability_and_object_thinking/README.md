# Bab 06: Mutability and Object Thinking

Chapter Code: CORE-04-06
Version: Core.Fundamentals.04.01
Last Updated: 2026-03-15
Status: Published

> **Deskripsi Singkat**: Memahami cara kerja objek di memori, mengapa ada data yang bisa diubah (Mutable) dan ada yang tetap (Immutable), serta cara menghindari bug "data yang berubah sendiri".

## 1. Analogi (Pendekatan Konsep)

### Analogi Singkat
> "Objek **Mutable** itu seperti **Papan Tulis Bersama**—siapa pun yang punya spidol bisa mengubah isinya, dan semua orang akan melihat perubahannya. Sementara objek **Immutable** itu seperti **Prasasti Batu**—isinya tidak bisa diganti. Jika ingin tulisan berbeda, Anda harus memahat prasasti yang baru."

### Analogi Panjang (Tanah Liat vs Balok Es)
Bayangkan Anda memiliki dua jenis wadah untuk menyimpan barang.

Wadah pertama terbuat dari **Tanah Liat (Mutable)**. Jika Anda ingin mengubah bentuknya (misal dari bulat menjadi kotak), Anda cukup menekan-nekan tanah liat tersebut. Wadahnya tetap sama, tapi bentuknya berubah. Di Python, ini seperti `List` atau `Dictionary`. Anda bisa menambah atau menghapus isinya tanpa mengganti objeknya.

Wadah kedua terbuat dari **Balok Es (Immutable)**. Di dalam es tersebut tertanam sebuah mainan. Jika Anda ingin mengganti mainannya, Anda tidak bisa membongkar es itu tanpa menghancurkannya. Anda harus membekukan balok es yang baru dengan mainan yang berbeda. Di Python, ini seperti `String` atau `Tuple`. Jika Anda "mengubah" sebuah string, sebenarnya Python membuatkan string baru untuk Anda di memori.

Memahami kapan menggunakan "Tanah Liat" dan kapan menggunakan "Es" adalah kunci agar program Anda tidak memiliki perilaku yang membingungkan.

## 2. Istilah Kunci (Key Terms)

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| Mutability | Kemampuan sebuah objek untuk diubah isinya setelah dibuat | `list`, `dict`, `set` |
| Immutability | Sifat objek yang isinya tidak bisa diubah sama sekali | `str`, `int`, `tuple` |
| Reference | Alamat atau label yang menunjuk ke objek di memori | `b = a` (keduanya menunjuk lokasi sama) |
| Shared State | Kondisi di mana beberapa bagian kode berbagi satu objek mutable | Satu list config dipakai di 5 fungsi |
| Side Effect | Perubahan yang tidak sengaja terjadi pada data di luar fungsi | Fungsi yang diam-diam mengubah list input |

## 3. Konsep Utama

### A. Wadah vs Isi (Reference)
Di Python, variabel bukanlah kotak yang berisi nilai, melainkan **Label** yang ditempelkan pada objek. Jika Anda membuat `b = a`, Anda sebenarnya menempelkan dua label pada satu objek yang sama. Jika objek itu mutable (seperti List), mengubah lewat label `a` akan membuat label `b` juga ikut berubah isinya.

### B. Bahaya Perubahan Tak Sengaja
Shared Mutable State adalah sumber bug yang paling sulit dilacak. Jika Anda mengirim sebuah List ke dalam fungsi, dan fungsi itu mengubah isinya, maka List asli Anda di luar fungsi juga akan ikut berubah. Ini disebut *Side Effect*.

### C. Kapan Pakai Immutable?
Gunakan objek Immutable (seperti Tuple) saat Anda ingin menjamin bahwa data tersebut tidak akan pernah berubah selama program berjalan. Ini sangat berguna untuk kunci dictionary atau data konfigurasi yang harus stabil.

### D. Identitas Objek
Gunakan fungsi `id()` untuk mengecek apakah dua variabel menunjuk ke objek yang sama persis di memori, atau gunakan operator `is`. Ingat: Dua objek bisa punya isi yang sama, tapi identitas yang berbeda.

## 4. Visualisasi Analogi

![Mutable vs Immutable - Clay Boxes and Sturdy Stones](assets/06_mutability_and_object_thinking.svg)

## 5. Peringatan / Jebakan Umum (Gotchas)

- **"Dampaknya ke Mana-mana"**: Hati-hati saat meng-copy list dengan `b = a`. Gunakan `b = a.copy()` jika Anda ingin membuat List baru yang isinya sama tapi terpisah identitasnya.
- **Mutable Default Argument**: Jangan pernah gunakan `def tambah_data(item, daftar=[])`. List `daftar` itu akan disimpan terus di memori dan isinya akan menumpuk setiap kali fungsi dipanggil. Gunakan `daftar=None` sebagai gantinya.
- **Shared References**: Mengubah isi list di dalam list lain sering kali menimbulkan kejutan jika Anda tidak memahami konsep *Shallow Copy* vs *Deep Copy*.

## 6. Referensi Kode Praktik

Buka folder `examples/` untuk melihat penerapan langsung:
- `01_reference_demo.py`: Bukti visual bahwa `b = a` tidak menyalin data, melainkan menyalin alamat.
- `02_mutable_defaults_fix.py`: Cara memperbaiki bug klasik "parameter yang ingat masa lalu".

## 7. Latihan (Validasi)

- [ ] Matikan komputer (opsional), ambil kertas, dan gambarkan alur referensi variabel saat Anda melakukan `a = [1]`, `b = a`, dan `a.append(2)`.
- [ ] Buatlah sebuah fungsi yang menerima list, tapi fungsi tersebut WAJIB mengembalikan list baru tanpa mengubah isi list aslinya.
- [ ] Buktikan lewat kode bahwa `str` adalah immutable dengan cara mencoba mengubah satu karakter di dalamnya menggunakan index (misal `s[0] = 'X'`) dan lihat error apa yang muncul.
