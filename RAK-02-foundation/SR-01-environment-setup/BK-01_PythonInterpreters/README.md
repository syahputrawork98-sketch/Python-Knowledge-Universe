# BK-01: Python Interpreters (Instalasi & Runtime) [x] Complete

> **"Python is both a language and an implementation. Understanding the interpreter is the first step to mastering the language."**

Buku ini membedah fondasi dari ekosistem Python: **Interpreter**. Kita akan mempelajari cara menginstal CPython secara benar, mengelola beberapa versi Python di satu mesin, dan cara berinteraksi dengan Python melalui Command Line Interface (CLI).

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python.org - Downloading Python](https://www.python.org/downloads/)
- **Primary Source**: [Python Docs - Using Python](https://docs.python.org/3/using/index.html)
- **Strategic Blueprint**: [RAK-02 Foundation](file:///i:/Workspace/Workspace-Syahputrawork/learning-matrix-blueprint/01-Language-Hubs/Python-Knowledge-Base.md)

---

## 🧠 The Essence (Narrative)
Python adalah bahasa yang diinterpretasikan. Kode yang Anda tulis (`.py`) tidak langsung dimengerti oleh CPU, melainkan diterjemahkan oleh interpreter (biasanya CPython) menjadi *bytecode* (`.pyc`) yang kemudian dijalankan oleh Virtual Machine. Memahami bagaimana memanggil interpreter yang tepat dari terminal adalah keahlian fundamental yang sering diabaikan.

---

## 🎨 Visual Logic (Interpretation Flow)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph LR
    Code[Source Code .py] -- 1. Compile --> Byte[Bytecode .pyc]
    Byte -- 2. Run --> PVM[Python Virtual Machine]
    PVM -- 3. Output --> Result([Execution Result])
    style PVM fill:#3776AB,stroke:#333,color:#fff
    style Result fill:#FFD43B,stroke:#333,color:#000
```

---

## 📑 Daftar Bab (The Syllabus)

| Bab | Fokus | Spesifikasi |
| :--- | :--- | :--- |
| **[CH-01_Installation](./CH-01_Installation/)** | Setup | Installing CPython & Path configuration. |
| **[CH-02_CLI_Interacting](./CH-02_CLI_Interacting/)** | Interaction | Using the REPL and script execution. |

---

## ⚠️ Pitfalls
- **Python 2 vs 3**: Selalu pastikan Anda menggunakan Python 3. Perintah `python` di beberapa sistem (seperti macOS/Linux lama) mungkin masih merujuk ke Python 2. Gunakan `python3` atau cek versi dengan `python --version`.
- **System PATH**: Jika terminal tidak mengenali perintah `python`, kemungkinan besar interpreter tidak terdaftar di sistem PATH Anda saat instalasi.

---
*Back to [SR-01 Environment Setup](../README.md)*
