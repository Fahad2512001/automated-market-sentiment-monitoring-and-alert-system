import time
from news_fetcher import fetch_news
from notifier import send_to_telegram

seen_titles = set()

while True:
    print("Checking for news...")
    news_items = fetch_news()

    new_sent = False

    for item in news_items:
        title = item["title"]
        if title not in seen_titles:
            seen_titles.add(title)
            message = f"{title}\n\n{item['url']}"
            send_to_telegram(message)
            new_sent = True

    # If no new news found
    if not new_sent:
        send_to_telegram("Wait, don’t get too hyped or make wrong decisions.")

    print("Waiting for next cycle...\n")
    time.sleep(300)  # Wait 5 minutes
