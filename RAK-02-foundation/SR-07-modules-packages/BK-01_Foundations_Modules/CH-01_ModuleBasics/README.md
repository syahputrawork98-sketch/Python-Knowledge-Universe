# CH-01: Module Basics (The Atomic Unit) [x] Complete

> **"A module is a file containing Python definitions and statements; it is the fundamental unit of code organization."**

Bab ini membedah dasar-dasar **Modul** dalam Python. Kita akan mempelajari perbedaan antara berkas yang dijalankan sebagai skrip utama dan berkas yang di-import sebagai pustaka, serta rahasia di balik idiom `if __name__ == "__main__"`.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - Modules](https://docs.python.org/3/tutorial/modules.html)
- **Strategic Blueprint**: [RAK-02 Foundation](file:///i:/Workspace/Workspace-Syahputrawork/learning-matrix-blueprint/01-Language-Hubs/Python-Knowledge-Base.md)

---

## 🧠 The Essence (Narrative)
Secara teknis, setiap berkas `.py` adalah sebuah modul. Saat Anda menjalankan berkas tersebut secara langsung, Python menetapkan variabel spesial `__name__` menjadi `"__main__"`. Namun, saat berkas tersebut di-import oleh modul lain, `__name__` akan berisi nama berkas itu sendiri. Idiom **`if __name__ == "__main__"`** memungkinkan modul yang sama bertindak sebagai pustaka (menyediakan fungsi tanpa menjalankan logika) sekaligus sebagai skrip yang bisa dieksekusi secara mandiri.

---

## 🎨 Visual Logic (Execution Context)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph TD
    Start([Execute python my_mod.py]) --> Eval{__name__ == "__main__"?}
    Eval -- Yes --> Script[Run Main Script Logic]
    Eval -- No --> Lib[Export Definitions Only]
    Script --> End([Success])
    Lib --> End
    style Eval fill:#3776AB,stroke:#333,color:#fff
```

---

## 🛠️ The Entry Point Idiom

```python
def my_function():
    return "Logic executed!"

# Pelindung Eksekusi
if __name__ == "__main__":
    # Kode di sini HANYA berjalan jika file ini dieksekusi langsung
    print("Running as script...")
    print(my_function())
```

---

## ⚠️ Pitfalls
- **Executable Modules**: Tanpa pelindung `if __name__ == "__main__"`, semua kode di level *top-level* akan langsung dijalankan saat modul di-import. Ini bisa menyebabkan efek samping yang tidak diinginkan (seperti mencetak sesuatu atau mengubah file) bagi modul yang meng-import-nya.
- **Naming Conflicts**: Hindari menamai modul Anda sama dengan modul bawaan Python (misal: `math.py`, `random.py`). Jika Anda melakukannya, modul Anda akan menutupi (*shadowing*) modul aslinya, menyebabkan error saat Anda mencoba meng-import modul bawaan tersebut.

---
*Back to [BK-01 Foundations & Modules](../README.md)*
