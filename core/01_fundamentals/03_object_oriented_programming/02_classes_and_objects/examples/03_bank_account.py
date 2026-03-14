class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Setoran Rp{amount} berhasil. Saldo baru: Rp{self.balance}")
        else:
            print("Jumlah setoran harus positif.")
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Penarikan Rp{amount} berhasil. Saldo tersisa: Rp{self.balance}")
        else:
            print("Saldo tidak cukup atau jumlah tidak valid.")

# --- Penggunaan ---
acc = BankAccount("Syahputra", 1000000)
acc.deposit(500000)
acc.withdraw(200000)
acc.withdraw(2000000)
