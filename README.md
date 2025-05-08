# 🧠 Fake News Detector

An AI-powered fake news detector built using **Streamlit** and **scikit-learn**. This project classifies news articles as **Real** or **Fake** using machine learning.

##  Demo
![App UI](screenshots/ui.png)

## 🎥 Demo
![Fake News Detector GIF](https://github.com/meramp11mmf/fake-news-detectorr/raw/main/fake%20news.gif)
 ![App Screenshot](https://github.com/meramp11mmf/fake-news-detectorr/raw/main/app.png)


##  How It Works

1. Dataset: [Fake and Real News Dataset - Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
2. Preprocessing with `pandas`
3. Feature extraction using `TF-IDF Vectorizer`
4. Classification using `Logistic Regression`
5. Frontend built with `Streamlit`

---

## 🛠 Technologies Used

- **Python 3.x**
- **Streamlit** – for interactive web UI
- **scikit-learn** – for ML models
- **Joblib** – to save/load models
- **TF-IDF** – for feature extraction

---

## 💻 How to Run the App Locally

```bash
git clone https://github.com/yourusername/fake-news-detector.git
cd fake-news-detector
pip install -r requirements.txt
streamlit run app.py
