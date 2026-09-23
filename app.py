import json
import re

import nltk
import streamlit as st

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==============================
# PAGE CONFIGURATION
# ==============================

st.set_page_config(
    page_title="AI FAQ Assistant",
    page_icon="🤖",
    layout="centered"
)


# ==============================
# CUSTOM CSS
# ==============================

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 38px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 17px;
        margin-bottom: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==============================
# NLTK CONFIGURATION
# ==============================

nltk.download("stopwords", quiet=True)

stop_words = set(stopwords.words("english"))


# ==============================
# LOAD FAQ DATA
# ==============================

with open("faqs.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)


# ==============================
# TEXT PREPROCESSING
# ==============================

synonyms = {
    "begin": "start",
    "begins": "start",
    "beginning": "start",
    "commence": "start",
    "commences": "start",
    "ends": "finish",
    "ending": "finish",
    "apply": "register",
    "applying": "register",
    "lose": "lost",
    "loses": "lost",
    "losing": "lost",
    "missing": "lost",
    "obtain": "get",
    "internet": "online",
    "through": "via",
    "see": "check",
    "view": "check",
    "look": "check"
}


def preprocess_text(text):
    """
    Converts text into normalized words.
    """

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z0-9\s]",
        "",
        text
    )

    words = text.split()

    words = [
        word
        for word in words
        if word not in stop_words
    ]

    words = [
        synonyms.get(word, word)
        for word in words
    ]

    return words


# ==============================
# TF-IDF SIMILARITY
# ==============================

faq_questions = [
    faq["question"]
    for faq in faqs
]


vectorizer = TfidfVectorizer(
    tokenizer=preprocess_text,
    token_pattern=None
)


faq_vectors = vectorizer.fit_transform(
    faq_questions
)


def calculate_similarity(user_question):
    """
    Calculates similarity between the user's question
    and all FAQ questions.
    """

    user_vector = vectorizer.transform(
        [user_question]
    )

    similarity_scores = cosine_similarity(
        user_vector,
        faq_vectors
    )

    return similarity_scores[0]


# ==============================
# FIND BEST ANSWER
# ==============================

def get_answer(user_question):

    user_words = set(
        preprocess_text(user_question)
    )

    # Special handling for lost or missing ID cards
    if "lost" in user_words:

        for faq in faqs:

            faq_words = set(
                preprocess_text(faq["question"])
            )

            if "lost" in faq_words:

                return faq["answer"], 1.0

    # Calculate TF-IDF similarity
    similarity_scores = calculate_similarity(
        user_question
    )

    best_index = similarity_scores.argmax()
    best_score = float(
        similarity_scores[best_index]
    )

    # Improve matching using common keywords
    for index, faq in enumerate(faqs):

        faq_words = set(
            preprocess_text(faq["question"])
        )

        common_words = user_words.intersection(
            faq_words
        )

        keyword_bonus = min(
            len(common_words) * 0.03,
            0.15
        )

        improved_score = (
            float(similarity_scores[index])
            + keyword_bonus
        )

        if improved_score > best_score:

            best_score = improved_score
            best_index = index

    # Fallback response
    if best_score < 0.15:

        return (
            "I'm sorry, I couldn't find a suitable answer. "
            "Please try asking about exams, fees, internships, "
            "attendance, timetable, or college services.",
            best_score
        )

    best_answer = faqs[best_index]["answer"]

    return best_answer, best_score


# ==============================
# HEADER
# ==============================

st.markdown(
    '<div class="main-title">🤖 AI FAQ Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Ask questions and get instant answers using NLP'
    '</div>',
    unsafe_allow_html=True
)


# ==============================
# SIDEBAR
# ==============================

with st.sidebar:

    st.header("📊 About the Chatbot")

    st.write(
        "This AI chatbot uses Natural Language Processing "
        "to match your question with the most relevant FAQ."
    )

    st.divider()

    st.write(
        f"📚 **Total FAQs:** {len(faqs)}"
    )

    st.write("🧠 **NLP:** Text Preprocessing")

    st.write("🔍 **Matching:** TF-IDF + Cosine Similarity")

    st.write("🐍 **Language:** Python")

    st.write("🎨 **UI:** Streamlit")

    st.divider()

    st.header("💡 Suggested Questions")

    suggested_questions = [
        "Where is the college library?",
        "What should I do if I lose my student ID card?",
        "How can I prepare for campus placements?",
        "What should I do if my online fee payment fails?",
        "How can I register for college events?"
    ]

    for question in suggested_questions:

        st.write(f"👉 {question}")


# ==============================
# CHAT HISTORY
# ==============================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ==============================
# WELCOME MESSAGE
# ==============================

if len(st.session_state.messages) == 0:

    st.info(
        "👋 Hello! I'm your AI FAQ Assistant. "
        "Ask me anything about college services."
    )


# ==============================
# DISPLAY CHAT HISTORY
# ==============================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"],
        avatar=(
            "👤"
            if message["role"] == "user"
            else "🤖"
        )
    ):

        st.write(message["content"])

        if "score" in message:

            confidence = min(
                message["score"] * 100,
                100
            )

            st.caption(
                f"🎯 Match Confidence: {confidence:.1f}%"
            )


# ==============================
# USER INPUT
# ==============================

user_question = st.chat_input(
    "💬 Type your question here..."
)


# ==============================
# PROCESS USER QUESTION
# ==============================

if user_question:

    with st.chat_message(
        "user",
        avatar="👤"
    ):

        st.write(user_question)

    response, score = get_answer(
        user_question
    )

    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        st.write(response)

        confidence = min(
            score * 100,
            100
        )

        if score >= 0.15:

            st.caption(
                f"🎯 Match Confidence: {confidence:.1f}%"
            )

        else:

            st.caption(
                "⚠️ No strong FAQ match found."
            )

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
            "score": score
        }
    )


# ==============================
# CLEAR CHAT
# ==============================

if st.session_state.messages:

    if st.button(
        "🧹 Clear Conversation"
    ):

        st.session_state.messages = []

        st.rerun()


# ==============================
# FOOTER
# ==============================

st.divider()

st.caption(
    "CodeAlpha Artificial Intelligence Internship • "
    "AI FAQ Chatbot"
)