# BK-03: Package Management (Manajemen Paket) [x] Complete

> **"A library is someone else's code that you can use to build your dream."**

Buku ini membedah **`pip`** (Package Installer for Python), gerbang menuju ekosistem raksasa PyPI (Python Package Index). Kita akan mempelajari cara mengelola dependensi pihak ketiga secara disiplin agar proyek Anda dapat berjalan di mana saja dengan andal.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
- **Strategic Blueprint**: [RAK-02 Foundation](file:///i:/Workspace/Workspace-Syahputrawork/learning-matrix-blueprint/01-Language-Hubs/Python-Knowledge-Base.md)

---

## 🧠 The Essence (Narrative)
Python memiliki salah satu ekosistem terbuka terbesar di dunia. Menggunakan `pip`, kita bisa memanggil fungsionalitas canggih (seperti AI, Web Server, Analisis Data) hanya dengan satu baris perintah. Namun, kekuatan ini membawa risiko ketidakcocokan versi (*Dependency Hell*). Oleh karena itu, mencatat versi paket dalam `requirements.txt` atau `pyproject.toml` adalah langkah wajib untuk menjaga integritas proyek.

---

## 🎨 Visual Logic (Dependency Workflow)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph LR
    PyPI[PyPI Repository] -- 1. pip install --> Local[Local venv]
    Local -- 2. pip freeze --> Req[requirements.txt]
    Req -- 3. pip install -r --> NewMachine[New Environment]
    style PyPI fill:#3776AB,stroke:#333,color:#fff
    style Req fill:#FFD43B,stroke:#333,color:#000
```

---

## 📑 Daftar Bab (The Syllabus)

| Bab | Fokus | Spesifikasi |
| :--- | :--- | :--- |
| **[CH-01_PipUsage](./CH-01_PipUsage/)** | Basics | `install`, `uninstall`, and `freeze`. |
| **[CH-02_StandardPackaging](./CH-02_StandardPackaging/)** | Standards | `requirements.txt` vs `pyproject.toml`. |

---

## ⚠️ Pitfalls
- **Missing Versioning**: Jangan menginstal paket tanpa mencatat versinya. Jika di masa depan paket tersebut meng-update kodenya (breaking change), proyek Anda akan rusak tanpa peringatan. Selalu gunakan `pip freeze > requirements.txt`.
- **Source Trust**: Jangan menginstal paket dari sumber yang tidak dikenal. Selalu periksa popularitas dan pemeliharaan paket di PyPI untuk menghindari *Malware* atau paket yang sudah ditinggalkan.

---
*Back to [SR-01 Environment Setup](../README.md)*
