# CH-02: Venv Handling (Operating the Nest) [x] Complete

> **"Creating an environment is as simple as a single command."**

Bab ini memberikan panduan praktis untuk mengelola lingkungan virtual menggunakan modul bawaan Python, `venv`. Kita akan mempelajari instruksi baris perintah untuk membuat, mengaktifkan, dan menonaktifkan lingkungan kerja Anda.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - venv module](https://docs.python.org/3/library/venv.html)
- **Strategic Blueprint**: [RAK-02 Foundation](file:///i:/Workspace/Workspace-Syahputrawork/learning-matrix-blueprint/01-Language-Hubs/Python-Knowledge-Base.md)

---

## 🧠 The Essence (Narrative)
Modul `venv` adalah tool standar sejak Python 3.3 untuk menciptakan lingkungan virtual ringan. Prosesnya terdiri dari tiga tahap: **Creation** (membuat folder), **Activation** (memberitahu terminal untuk menggunakan salinan Python tersebut), dan **Deactivation** (kembali ke Python global). Perbedaan utama terletak pada skrip aktivasi yang berbeda antara sistem Windows (PowerShell) dan Unix (Bash/Zsh).

---

## 🎨 Visual Logic (Environment Lifecycle)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph LR
    A[Create: python -m venv .venv] --> B[Activate: source/activate]
    B --> C[Working state: (venv)]
    C --> D[Deactivate: deactivate]
    D --> E[Global State]
    style B fill:#3776AB,stroke:#333,color:#fff
    style C fill:#3776AB,stroke:#333,color:#fff
```

---

## 🛠️ Operational Commands

### 1. Creating the Environment
Jalankan perintah ini di dalam folder proyek Anda:
```bash
python -m venv .venv
```
*(Nama `.venv` adalah standar konvensi, namun Anda bisa menamainya apapun).*

### 2. Activating (System Dependent)

| Platform | Command / Shell |
| :--- | :--- |
| **Windows** | `.venv\Scripts\Activate.ps1` (PowerShell) |
| **Windows** | `.venv\Scripts\activate.bat` (Command Prompt) |
| **Unix/macOS** | `source .venv/bin/activate` (Bash/Zsh) |

### 3. Deactivating
Untuk kembali ke lingkungan global, cukup ketik:
```bash
deactivate
```

---

## ⚠️ Pitfalls
- **Ignored Folders**: Folder `.venv` berisi ribuan file kecil. **Selalu masukkan `.venv/` ke dalam file `.gitignore`** Anda agar tidak terunggah ke repositori Git.
- **Execution Policy (Windows)**: Jika aktivasi gagal di PowerShell, Anda mungkin perlu menjalankan `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.

---
*Back to [BK-02 Virtual Environments](../README.md)*
