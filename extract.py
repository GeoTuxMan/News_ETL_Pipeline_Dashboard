import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract():
    url = "https://feeds.bbci.co.uk/news/world/rss.xml"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "xml")

    articles = []
    for item in soup.find_all("item", limit=5):
        title = item.title.text
        link = item.link.text

        # Fetch content from article page
        content = "No content available"
        try:
            article_page = requests.get(link)
            article_soup = BeautifulSoup(article_page.text, "html.parser")
            paragraphs = article_soup.select("div[data-component='text-block'] p")
            if not paragraphs:
                paragraphs = article_soup.find_all("p")
            if paragraphs:
                content = " ".join(p.get_text(strip=True) for p in paragraphs)
        except Exception as e:
            print(f"Eroare la descărcarea articolului {link}: {e}")

        articles.append({
            "title": title,
            "link": link,
            "content": content
        })

    return pd.DataFrame(articles)

if __name__ == "__main__":
    df = extract()
    print(df.head())
    print("Columns:", df.columns)
