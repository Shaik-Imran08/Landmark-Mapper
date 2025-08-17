# 🗺️ Landmark Mapper - Discover, Describe & Contribute  

## 📌 Project Aim  
Landmark Mapper is an **AI-powered cultural mapping tool** that helps communities document, describe, and enrich information about landmarks.  
The project combines **OCR, local language descriptions, and AI (RAG)** to generate enhanced landmark insights, while also building a **cultural corpus** contributed by users.  

## 🚀 Features  
- 📤 **Upload Landmark Images**: Accepts `.jpg`, `.jpeg`, `.png` files.  
- 🔎 **OCR (Optical Character Recognition)**: Extracts text from landmark images using Tesseract.  
- 📝 **User Descriptions**: Allows users to describe landmarks in their **local languages**.  
- 🤖 **RAG (Retrieval-Augmented Generation)**: Enhances descriptions using HuggingFace RAG models.  
- 🌍 **Corpus Contribution**: Builds a multilingual cultural dataset with user contributions.  

## ⚙️ How It Works  
1. User uploads an image of a landmark.  
2. The app displays the image and optionally runs **OCR** to extract visible text.  
3. User provides a **local language description** of the landmark.  
4. On clicking **Analyze with AI**, the app:  
   - Retrieves relevant context with **RAG Retriever**  
   - Generates enriched information with **RAG TokenForGeneration**  
5. The final enhanced description is shown, and the user’s input is stored as part of the **landmark knowledge corpus**.  

## 🛠️ Tech Stack  
- **Frontend**: Streamlit (Python web app)  
- **OCR**: Pytesseract + Pillow  
- **AI Models**: HuggingFace Transformers (RAG model: `facebook/rag-token-base`)  
- **Datasets**: HuggingFace Datasets integration  
- **Backend**: Python




