# 02_scope_legb.py
"""
Demonstrasi aturan LEGB (Local, Enclosing, Global, Built-in).
"""

x = "Global X" # Global Scope

def outer_function():
    x = "Enclosing X" # Enclosing Scope
    
    def inner_function():
        x = "Local X" # Local Scope
        print(f"Di dalam inner: {x}")
        
    inner_function()
    print(f"Di dalam outer: {x}")

print("--- Menjalankan LEGB Demo ---")
outer_function()
print(f"Di level modul: {x}")

# Menggunakan kata kunci 'global'
y = 10
def ubah_global():
    global y
    y = 20
    print(f"Ubah global Y menjadi: {y}")

ubah_global()
print(f"Y sekarang adalah: {y}")
