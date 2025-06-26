from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
API_URL = os.getenv("API_URL")
SMM_KEY = os.getenv("SMM_KEY")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

@app.post(f"/webhook/{TELEGRAM_TOKEN}")
async def telegram_webhook(request: Request):
    data = await request.json()
    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "")

    if text == "/start":
        send_message(chat_id, "👋 Welcome to Rise Online Bot!\nChoose a platform to get started.")
    return {"ok": True}
