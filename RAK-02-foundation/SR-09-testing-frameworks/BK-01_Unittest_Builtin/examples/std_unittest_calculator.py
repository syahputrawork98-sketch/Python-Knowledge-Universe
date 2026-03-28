"""
LAB PRACTICAL: Standard Unittest Suite
Standard: PPM V4 - Gold Standard

Tujuan: Memahami struktur xUnit dan siklus hidup TestCase.
Guna: Menjamin kualitas logika unit terkecil dalam sistem.
"""

import unittest

# 1. THE CODE TO TEST (The System Under Test - SUT)
class Calculator:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return a / b

# 2. THE TEST CLASS
class TestCalculator(unittest.TestCase):
    
    # Executed BEFORE each test method
    def setUp(self):
        print("\n[SETUP] 🛠️ Initializing Calculator instance...")
        self.calc = Calculator()

    # TEST: Addition logic
    def test_addition(self):
        print("[TEST]  Testing addition...")
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1, 1), 0)

    # TEST: Division logic (Normal case)
    def test_division(self):
        print("[TEST]  Testing standard division...")
        self.assertEqual(self.calc.divide(10, 2), 5)

    # TEST: Exception handling (Edge case)
    def test_division_by_zero(self):
        print("[TEST]  Testing error handling for zero divisor...")
        # Verification that ZeroDivisionError is raised
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    # Executed AFTER each test method
    def tearDown(self):
        print("[TEARDOWN] 🧹 Cleaning up resources...")
        del self.calc

# 3. RUNNER
if __name__ == "__main__":
    print("=" * 60)
    print("🧪 UNITTEST SUITE EXECUTION")
    print("=" * 60)
    
    # Running the tests
    unittest.main()
