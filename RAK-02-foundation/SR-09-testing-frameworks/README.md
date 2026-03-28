# SR-09: Testing Frameworks (The Quality Gate)

> **"If it's not tested, it's broken by design."**

Sub-Rak ini mengeksplorasi mekanisme penjaminan kualitas kode melalui **Testing Frameworks**. Kita akan membedah standar pengujian dari pustaka bawaan `unittest`, kekuatan industri `pytest`, hingga strategi isolasi kode menggunakan `mocking`. Ini adalah gerbang kualitas terakhir dalam fase pondasi Python.

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **BK-01_Unittest_Builtin** | Standard Lib | xUnit style testing dengan kelas dan assertions. |
| **BK-02_Pytest_Modern** | Modern Tooling | Functional testing, fixtures, dan parametrization. |
| **BK-03_Mocking_Strategy** | Isolation | Teknik `mock` dan `patch` untuk memutus dependensi. |

---

## 🎯 Key Learning Goals
- Memahami siklus hidup pengujian (Setup-Run-Teardown).
- Menguasai penulisan test case yang atomik dan independen.
- Mampu mensimulasikan kegagalan eksternal menggunakan **Mocking**.
- Menjalankan test suite secara otomatis dan mengukur *code coverage*.

---

## 🧪 Prasyarat Teknis
- Pemahaman OOP (SR-06) untuk unittest.
- Instalasi `pytest` (pip install pytest).

## ⏭️ Next Step
Sebagai penutup fase pondasi, tingkatkan presisi kode Anda dengan sistem penanda tipe di **[SR-10: Typing Hints](../SR-10-typing-hints/README.md)**.

---
*Back to [Rak-02 Foundation](../README.md)*
