# Контрольная работа по Python (Части 9–10)

**Темы:** словари (`dict`), функции (`def`), обработка ошибок (`try/except/raise`), модули и импорты, основы ООП (`class`), `pandas`, визуализация (`matplotlib` / `seaborn`), основы `Flask` и веб-парсинг (`requests` / `BeautifulSoup`).  
**Продолжительность:** 80 минут (1 академическая пара).  
**Максимальная оценка:** 10 баллов (Часть A — 3.0 балла, Часть B — 3.5 балла, Часть C — 3.5 балла).

---

## Вариант 1

### Часть A. Блиц-вопросы (6 заданий × 0.5 балла = 3.0 балла)

**A1 (Что выведет?).** Запишите точный вывод кода и кратко поясните почему:
```python
d = {1: "one", True: "true", 2: "two"}
print(len(d), d[1], d.get(3, "missing"))
```

**A2 (Найди ошибку).** Почему функция при втором вызове вернёт неожиданный результат? Исправьте её заголовок и тело:
```python
def append_tag(tag, tags=[]):
    tags.append(tag)
    return tags
```

**A3 (Что выведет?).** Запишите вывод кода:
```python
steps = []
try:
    val = int("15")
    steps.append("try")
except ValueError:
    steps.append("except")
else:
    steps.append("else")
finally:
    steps.append("finally")
print(steps)
```

**A4 (Выбор — pandas).** Какое выражение корректно отфильтрует строки `df`, где `price > 100` и `city == "Berlin"`?
1. `df[df["price"] > 100 and df["city"] == "Berlin"]`
2. `df[(df["price"] > 100) & (df["city"] == "Berlin")]`
3. `df[df["price"] > 100, df["city"] == "Berlin"]`
4. `df.filter("price > 100 & city == Berlin")`

**A5 (Выбор — визуализация).** Какой график лучше всего показывает медиану, межквартильный размах и выбросы числового признака в разрезе нескольких категорий?
1. `sns.lineplot`
2. `sns.boxplot`
3. `plt.pie`
4. `sns.scatterplot`

**A6 (Найди ошибку — Flask + BeautifulSoup).** В приведённом фрагменте допущены **две** ошибки (одна синтаксическая в `BeautifulSoup`, одна типизированная во `Flask`). Найдите и исправьте обе:
```python
@app.route("/count")
def count_prices():
    soup = BeautifulSoup(HTML_DOC, "html.parser")
    tags = soup.find_all("span", class="price")
    return len(tags)
```

---

### Часть B. Базовое программирование и ООП (3 задачи = 3.5 балла)

**B1 (Словари и функции — 1.0 балл).**  
Напишите функцию `merge_carts(c1: dict[str, int], c2: dict[str, int], min_qty: int = 1) -> dict[str, int]`, которая объединяет две корзины покупок (складывая количества для совпадающих товаров) и оставляет в результирующем словаре только позиции с итоговым количеством `>= min_qty`. Исходные словари изменяться не должны.

**B2 (Обработка ошибок и `json` — 1.0 балл).**  
Напишите функцию `parse_scores(lines: list[str]) -> tuple[dict[str, float], int]`, принимающую список JSON-строк вида `'{"user": "ira", "score": 85}'`.
- Если строка не является валидным JSON (`json.JSONDecodeError`), не содержит ключей `"user"` / `"score"`, или `"score"` не приводится к `float` в диапазоне `0..100` — строка считается ошибочной.
- Для каждого корректного пользователя сохраните **максимальный** встретившийся балл и верните кортеж `(словарь_лучших_баллов, количество_ошибочных_строк)`.

**B3 (Основы ООП — 1.5 балла).**  
Реализуйте класс `Wallet`:
- Конструктор `__init__(self, owner: str, balance: float = 0.0)`: если `balance < 0`, выбрасывает `ValueError`.
- Метод `top_up(self, amount: float) -> None`: пополняет баланс; если `amount <= 0`, выбрасывает `ValueError`.
- Метод `pay(self, amount: float) -> bool`: если `amount <= 0`, выбрасывает `ValueError`; если средств достаточно — уменьшает баланс и возвращает `True`, иначе не меняет баланс и возвращает `False`.
- Метод `__str__(self) -> str`: возвращает строку `"<owner>: <balance:.2f> RUB"`.

