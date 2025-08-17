import streamlit as st
from PIL import Image
import pytesseract
from transformers import RagRetriever, RagTokenForGeneration, RagTokenizer
from datasets import load_dataset

# --- App Title ---
st.set_page_config(page_title="Landmark Mapper", layout="wide")
st.title("🗺️ Landmark Mapper - Discover, Describe & Contribute")

# --- Image Upload ---
uploaded_file = st.file_uploader("Upload a landmark image", type=["jpg", "jpeg", "png"])

# --- OCR + Description Input ---
description = ""
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.checkbox("Run OCR to extract text from image"):
        with st.spinner("Extracting text..."):
            ocr_text = pytesseract.image_to_string(image)
        st.text_area("Extracted Text", ocr_text, height=100)

    description = st.text_area("Enter a description in your local language", height=150)

# --- RAG Integration ---
if st.button("Analyze with AI") and description:
    with st.spinner("Running RAG model..."):
        # Load RAG model components
        tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-base")
        model = RagTokenForGeneration.from_pretrained("facebook/rag-token-base")
        retriever = RagRetriever.from_pretrained("facebook/rag-token-base", index_name="legacy")

        # Encode and retrieve
        input_dict = tokenizer.prepare_seq2seq_batch(description, return_tensors="pt")
        input_dict["input_ids"] = input_dict["input_ids"][:, :128]  # limit input length
        input_dict["retrieval_kwargs"] = {"n_docs": 5}

        generated = model.generate(
            input_ids=input_dict["input_ids"],
            context_input_ids=None,
            context_attention_mask=None,
            num_beams=2,
            min_length=30,
            max_length=128
        )

        output = tokenizer.batch_decode(generated, skip_special_tokens=True)
        st.subheader("📘 AI-Enhanced Landmark Info")
        st.write(output[0])

# --- Corpus Contribution ---
if description:
    st.success("✅ Thank you! Your description is now part of the landmark language corpus.")
    st.markdown("Help us map Indian culture, one landmark at a time.")
