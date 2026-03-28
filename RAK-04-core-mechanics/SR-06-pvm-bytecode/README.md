# SR-06: PVM & Bytecode (Runtime Execution) [x] Complete

> **"Code is a letter to the future; bytecode is its delivery vehicle."**

Sub-Rak ini mengeksplorasi jeroan **Python Virtual Machine (PVM)**. Kita akan membedah bagaimana kode sumber Anda diolah menjadi instruksi tingkat rendah yang dimengerti oleh pengeksekusi internal CPython, serta mempelajari teknik dekompilasi untuk membedah kinerja kode di level mesin virtual.

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_Compilation_Genesis](./BK-01_Compilation_Genesis/)** | AST to Bytecode | Menelusuri alur kompilasi internal. |
| **[BK-02_Bytecode_Disassembly](./BK-02_Bytecode_Disassembly/)** | PVM Opcodes | Membedah instruksi mesin virtual (Py 3.11+). |

---

## 🎯 Key Learning Goals
- Memahami alur kerja **Compilation Pipeline** CPython (Lexer -> Parser -> AST -> Bytecode).
- Mampu melakukan **Disassembly** kode menggunakan modul `dis` untuk analisis performa.
- Memahami prinsip **Stack-based Virtual Machine** (PUSH/POP logic).
- Menguasai teknik introspeksi AST untuk memahami struktur logis bahasa.

---

## 🧪 Prasyarat Teknis
- Pemahaman dasar Control Flow (RAK-02 SR-04).
- Pengetahuan dasar tentang arsitektur komputer (Stack vs Heap) sangat disarankan.

---

## ⏭️ Next Step
Setelah menguasai bagaimana kode dieksekusi, mari kita beralih ke cara Python mengelola sumber daya fisik di **[SR-05: Memory Management (Memori & GC)](../SR-05-memory/README.md)**.

---
*Back to [Rak-04 Core Mechanics](../README.md)*
