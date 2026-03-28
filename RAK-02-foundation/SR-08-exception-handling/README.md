# SR-08: Exception Handling (Guarding the Flow)

> **"Error handling is not about fixing errors; it's about building programs that can survive them."**

Sub-Rak ini mengeksplorasi mekanisme penanganan kesalahan (*Exception Handling*) dalam Python. Kita akan membedah alur eksekusi `try-except`, pembuatan eksepsi kustom untuk logika bisnis, hingga manajemen sumber daya otomatis menggunakan *Context Managers*.

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **BK-01_Foundations_Exceptions** | Control Flow | Sintaks `try-except-else-finally` dan hirarki eksepsi. |
| **BK-02_CustomExceptions_Guards** | Advanced Logic | Pembuatan eksepsi kustom dan penggunaan `assert`. |
| **BK-03_ContextManagers** | Resource Mgmt | Protokol `with`, `__enter__/__exit__`, dan `contextlib`. |

---

## 🎯 Key Learning Goals
- Memahami alur eksekusi pipa **Try-Except-Else-Finally**.
- Mampu mendesain hirarki eksepsi kustom yang bermakna bagi domain bisnis.
- Menguasai teknik pengelolaan sumber daya otomatis via **Context Managers**.

---

## 🧪 Prasyarat Teknis
- Pemahaman tentang fungsi dan scoping (SR-05).
- Pemahaman paradigma OOP (SR-06).

## ⏭️ Next Step
Setelah alur program aman, mari kita bangun gerbang kualitas terakhir untuk memvalidasi seluruh logika kita di **[SR-09: Testing Frameworks](../SR-09-testing-frameworks/README.md)**.

---
*Back to [Rak-02 Foundation](../README.md)*
