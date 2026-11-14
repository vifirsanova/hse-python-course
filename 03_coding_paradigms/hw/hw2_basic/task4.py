# task4.py — Домашняя работа 10, базовый уровень.
# Задача 4. Простое приложение Flask и разбор HTML в BeautifulSoup.


# ============================================================
# Задача 4. Простое приложение Flask и разбор HTML
# ============================================================
# Часть A (Flask):
#   4.1. Создать Flask-приложение с маршрутами:
#        - "/status" -> JSON {"status": "ok"}
#        - "/greet/<name>" -> строка f"Hi, {name}!"
#   4.2. Добавить в Flask-приложение (или создать новое) маршрут "/multiply":
#        читает целые query-параметры a и b (по умолчанию 1) и возвращает
#        строку str(a * b).
#
# Часть B (BeautifulSoup):
#   4.3. Из HTML-строки вернуть текст первого тега <h1> (strip=True),
#        а если тега <h1> нет — пустую строку "".
#   4.4. Извлечь список всех непустых атрибутов href из тегов <a>.
#   4.5. Найти все теги <span class="price">, перевести их текст в int
#        и вернуть сумму всех цен.

from bs4 import BeautifulSoup
from flask import Flask, jsonify, request


def hw_4_1_basic_app() -> Flask:
    """Создать Flask-приложение с маршрутами '/status' и '/greet/<name>'."""
    # TODO: реализовать
    pass


def hw_4_2_multiply_app() -> Flask:
    """Создать Flask-приложение с маршрутом '/multiply?a=...&b=...'."""
    # TODO: реализовать
    pass


def hw_4_3_extract_h1(html: str) -> str:
    """Вернуть очищенный текст первого <h1> или '' при его отсутствии."""
    # TODO: реализовать
    pass


def hw_4_4_extract_links(html: str) -> list[str]:
    """Вернуть список всех непустых значений href у тегов <a>."""
    # TODO: реализовать
    pass


def hw_4_5_sum_prices(html: str) -> int:
    """Просуммировать целые числа внутри всех <span class='price'>."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    c1 = hw_4_1_basic_app().test_client()
    assert c1.get("/status").get_json() == {"status": "ok"}
    assert c1.get("/greet/Ira").get_data(as_text=True) == "Hi, Ira!"

    c2 = hw_4_2_multiply_app().test_client()
    assert c2.get("/multiply?a=6&b=7").get_data(as_text=True) == "42"
    assert c2.get("/multiply").get_data(as_text=True) == "1"

    assert hw_4_3_extract_h1("<div><h1> Welcome </h1></div>") == "Welcome"
    assert hw_4_3_extract_h1("<div><p>No header</p></div>") == ""

    links_html = '<a href="/home">Home</a><a>Empty</a><a href="https://hse.ru">HSE</a>'
    assert hw_4_4_extract_links(links_html) == ["/home", "https://hse.ru"]

    prices_html = (
        '<div><span class="price">150</span>'
        '<span class="old">200</span>'
        '<span class="price"> 350 </span></div>'
    )
    assert hw_4_5_sum_prices(prices_html) == 500

    print("task4 (hw2_basic): все assert-тесты пройдены.")
