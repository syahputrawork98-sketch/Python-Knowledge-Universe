# CH-02: ContextLib (Lightweight Managers) [x] Complete

> **"Sometimes a full class with __enter__ and __exit__ is overkill; that's where contextlib shines."**

Bab ini membedah modul **`contextlib`**, khususnya dekorator **`@contextmanager`**. Kita akan mempelajari cara membuat manajer konteks yang ringan menggunakan generator (fungsi dengan `yield`) sebagai alternatif pembuatan kelas penuh.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - contextlib](https://docs.python.org/3/library/contextlib.html)
- **Strategic Blueprint**: [RAK-02 Foundation](file:///i:/Workspace/Workspace-Syahputrawork/learning-matrix-blueprint/01-Language-Hubs/Python-Knowledge-Base.md)

---

## 🧠 The Essence (Narrative)
Dekorator `@contextmanager` memungkinkan Anda mendefinisikan manajer konteks hanya dengan satu fungsi generator. Alurnya sangat intuitif:
1. Kode **sebelum `yield`** bertindak sebagai `__enter__`.
2. Nilai yang di-**`yield`** diikat ke variabel `as` pada blok `with`.
3. Kode **setelah `yield`** bertindak sebagai `__exit__`.
Ini sangat cocok untuk pembungkus sederhana seperti penanda waktu (*timer*), penanganan log, atau pengaturan lingkungan sementara.

---

## 🎨 Visual Logic (Generator Pipeline)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph TD
    Entry([with fun_manager():]) --> Pre[1. Logic before yield]
    Pre --> Yield[2. Yield control to with block]
    Yield --> Post[3. Logic after yield - Cleanup]
    Post --> Out([Exited])
    style Pre fill:#3776AB,stroke:#333,color:#fff
    style Post fill:#FFD43B,stroke:#333,color:#000
```

---

## 🛠️ Implementation Example

```python
from contextlib import contextmanager

@contextmanager
def temporary_indent(depth):
    print(" " * depth, "[START SECTION]")
    try:
        yield # Context given to with block
    finally:
        # Guarantee cleanup even if exception occurs in with
        print(" " * depth, "[END SECTION]")

with temporary_indent(4):
    print("    Running nested task...")
```

---

## ⚠️ Pitfalls
- **Missing `try-finally`**: Saat menggunakan `@contextmanager`, jika blok kode di dalam `with` melempar eksepsi, kode setelah `yield` tidak akan pernah dijalankan kecuali Anda membungkus `yield` dalam blok `try-finally`. Selalu gunakan `try-finally` untuk menjamin sumber daya dibersihkan.
- **Complex Logic**: Jika logika penyiapan (*setup*) dan pembersihan (*teardown*) sangat kompleks dan membutuhkan banyak *state*, kembalilah menggunakan implementasi berbasis **Kelas** agar lebih tertata.

---
*Back to [BK-03 ContextManagers](../README.md)*
