import pandas as pd
import re
from textblob import TextBlob
import nltk


from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words("english"))

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9.,!? ]", "", text)
    return text.strip()

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # -1 negativ, 1 pozitiv

def transform(df):
    df["clean_content"] = df["content"].apply(clean_text)
    df["sentiment"] = df["clean_content"].apply(analyze_sentiment)
    df["word_count"] = df["clean_content"].apply(lambda x: len(x.split()))
    return df
