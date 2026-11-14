# Практическое руководство по веб-парсингу на Python

Это пошаговая инструкция по сбору открытых данных с веб-страниц с помощью библиотек `requests` и `BeautifulSoup` (`bs4`), их очистке и сохранению в таблицы `pandas` для дальнейшего анализа.

---

## 1. Как устроен веб-парсинг: общая схема

Когда вы открываете сайт в браузере, происходит обмен по протоколу **HTTP**:
1. **Клиент** (браузер или ваш Python-скрипт) отправляет `GET`-запрос на URL-адрес сервера.
2. **Сервер** возвращает **HTTP-код состояния** и текст страницы (чаще всего **HTML** или **JSON**).
3. **Парсер** (`BeautifulSoup`) превращает сырой HTML-текст в дерево тегов, по которому удобно искать заголовки, цены, таблицы и ссылки.
4. **Аналитический блок** (`pandas`) очищает типы данных, убирает дубликаты и сохраняет датасет в `.csv` или `.json`.

### Основные HTTP-коды ответа

| Код | Расшифровка | Что это значит для парсера |
|---|---|---|
| `200` | `OK` | Страница успешно получена, можно разбирать `response.text` |
| `301` / `302` | `Redirect` | Перенаправление (`requests` по умолчанию переходит сам) |
| `400` | `Bad Request` | Ошибка в параметрах запроса / некорректный URL |
| `403` | `Forbidden` | Доступ запрещён (часто из-за отсутствия заголовка `User-Agent`) |
| `404` | `Not Found` | Страница не существует (например, закончились страницы каталога) |
| `429` | `Too Many Requests` | Вы отправляете запросы слишком часто — нужно увеличить паузу `time.sleep()` |
| `500` / `503` | `Server Error` | Временная ошибка на стороне сайта — стоит повторить запрос позже |

---

## 2. Этика и правила безопасного парсинга

Перед тем как писать код, обязательно проверьте четыре правила:

1. **Проверьте `/robots.txt` и правила сайта.** Откройте `https://example.com/robots.txt`: строки `Disallow:` показывают разделы, которые владельцы сайта просят не обходить роботами.
2. **Не собирайте персональные и закрытые данные.** Работайте только с публично доступными открытыми каталогами, таблицами и справочниками без обхода авторизации и капчи.
3. **Ограничивайте частоту запросов.** Ставьте паузу `time.sleep(1.0)` (или `random.uniform(1.0, 2.5)`) между запросами к страницам, чтобы не создавать нагрузку на сервер.
4. **Кэшируйте результат.** Сначала сохраните собранные данные в `.csv` / `.json`, а все эксперименты с `pandas` и графиками проводите уже по локальному файлу, не скачивая сайт заново при каждом запуске.

---

## 3. Установка необходимых библиотек

```bash
pip install requests beautifulsoup4 lxml pandas matplotlib seaborn
```

Проверка установки в Python:

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
```

---

## 4. Шаг 1: исследование страницы в браузере (DevTools)

Прежде чем писать код, изучите разметку страницы:
1. Откройте нужную страницу в браузере.
2. Нажмите правой кнопкой мыши на интересующий элемент (например, название или цену карточки) и выберите **«Исследовать код» / «Inspect»** (`F12` или `Cmd+Option+I`).
3. Посмотрите:
   - в каком **теге** лежит весь объект (например, `<article class="product_pod">` или `<div class="card">`);
   - в каком дочернем теге лежит название (`<h3><a title="...">`), цена (`<p class="price_color">`), ссылка (`href="..."`);
   - меняется ли URL при переходе на страницу 2 (`?page=2` или `/page-2.html`).
4. **Проверка на динамический контент (JavaScript):** нажмите `Ctrl+U` (**Просмотр кода страницы / View Page Source**) и поищите текст товара через `Ctrl+F`.
   - Если текст есть в исходном HTML — `requests + BeautifulSoup` отлично подойдут!
   - Если исходный HTML пустой, то данные подгружаются через фоновые JSON-запросы (вкладка **Network -> Fetch/XHR** в DevTools).

---

## 5. Шаг 2: скачивание страницы через `requests`

Всегда передавайте заголовок `User-Agent` и ограничение времени ожидания `timeout` (без `timeout` скрипт может зависнуть навсегда при обрыве соединения):

```python
import requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}


