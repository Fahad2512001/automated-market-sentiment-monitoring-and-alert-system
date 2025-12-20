import requests
from config import CRYPTO_PANIC_API_KEY
from notifier import send_to_telegram

def fetch_news():
    url = f"https://cryptopanic.com/api/developer/v2/posts/?auth_token=b9b125d3d6aab48634e50192e39268635170786f&filter=important"
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
