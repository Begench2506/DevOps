import pytest
from app import app, r  # Импортируем приложение и Redis

@pytest.fixture
def client():
    """Тестовый клиент Flask."""
    with app.test_client() as client:
        yield client

def test_home(client):
    """Юнит-тест для главной страницы."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Скоро здесь будет веб-приложение ТОРИ Арена!" in response.data

def test_redis_connection():
    """Тест подключения к Redis."""
    r.set("test_key", "test_value")
    value = r.get("test_key").decode("utf-8")
    assert value == "test_value"

def test_redis_visits(client):
    """Интеграционный тест увеличения счетчика посещений."""
    initial_visits = int(r.get("visits") or 0)
    client.get('/')
    new_visits = int(r.get("visits"))
    assert new_visits == initial_visits + 1
