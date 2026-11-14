# task4.py — Домашняя работа 9, продвинутый уровень.
# Задача 4. Аналитический модуль ведомости курса (math, statistics, Counter, json, random).


# ============================================================
# Задача 4. Аналитический модуль ведомости курса
# ============================================================
# Ведомость курса приходит в формате JSON-списка объектов:
#   [{"student": "Ira", "score": 88}, {"student": "Max", "score": 71}, ...]
#
# Шкала перевода балла (0..100) в буквенную оценку:
#   - 85..100 -> "A"
#   - 70..84  -> "B"
#   - 50..69  -> "C"
#   - 0..49   -> "F"
#
# Подзадачи:
#   4.1. Перевести числовой балл score в букву ("A", "B", "C", "F");
#        если score < 0 или score > 100, выбросить ValueError.
#   4.2. Из JSON-строки ведомости посчитать словарь статистик
#        {"count": int, "mean": float, "median": float} (округление до 2 знаков;
#        для пустого списка вернуть {"count": 0, "mean": 0.0, "median": 0.0}).
#   4.3. Построить распределение буквенных оценок через Counter и вернуть
#        обычный словарь dict (например, {"A": 2, "B": 1}).
#   4.4. С помощью random.Random(seed).sample(names, k) выбрать k студентов
#        для выборочной перепроверки работ (если k > len(names), выбрать всех).
#   4.5. Сформировать итоговый JSON-отчёт (sort_keys=True) со статистикой
#        и распределением оценок: {"grades": {...}, "stats": {...}}.

from collections import Counter
import json
import random
import statistics


def hw_4_1_letter_grade(score: int) -> str:
    """Вернуть буквенную оценку A/B/C/F или выбросить ValueError."""
    # TODO: реализовать
    pass


def hw_4_2_score_stats(raw_json: str) -> dict:
    """Распарсить JSON и вернуть {'count': ..., 'mean': ..., 'median': ...}."""
    # TODO: реализовать
    pass


def hw_4_3_grade_distribution(raw_json: str) -> dict[str, int]:
    """Вернуть словарь частот буквенных оценок."""
    # TODO: реализовать
    pass


def hw_4_4_audit_sample(raw_json: str, k: int, seed: int = 42) -> list[str]:
    """Выбрать k имён студентов через random.Random(seed).sample."""
    # TODO: реализовать
    pass


def hw_4_5_build_report(raw_json: str) -> str:
    """Сформировать итоговую JSON-строку с ключами 'grades' и 'stats'."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    assert hw_4_1_letter_grade(90) == "A"
    assert hw_4_1_letter_grade(75) == "B"
    assert hw_4_1_letter_grade(50) == "C"
    assert hw_4_1_letter_grade(30) == "F"
    try:
        hw_4_1_letter_grade(105)
        assert False, "Ожидалось исключение ValueError"
    except ValueError:
        pass

    sample_json = json.dumps([
        {"student": "Ira", "score": 90},
        {"student": "Max", "score": 75},
        {"student": "Ann", "score": 85},
        {"student": "Bob", "score": 40},
    ])

    assert hw_4_2_score_stats(sample_json) == {"count": 4, "mean": 72.5, "median": 80.0}
    assert hw_4_2_score_stats("[]") == {"count": 0, "mean": 0.0, "median": 0.0}

    assert hw_4_3_grade_distribution(sample_json) == {"A": 2, "B": 1, "F": 1}

    sample_audit = hw_4_4_audit_sample(sample_json, 2, seed=10)
    assert len(sample_audit) == 2 and set(sample_audit).issubset({"Ira", "Max", "Ann", "Bob"})
    assert len(hw_4_4_audit_sample(sample_json, 10, seed=10)) == 4

    report = json.loads(hw_4_5_build_report(sample_json))
    assert report["grades"] == {"A": 2, "B": 1, "F": 1}
    assert report["stats"]["mean"] == 72.5

    print("task4 (hw1_advanced): все assert-тесты пройдены.")
