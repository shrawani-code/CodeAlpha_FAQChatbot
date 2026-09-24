# 🤖 AI FAQ Chatbot

An NLP-based FAQ chatbot developed using **Python, NLTK, Scikit-learn, and Streamlit**. The chatbot processes user questions and finds the most relevant FAQ using **TF-IDF vectorization and cosine similarity**.

## 📌 Project Overview

The AI FAQ Chatbot is designed to answer frequently asked college-related questions using a predefined FAQ knowledge base.

Users can ask questions related to:

* College working hours
* Examinations
* Attendance
* Fees
* Library services
* Internships
* Student ID cards
* College events
* Study materials
* Faculty communication

The chatbot processes the user's question, compares it with the available FAQ questions, and displays the most relevant answer.

## ✨ Features

* 💬 Interactive chatbot interface
* 🧠 Natural Language Processing
* 🔍 TF-IDF-based text vectorization
* 📊 Cosine similarity for question matching
* 🧹 Text preprocessing and stopword removal
* 🔄 Synonym normalization
* 🎯 Similarity-based confidence score
* 💬 Chat history
* 💡 Suggested questions
* 🧹 Clear conversation option
* ⚠️ Fallback response for unsupported questions
* 🎨 Streamlit-based user interface

## 🛠️ Technologies Used

* **Python**
* **NLTK**
* **Scikit-learn**
* **Streamlit**
* **JSON**

## ⚙️ How It Works

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
```

## 📂 Project Structure

```text
CodeAlpha_FAQChatbot/
│
├── app.py
├── faqs.json
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/shrawani-code/CodeAlpha_FAQChatbot.git
```

### 2. Navigate to the project folder

```bash
cd CodeAlpha_FAQChatbot
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🎓 Internship Project

This project was developed as part of my **CodeAlpha Artificial Intelligence Internship**.

## 👩‍💻 Author

**Shrawani Anand Gholap**

GitHub: https://github.com/shrawani-code
LinkedIn: https://www.linkedin.com/in/shrawani-gholap-505423415/
