# task4.py — Домашняя работа 9, базовый уровень.
# Задача 4. Стандартная библиотека Python (math, collections, json).


# ============================================================
# Задача 4. Стандартная библиотека Python
# ============================================================
# Практикуем использование встроенных модулей math, collections и json.
#
# Подзадачи:
#   4.1. По числу предметов total_items и вместимости одной коробки box_size
#        вернуть минимальное число коробок (округление вверх math.ceil).
#   4.2. По координатам двух точек (x1, y1) и (x2, y2) вернуть евклидово
#        расстояние между ними, округлённое до 2 знаков.
#   4.3. С помощью collections.Counter вернуть список из k самых частых
#        элементов списка items в виде пар (элемент, частота).
#   4.4. Принять JSON-строку с настройками пользователя и вернуть значение
#        ключа "theme" (или "light", если ключа нет).
#   4.5. Упаковать словарь result в отсортированную JSON-строку
#        (sort_keys=True).

from collections import Counter
import json
import math


def hw_4_1_boxes_needed(total_items: int, box_size: int) -> int:
    """Вернуть минимальное число коробок через math.ceil."""
    # TODO: реализовать
    pass


def hw_4_2_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Вернуть расстояние между точками, округлённое до 2 знаков."""
    # TODO: реализовать
    pass


def hw_4_3_top_k(items: list, k: int) -> list[tuple]:
    """Вернуть k самых частых элементов через Counter.most_common(k)."""
    # TODO: реализовать
    pass


def hw_4_4_read_theme(config_json: str) -> str:
    """Распарсить JSON и вернуть значение 'theme' или 'light'."""
    # TODO: реализовать
    pass


def hw_4_5_to_json(result: dict) -> str:
    """Преобразовать словарь в JSON-строку с sort_keys=True."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    assert hw_4_1_boxes_needed(25, 10) == 3
    assert hw_4_1_boxes_needed(20, 10) == 2
    assert hw_4_1_boxes_needed(0, 10) == 0

    assert hw_4_2_distance(0, 0, 3, 4) == 5.0
    assert hw_4_2_distance(1, 1, 2, 2) == 1.41

    assert hw_4_3_top_k(["a", "b", "a", "c", "a", "b"], 2) == [("a", 3), ("b", 2)]

    assert hw_4_4_read_theme('{"theme": "dark", "lang": "ru"}') == "dark"
    assert hw_4_4_read_theme('{"lang": "ru"}') == "light"

    assert hw_4_5_to_json({"b": 2, "a": 1}) == '{"a": 1, "b": 2}'

    print("task4 (hw1_basic): все assert-тесты пройдены.")
