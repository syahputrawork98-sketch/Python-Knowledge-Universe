# 02_interactive_input.py
# File ini mendemonstrasikan bahwa skrip bisa berhenti di tengah baris
# untuk meminta interaksi manusia menggunakan terminal.

print("--- Robot Penyapa ---")

# Program berhenti dan menunggu ketikan lalu ditekan ENTER.
nama = input("Tuliskan nama Anda di sini: ")

print("\n--- Memproses Data ---")

# F-String untuk menyematkan data ke dalam kalimat teks.
print(f"Halo {nama}, mari kita belajar membangun fondasi Python!")
