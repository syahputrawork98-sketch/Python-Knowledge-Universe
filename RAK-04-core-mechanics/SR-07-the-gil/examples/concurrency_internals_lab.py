"""
LAB PRACTICAL: Concurrency Internals (The GIL Experiment)
Standard: PPM V4 - Gold Standard

Tujuan: Membuktikan batasan GIL secara empiris.
Guna: Memilih strategi paralelisme yang tepat (Threads vs Processes).
"""

import time
import threading
import multiprocessing
import os

# 1. CPU-BOUND TASK (Calculations)
def cpu_bound_task(n):
    print(f"   [START] PID: {os.getpid()} - Process/Thread working...")
    count = 0
    while count < n:
        count += 1
    return count

# 2. I/O-BOUND TASK (Simulated delay)
def io_bound_task(sec):
    print(f"   [START] PID: {os.getpid()} - I/O waiting...")
    time.sleep(sec)
    return "Done"

def run_concurrently(task_func, args, mode="threads"):
    """Helper to run tasks in parallel."""
    start_time = time.time()
    workers = []
    
    if mode == "threads":
        Constructor = threading.Thread
    else:
        Constructor = multiprocessing.Process
        
    for _ in range(2):
        w = Constructor(target=task_func, args=(args,))
        workers.append(w)
        w.start()
        
    for w in workers:
        w.join()
        
    end_time = time.time()
    return end_time - start_time

def run_lab():
    print("=" * 60)
    print("🚀 PYTHON GIL & CONCURRENCY LAB")
    print("=" * 60)

    # PARTE 1: CPU-BOUND (The GIL Battle)
    print("\n1. CPU-BOUND TEST (2 million increments x 2)")
    # Sequential
    start = time.time()
    cpu_bound_task(2_000_000)
    cpu_bound_task(2_000_000)
    seq_time = time.time() - start
    print(f"   [TIME] Sequential: {seq_time:.4f}s")
    
    # Threaded (GIL will bottleneck)
    thread_time = run_concurrently(cpu_bound_task, 2_000_000, mode="threads")
    print(f"   [TIME] Multi-threaded: {thread_time:.4f}s (Likely slower than sequential due to GIL overhead)")
    
    # Processed (True parallelism)
    proc_time = run_concurrently(cpu_bound_task, 2_000_000, mode="processes")
    print(f"   [TIME] Multi-processing: {proc_time:.4f}s (True Parallelism - Bypass GIL)")

    # PARTE 2: I/O-BOUND (The GIL Release)
    print("\n2. I/O-BOUND TEST (1 second sleep x 2)")
    # Sequential
    start = time.time()
    io_bound_task(1)
    io_bound_task(1)
    seq_io = time.time() - start
    print(f"   [TIME] Sequential: {seq_io:.4f}s")
    
    # Threaded (GIL is released during sleep)
    thread_io = run_concurrently(io_bound_task, 1, mode="threads")
    print(f"   [TIME] Multi-threaded: {thread_io:.4f}s (Almost simultaneous!)")

    print("\n" + "=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    run_lab()