---

### Часть C. Анализ данных, визуализация и парсинг (3 задачи = 3.5 балла)

**C1 (`pandas` — 1.5 балла).**  
Дан `DataFrame` `orders` со столбцами `"order_id"`, `"city"`, `"category"`, `"price"`, `"qty"`, `"discount"` (с возможными пропусками `NaN`) и `"status"` (`"paid"` / `"cancelled"`).  
Напишите функцию `city_summary(orders: pd.DataFrame) -> pd.DataFrame`, которая:
1. Не меняя исходный `orders`, заменяет пропуски в `"discount"` нулями и вычисляет столбец `"revenue" = price * qty * (1 - discount / 100)`.
2. Оставляет только оплаченные заказы (`status == "paid"`).
3. Группирует данные по `"city"`, считает количество заказов (`"orders_cnt"`) и суммарную выручку (`"total_revenue"`), сортирует по убыванию `"total_revenue"` и возвращает полученную таблицу.

**C2 (Визуализация — 1.0 балл).**  
Напишите функцию `plot_category_revenue(df: pd.DataFrame, out_path: str)`, которая по таблице со столбцами `"category"` и `"revenue"` строит через `fig, ax = plt.subplots(figsize=(7, 4))` столбчатый график средней выручки по категориям (`sns.barplot`), задаёт заголовок `"Mean Revenue by Category"`, подписи осей `"Category"` и `"Revenue"`, сохраняет график в `out_path` и закрывает фигуру.

**C3 (Парсинг `BeautifulSoup` — 1.0 балл).**  
Напишите функцию `extract_courses(html: str) -> list[dict]`, разбирающую HTML со списком карточек курсов:
```html
<div class="course" data-credits="4">
  <a class="title" href="/c/python">Python Basics</a>
  <span class="hours"> 36 ч. </span>
</div>
```
Функция должна вернуть список словарей `{"title": str, "url": str, "credits": int, "hours": int}`, безопасно пропуская карточки, в которых отсутствует ссылка `.title` или не удаётся извлечь целое число часов.

---

## Вариант 2

### Часть A. Блиц-вопросы (6 заданий × 0.5 балла = 3.0 балла)

**A1 (Что выведет?).** Запишите точный вывод кода и кратко поясните почему:
```python
d = {"a": 10, "b": 20, "c": 10}
inv = {v: k for k, v in d.items()}
print(len(inv), inv[10])
```

**A2 (Найди ошибку).** Почему оба экземпляра `Student` оказываются с одинаковыми оценками? Исправьте класс:
```python
class Student:
    grades = []
    def __init__(self, name):
        self.name = name
```

**A3 (Выбор — модули и `__name__`).** Вы написали в файле `helpers.py` проверку `if __name__ == "__main__": run_tests()`, а затем в файле `app.py` выполнили `import helpers`. Что произойдёт при запуске `python app.py`?
1. Вызовется `run_tests()`, так как `helpers.py` загружается целиком
2. `run_tests()` НЕ вызовется, так как внутри `helpers` переменная `__name__` равна `"helpers"`
3. Возникнет `ImportError`
4. Переменная `__name__` в обоих файлах равна `"__main__"`

**A4 (Что выведет? — `pandas`).** Запишите вывод кода:
```python
df = pd.DataFrame({"x": [5, None, 10, 15]})
print(int(df["x"].isna().sum()), float(df["x"].fillna(0).mean()))
```

**A5 (Найди ошибку — `matplotlib`).** Почему файл `report.png` сохраняется пустым белым прямоугольником? Исправьте код:
```python
plt.bar(["Q1", "Q2"], [120, 180])
plt.title("Quarterly Sales")
plt.show()
plt.savefig("report.png")
```

**A6 (Выбор — парсинг и HTTP).** При обходе сайта ваш скрипт начал получать HTTP-код `429`. Что он означает и какое действие верное?
1. Страница удалена; прекратить сбор
2. Ошибка синтаксиса HTML; сменить `"html.parser"` на `"lxml"`
3. Превышен лимит частоты запросов (`Too Many Requests`); увеличить паузу `time.sleep()`
4. Ошибка кодировки; установить `response.encoding = "utf-8"`

