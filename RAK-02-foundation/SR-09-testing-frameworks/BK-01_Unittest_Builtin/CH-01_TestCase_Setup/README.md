# CH-01: TestCase & Setup (The Standard Lifecycle) [x] Complete

> **"Unit tests are the first consumer of your code; if they are hard to write, your code is hard to use."**

Bab ini membedah dasar-dasar **`unittest`**, pustaka pengujian bawaan Python yang terinspirasi oleh JUnit. Kita akan mempelajari bagaimana menyusun kelas pengujian, memahami siklus hidup pengujian, dan menjaga isolasi antar test case melalui metode `setUp` dan `tearDown`.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - unittest](https://docs.python.org/3/library/unittest.html)
- **Strategic Blueprint**: [RAK-02 Foundation](file:///i:/Workspace/Workspace-Syahputrawork/learning-matrix-blueprint/01-Language-Hubs/Python-Knowledge-Base.md)

---

## 🧠 The Essence (Narrative)
`unittest` bekerja dengan mekanisme **Object Oriented**. Anda membuat kelas yang mewarisi **`unittest.TestCase`**. Setiap metode yang dimulai dengan awalan **`test_`** akan dianggap sebagai satu unit pengujian yang independen. Untuk memastikan setiap tes berjalan dalam kondisi "bersih", kita menggunakan:
1. **`setUp()`**: Dijalankan **SEBELUM** setiap metode tes (untuk inisialisasi).
2. **`tearDown()`**: Dijalankan **SESUDAH** setiap metode tes (untuk pembersihan).

---

## 🎨 Visual Logic (Testing Lifecycle)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph TD
    Start([Run Test Suite]) --> SU[1. setUp()]
    SU --> Test[2. test_method()]
    Test --> TD[3. tearDown()]
    TD --> Next{More tests?}
    Next -- Yes --> SU
    Next -- No --> End([Generation Report])
    style SU fill:#3776AB,stroke:#333,color:#fff
    style TD fill:#FFD43B,stroke:#333,color:#000
```

---

## 🛠️ Basic Test Structure

```python
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Inisialisasi unit yang akan diuji
        self.calc = Calculator()

    def test_add(self):
        # Unit test sesungguhnya
        self.assertEqual(self.calc.add(2, 3), 5)

    def tearDown(self):
        # Pembersihan (jika perlu)
        del self.calc

if __name__ == "__main__":
    unittest.main()
```

---

## ⚠️ Pitfalls
- **Naming Prefix**: Python tidak akan menjalankan metode Anda jika tidak diawali dengan `test_`. Pastikan nama metode Anda jelas, misal: `test_login_with_invalid_password`.
- **Test Dependencies**: Hindari ketergantungan antar metode tes. Tes A tidak boleh bergantung pada data yang dihasilkan oleh Tes B. Gunakan `setUp` untuk memastikan setiap tes memiliki data awal yang konsisten secara mandiri.

---
*Back to [BK-01 Unittest_Builtin](../README.md)*
