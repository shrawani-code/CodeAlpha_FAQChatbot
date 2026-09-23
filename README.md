# 🤖 AI FAQ Chatbot

An NLP-based FAQ chatbot developed using Python, NLTK, Scikit-learn, and Streamlit. The chatbot matches user questions with the most relevant FAQ using TF-IDF and cosine similarity.

## 📌 Project Overview

The AI FAQ Chatbot is designed to answer frequently asked college-related questions.

Users can ask questions about:

- College working hours
- Examinations
- Attendance
- Fees
- Library services
- Internships
- Student ID cards
- College events
- Study materials
- Faculty communication

The chatbot processes the user's question and identifies the most relevant FAQ from a predefined knowledge base.

## ✨ Features

- 💬 Interactive chatbot interface
- 🧠 Natural Language Processing
- 🔍 TF-IDF based text vectorization
- 📊 Cosine similarity for question matching
- 🔤 Text preprocessing and stopword removal
- 🔄 Synonym normalization
- 🎯 Similarity-based confidence score
- 💭 Chat history
- 💡 Suggested questions
- 🧹 Clear conversation option
- ⚠️ Fallback response for unsupported questions

## 🛠️ Technologies Used

- Python
- NLTK
- Scikit-learn
- Streamlit
- JSON

## 🧠 How It Works

The chatbot follows these steps:

```text
User Question
      ↓
Text Preprocessing
      ↓
Stopword Removal
      ↓
Synonym Normalization
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity
      ↓
Best FAQ Match
      ↓
Answer Displayed
