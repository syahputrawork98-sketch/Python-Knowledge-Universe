# BK-02: Method Binding (Transformasi Fungsi) [x] Complete

> **"Methods in Python are just functions that have been 'bound' to an instance through the descriptor protocol."**

Buku ini membedah misteri di balik **`self`**. Kita akan mempelajari bagaimana fungsi yang didefinisikan di dalam kelas secara otomatis mendapatkan referensi ke instance objek melalui mekanisme **Method Binding** yang didukung oleh protokol descriptor.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - Functions & Methods](https://docs.python.org/3/howto/descriptor.html#functions-and-methods)
- **Strategic Blueprint**: [RAK-04 Core Mechanics](file:///i:/Workspace/Workspace-Syahputrawork/01-Language-Hubs-Workspace/Python-Knowledge-Base/RAK-04-core-mechanics/README.md)

---

## 🧠 The Essence (Narrative)
Pernahkah Anda bertanya mengapa `obj.method()` secara otomatis mengirimkan `obj` sebagai parameter pertama (`self`)? Jawabannya: **Fungsi adalah Descriptor**. Saat Anda memanggil fungsi dari sebuah instance (`obj.method`), Python memanggil `method.__get__(obj, type(obj))`. Panggilan ini menghasilkan objek baru yang disebut **Bound Method**. Objek ini "membungkus" fungsi asli dan instance objek tersebut, sehingga saat dipanggil, ia menyisipkan instance sebagai argumen pertama secara otomatis. Tanpa mekanisme ini, Python tidak akan memiliki paradigma OOP yang dinamis dan fleksibel.

---

## 🎨 Visual Logic (Method Binding Workflow)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph TD
    Call[Call: obj.say_hello] --> Get[Internal: say_hello.__get__(obj, User)]
    Get -- Result --> Wrap[Bound Method Object]
    Wrap -- contains --> Pointer[Function Pointer]
    Wrap -- contains --> Instance[Instance: obj]
    Wrap -- Executed as --> Final[say_hello(obj)]
    style Get fill:#3776AB,stroke:#333,color:#fff
    style Wrap fill:#FFD43B,stroke:#333,color:#000
```

---

## 🛠️ The "Self" Injection: Manual Emulation
```python
class MyClass:
    def greet(self):
        print(f"Hello from {self}")

# Manual Binding:
obj = MyClass()
greet_func = MyClass.greet
bound_method = greet_func.__get__(obj, MyClass)
bound_method() # Sama dengan obj.greet()
```

---

## ⚠️ Pitfalls
- **Class Access**: Jika Anda memanggil fungsi langsung dari kelas (`MyClass.greet`), descriptor tidak melakukan *binding* karena argumen instance-nya adalah `None`. Ini menghasilkan fungsi asli biasa (*unbound function*), dan Anda harus mengirimkan `self` secara manual: `MyClass.greet(obj)`.
- **Static vs Class methods**: `@staticmethod` dan `@classmethod` adalah descriptor khusus yang mengubah perilaku `__get__` ini agar mengembalikan fungsi asli tanpa binding (static) atau mengikat ke kelas alih-alih instance (classmethod).

---
*Back to [SR-03 Descriptors](../README.md)*
