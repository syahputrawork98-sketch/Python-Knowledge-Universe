"""
LAB PRACTICAL: Conceptual RAG (Retrieval-Augmented Generation)
Standard: PPM V4 - Gold Standard

Tujuan: Memahami alur kerja RAG (Ingestion -> Retrieval -> Generation).
Guna: Dasar pembuatan kustom Chatbots dengan data internal perusahaan.
"""

import time

class MockVectorDB:
    def __init__(self):
        self.documents = []
        self.knowledge_base = {
            "cuti": "Karyawan berhak atas cuti tahunan selama 12 hari kerja.",
            "asuransi": "Asuransi kesehatan mencakup rawat inap dan rawat jalan bagi karyawan tetap.",
            "bonus": "Bonus akhir tahun diberikan berdasarkan performa tahunan dan profit perusahaan."
        }

    def search(self, query: str):
        """Simulasi pencarian semantik (Keywords mapping)."""
        print(f"   [RETRIEVAL] Searching for: '{query}'...")
        time.sleep(1) # Simulasi latensi pencarian
        for key, text in self.knowledge_base.items():
            if key in query.lower():
                return text
        return "Informasi tidak ditemukan di basis data."

class RAGOrchestrator:
    def __init__(self, db: MockVectorDB):
        self.db = db

    def ask(self, user_query: str):
        print("=" * 60)
        print(f"🚀 USER QUERY: {user_query}")
        
        # 1. RETRIEVAL STAGE
        context = self.db.search(user_query)
        print(f"   [CONTEXT] Found: {context}")

        # 2. PROMPT AUGMENTATION STAGE
        prompt = f"""
        Anda adalah asisten AI profesional. Berikan jawaban HANYA berdasarkan konteks di bawah ini.
        Konteks: {context}
        Pertanyaan: {user_query}
        Jawaban:
        """
        
        # 3. GENERATION STAGE (Simulated LLM)
        print("   [LLM] Generating Answer...")
        time.sleep(1)
        response = f"Berdasarkan data perusahaan, {context.lower()}"
        
        print(f"\n✨ AI RESPONSE: {response}")
        print("=" * 60)

if __name__ == "__main__":
    db = MockVectorDB()
    rag = RAGOrchestrator(db)
    
    # Test Case 1: Knowledge available
    rag.ask("Bagaimana aturan tentang cuti tahunan?")
    
    # Test Case 2: Knowledge available
    rag.ask("Apakah asuransi kesehatan ditanggung?")
    
    # Test Case 3: Knowledge missing
    rag.ask("Berapa gaji manajer?")
