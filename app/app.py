from flask import Flask
import redis
import os

app = Flask(__name__)

# Подключение к Redis
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def home():
   	# Увеличиваем счетчик посещений в Redis
	visits = r.incr("visits") # Ключ "visits" увеличивается при каждом посещении
	return f"Скоро здесь будет веб-приложение ТОРГ Арена! Страница посещена {visits} раз."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
