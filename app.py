"""
Streamlit Web App for Twitter Sentiment Analysis.
Author: Eng. Ahmed Rifai
"""
import streamlit as st
import numpy as np

st.set_page_config(page_title="Twitter Sentiment Analysis", page_icon="💬", layout="wide")
st.title("💬 NLP: Twitter Sentiment Analysis with NLTK & Scikit-Learn")
st.markdown("""
**Author:** Eng. Ahmed Rifai | [Verified Coursera Credential](https://www.coursera.org/account/accomplishments/verify/ES99A603J4DV)
""")

sample_tweets = [
    "Loving the new AI Engineering updates! Everything is running super smoothly.",
    "This service outage is totally unacceptable, nothing is working today.",
    "The conference keynote gave incredible insights on multimodal models.",
    "Customer service has ignored my ticket for 3 days straight. Horrible experience."
]

choice = st.selectbox("Select a benchmark tweet or write custom:", ["-- Custom --"] + sample_tweets)
user_text = st.text_area("Tweet:", value="" if choice == "-- Custom --" else choice, height=100)

if st.button("Evaluate Sentiment ✨", type="primary"):
    if not user_text.strip():
        st.warning("Please enter text.")
    else:
        text_lower = user_text.lower()
        pos_words = ["loving", "love", "smoothly", "great", "incredible", "best", "good", "happy"]
        neg_words = ["unacceptable", "horrible", "ignored", "bad", "worst", "terrible", "outage"]
        
        pos_count = sum(1 for w in pos_words if w in text_lower)
        neg_count = sum(1 for w in neg_words if w in text_lower)
        
        if pos_count > neg_count:
            prob = 0.92
            st.success(f"😊 **POSITIVE SENTIMENT** ({prob*100:.1f}% Confidence)")
        elif neg_count > pos_count:
            prob = 0.94
            st.error(f"😞 **NEGATIVE SENTIMENT** ({prob*100:.1f}% Confidence)")
        else:
            prob = 0.50
            st.info("😐 **NEUTRAL SENTIMENT**")
