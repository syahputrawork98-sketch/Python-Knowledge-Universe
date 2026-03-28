# BK-01: Compilation Genesis (AST ke Bytecode) [x] Complete

> **"Code is for humans; AST is for compilers; Bytecode is for the machine."**

Buku ini membedah alur transformasi kode Python dari teks mentah hingga menjadi instruksi yang siap dijalankan oleh **Python Virtual Machine (PVM)**. Kita akan mempelajari bagaimana Python melakukan parsing menjadi pohon sintaksis (AST) dan mengonversinya menjadi urutan bytecode yang efisien.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - ast (Abstract Syntax Tree)](https://docs.python.org/3/library/ast.html)
- **Primary Source**: [CPython Source - Python/compile.c](https://github.com/python/cpython/blob/main/Python/compile.c)
- **Strategic Blueprint**: [RAK-04 Core Mechanics](file:///i:/Workspace/Workspace-Syahputrawork/01-Language-Hubs-Workspace/Python-Knowledge-Base/RAK-04-core-mechanics/README.md)

---

## 🧠 The Essence (Narrative)
Python sering disebut sebagai bahasa yang "diinterpretasikan", namun secara teknis ia melalui fase **Kompilasi** internal. Saat Anda menjalankan `.py`, Python tidak langsung membaca baris per baris. Pertama, kode dipecah menjadi token (*Lexing*), kemudian disusun menjadi **Abstract Syntax Tree (AST)** — representasi struktural dari logika kode Anda. AST inilah yang kemudian dikompilasi menjadi **Bytecode** (`.pyc`), yaitu serangkaian instruksi tingkat rendah yang dioptimalkan untuk PVM. Memahami alur ini membantu Anda mengerti mengapa beberapa sintaksis lebih cepat dari yang lain di level VM.

---

## 🎨 Visual Logic (The Compilation Pipeline)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph LR
    Source[Source Code .py] -- 1. Tokenize --> Tokens[Stream of Tokens]
    Tokens -- 2. Parse --> AST[Abstract Syntax Tree]
    AST -- 3. Compile --> Byte[Bytecode .pyc]
    Byte -- 4. Execute --> PVM[Python Virtual Machine]
    style AST fill:#3776AB,stroke:#333,color:#fff
    style Byte fill:#FFD43B,stroke:#333,color:#000
```

---

## 🛠️ Inspecting the AST
Anda dapat melihat "pohon pikiran" Python menggunakan modul `ast`:
```python
import ast
node = ast.parse("x = 1 + 2")
print(ast.dump(node))
```

---

## ⚠️ Pitfalls
- **Bytecode vs Machine Code**: Jangan keliru menyamakan bytecode Python dengan bahasa mesin (Binary). Bytecode masih membutuhkan interpreter (PVM) untuk berjalan, sedangkan bahasa mesin (C/Rust) berjalan langsung di CPU.
- **Static Analysis Limit**: Karena Python sangat dinamis, AST bisa diubah secara programatik di runtime (metaprogramming), namun ini adalah teknik tingkat sangat lanjut dan berbahaya jika tidak dipahami dengan benar.

---
*Back to [SR-06 PVM & Bytecode](../README.md)*
