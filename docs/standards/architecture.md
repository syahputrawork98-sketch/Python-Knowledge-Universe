# Arsitektur & Hierarki Struktur (Python Edition)

Proyek **Python Knowledge Base** disusun dengan analogi **Perpustakaan Pythonic (The Pythonic Library)** untuk mentransformasika dokumentasi teknis (seperti Python Docs, PEP, & Standard Library) menjadi unit pelajaran yang sistematis dan mudah dipahami.

## Analogi Struktur

Berikut adalah pemetaannya ke dalam direktori bertingkat:

| Tingkatan | Analogi | Contoh Direktori | Keterangan |
| :--- | :--- | :--- | :--- |
| **Level 1** | **Perpustakaan (Library)** | `/` (root) | Seluruh sistem proyek (Python Engine). |
| **Level 2** | **Rak (Shelf)** | `RAK-01-setup/` | Pengelompokan besar domain ilmu. |
| **Level 3** | **Sub-Rak (Sub-shelf)** | `SR-01_Foundations/` | Grup materi berbasis area spesifik. |
| **Level 4** | **Buku (Book)** | `BK-01_Tutorial/` | Koleksi bab yang membentuk satu topik besar. |
| **Level 5** | **Bab (Chapter)** | `CH-01_Overview/` | Unit terkecil wajib (Folder Bab). |

---

## Karakteristik & Autentisitas (Branding)

Untuk menjaga "nyawa" dan keunikan bahasa Python, setiap konten wajib mengikuti pedoman berikut:

- **Analogi Utama**: **Perpustakaan Pythonic (The Pythonic Library)**.
- **Tone Suara**: **Ramah, Edukatif, dan "Zen"**. Python adalah tentang keterbacaan; tulislah narasi yang mengalir seperti membaca buku yang bagus.
- **Filosofi Penulisan**: Fokus pada *Readability* dan *Simplicity* (The Zen of Python). Tekankan prinsip "There should be one-- and preferably only one --obvious way to do it."
- **Visual**: Gunakan estetika yang bersih dan hangat, mencerminkan sifat Python yang "Batteries Included".

---

## Aturan Pewajiban `README.md`

Guna memudahkan navigasi, setiap tingkatan direktori **WAJIB** memiliki file `README.md`:

- **Root (`/README.md`)**: Visi keseluruhan (The Pythonic Architect 🐍).
- **Rak (`RAK-XX/README.md`)**: Tujuan dan cakupan Rak tersebut.
- **Buku (`BK-XX/README.md`)**: Sinopsis dan orientasi filosofis materi.
- **Bab (`CH-XX/README.md`)**: Materi inti (PPM Stage 1).

---

## Kriteria "Gold Standard" (100% Complete)

Sebuah unit dianggap **Completed** jika memenuhi 4 pilar kualitas:

> [!IMPORTANT]
> **Pilar 1: Documentation-Sync Accurate**  
> Konten diverifikasi terhadap dokumentasi resmi Python (`docs.python.org`).
>
> **Pilar 2: Pythonic Examples**  
> Minimal 1 contoh kode (`.py`) di folder `examples/`.  
> *Catatan*: Jika materi bersifat teoretis, tetap buat file `.py` dengan komentar penjelasan.
>
> **Pilar 3: Mental Model Visual**  
> Minimal 1 diagram (Mermaid/SVG) di folder `assets/`.
>
> **Pilar 4: Narrative Excellence**  
> Penjelasan menggunakan standar PPM V4: Manusiawi, ada analogi, dan menggunakan **Bahasa Arsitek (Senior Terminology)**.
