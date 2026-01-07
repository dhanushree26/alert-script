import requests
from bs4 import BeautifulSoup

URL = "https://karurcinemas.com/"
MOVIE = "Jana Nayagan"

BOT_TOKEN = "8413025462:AAG00S2gQzWQ_RuWDbWzFLfrqQOzHayoB1I"
CHAT_ID = "7447216774"

def send_alert(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def check_booking():
    r = requests.get(URL, timeout=15)
    soup = BeautifulSoup(r.text, "html.parser")

    if MOVIE.lower() in soup.get_text().lower():
        send_alert(f"🎬 BOOKING OPEN!\n\n{MOVIE} tickets are LIVE on Karur Cinemas!")
        return True
    return False

if check_booking():
    print("Booking found")
else:
    print("Not yet")
