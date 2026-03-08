# Python Specializations

Bagian ini adalah sub-rak terapan dari Python Knowledge Universe.

Jika `core/` membangun fondasi, maka `specializations/` menunjukkan bagaimana Python dipakai di konteks nyata per domain.

## Peran Bagian Specializations

- mengarahkan pembaca dari konsep dasar ke penerapan nyata
- menyediakan jalur belajar per domain
- menjadi tempat kumpulan buku tematik berbasis use case

## Struktur Sub-rak

Model organisasi di bagian ini:

1. `specializations/` adalah sub-rak terapan.
2. `specializations/<domain>/` adalah sub-rak domain.
3. `specializations/<domain>/<book>/` adalah buku di domain tersebut.

## Domain yang Tersedia

| Domain | Fokus | Contoh Topik Buku | Status |
|---|---|---|---|
| `web-development` | Pengembangan aplikasi web | backend API, auth, deployment | Planned |
| `data-science` | Analisis data dan visualisasi | data wrangling, EDA, dashboarding | Planned |
| `machine-learning` | Pengembangan model ML | feature engineering, model training, evaluation | Planned |
| `ai-engineering` | Sistem AI berbasis Python | LLM apps, RAG, AI pipelines | Planned |
| `automation` | Otomatisasi proses dan tugas | scripting, workflow automation, task runners | Planned |

## Struktur Direktori

```text
specializations/
|
|-- README.md
|-- web-development/
|   |-- README.md
|   `-- <book>/
|-- data-science/
|   |-- README.md
|   `-- <book>/
|-- machine-learning/
|   |-- README.md
|   `-- <book>/
|-- ai-engineering/
|   |-- README.md
|   `-- <book>/
`-- automation/
    |-- README.md
    `-- <book>/
```

## Cara Menggunakan Bagian Ini

1. Selesaikan fondasi di `core/` sesuai domain yang ingin dipilih.
2. Pilih satu domain specialization.
3. Ikuti buku dalam domain secara berurutan (`01_`, `02_`, `03_`, dst).
4. Gunakan jalur referensi jika hanya butuh topik tertentu.

## Standar Isi Buku Specialization

- setiap buku berada dalam folder bernomor, contoh `01_llm_fundamentals`
- setiap buku wajib punya `README.md` sebagai peta isi
- buku harus memisahkan bagian konsep, praktik, dan project
- setiap buku wajib menyebut prasyarat Core yang dibutuhkan
- referensi teknis harus mengutamakan dokumentasi resmi

## Filosofi Specializations

Core Python memberi fondasi umum.

Specializations memberi arah penerapan Python agar pembaca mampu membangun solusi nyata sesuai domain.