---

### Часть B. Базовое программирование и ООП (3 задачи = 3.5 балла)

**B1 (Словари и `Counter` — 1.0 балл).**  
Напишите функцию `top_domains(emails: list[str], k: int = 3) -> list[tuple[str, int]]`, которая принимает список строк email-адресов вида `"user@domain.ru"` (строки без ровно одного символа `@` или с пустым доменом игнорируются), приводит домен к нижнему регистру и возвращает `k` самых частых доменов в формате `[(домен, количество), ...]`.

**B2 (Функции и обработка ошибок — 1.0 балл).**  
Напишите функцию `apply_discounts(prices: list, percent: float) -> tuple[list[float], int]`:
- Если `percent < 0` или `percent > 100`, функция сразу выбрасывает `ValueError("Invalid percent")`.
- Для каждого элемента списка `prices` пытается преобразовать его во `float`: если число `>= 0`, добавляет в выходной список округлённую до 2 знаков цену со скидкой `round(val * (1 - percent / 100), 2)`; если элемент не приводится к `float` или отрицателен — увеличивает счётчик ошибок.
- Возвращает `(список_цен_со_скидкой, счётчик_ошибок)`.

**B3 (Основы ООП — 1.5 балла).**  
Реализуйте класс `TaskTracker`:
- Конструктор `__init__(self, project: str)` создаёт пустой словарь задач `self.tasks = {}` вида `{название: выполнена_bool}`.
- Метод `add_task(self, title: str) -> None`: если `title.strip()` пустой — `ValueError`; если задача уже есть — не перезаписывает её статус, иначе добавляет со статусом `False`.
- Метод `complete(self, title: str) -> None`: помечает задачу выполненной (`True`), а если такой задачи нет — выбрасывает `KeyError`.
- Метод `progress(self) -> float`: возвращает процент выполненных задач от `0.0` до `100.0` (округлённый до 1 знака), либо `0.0`, если задач пока нет.

---

### Часть C. Анализ данных, визуализация и Flask (3 задачи = 3.5 балла)

**C1 (`pandas` — 1.5 балла).**  
Дан `DataFrame` `rides` со столбцами `"ride_id"`, `"driver"`, `"zone"`, `"distance_km"`, `"fare"`, `"tip"` (может содержать `NaN`).  
Напишите функцию `best_zones(rides: pd.DataFrame, min_rides: int = 2) -> pd.DataFrame`, которая:
1. Не меняя исходную таблицу, заменяет `NaN` в `"tip"` на `0.0` и создаёт столбец `"total_pay" = fare + tip`.
2. Группирует поездки по `"zone"`, вычисляя число поездок `"rides_cnt"` и средний чек `"avg_pay"` (округлённый до 2 знаков).
3. Оставляет только зоны с `rides_cnt >= min_rides` и сортирует результат по убыванию `"avg_pay"`.

**C2 (Визуализация — 1.0 балл).**  
Напишите функцию `plot_fare_vs_distance(rides: pd.DataFrame, out_path: str)`, которая строит `sns.scatterplot(data=rides, x="distance_km", y="fare", hue="zone", ax=ax)`, задаёт заголовок `"Fare vs Distance"`, подписи осей `"Distance (km)"` и `"Fare"`, сохраняет фигуру в `out_path` и закрывает её.

**C3 (`Flask` JSON API — 1.0 балл).**  
Напишите функцию `create_books_app(books: list[dict]) -> Flask`, где каждая книга имеет вид `{"id": int, "title": str, "year": int}`:
- Маршрут `GET /books/<int:book_id>` возвращает JSON книги со статусом `200`, а если книги с таким `id` нет — `{"error": "not found"}` со статусом `404`.
- Маршрут `GET /books` поддерживает необязательный параметр `?from_year=YYYY`: возвращает JSON-список книг с `year >= int(from_year)`, а при нечисловом `from_year` возвращает `{"error": "bad year"}` со статусом `400`.

---

## Ключи и эталонные решения для преподавателя

### Ответы к Части A

