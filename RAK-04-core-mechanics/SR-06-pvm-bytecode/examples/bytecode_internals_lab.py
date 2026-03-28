"""
LAB PRACTICAL: Bytecode Internals (AST & PVM)
Standard: PPM V4 - Gold Standard

Tujuan: Memahami bagaimana kode sumber diolah menjadi instruksi mesin virtual.
Guna: Optimasi performa dan debugging tingkat rendah.
"""

import ast
import dis
import sys

def get_bytecode(func):
    """Utility to print disassembled bytecode."""
    print(f"\n   [DIS] Disassembling '{func.__name__}':")
    dis.dis(func)

def run_lab():
    print("=" * 60)
    print("🚀 PYTHON RUNTIME & BYTECODE LAB")
    print("=" * 60)

    # 1. AST: Abstract Syntax Tree Genesis
    print("\n1. AST: The Tree of Thoughts")
    code_snippet = "x = (1 + 2) * 3"
    tree = ast.parse(code_snippet)
    print(f"   [DATA] Code: '{code_snippet}'")
    print(f"   [AST] Structure: {ast.dump(tree)}")
    
    # 2. Bytecode: The PVM Instructions
    print("\n2. Bytecode: Stack-based VM Instructions")
    
    def simple_add():
        x = 1
        y = 2
        return x + y
        
    def efficient_add():
        return 1 + 2 # Constant folding optimization

    get_bytecode(simple_add)
    get_bytecode(efficient_add)

    # 3. Instruction Comparison (Optimization)
    print("\n3. Modern Python Optimization (3.11+ Specialized)")
    print(f"   [INFO] Current Version: {sys.version.split()[0]}")
    
    def loop_range():
        for i in range(10):
            pass
            
    get_bytecode(loop_range)

    print("\n" + "=" * 60)
    print("✅ Lab Completed.")

if __name__ == "__main__":
    run_lab()
