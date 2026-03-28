"""
LAB PRACTICAL: PyTorch Training Loop (Linear Regression)
Standard: PPM V4 - Gold Standard

Tujuan: Memahami mekanisme Autograd dan siklus pelatihan model (Loop).
Guna: Dasar pelatihan neural networks kelas dunia.
"""

import torch
import torch.nn as nn
import torch.optim as optim

def run_training_lab():
    print("=" * 60)
    print("🚀 PYTORCH TRAINING LOOP LAB: Linear Regression")
    print("=" * 60)

    # 1. GENERATE DATA: y = 2x + 1
    # Adding some noise
    X = torch.linspace(0, 5, 20).view(-1, 1)
    y = 2 * X + 1 + torch.randn(X.size()) * 0.5
    
    print("\n1. Model Initialization...")
    # 2. DEFINE MODEL (Linear layer: y = Wx + b)
    model = nn.Linear(1, 1)
    
    # 3. DEFINE LOSS & OPTIMIZER
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    print("\n2. Starting Training Cycle (50 Epochs):")
    # 4. TRAINING LOOP
    for epoch in range(1, 101):
        # Forward Pass
        outputs = model(X)
        loss = criterion(outputs, y)
        
        # Backward Pass (The Magic of Autograd)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if epoch % 10 == 0:
            print(f"   [EPOCH {epoch:3}] Loss: {loss.item():.4f} | W={model.weight.item():.2f}, b={model.bias.item():.2f}")

    # 5. FINAL RESULTS
    print("\n3. Final Training Results:")
    w_final = model.weight.item()
    b_final = model.bias.item()
    print(f"   [MODEL] Equation: y = {w_final:.2f}x + {b_final:.2f}")
    print(f"   [NOTE] Target was: y = 2.0x + 1.0")

    print("\n" + "=" * 60)
    print("✅ Lab Completed. PyTorch successfully minimized the error via gradients.")

if __name__ == "__main__":
    run_training_lab()
