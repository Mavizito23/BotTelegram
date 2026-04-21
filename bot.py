import requests
import random
import json
import os
import urllib.parse

def enviar_telegram_imagen(mensaje, formula_latex):
    token = os.environ.get('TELEGRAM_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    
    # 1. Generamos la URL de la imagen (la fórmula renderizada)
    # Codificamos la fórmula para que sea una URL válida
    formula_codificada = urllib.parse.quote(formula_latex)
    # URL de la API de renderizado (fórmula blanca sobre fondo transparente)
    url_imagen = f"https://quicklatex.com/latex3.f?formula={formula_codificada}&fsize=20px&fcolor=000000"
    
    # 2. Enviamos la foto a través de la API de Telegram
    # Telegram permite enviar fotos pasando directamente la URL
    url_telegram = f"https://api.telegram.org/bot{token}/sendPhoto"
    payload = {
        "chat_id": chat_id,
        "photo": url_imagen,
        "caption": f"*Flashcard del Día*\n\n*Pregunta:* {mensaje}",
        "parse_mode": "Markdown"
    }
    requests.post(url_telegram, data=payload)

def main():
    with open('flashcards.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    card = random.choice(data)
    # El mensaje es la pregunta y la foto es la respuesta (la fórmula)
    enviar_telegram_imagen(card['q'], card['a'])

if __name__ == "__main__":
    main()
