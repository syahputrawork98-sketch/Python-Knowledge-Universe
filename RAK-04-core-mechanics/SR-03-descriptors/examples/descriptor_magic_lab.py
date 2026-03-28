"""
LAB PRACTICAL: Descriptor Magic (Validation & Binding)
Standard: PPM V4 - Gold Standard

Tujuan: Memahami protokol descriptor dan mekanisme pengikatan metode.
Guna: Membangun sistem validasi data dan kontrol akses tingkat lanjut.
"""

# 1. THE VALIDATOR DESCRIPTOR
class Integer:
    """A descriptor that ensures the value is an integer."""
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"'{self.name}' must be an int, got {type(value).__name__}")
        print(f"   [LOG] Setting {self.name} to {value}")
        instance.__dict__[self.name] = value

class Account:
    # Descriptors must be class-level attributes
    balance = Integer("balance")
    id_code = Integer("id_code")

    def __init__(self, id_code, balance):
        self.id_code = id_code
        self.balance = balance

# 2. THE METHOD BINDING MECHANISM
class Speaker:
    def say_hello(self):
        print(f"   [METHOD] Hello from {self}")

def run_lab():
    print("=" * 60)
    print("🚀 DESCRIPTOR & BINDING LAB")
    print("=" * 60)

    # 1. Testing Validator Descriptor
    print("\n1. Testing Descriptor Validation")
    try:
        acc = Account(101, 5000)
        print(f"   [OK] Account created. Balance: {acc.balance}")
        
        print("   [ACTION] Attempting to set balance to 'string'...")
        acc.balance = "five thousand"
    except TypeError as e:
        print(f"   [CAUGHT] Got expected error: {e}")

    # 2. Testing Method Binding
    print("\n2. Testing Method Binding Mechanics")
    sp = Speaker()
    
    # Accessing from instance: Bound Method
    bound = sp.say_hello
    print(f"   [INFO] Access from instance: {bound}")
    print(f"   [INFO] Is bound to instance? {bound.__self__ is sp}")
    bound() # Calls say_hello(sp)

    # Accessing from class: Regular Function
    unbound = Speaker.say_hello
    print(f"   [INFO] Access from class: {unbound}")
    try:
        print("   [ACTION] Calling unbound function Speaker.say_hello()...")
        unbound() # This will fail because 'self' is missing
    except TypeError as e:
        print(f"   [CAUGHT] Got expected error: {e}")

    print("\n" + "=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    run_lab()
