"""
LAB PRACTICAL: Custom Exceptions & Business Guards
Standard: PPM V4 - Gold Standard

Tujuan: Membangun sistem penanganan error berbasis domain bisnis.
Guna: Memberikan informasi kegagalan yang bermakna bagi pengembang dan pengguna.
"""

# 1. Custom Exception Hierarchy
class BankingError(Exception):
    """Base class for all banking exceptions."""
    pass

class InsufficientFundsError(BankingError):
    """Raised when account balance is lower than withdrawal amount."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"❌ Insufficient funds: Balance ${balance}, Attempted ${amount}")

class InvalidAccountError(BankingError):
    """Raised when account number is invalid."""
    pass

# 2. Business Logic with Guards
class ATM:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def withdraw(self, amount):
        # A. ASSERTION: Internal check (Developer audit)
        # Asserts that the system is not trying to process negative amounts
        assert amount > 0, "⚠️ Internal Logic Error: Withdrawal amount must be positive!"

        # B. EXCEPTION: Business rule (End-user error handling)
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        
        self.balance -= amount
        print(f"💰 Withdrawal success: ${amount}. Remaining: ${self.balance}")
        return self.balance

def run_lab():
    print("=" * 60)
    print("🏦 BANKING SYSTEM ERROR GUARD LAB")
    print("=" * 60)

    my_atm = ATM("ACC-777", 1000)

    # Success Scenario
    print("\nScenario 1: Standard Withdrawal")
    my_atm.withdraw(200)

    # Custom Exception Scenario
    print("\nScenario 2: Insufficient Funds")
    try:
        my_atm.withdraw(1500)
    except InsufficientFundsError as e:
        print(f"Captured: {e}")
    except BankingError as e:
        print(f"Caught at general banking level: {e}")

    # Assertion Scenario (Will crash unless caught, but meant for dev-time)
    print("\nScenario 3: Internal Logic Failure (Assertion)")
    try:
        # Code might have a bug passing negative value
        my_atm.withdraw(-50) 
    except AssertionError as e:
        print(f"Internal Audit Failed: {e}")

    print("=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    run_lab()