**Вариант 1:**
- **A1:** `2 true missing` (так как в Python `True == 1` и `hash(True) == hash(1)`, ключ `1` перезаписывается значением `"true"`).
- **A2:** Список по умолчанию создаётся один раз при объявлении функции. Исправление: `def append_tag(tag, tags=None): if tags is None: tags = []; tags.append(tag); return tags`.
- **A3:** `['try', 'else', 'finally']`.
- **A4:** Вариант **2**.
- **A5:** Вариант **2** (`sns.boxplot`).
- **A6:** 1) `class_="price"` вместо `class="price"`; 2) `return str(len(tags))` (или `jsonify({"count": len(tags)})`), так как обработчик `Flask` не может возвращать голое целое число `int`.

**Вариант 2:**
- **A1:** `2 c` (при совпадении значения `10` более поздний ключ `"c"` перезаписал `"a"`).
- **A2:** `grades = []` — атрибут класса, общий для всех экземпляров. Нужно перенести `self.grades = []` внутрь `__init__`.
- **A3:** Вариант **2**.
- **A4:** `1 7.5` (один `NaN`; после замены на `0` среднее от `[5, 0, 10, 15]` равно `30 / 4 = 7.5`).
- **A5:** `plt.show()` закрывает и очищает текущую фигуру; нужно вызывать `plt.savefig("report.png")` **перед** `plt.show()`.
- **A6:** Вариант **3**.

---

### Краткие эталонные решения Частей B и C (Вариант 1)

```python
import json
import re
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup


def merge_carts(c1: dict[str, int], c2: dict[str, int], min_qty: int = 1) -> dict[str, int]:
    keys = set(c1) | set(c2)
    return {
        k: total
        for k in keys
        if (total := c1.get(k, 0) + c2.get(k, 0)) >= min_qty
    }


def parse_scores(lines: list[str]) -> tuple[dict[str, float], int]:
    best: dict[str, float] = {}
    errors = 0
    for raw in lines:
        try:
            obj = json.loads(raw)
            user = str(obj["user"]).strip()
            score = float(obj["score"])
            if not user or not (0.0 <= score <= 100.0):
                raise ValueError("out of range")
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            errors += 1
            continue
        if user not in best or score > best[user]:
            best[user] = score
    return best, errors


class Wallet:
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Negative initial balance")
        self.owner = owner
        self.balance = float(balance)

    def top_up(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def pay(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def __str__(self) -> str:
        return f"{self.owner}: {self.balance:.2f} RUB"


def city_summary(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.copy()
    df["discount"] = df["discount"].fillna(0.0)
    df["revenue"] = df["price"] * df["qty"] * (1.0 - df["discount"] / 100.0)
    paid = df[df["status"] == "paid"]
    return (
        paid.groupby("city")["revenue"]
        .agg(orders_cnt="count", total_revenue="sum")
        .sort_values("total_revenue", ascending=False)
    )


def plot_category_revenue(df: pd.DataFrame, out_path: str) -> None:
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(data=df, x="category", y="revenue", ax=ax)
    ax.set_title("Mean Revenue by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Revenue")
    fig.tight_layout()
    fig.savefig(out_path)
    plt.close(fig)


def extract_courses(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    results = []
    for div in soup.find_all("div", class_="course"):
        try:
            a_tag = div.find("a", class_="title")
            h_tag = div.find("span", class_="hours")
            if a_tag is None or h_tag is None:
                continue
            m = re.search(r"\d+", h_tag.get_text())
            if m is None:
                continue
            results.append({
                "title": a_tag.get_text(strip=True),
                "url": a_tag.get("href", ""),
                "credits": int(div.get("data-credits", 0)),
                "hours": int(m.group(0)),
            })
        except ValueError:
            continue
    return results
```

---

### Критерии начисления баллов за задачи с кодом (Части B и C)

- **Полный балл (100%):** алгоритм полностью корректен, учтены граничные случаи из условия (пустые коллекции, `NaN`, некорректный ввод), не мутируются входные аргументы, соблюдены имена и типы возвращаемых значений.
- **Частичный балл (50–75%):** основная логика верна, но упущен один граничный случай (например, не закрыта фигура `plt.close`, изменена исходная таблица без `.copy()`, не проверен один из видов ошибок).
- **Минимальный балл (25%):** верна общая идея и структура функции/класса, но код содержит существенную логическую или синтаксическую ошибку, мешающую прохождению базовых тестов.
