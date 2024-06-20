from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_hour = datetime.now().hour
    print(f"Current hour: {current_hour}")  # Добавьте эту строку для отладки

    if 6 <= current_hour < 12:
        greeting = "Доброе утро"
    elif 12 <= current_hour < 18:
        greeting = "Добрый день"
    elif 18 <= current_hour < 24:
        greeting = "Добрый вечер"
    else:
        greeting = "Доброй ночи"

    print(f"Greeting: {greeting}")  # Добавьте эту строку для отладки
    return render_template('index.html', greeting=greeting)