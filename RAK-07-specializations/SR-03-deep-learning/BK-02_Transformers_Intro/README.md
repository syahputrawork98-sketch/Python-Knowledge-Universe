# BK-02: Transformers & Local Models (Open-Source Intelligence) [x] Complete

> **"Yesterday's AI was a superpower; today's AI is a library you can run on your own hardware."**

Buku ini membedah **Transformers**, arsitektur revolusioner yang mendasari hampir seluruh model bahasa modern (Generative AI). Kita akan mempelajari bagaimana menggunakan ekosistem **Hugging Face** untuk menjalankan model-model canggih seperti **Llama-3**, **Mistral**, dan **Gemma** secara lokal—memberikan privasi dan efisiensi biaya yang tidak dimiliki oleh API tertutup.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers/index)
- **Model Registry**: [Hugging Face Hub (The "GitHub of AI")](https://huggingface.co/models)

---

## 🧠 The Essence (Narrative)
Era AI modern dimulai saat paper *"Attention is All You Need"* dipublikasikan. Arsitektur Transformer membuang mekanisme pemrosesan teks yang berurutan (seperti RNN/LSTM) dan menggantinya dengan **Mechanism of Attention**: kemampuan model untuk melihat seluruh kalimat secara bersamaan dan menentukan kata mana yang paling penting bagi makna kalimat tersebut. Intisari dari bab ini adalah memahami bagaimana **Tokenizer** memecah teks menjadi potongan kecil (bukan hanya kata) dan bagaimana **Weights** (bobot numerik) mewakili kecerdasan model.

---

## 🎨 Visual Logic (Transformer Architecture Simplified)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#FFD43B', 'primaryTextColor': '#000', 'lineColor': '#3776AB'}}}%%
graph TD
    Input[Input Text: 'Python is'] --> Token[Tokenizer: [45, 12, 5]]
    Token --> Embed[Embedding Space: Latent Meaning]
    Embed --> Attn[Self-Attention Layer: Relationships]
    Attn --> Feed[Feed Forward: Transformation]
    Feed --> Output[Prediction: 'Powerful']
    
    style Attn fill:#FFD43B,stroke:#333,color:#000
    style Output fill:#3776AB,stroke:#333,color:#fff
```

---

## 🛠️ Implementation: Local Inference with HF
```python
from transformers import pipeline

# 1. Pipeline Initialization (Auto-downloads model & tokenizer)
generator = pipeline("text-generation", model="gpt2") # Model kecil untuk tes

# 2. Text Generation
result = generator("The future of Python is", max_length=30, num_return_sequences=1)

# 3. Output Analysis
print(f"   [RESULT] {result[0]['generated_text']}")
```

---

## ⚠️ Pitfalls
- **VRAM Hunger**: Menjalankan model besar (seperti Llama 70B) membutuhkan kartu grafis (GPU) dengan memori (VRAM) yang sangat besar. Gunakan teknik **Quantization** (seperti GGUF atau 4-bit/8-bit precision) untuk menjalankan model besar di perangkat keras standar.
- **Weight Drift**: Menjalankan model berbeda (misal: Llama vs Mistral) dengan tokenizer yang sama akan menghasilkan output yang acak-acakan. Selalu gunakan `AutoTokenizer` yang sesuai dengan model spesifiknya.
- **License Compliance**: Model open-source tidak selalu berarti bebas digunakan untuk tujuan komersial. Pastikan Anda memeriksa lisensi model tersebut (misalnya Llama-3 memiliki lisensi khusus meskipun kodenya terbuka).

---
*Back to [SR-03 GenAI & LLM Ops](../README.md)*
