# Python Knowledge Base: Total Deconstruction Plan

> **Status Spec-Sync**: v3.13+ (Full Alignment)
> **Last Updated**: 2026-03-19

Arsitektur **Source-Driven 12-Rack** ini mencerminkan taksonomi asli [docs.python.org/3/](https://docs.python.org/3/).

---

## 🏗 Justifikasi Teknis (The Mirroring Principle)

Setiap Rak dipetakan langsung ke kategori navigasi utama di dokumentasi resmi Python.

### 1. RAK-01: Setup & Usage
Instalasi, konfigurasi environment, dan command line usage.

### 2. RAK-02: The Python Tutorial
Panduan naratif (Handbook) untuk memahami "Pythonic Way".

### 3. RAK-03: Language Reference
Spesifikasi formal sintaksis, data model, dan execution model.

### 4. RAK-04: Library Ref: Built-ins & Essentials
Fungsi bawaan, tipe data dasar, konstanta, dan exception.

### 5. RAK-05: Library Ref: Data & Text Processing
Manipulasi string (`re`), representasi data (`json`, `xml`), dan matematika.

### 6. RAK-06: Library Ref: OS & Concurrency
Interaksi sistem (`os`, `sys`), file system (`pathlib`), dan threading/asyncio.

### 7. RAK-07: Library Ref: Networking & Web
Protokol HTTP, socket programming, dan client/server utilities.

### 8. RAK-08: Python HOWTOs
Panduan tematik mendalam (Regex HOWTO, Logging HOWTO, etc.).

### 9. RAK-09: Distributing & Installing
Ekosistem `pip`, `venv`, `setuptools`, dan `wheel`.

### 10. RAK-10: Extending & C-API
Integrasi low-level dengan C/C++ dan penulisan extension.

### 11. RAK-11: What's New (Evolution)
Changelog rilis terbaru dan arah perkembangan PEP.

### 12. RAK-12: FAQs & Glossary
Kamus istilah dan jawaban atas pertanyaan umum komunitas.

---

## 🗄 Peta Arsitektur Detail

| Rak | Sub-Rak (SR) | Buku (BK) | Deskripsi BK |
| :--- | :--- | :--- | :--- |
| **RAK-01** | SR-01: Setup | BK-01: Installation | Windows/Mac/Linux setup. |
| **RAK-02** | SR-01: Tutorial | BK-01: Foundations | Variables, Control Flow. |
| | | BK-02: Data Structures | Lists, Dics, Tuples. |
| **RAK-03** | SR-01: Specs | BK-01: Data Model | Objects, types, & identity. |
| | | BK-02: Execution | Naming & Binding. |
| **RAK-04** | SR-01: Essentials | BK-01: Built-in Funcs | `print`, `len`, `range`. |
| | | BK-02: Exceptions | Hierarchy & Handling. |
| **RAK-05** | SR-01: Text | BK-01: String API | Formatting & Template. |
| | SR-02: Data | BK-02: Persistence | `pickle`, `sqlite3`, `csv`. |
| **RAK-06** | SR-01: Systems | BK-01: OS Interface | Files, Directories, Processes. |
| | SR-02: Async | BK-02: Concurrency | Threading vs Asyncio logic. |
| **RAK-07** | SR-01: Web | BK-01: Internet Pkgs | `urllib`, `http`, `smtplib`. |
| **RAK-08** | SR-01: Themes | BK-01: Logging | Advanced logging patterns. |
| **RAK-09** | SR-01: Packaging| BK-01: Virtual Envs | Dependency isolation. |
| **RAK-10** | SR-01: C-API | BK-01: Extending | Creating Python modules in C. |
| **RAK-11** | SR-01: Logs | BK-01: Release Notes | From Python 2 legacy to 3.x. |
| **RAK-12** | SR-01: Info | BK-01: Python FAQ | Technical & Design questions. |

---

## 📜 Log Sinkronisasi (Spec-Log)

| Versi Python | Tanggal Audit | Perubahan Arsitektur | Status |
| :--- | :--- | :--- | :--- |
| **v3.13** | 2026-03-19 | Inisialisasi 12-Rack (Source-Driven Python Docs). | ✅ Synced |
