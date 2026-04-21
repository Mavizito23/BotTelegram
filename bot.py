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

    formula_url = urllib.parse.quote(card['a'])
    latex_image_url = f"[https://quicklatex.com/latex3.f?formula=](https://quicklatex.com/latex3.f?formula=){formula_url}&fsize=15px&fcolor=000000"
    
    mensaje = f"*Flashcard del Día*\n\n*Q:* {card['q']}\n\n*A (en LaTeX):*\n{latex_image_url}"
    
    enviar_telegram(mensaje)

if __name__ == "__main__":
    main()
