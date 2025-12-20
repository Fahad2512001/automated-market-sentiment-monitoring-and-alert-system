import time
from news_fetcher import fetch_news
from sentiment_analyzer import analyze_sentiment
from notifier import send_to_telegram

def process_news():
    news_items = fetch_news()
    for item in news_items:
        title = item.get("title", "")
        url = item.get("url", "")
        published = item.get("published_at", "")

        score, impact = analyze_sentiment(title)
        if impact != "Low":
            send_to_telegram(title, url, score, impact, published)

if __name__ == "__main__":
    while True:
        process_news()
        print("Waiting for next cycle...")
        time.sleep(600)  # 10 mins
