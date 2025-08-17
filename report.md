📋 Landmark Mapper - REPORT.md

🧑‍🤝‍🧑 Team Info

Team Name: Landmark Mappers

Team Members: Shaik Imran (Lead Developer), [Add more if any]

Affiliation: Swecha / viswam.ai Startup Simulation 2025

Track: AI for Culture & Community

🌍 Application Overview

Landmark Mapper is a Streamlit-based web app that enables users to upload images of local Indian landmarks and contribute regional descriptions. Using OCR and AI (RAG model), it enriches cultural data and builds a multilingual corpus of landmark knowledge from grassroots contributors.

🧠 AI Components

OCR: pytesseract extracts textual elements from uploaded images.

AI Language Model: facebook/rag-token-base from Hugging Face is used for retrieval-augmented generation to understand and enhance landmark descriptions.

Tokenizer: RagTokenizer for input pre-processing.

Retriever: RagRetriever integrates Wikipedia-style retrieval.

🏗️ Architecture

Frontend: Streamlit app with image uploader, text input, and AI output.

Backend:

Image processed with Pillow

OCR with pytesseract

RAG pipeline (Hugging Face Transformers & Datasets)

Hosting: Deployed live on Hugging Face Spaces

[User Image] --
               |--> [OCR Text] --> [User Description] --> [RAG Model] --> [Enhanced Output]

🧪 Testing

✅ Verified OCR on sample images (temples, statues, historical sites)

✅ AI summary generation tested in English, Hindi, and Telugu

✅ UI tested on desktop and mobile

❗ Pending: Save collected descriptions to database or file for long-term dataset generation

🛣️ Roadmap

Phase

Feature

Status

Week 1

Streamlit UI, OCR integration

✅ Complete

Week 2

Hugging Face RAG setup

✅ Complete

Week 3

Deploy to Spaces, add multilingual input

✅ Complete

Week 4

Contribution tracking, roadmap & analytics

🔄 In Progress

📈 User Growth Strategy

Partner with rural tech camps, colleges, and local orgs

Encourage users to upload local heritage spots

Provide leaderboard or certificate-based recognition

Embed QR code in physical locations to crowdsource data

🔮 Future Vision

🌐 Expand to mobile-first app experience

🗺️ Use geolocation & reverse geocoding to auto-detect locations

🏛️ Collaborate with tourism departments for verification

📚 Publish open-access corpus of Indian landmark descriptions

🧠 Fine-tune multilingual LLM on collected landmark data

📎 Links

🔗 Code Repo: https://code.swecha.org/YOUR_USERNAME/landmark-mapper

🌐 Live App: https://huggingface.co/spaces/YOUR_USERNAME/landmark-mapper

🎥 Demo Video: [Upload YouTube or Drive link here once recorded]

Built for viswam.ai Startup Simulation Challenge, 2025 ✨

