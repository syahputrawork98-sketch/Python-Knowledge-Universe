"""
LAB PRACTICAL: FastAPI Async & Pydantic Validation
Standard: PPM V4 - Gold Standard

Tujuan: Memahami asinkronitas dalam penanganan HTTP request.
Guna: Dasar pembuatan mikroservis berperforma tinggi.
"""

import asyncio
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import List, Optional

app = FastAPI(title="Modern Inventory API")

# 1. SCHEMA (Pydantic V2)
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    is_offer: bool = False

# 2. MOCK ASYNC DATABASE
class MockDatabase:
    def __init__(self):
        self.data = []

    async def save(self, item: Item):
        """Simulasi I/O Database asinkron (Latency)."""
        print(f"   [DB] Saving {item.name}...")
        await asyncio.sleep(1) # Tunggu 1 detik (Non-blocking)
        self.data.append(item)
        return True

db = MockDatabase()

# 3. ENDPOINTS
@app.get("/")
async def read_root():
    return {"status": "Active", "engine": "FastAPI Async"}

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    """
    Endpoint ini mengonsumsi JSON, memvalidasinya dengan Item model,
    dan menyimpannya secara asinkron.
    """
    await db.save(item)
    return item

@app.get("/items/", response_model=List[Item])
async def read_items():
    return db.data

# 4. EXECUTION NOTE
if __name__ == "__main__":
    print("=" * 60)
    print("🚀 FASTAPI ASYNC LAB")
    print("   Run this with: uvicorn fastapi_async_lab:app --reload")
    print("=" * 60)
