# BK-02: Dunder Internals (Protokol Objek) [x] Complete

> **"Dunder methods are not just hooks; they are the contract between your object and the Python interpreter."**

Buku ini membedah **Dunder Methods** (Double Underscore), mesin penggerak di balik fleksibilitas Python. Kita akan mempelajari bagaimana interpreter menerjemahkan sintaksis sederhana (seperti `+`, `==`, atau `len()`) ke pemanggilan metode internal di dalam objek Anda.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Language Reference - Data Model](https://docs.python.org/3/reference/datamodel.html)
- **Strategic Blueprint**: [RAK-04 Core Mechanics](file:///i:/Workspace/Workspace-Syahputrawork/01-Language-Hubs-Workspace/Python-Knowledge-Base/RAK-04-core-mechanics/README.md)

---

## 🧠 The Essence (Narrative)
Python memiliki filosofi **"User-defined classes should behave like built-in types"**. Mengapa kita bisa menjumlahkan dua angka dengan `+`? Karena tipe data `int` memiliki dunder `__add__`. PEP dan Data Model menetapkan protokol ini agar objek apa pun yang Anda buat dapat diintegrasikan dengan sintaksis bahasa secara mulus. Jika Anda ingin objek Anda bisa "dipanggil" seperti fungsi, Anda implementasikan `__call__`. Jika ingin bisa dihitung isinya, Anda implementasikan `__len__`. Inilah rahasia di balik kekuatan **Duck Typing** Python.

---

## 🎨 Visual Logic (Syntax to Dunder Translation)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph TD
    Syntax[Sintaksis: 'a + b'] -- 1. Interpreter Check --> Slot[Lookup type(a) Slot: nb_add]
    Slot -- 2. Result --> Dunder[Call: a.__add__(b)]
    Dunder -- 3. Final --> Result([Calculated Result])
    style Slot fill:#3776AB,stroke:#333,color:#fff
    style Result fill:#FFD43B,stroke:#333,color:#000
```

---

## 📑 Protokol Dasar (The Essentials)

| Dunder | Kegunaan | Contoh Sintaksis |
| :--- | :--- | :--- |
| `__init__` | Inisialisasi status objek | `MyClass()` |
| `__repr__` | Representasi "Developer" (Ambiguous-free) | `repr(obj)` |
| `__str__` | Representasi "User" (Readable) | `str(obj)` atau `print(obj)` |
| `__eq__` | Perbandingan kesamaan nilai | `a == b` |
| `__hash__` | Memasukkan objek ke set/dict | `hash(obj)` |

---

## ⚠️ Pitfalls
- **repr vs str**: Jangan menggabungkan fungsi keduanya. `__repr__` harus seakurat mungkin (idealnya bisa didebug atau dibuat ulang), sedangkan `__str__` fokus pada keindahan tampilan untuk pengguna akhir.
- **Equality without Hash**: Jika Anda mengimplementasikan `__eq__` namun lupa mengimplementasikan `__hash__`, Python akan menonaktifkan kemampuan objek tersebut untuk dijadikan kunci dalam Dictionary atau isi dalam Set demi keamanan (karena kesamaan objek telah berubah perilakunya).

---
*Back to [SR-01 Data Model](../README.md)*
