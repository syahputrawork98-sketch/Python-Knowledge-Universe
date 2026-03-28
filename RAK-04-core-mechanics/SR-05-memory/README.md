# SR-05: Memory Management (Memori & GC) [x] Complete

> **"Memory management in Python is a quiet, powerful dance between instant reclamation and generational cleaning."**

Sub-Rak ini mengeksplorasi bagaimana CPython mengelola sumber daya paling berharga: **Memori**. Kita akan membedah strategi lapis ganda yang menjaga Python tetap efisien — dari penghitungan referensi yang deterministik hingga deteksi siklus yang cerdas (Garbage Collection), serta bagaimana alokator memori kustom Python berinteraksi dengan Sistem Operasi.

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_Reference_Counting](./BK-01_Reference_Counting/)** | Immediate Release | Mekanisme utama dealokasi objek di Python. |
| **[BK-02_Cyclic_GC](./BK-02_Cyclic_GC/)** | Circular References | Pertahanan kedua: Generational Garbage Collector. |
| **[BK-03_Memory_Allocators](./BK-03_Memory_Allocators/)** | PyMalloc | Hirarki Arenas, Pools, dan Blocks (Level C). |

---

## 🎯 Key Learning Goals
- Memahami beda antara **Reference Counting** vs **Garbage Collection**.
- Mampu mendeteksi dan menyelesaikan masalah **Circular References**.
- Menguasai penggunaan modul `gc` untuk optimalisasi performa aplikasi besar.
- Memahami hirarki alokasi memori internal CPython untuk objek kecil.
- Menguasai teknik introspeksi memori menggunakan `sys` dan `ctypes`.

---

## 🧪 Prasyarat Teknis
- Pemahaman PyObject Structure (RAK-04 SR-01).
- Pemahaman dasar tentang penggunaan RAM dan Pointer/Referencing.

---

## ⏭️ Next Step
Setelah menguasai pengelolaan memori, mari kita tantang pemahaman kita tentang konkurensi di level interpreter melalui **[SR-07: The GIL (Global Interpreter Lock)](../SR-07-the-gil/)**.

---
*Back to [Rak-04 Core Mechanics](../README.md)*
