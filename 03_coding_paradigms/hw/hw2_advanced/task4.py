# task4.py — Домашняя работа 10, продвинутый уровень.
# Задача 4. Парсер HTML-каталога книг + JSON API на Flask.


# ============================================================
# Задача 4. Парсер HTML-каталога книг + JSON API на Flask
# ============================================================
# Соединяем веб-парсинг, pandas и микросервис на Flask!
#
# Каждая карточка книги в HTML-каталоге имеет вид:
#   <article class="book" data-rating="4">
#     <h3><a href="/books/10">Fluent Python</a></h3>
#     <p class="price">$45.50</p>
#   </article>
#
# Подзадачи:
#   4.1. Распарсить одну карточку <article class="book"> в словарь:
#        {"title": str, "url": str, "price": float, "rating": int}
#        (символ "$" в начале цены убрать; если нет цены или заголовка —
#        выбросить ValueError).
#   4.2. Распарсить всю HTML-страницу со множеством карточек <article class="book">,
#        пропуская битые карточки через try/except ValueError, и вернуть список словарей.
#   4.3. Преобразовать список карточек в pd.DataFrame и вернуть словарь сводной
#        статистики {"count": int, "avg_price": float, "max_rating": int}
#        (avg_price округлить до 2 знаков; для пустого списка — нули).
#   4.4. Создать Flask-приложение поверх HTML-каталога с маршрутами:
#        - "/api/books" -> JSON-список книг с поддержкой необязательных
#          query-параметров ?min_rating=R (int) и ?max_price=P (float);
#          если параметр передан некорректно (не число) — вернуть
#          jsonify({"error": "bad query"}), 400;
#        - "/api/stats" -> JSON со статистикой из 4.3.

import pandas as pd
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request


def hw_4_1_parse_card(card_tag) -> dict:
    """Извлечь словарь {'title', 'url', 'price', 'rating'} из тега <article>."""
    # TODO: реализовать
    pass


def hw_4_2_parse_catalog(html: str) -> list[dict]:
    """Извлечь все валидные карточки книг со страницы, пропуская битые."""
    # TODO: реализовать
    pass


def hw_4_3_catalog_stats(books: list[dict]) -> dict:
    """Посчитать {'count', 'avg_price', 'max_rating'} через pandas."""
    # TODO: реализовать
    pass


def hw_4_4_create_catalog_api(html: str) -> Flask:
    """Создать Flask-сервис с маршрутами '/api/books' и '/api/stats'."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    sample_html = """
    <section>
      <article class="book" data-rating="5">
        <h3><a href="/books/1">Fluent Python</a></h3>
        <p class="price">$50.00</p>
      </article>
      <article class="book" data-rating="3">
        <h3><a href="/books/2">Intro to HTML</a></h3>
        <p class="price">$20.00</p>
      </article>
      <article class="book" data-rating="4">
        <h3>Broken Card Without Price</h3>
      </article>
    </section>
    """

    books = hw_4_2_parse_catalog(sample_html)
    assert books == [
        {"title": "Fluent Python", "url": "/books/1", "price": 50.0, "rating": 5},
        {"title": "Intro to HTML", "url": "/books/2", "price": 20.0, "rating": 3},
    ]

    stats = hw_4_3_catalog_stats(books)
    assert stats == {"count": 2, "avg_price": 35.0, "max_rating": 5}
    assert hw_4_3_catalog_stats([]) == {"count": 0, "avg_price": 0.0, "max_rating": 0}

    client = hw_4_4_create_catalog_api(sample_html).test_client()
    assert len(client.get("/api/books").get_json()) == 2
    assert len(client.get("/api/books?min_rating=4").get_json()) == 1
    assert len(client.get("/api/books?max_price=25").get_json()) == 1
    bad_resp = client.get("/api/books?min_rating=five")
    assert bad_resp.status_code == 400 and bad_resp.get_json() == {"error": "bad query"}
    assert client.get("/api/stats").get_json() == stats

    print("task4 (hw2_advanced): все assert-тесты пройдены.")
