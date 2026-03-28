# SR-03: Descriptors (Attribute Magic) [x] Complete

> **"Descriptors are the hidden gears of Python's class attribute system."**

Sub-Rak ini mengeksplorasi **Descriptor Protocol**, mekanisme yang sangat kuat namun seringkali dianggap "ajaib" yang memungkinkan kita membajak akses atribut objek. Kita akan membedah bagaimana properti, metode, dan fungsi dekorator bawaan lainnya diimplementasikan menggunakan protokol tingkat rendah ini.

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_Descriptor_Protocol](./BK-01_Descriptor_Protocol/)** | Get/Set/Delete | Mekanisme pembajakan akses atribut tingkat kelas. |
| **[BK-02_Method_Binding](./BK-02_Method_Binding/)** | Bound Methods | Bagaimana fungsi berubah menjadi metode melalui descriptor. |

---

## 🎯 Key Learning Goals
- Memahami beda antara **Data Descriptors** vs **Non-data Descriptors**.
- Mampu mengimplementasikan validator data kustom menggunakan dunder `__set__`.
- Menguasai teknik **Method Binding** dan alasan teknis di balik argumen `self`.
- Membedah implementasi internal `@property`, `@classmethod`, dan `@staticmethod`.

---

## 🧪 Prasyarat Teknis
- Pemahaman Data Model (RAK-04 SR-01).
- Pemahaman siklus hidup objek (Instansiasi & Atribut).

---

## ⏭️ Next Step
Setelah menguasai kontrol atribut, mari kita beralih ke level yang lebih rendah lagi untuk melihat bagaimana kode kita dieksekusi oleh mesin virtual di **[SR-06: PVM & Bytecode (Runtime Execution)](../SR-06-pvm-bytecode/README.md)**.

---
*Back to [Rak-04 Core Mechanics](../README.md)*
