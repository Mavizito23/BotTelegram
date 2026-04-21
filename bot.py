import requests
import random
import json
import os
import urllib.parse

def main():
    with open('flashcards.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    card = random.choice(data)
    
    # --- LA MAGIA ESTÁ AQUÍ ---
    # \dpi{300} -> Sube la resolución al máximo.
    # \huge -> Hace que el tamaño de fuente base sea grande.
    # \color{black} -> Asegura que sea legible sobre el fondo blanco/oscuro de Telegram.
    formula = card['a']
    formula_encoded = urllib.parse.quote(formula)
    url_imagen = f"https://latex.codecogs.com/png.latex?\\dpi{{300}}\\huge\\color{{black}}{{{formula_encoded}}}"
    
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
    print(f"Status Code: {response.status_code}")
    print(f"Respuesta: {response.text}")

if __name__ == "__main__":
    main()
