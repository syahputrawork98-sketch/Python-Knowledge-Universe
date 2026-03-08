# Python Knowledge Universe

Python Knowledge Universe adalah rak buku digital tentang Python yang disusun terstruktur, modular, dan terus berkembang.

Repository ini dirancang sebagai:
- sistem pembelajaran Python
- peta pengetahuan Python
- fondasi website dokumentasi
- portfolio teknikal

Tujuan utamanya adalah membangun struktur pengetahuan Python yang jelas, bertahap, dan mudah dipahami oleh manusia maupun AI.

## Tujuan Proyek

- menyusun pengetahuan Python secara sistematis
- menyediakan jalur belajar Python yang jelas
- menjadi referensi Python jangka panjang
- menjadi dokumentasi yang terus berkembang
- menjadi dasar untuk website pembelajaran Python

## Struktur Pengetahuan

Repository ini dibagi menjadi dua bagian utama.

### 1. Core Python

Core adalah sub-rak fondasi. Setiap folder di dalam `core/` adalah buku utama.

Direktori inti:
- `core/01_python_basics`
- `core/02_language_design`
- `core/03_execution_model`
- `core/04_object_model`
- `core/05_memory_management`
- `core/06_modules_import_system`
- `core/07_standard_library`
- `core/08_file_system_io`
- `core/09_networking`
- `core/10_concurrency`
- `core/11_async_programming`
- `core/12_testing`
- `core/13_packaging`
- `core/14_virtual_environments`
- `core/15_tooling`

### 2. Python Specializations

Specializations adalah sub-rak terapan. Setiap domain di dalam `specializations/` adalah sub-rak domain, lalu di dalamnya akan berisi banyak buku.

Setelah memahami Core Python, pembaca dapat melanjutkan ke jalur:
- Web Development
- Data Science
- Machine Learning
- AI Engineering
- Automation

## Arsitektur Rak

Model organisasi repository ini:

1. `root` adalah rak utama (library Python Knowledge Universe).
2. `core/` adalah sub-rak fondasi.
3. `core/<book>/` adalah buku.
4. `specializations/` adalah sub-rak terapan.
5. `specializations/<domain>/` adalah sub-rak domain.
6. `specializations/<domain>/<book>/` adalah buku di domain tersebut.

## Struktur Repository

```text
python-knowledge-universe/
|
|-- README.md
|-- docs/
|   |-- roadmap.md
|   |-- glossary.md
|   `-- contribution-guide.md
|
|-- core/
|   |-- README.md
|   |-- 01_python_basics/
|   |-- 02_language_design/
|   |-- 03_execution_model/
|   |-- 04_object_model/
|   |-- 05_memory_management/
|   |-- 06_modules_import_system/
|   |-- 07_standard_library/
|   |-- 08_file_system_io/
|   |-- 09_networking/
|   |-- 10_concurrency/
|   |-- 11_async_programming/
|   |-- 12_testing/
|   |-- 13_packaging/
|   |-- 14_virtual_environments/
|   `-- 15_tooling/
|
`-- specializations/
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

## Cara Menggunakan Repository

### 1. Jalur Belajar Berurutan

Urutan rekomendasi untuk pemula:

1. Python Basics
2. Language Design
3. Execution Model
4. Object Model
5. Memory Management
6. Modules and Import System
7. Standard Library
8. File System and IO
9. Networking
10. Concurrency
11. Async Programming
12. Testing
13. Packaging
14. Virtual Environments
15. Tooling

Lanjutkan ke bagian specialization setelah menyelesaikan core.

### 2. Jalur Referensi

Jika sudah familiar dengan Python, pembaca dapat langsung menuju topik tertentu sesuai kebutuhan.

## Status Proyek

- `Planned`: topik direncanakan
- `In Progress`: topik sedang ditulis
- `Published`: topik tersedia
- `Revision`: topik perlu diperbarui

## Kontribusi

Kontribusi terbuka untuk:
- perbaikan dokumentasi
- penambahan topik
- contoh kode
- peningkatan struktur

Lihat panduan kontribusi di `docs/contribution-guide.md`.

## Visi Jangka Panjang

- website dokumentasi Python
- sistem pembelajaran Python
- knowledge base Python
- referensi teknikal Python

## Filosofi Proyek

Belajar Python bukan hanya tentang sintaks, tetapi memahami bagaimana bahasa ini bekerja secara mendalam.

## Author

Project ini dibuat sebagai bagian dari perjalanan belajar dan eksplorasi Python.
