import requests
import random
import json
import os
import urllib.parse

def main():
    with open('flashcards.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    card = random.choice(data)
    formula_latex = card['a']
    formula_encoded = urllib.parse.quote(formula_latex)
    url_imagen = f"https://quicklatex.com/latex3.f?formula={formula_encoded}&fsize=20px&fcolor=000000&mode=0"
    
    token = os.environ.get('TELEGRAM_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    
    url_telegram = f"https://api.telegram.org/bot{token}/sendPhoto"
    
    payload = {
        "chat_id": chat_id,
        "photo": url_imagen,
        "caption": f"🧠 *Flashcard: {card['q']}*",
        "parse_mode": "Markdown"
    }
    
    response = requests.post(url_telegram, data=payload)
    
    # --- ESTA LÍNEA ES LA CLAVE ---
    print(f"Status Code: {response.status_code}")
    print(f"Respuesta de Telegram: {response.text}")
    
    if response.status_code != 200:
        print("¡Error detectado! Revisa el mensaje de arriba.")

if __name__ == "__main__":
    main()
