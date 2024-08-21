#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
from googletrans import Translator, LANGUAGES, LANGUAGES as lang_dict

# Streamlit app
st.title("Language Translator")

# Text input
text_input = st.text_area("Enter text to translate:")

if text_input:
    # Initialize translator
    translator = Translator()

    # Detect language
    detected = translator.detect(text_input)
    detected_lang = detected.lang
    detected_language_name = LANGUAGES.get(detected_lang, 'Unknown')

    st.write(f"Detected language: {detected_language_name}")

    # Language selection
    target_language = st.selectbox(
        "Choose target language:",
        options=list(LANGUAGES.keys()),
        format_func=lambda x: LANGUAGES[x]
    )

    # Translate text
    if st.button("Translate"):
        try:
            translation = translator.translate(text_input, dest=target_language)
            st.subheader("Translated Text")
            st.write(translation.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")


# In[ ]:




