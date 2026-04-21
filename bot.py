import requests
import random
import json
import os

def enviar_telegram(mensaje):
    # Lee las credenciales de las variables de entorno
    token = os.environ.get('TELEGRAM_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": mensaje, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

def main():
    with open('flashcards.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    card = random.choice(data)

    mensaje = f"🧠 *Flashcard del Día*\n\n*Q:* {card['q']}\n\n*A:* `{card['a']}`"
    
    enviar_telegram(mensaje)

if __name__ == "__main__":
    main()
