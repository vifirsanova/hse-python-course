# task2.py — Домашняя работа 10, базовый уровень.
# Задача 2. Базовый анализ каталога фильмов в pandas.


# ============================================================
# Задача 2. Базовый анализ каталога фильмов в pandas
# ============================================================
# Дана таблица фильмов df со столбцами:
#   "title" (str), "genre" (str), "rating" (float),
#   "budget" (float), "gross" (float).
#
# Подзадачи:
#   2.1. Вернуть кортеж (число_строк, список_названий_столбцов).
#   2.2. Вернуть DataFrame с фильмами, у которых rating >= min_rating.
#   2.3. Вернуть копию df с новым столбцом "profit" = gross - budget.
#   2.4. Посчитать средний рейтинг по каждому жанру и вернуть словарь
#        {genre: round(mean_rating, 2)}.
#   2.5. Вернуть список названий ("title") топ-n самых кассовых фильмов
#        по убыванию столбца "gross".

import pandas as pd


def hw_2_1_table_info(df: pd.DataFrame) -> tuple[int, list[str]]:
    """Вернуть (количество строк, список столбцов)."""
    # TODO: реализовать
    pass


def hw_2_2_filter_by_rating(df: pd.DataFrame, min_rating: float) -> pd.DataFrame:
    """Вернуть строки с rating >= min_rating."""
    # TODO: реализовать
    pass


def hw_2_3_add_profit(df: pd.DataFrame) -> pd.DataFrame:
    """Вернуть копию таблицы со столбцом 'profit' = gross - budget."""
    # TODO: реализовать
    pass


def hw_2_4_mean_rating_by_genre(df: pd.DataFrame) -> dict[str, float]:
    """Вернуть словарь средних рейтингов по жанрам (round до 2 знаков)."""
    # TODO: реализовать
    pass


def hw_2_5_top_grossing_titles(df: pd.DataFrame, n: int = 3) -> list[str]:
    """Вернуть список названий топ-n фильмов по убыванию 'gross'."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    movies = pd.DataFrame({
        "title": ["Film A", "Film B", "Film C", "Film D"],
        "genre": ["Drama", "Sci-Fi", "Drama", "Sci-Fi"],
        "rating": [8.2, 7.5, 6.8, 8.9],
        "budget": [20.0, 100.0, 15.0, 120.0],
        "gross": [80.0, 250.0, 10.0, 500.0],
    })

    assert hw_2_1_table_info(movies) == (
        4, ["title", "genre", "rating", "budget", "gross"]
    )
    assert list(hw_2_2_filter_by_rating(movies, 8.0)["title"]) == ["Film A", "Film D"]

    with_profit = hw_2_3_add_profit(movies)
    assert "profit" not in movies.columns
    assert list(with_profit["profit"]) == [60.0, 150.0, -5.0, 380.0]

    assert hw_2_4_mean_rating_by_genre(movies) == {"Drama": 7.5, "Sci-Fi": 8.2}
    assert hw_2_5_top_grossing_titles(movies, 2) == ["Film D", "Film B"]

    print("task2 (hw2_basic): все assert-тесты пройдены.")
