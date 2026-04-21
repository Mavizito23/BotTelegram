import requests
import random
import json
import os
import urllib.parse

def main():
    # 1. Cargar el JSON
    with open('flashcards.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    card = random.choice(data)
    
    # 2. Preparar la fórmula para la URL
    # QuickLaTeX espera el LaTeX puro. Urllib.parse.quote convierte caracteres 
    # como '\', '{', '}' en formato URL seguro.
    formula_latex = card['a']
    formula_encoded = urllib.parse.quote(formula_latex)
    
    # URL de la API de renderizado (se ve con calidad de imprenta)
    url_imagen = f"https://quicklatex.com/latex3.f?formula={formula_encoded}&fsize=20px&fcolor=000000&mode=0"
    
    # 3. Enviar a Telegram como Foto
    token = os.environ.get('TELEGRAM_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    
    url_telegram = f"https://api.telegram.org/bot{token}/sendPhoto"
    
    payload = {
        "chat_id": chat_id,
        "photo": url_imagen,
        "caption": f"🧠 *Flashcard de Probabilidad*\n\n*Pregunta:* {card['q']}",
        "parse_mode": "Markdown"
    }
    
    requests.post(url_telegram, data=payload)

if __name__ == "__main__":
    main()
