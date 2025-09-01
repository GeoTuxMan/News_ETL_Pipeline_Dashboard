from flask import Flask, render_template
import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # folderul dashboard/
DB_PATH = os.path.join(BASE_DIR, "..", "news.db")   


app = Flask(__name__)

def get_articles():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM articles", conn)
    conn.close()
    return df

@app.route("/")
def index():
    df = get_articles()
    # statistics
    avg_sentiment = df["sentiment"].mean()
    total_articles = len(df)
    return render_template("index.html", articles=df.to_dict(orient="records"),
                           avg_sentiment=avg_sentiment, total_articles=total_articles)

@app.route("/article/<int:article_id>")
def article(article_id):
    df = get_articles()
    if article_id >= len(df):
        return "Article not found", 404
    art = df.iloc[article_id].to_dict()
    return render_template("article.html", article=art)

if __name__ == "__main__":
    app.run(debug=True)

