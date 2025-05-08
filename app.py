import streamlit as st
import joblib

# Load model and vectorizer with error handling
try:
    model = joblib.load(r"C:\Users\melha\Downloads\app\model.pkl")
    vectorizer = joblib.load(r"C:\Users\melha\Downloads\app\vectorizer.pkl")
except Exception as e:
    st.error(f"Error loading model or vectorizer: {e}")
    st.stop()

st.set_page_config(page_title="🧠 Fake News Detector")
st.title("📰 AI Fake News Detector")

user_input = st.text_area("Paste a news article or headline here:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Vectorize and predict
        input_tfidf = vectorizer.transform([user_input])
        prediction = model.predict(input_tfidf)[0]
        proba = model.predict_proba(input_tfidf)[0]

        label = "🟢 Real News" if prediction == 1 else "🔴 Fake News"
        confidence = round(proba[prediction] * 100, 2)

        st.subheader(label)
        st.write(f"**Confidence:** {confidence}%")

        # Fact-checking for fake news
        if label == "🔴 Fake News":
            fact_check_url = f"https://www.google.com/search?q={user_input.replace(' ', '+')}+site:snopes.com+OR+site:reuters.com"
            st.markdown(f"**Fact-check this news**: [Search fact-check results here]({fact_check_url})")

st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")
