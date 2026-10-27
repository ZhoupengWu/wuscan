import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN_BOT = os.getenv("TOKEN_TELEGRAM")
CHAT_ID = os.getenv("CHAT_ID")

def isAvaibleBot() -> bool:
    return bool(TOKEN_BOT)

def _makeRequest(http_method: str, method_name: str, data: dict = None):
    if not isAvaibleBot():
        return {"err": "Manca TOKEN_TELEGRAM"}

    url = f"https://api.telegram.org/bot{TOKEN_BOT}/{method_name}"
    http_method = http_method.strip().lower()

    try:
        if http_method == "get":
            response = requests.get(url, data, timeout=10)
        elif http_method == "post":
            response = requests.post(url, json=data, timeout=10)
        else:
            return {"err": f"Metodo HTTP non supportato: {http_method}"}

        body = response.json()
    except (requests.RequestException, ValueError) as e:
        return {"err": str(e)}

    if not response.ok:
        return {"err": body}

    return body

def sendMessage(text: str, chat_id: str = None):
    return _makeRequest("post", "sendMessage", {
        "chat_id": chat_id or CHAT_ID,
        "text": text
    })
