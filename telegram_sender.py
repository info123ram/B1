import requests

BOT_TOKEN = "7697785458:AAE1C-nPYgjFtUxynQg1T4LJoYejd0pnC5c"
CHAT_ID = "5539280400"

def send_available_usernames(username):
    text = f"✅ Available Username: @{username}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)
