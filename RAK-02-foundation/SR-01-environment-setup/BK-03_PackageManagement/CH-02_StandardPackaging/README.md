# CH-02: Standard Packaging (The Modern Standard) [x] Complete

> **"A project is more than just code; it's a package."**

Bab ini memperkenalkan standar modern dalam pengemasan dan distribusi Python. Kita akan beralih dari cara lama (`setup.py`) ke standar baru yang menggunakan berkas **`pyproject.toml`** sebagai pusat deklarasi metadata proyek.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- **Strategic Blueprint**: [RAK-02 Foundation](file:///i:/Workspace/Workspace-Syahputrawork/learning-matrix-blueprint/01-Language-Hubs/Python-Knowledge-Base.md)

---

## 🧠 The Essence (Narrative)
Sejarah pengemasan Python pernah sangat membingungkan dengan banyaknya tool yang berbeda. Sejak munculnya **PEP 517** dan **PEP 518**, komunitas Python menyepakati penggunaan berkas tunggal `pyproject.toml`. Berkas ini mendefinisikan sistem *build*, dependensi, dan metadata proyek (seperti nama, versi, dan penulis) dalam format TOML yang mudah dibaca baik oleh manusia maupun mesin.

---

## 🎨 Visual Logic (Project Structure)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph TD
    Root[Project Root] --> Src[src/ / my_package/]
    Root --> Meta["pyproject.toml (Metadata)"]
    Root --> Tests[tests/]
    Root --> Docs[docs/]
    Root --> ENV[.venv/ (Isolated)]
    style Meta fill:#3776AB,stroke:#333,color:#fff
```

---

## 🛠️ The core File: pyproject.toml
Contoh struktur minimal `pyproject.toml`:
```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my-awesome-tool"
version = "0.1.0"
dependencies = [
    "requests >= 2.25.0",
]
```

---

## ⚠️ Pitfalls
- **Legacy Files**: Menemukan proyek lama dengan `setup.py` atau `setup.cfg` adalah hal umum. Penting untuk mengetahui cara membaca keduanya, meskipun standar baru lebih disarankan.
- **Dependency Versioning**: Tidak mencantumkan batasan versi (`>=`, `==`) dapat menyebabkan proyek Anda gagal berfungsi di komputer orang lain jika library tersebut diperbarui dengan fitur yang merusak (*breaking changes*).

---
*Back to [BK-03 Package Management](../README.md)*
