import requests
from config import CRYPTO_PANIC_API_KEY
from notifier import send_to_telegram

def fetch_news():
    url = f"Your URL here"
    try:
        response = requests.get(url)
        response.raise_for_status()

        news = response.json().get("results", [])
        if not news:
            send_to_telegram("wait don’t get too hyped or make wrong decision")

        return news

    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        send_to_telegram("wait don’t get too hyped or make wrong decision")
        return []

