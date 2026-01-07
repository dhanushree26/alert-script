import requests
from bs4 import BeautifulSoup
import os

URL = "https://karurcinemas.com/"
MOVIE = "Jana Nayagan"

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = "7447216774"

def send_alert(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def check_booking():
    r = requests.get(URL, timeout=15)
    soup = BeautifulSoup(r.text, "html.parser")
    page_text = soup.get_text().lower()

    if MOVIE.lower() in page_text:
        send_alert(
            f"🎬 BOOKING OPEN!\n\n{MOVIE} tickets are LIVE on Karur Cinemas!"
        )
    else:
        # TEMPORARY TEST MESSAGE
        send_alert(
            f"❌ Test check:\n{MOVIE} booking NOT found yet."
        )

check_booking()
