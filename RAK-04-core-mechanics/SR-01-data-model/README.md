# SR-01: Data Model (Object Anatomy) [x] Complete

> **"Objects are abstractions of data; structures are the reality of that data."**

Sub-Rak ini membedah fondasi dari segala sesuatu di Python: **Objek**. Kita akan melangkah melampaui sintaksis untuk melihat bagaimana CPython merepresentasikan data di memori melalui struktur `PyObject`, serta bagaimana protokol Dunder memungkinkan objek buatan kita berperilaku layaknya tipe data bawaan.

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_PyObject_Structure](./BK-01_PyObject_Structure/)** | C Anatomy | Membedah header objek, refcount, dan type pointer. |
| **[BK-02_Dunder_Internals](./BK-02_Dunder_Internals/)** | Protocols | Mekanisme penerjemahan sintaksis ke metode internal. |

---

## 🎯 Key Learning Goals
- Memahami struktur fisik objek Python di memori (Object Header).
- Mampu membedakan antara **Identitas** (`id`), **Nilai** (`==`), dan **Tipe** (`type`).
- Menguasai cara kerja **Reference Counting** di level terendah.
- Mampu mengimplementasikan protokol objek standar (`__repr__`, `__eq__`) secara benar.

---

## 🧪 Prasyarat Teknis
- Pemahaman dasar Tipe Data (RAK-02 SR-02) dan Class (RAK-02 SR-06).
- Pengetahuan dasar tentang variabel sebagai pointer/referensi.

---

## ⏭️ Next Step
Setelah memahami anatomi objek, mari kita pelajari bagaimana cara mengontrol akses ke atribut objek tersebut melalui keajaiban **[SR-03: Descriptors (Attribute Magic)](../SR-03-descriptors/README.md)**.

---
*Back to [Rak-04 Core Mechanics](../README.md)*