def fetch_html(url: str, timeout: int = 10) -> str | None:
    """Безопасно скачать HTML-страницу и вернуть текст или None при ошибке."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=timeout)
        response.raise_for_status()  # выбросит HTTPError для кодов 4xx и 5xx
        response.encoding = response.apparent_encoding  # защита от «кракозябр»
        return response.text
    except requests.RequestException as exc:
        print(f"[WARN] Не удалось загрузить {url}: {exc}")
        return None
```

### Передача query-параметров через словарь `params`

Вместо ручной склейки строк URL передавайте параметры словарём — `requests` сам корректно закодирует пробелы и кириллицу:

```python
params = {"q": "анализ данных", "page": 2}
response = requests.get("https://example.com/search", params=params, headers=HEADERS, timeout=10)
print(response.url)  # https://example.com/search?q=%D0%B0%D0%BD...&page=2
```

---

## 6. Шаг 3: разбор HTML в `BeautifulSoup`

Создаём объект `soup`:

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")  # или "lxml", если установлен lxml
```

### Главные методы поиска элементов

| Метод | Что возвращает | Пример использования |
|---|---|---|
| `soup.find("tag", class_="...")` | Первый подходящий тег или `None` | `soup.find("h1", class_="title")` |
| `soup.find_all("tag", class_="...")` | Список всех подходящих тегов (`[]`, если нет) | `soup.find_all("div", class_="item")` |
| `soup.select_one("css selector")` | Первый тег по CSS-селектору или `None` | `card.select_one("h3 > a")` |
| `soup.select("css selector")` | Список тегов по CSS-селектору | `soup.select("table.stats tbody tr")` |

> **Важно:** слово `class` — зарезервированное ключевое слово Python (для объявления классов ООП). Поэтому в `find` и `find_all` атрибут HTML-класса всегда пишется с подчёркиванием: `class_="price"`.

### Извлечение текста и атрибутов без ошибок `AttributeError`

Самая частая ошибка новичков — вызвать `.get_text()` сразу на результате `find()`, когда элемент отсутствует на одной из карточек (например, старая цена без скидки):

```python
# ОПАСНО: если span.old-price нет, find() вернёт None -> AttributeError!
# old_price = card.find("span", class_="old-price").get_text(strip=True)

# БЕЗОПАСНО: проверяем на None
old_tag = card.find("span", class_="old-price")
old_price = old_tag.get_text(strip=True) if old_tag is not None else None

# Безопасное чтение атрибута (например, href или src):
link_tag = card.select_one("h3 a")
href = link_tag.get("href", "") if link_tag is not None else ""
```

Превращение относительных ссылок (`/catalogue/book_1/index.html`) в полные URL:

```python
from urllib.parse import urljoin

full_url = urljoin("https://books.toscrape.com/catalogue/", href)
```

---

## 7. Шаг 4: очистка строковых данных

Данные из HTML всегда приходят строками с лишними символами валют, пробелами и словами:

```python
import re


def clean_price(raw_price: str) -> float:
    """Извлечь число из строки вида '£51.77' или '1 290,50 ₽'."""
    normalized = raw_price.replace("\xa0", "").replace(" ", "").replace(",", ".")
    match = re.search(r"\d+(?:\.\d+)?", normalized)
    if match is None:
        raise ValueError(f"Не удалось распознать цену: {raw_price!r}")
    return float(match.group(0))
```

---

## 8. Шаг 5: сквозной рабочий пример с пагинацией и сохранением в CSV

Ниже приведён полный шаблон парсера учебной песочницы `https://books.toscrape.com` (сайт специально создан для тренировки веб-скрейпинга):

```python
import time
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{page}.html"
SITE_ROOT = "https://books.toscrape.com/catalogue/"
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
HEADERS = {"User-Agent": "HSE-Python-Course-Scraper/1.0"}


def parse_book_card(card) -> dict:
    """Распарсить одну карточку <article class='product_pod'>."""
    link = card.select_one("h3 a")
    price_tag = card.select_one("p.price_color")
    rating_tag = card.select_one("p.star-rating")

    if link is None or price_tag is None:
        raise ValueError("В карточке отсутствует название или цена")

    title = link.get("title") or link.get_text(strip=True)
    rel_url = link.get("href", "")
    raw_price = price_tag.get_text(strip=True).lstrip("£Â")

    classes = rating_tag.get("class", []) if rating_tag else []
    rating_word = next((c for c in classes if c in RATING_MAP), "")

    return {
        "title": title.strip(),
        "price_gbp": float(raw_price),
        "rating": RATING_MAP.get(rating_word, 0),
        "url": urljoin(SITE_ROOT, rel_url),
    }


def scrape_books(max_pages: int = 3, delay_sec: float = 1.0) -> pd.DataFrame:
    """Обойти первые max_pages страниц каталога и вернуть DataFrame."""
    records = []
    for page in range(1, max_pages + 1):
        url = BASE_URL.format(page=page)
        try:
            resp = requests.get(url, headers=HEADERS, timeout=10)
            if resp.status_code == 404:
                break
            resp.raise_for_status()
        except requests.RequestException as exc:
            print(f"Ошибка сети на странице {page}: {exc}")
            continue

        soup = BeautifulSoup(resp.text, "html.parser")
        for card in soup.find_all("article", class_="product_pod"):
            try:
                records.append(parse_book_card(card))
            except ValueError as err:
                print(f"Пропущена битая карточка: {err}")

        time.sleep(delay_sec)

    return pd.DataFrame(records)


if __name__ == "__main__":
    df = scrape_books(max_pages=2, delay_sec=1.0)
    print(f"Собрано записей: {len(df)}")
    df.to_csv("books_dataset.csv", index=False, encoding="utf-8")
```

---

## 9. Шпаргалка по частым проблемам и их решению

1. **`AttributeError: 'NoneType' object has no attribute 'get_text'`**
   - *Причина:* `soup.find(...)` не нашёл тег и вернул `None`.
   - *Решение:* проверьте селектор и добавьте `if tag is not None:` перед чтением текста.
2. **`403 Forbidden` при `requests.get(url)`**
   - *Причина:* сервер блокирует стандартный заголовок `python-requests/...`.
   - *Решение:* передайте корректный словарь `headers={"User-Agent": "..."}` и проверьте `robots.txt`.
3. **Пустой список `[]` при `soup.find_all(...)`, хотя в браузере элементы видны**
   - *Причина:* данные подгружаются динамически через JavaScript после загрузки страницы или вы опечатались в имени класса.
   - *Решение:* проверьте исходный код страницы (`Ctrl+U`) или посмотрите вкладку `Network -> Fetch/XHR` (часто там есть готовый открытый JSON-эндпоинт!).
4. **Нечитаемые символы вместо русских букв (`ÐÑÐ¸Ð²ÐµÑ`)**
   - *Причина:* сервер не указал UTF-8 в HTTP-заголовках.
   - *Решение:* укажите `response.encoding = "utf-8"` (или `response.apparent_encoding`) до обращения к `response.text`.
5. **Скрипт падает на 87-й карточке из 200, и все данные теряются**
   - *Причина:* нет `try / except` вокруг разбора отдельной карточки.
   - *Решение:* оборачивайте парсинг каждой карточки в `try / except (ValueError, KeyError)` и сохраняйте промежуточный результат.
