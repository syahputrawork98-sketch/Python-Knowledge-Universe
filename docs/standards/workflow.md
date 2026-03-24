# Alur Kerja Penulisan (PPM) V4 - Python Edition

Proyek **Python Knowledge Base** disusun dengan standar **Unified Gold Standard**. 

## Tahapan PPM (Prosedur Penulisan Materi) V4

Setiap penyusunan `README.md` unit materi (CH/SEC) wajib disusun dengan **urutan representasi** 5 Tahapan (Gold Standard) berikut secara disiplin:

### 1. Tahap 1: Source Alignments & Judul
- **Header**: Judul materi yang diiringi dengan metafora/analogi singkat.
- **Source Link**: Tautan spesifik langsung ke docs.python.org atau PEP yang relevan sebagai jaminan akurasi.

### 2. Tahap 2: Konsep & Esensi (Definisi & Rasionalitas)
- **Definisi ("Apa itu?")**: Menjelaskan konsep dasar secara formal dan teknis.
- **Rasionalitas ("Why & How?")**: Membedah alasan fitur diciptakan dan masalah apa yang ia selesaikan.
- **Analogi Model Mental**: Menjabarkannya dalam contoh dunia nyata.
- **Terminologi Teknis**: Istilah senior yang digunakan oleh arsitek.

### 3. Tahap 3: Visualisasi Sistem (Mermaid)
- **Inline Diagram**: Diagram Mermaid (seperti *Call Stack*, *Memory Layout*, *Bytecode Flow*) diletakkan secara **inline** (````mermaid````) tepat setelah penjelasan konsep. 
- **Fokus Visual**: Memfokuskan pada arus eksekusi atau manajemen memori berdasar konsep yang dibahas.

### 4. Tahap 4: Mekanisme Pembuktian (Algoritma Detil)
- **Detail Balik Layar**: Menguliti bagaimana kode dieksekusi oleh mesin CPython secara *Low-Level* (Bytecode, Evaluation Loop, Object C-API).

### 5. Tahap 5: Multi-file Lab Praktis (Examples)
- **Kewajiban Referensi**: Setiap teori yang dikemukakan di atas diakhiri dengan referensi pembelajaran praktik.
- **Struktur Folder `examples/`**: Harus memiliki beberapa skrip `.py` berurutan dengan prefix numerik (misal: `01_dasar.py`, `02_edge_cases.py`). 

### Pengecualian Eksplisit "Nil Content" (Narasi Sejarah)
Jika suatu unit (terutama di RAK-01) murni bersifat historis atau konseptual non-teknis:
- **Tulis Penafian**: Wajib menyertakan teks *"Unit ini tidak membutuhkan Lab Praktis/Visualisasi karena bersifat penjelasan sejarah/konsep naratif."* pada bagian `README.md` terkait.
- **Pelarangan Direktori**: **JANGAN** membuat direktori `assets/` maupun `examples/` yang pada akhirnya akan dibiarkan kosong, demi mencegah penumpukan struktur kosong.

---
*Target Akhir: Mencapai [Gold Standard](./architecture.md#kriteria-gold-standard-100-complete).*
