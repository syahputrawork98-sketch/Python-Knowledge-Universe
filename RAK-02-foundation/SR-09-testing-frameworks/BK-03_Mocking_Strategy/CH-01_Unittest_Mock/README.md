# CH-01: Mocking & Patching (Isolation Techniques) [x] Complete

> **"A unit test should not depend on anything except the unit it is testing."**

Bab ini membedah teknik **Mocking** menggunakan pustaka `unittest.mock`. Kita akan mempelajari bagaimana mensimulasikan objek yang kompleks (seperti API eksternal atau Database) agar unit test kita berjalan cepat, deterministik, dan bebas dari ketergantungan infrastruktur luar.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- **Strategic Blueprint**: [RAK-02 Foundation](file:///i:/Workspace/Workspace-Syahputrawork/learning-matrix-blueprint/01-Language-Hubs/Python-Knowledge-Base.md)

---

## 🧠 The Essence (Narrative)
**Mocking** adalah proses mengganti objek asli dengan objek tiruan (*Mock Object*) yang perilakunya bisa kita kendalikan. Fungsi utamanya adalah **Isolasi**. Jika fungsi Anda memanggil API cuaca, Anda tentu tidak ingin tes Anda gagal hanya karena internet mati. Dengan `patch`, Anda mencegat panggilan ke fungsi asli dan mengembalikan nilai buatan (*Return Value*). Anda juga bisa memverifikasi apakah fungsi tersebut dipanggil dengan argumen yang benar atau berapa kali ia dipanggil.

---

## 🎨 Visual Logic (Mocking Isolation)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph LR
    Func[My Function] -- 1. calls --> Ext[External API]
    Func -- 2. calls --> Mock[MagicMock Object]
    Mock -- 3. returns --> Fake[Fake Data]
    Ext -. 4. blocked .-> NoInternet[No Connectivity Needed]
    style Mock fill:#3776AB,stroke:#333,color:#fff
    style Fake fill:#FFD43B,stroke:#333,color:#000
```

---

## 🛠️ Implementation Template: Patching

```python
from unittest.mock import patch

def get_status():
    # Bayangkan ini memanggil API sungguhan
    pass

def test_logic_using_api():
    # Mencegat get_status dan mengembalikan "OK"
    with patch("__main__.get_status") as mock_get:
        mock_get.return_value = "OK"
        
        # Eksekusi logika
        result = get_status()
        
        assert result == "OK"
        mock_get.assert_called_once()
```

---

## ⚠️ Pitfalls
- **Where to Patch**: Ini adalah kesalahan paling umum. Anda harus mem-patch objek di tempat ia **di-import/digunakan**, bukan di tempat ia didefinisikan. Jika modul `A` meng-import `func` dari modul `B`, maka Anda harus mem-patch `A.func`.
- **Testing the Mock**: Jangan sampai Anda malah mengetes apakah Mock Object bekerja dengan benar. Fokuslah pada bagaimana unit kode Anda bereaksi terhadap nilai yang dikembalikan oleh Mock tersebut.

---
*Back to [BK-03_Mocking_Strategy](../README.md)*
