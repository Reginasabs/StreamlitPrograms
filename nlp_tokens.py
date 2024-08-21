#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk

nltk.download('punkt')

def tokenize_text(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    unique_words = set(words)
    print("Sentences:", sentences)  # Debug output
    print("Words:", words)          # Debug output
    print("Unique Words:", unique_words)  # Debug output
    return sentences, unique_words

st.title("Text Tokenization App")

text_input = st.text_area("Enter your text here:", key='text_area_1')

if text_input:
    sentences, unique_words = tokenize_text(text_input)

    st.subheader("Sentence Tokens")
    st.write(sentences)

    st.subheader("Unique Word Tokens")
    st.write(sorted(unique_words))


# In[ ]:




