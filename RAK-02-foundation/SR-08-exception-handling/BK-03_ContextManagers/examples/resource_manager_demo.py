"""
LAB PRACTICAL: Resource Management with Context Managers
Standard: PPM V4 - Gold Standard

Tujuan: Memahami protokol __enter__/__exit__ dan dekorator @contextmanager.
Guna: Menjamin penutupan sumber daya dan otomatisasi setup/teardown.
"""

import time
from contextlib import contextmanager

# 1. CLASS-BASED CONTEXT MANAGER
class ExecutionTimer:
    """A context manager to measure execution time of a code block."""
    def __init__(self, task_name):
        self.task_name = task_name

    def __enter__(self):
        print(f"⏱️ [TIMER] Starting task: {self.task_name}")
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"✅ [TIMER] Task '{self.task_name}' finished in {self.elapsed:.4f}s")
        # Return False to propagate exceptions (default)

# 2. FUNCTION-BASED CONTEXT MANAGER (@contextmanager)
@contextmanager
def file_writer(filename):
    """A context manager for simplified file writing."""
    print(f"📂 [FILE] Opening {filename}")
    f = open(filename, "w")
    try:
        # yield acts as __enter__
        yield f
    finally:
        # Guarantee cleanup acts as __exit__
        print(f"🧹 [FILE] Closing {filename}")
        f.close()

def run_lab():
    print("=" * 60)
    print("🪄 RESOURCE MANAGER DEMO LAB")
    print("=" * 60)

    # Example 1: Timing a block
    print("\nExample 1: Using Class-based Timer")
    with ExecutionTimer("Complex Calculation"):
        # Simulate heavy work
        sum(i * i for i in range(1_000_000))

    # Example 2: File Writing
    print("\nExample 2: Using Function-based File Writer")
    with file_writer("lab_output.txt") as f:
        f.write("Standardized Python Hub Log: Success\n")
        print("   Writing to file inside context...")

    # Example 3: Error Recovery in Context
    print("\nExample 3: Error Protection")
    try:
        with file_writer("error_log.txt") as f:
            print("   About to crash...")
            10 / 0 # This will trigger finally
    except ZeroDivisionError:
        print("   ❌ Error caught safely at top level.")

    print("=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    run_lab()
