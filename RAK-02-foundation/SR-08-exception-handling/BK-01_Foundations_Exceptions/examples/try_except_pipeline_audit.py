"""
LAB PRACTICAL: Try-Except-Else-Finally Pipeline Audit
Standard: PPM V4 - Gold Standard

Tujuan: Memahami urutan eksekusi blok penanganan kesalahan.
Guna: Menghindari kebocoran memori dan memastikan integritas alur program.
"""

def complex_operation(divisor):
    print(f"\n🚀 Starting operation with divisor: {divisor}")
    print("-" * 40)
    
    try:
        # 1. Try to perform risky logic
        print("[TRY]   Attempting division...")
        result = 100 / divisor
        
    except ZeroDivisionError:
        # 2. Specific case handling
        print("[EXCEPT] ❌ ZeroDivisionError caught!")
        result = None
        
    except ArithmeticError:
        # 3. General case (Parent of ZeroDivisionError)
        print("[EXCEPT] ❌ ArithmeticError caught!")
        result = None
        
    else:
        # 4. Success-only logic
        print("[ELSE]   ✅ No exception occurred. Result saved.")
        
    finally:
        # 5. Always-execute cleanup logic
        print("[FINALLY] 🧹 This block ALWAYS runs. Cleaning resources.")

    print("-" * 40)
    return result

def run_lab():
    print("=" * 60)
    print("🛠️ EXCEPTION PIPELINE AUDIT LAB")
    print("=" * 60)

    # Scenario 1: Success (divisor = 5)
    print("\nScenario 1: SUCCESSFUL FLOW")
    res1 = complex_operation(5)
    print(f"Final Outcome: {res1}")

    # Scenario 2: ZeroDivisionError (divisor = 0)
    print("\nScenario 2: EXCEPTION FLOW")
    res2 = complex_operation(0)
    print(f"Final Outcome: {res2}")

    # Insight on Hierarchy
    print("\n💡 INSIGHT: HIERARCHY TEST")
    try:
        raise ZeroDivisionError("Inner error")
    except ArithmeticError:
        print("   ArithmeticError (Parent) can catch ZeroDivisionError (Child)")
    except ZeroDivisionError:
        print("   ZeroDivisionError (Child) - This line will NOT be reached if Parent catches first.")

    print("=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    run_lab()
