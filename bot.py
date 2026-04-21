import requests
import random
import json
import os
import urllib.parse

def main():
    with open('flashcards.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    card = random.choice(data)
    
    # Preparamos la fórmula para CodeCogs
    # Usamos una URL de CodeCogs que es más amigable para bots
    formula = card['a']
    
    # Codificamos la fórmula
    formula_encoded = urllib.parse.quote(formula)
    
    # Nueva URL de renderizado con CodeCogs
    # \dpi{120} controla el tamaño, \huge hace que sea legible en el móvil
    url_imagen = f"https://latex.codecogs.com/png.latex?\\dpi{{120}}\\huge\\color{{black}}{{{formula_encoded}}}"
    
    token = os.environ.get('TELEGRAM_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    
    url_telegram = f"https://api.telegram.org/bot{token}/sendPhoto"
    
    payload = {
        "chat_id": chat_id,
        "photo": url_imagen,
        "caption": f"🧠 *Flashcard de Probabilidad*\n\n*Pregunta:* {card['q']}",
        "parse_mode": "Markdown"
    }
    
    response = requests.post(url_telegram, data=payload)
    
    # Log para diagnóstico
    print(f"Status Code: {response.status_code}")
    print(f"Respuesta de Telegram: {response.text}")

if __name__ == "__main__":
    main()
