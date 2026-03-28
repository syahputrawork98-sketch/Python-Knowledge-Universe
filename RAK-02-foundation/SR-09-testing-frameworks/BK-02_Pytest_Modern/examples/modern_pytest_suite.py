"""
LAB PRACTICAL: Modern Pytest Suite
Standard: PPM V4 - Gold Standard

Tujuan: Memahami penggunaan Fixtures dan Parametrization.
Guna: Menulis pengujian yang efisien, kering (DRY), dan skalabel.
"""

import pytest

# 1. THE CODE TO TEST
class Database:
    def __init__(self):
        self.connected = False
    def connect(self): self.connected = True
    def close(self): self.connected = False
    def query(self, q): return f"Result of {q}"

# 2. THE FIXTURE (Dependency Injection)
# Scope module means it runs once for this file
@pytest.fixture(scope="module")
def db_conn():
    print("\n   [SETUP] 🔌 Initializing Database Connection...")
    db = Database()
    db.connect()
    yield db # This is what the test gets
    print("\n   [TEARDOWN] 🧹 Closing Database Connection...")
    db.close()

# 3. TEST CASES WITH FIXTURES
def test_db_connection(db_conn):
    print("      Testing DB connection status...")
    assert db_conn.connected is True

def test_db_query(db_conn):
    print("      Testing DB query logic...")
    assert db_conn.query("GetUsers") == "Result of GetUsers"

# 4. TEST CASE WITH PARAMETRIZATION (Data-driven)
@pytest.mark.parametrize("input_val, expected", [
    (1, 2),
    (5, 6),
    (10, 11),
    (-1, 0),
])
def test_increment(input_val, expected):
    print(f"      Testing increment: {input_val} -> {expected}")
    assert input_val + 1 == expected

# 5. TEST FOR EXCEPTIONS (The Pytest Way)
def test_zero_division():
    print("      Testing exception handling...")
    with pytest.raises(ZeroDivisionError):
        1 / 0
