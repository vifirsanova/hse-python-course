# task3.py — Домашняя работа 6, продвинутый уровень.
# Задача 3. Парсер логов и классификация событий.


# ============================================================
# Задача 3. Парсер логов и классификация событий
# ============================================================
# На вход приходит строка лога вида
#   "2026-10-05 12:30:45|LEVEL|message"
# Например: "2026-10-05 12:30:45|ERROR|disk full"
#
# Подзадачи:
#   3.1. Вернуть дату (часть до первого '|').
#   3.2. Вернуть уровень (вторая часть).
#   3.3. Вернуть сообщение (третья часть).
#   3.4. Вернуть True, если строка содержит ровно три части
#        и они все непустые.
#   3.5. Вернуть True, если уровень — "ERROR" или "WARN".
#   3.6. Вернуть True, если дата соответствует шаблону YYYY-MM-DD
#        (использовать re.fullmatch по первой части).
#   3.7. Нормализовать лог: уровень в верхнем регистре,
#        сообщение в нижнем, склеить через '|'.

import re


def hw_3_1_date(line: str) -> str:
    """Вернуть дату (до первого '|')."""
    # TODO: реализовать
    pass


def hw_3_2_level(line: str) -> str:
    """Вернуть уровень (вторая часть)."""
    # TODO: реализовать
    pass


def hw_3_3_message(line: str) -> str:
    """Вернуть сообщение (третья часть)."""
    # TODO: реализовать
    pass


def hw_3_4_well_formed(line: str) -> bool:
    """Вернуть True, если ровно три непустые части."""
    # TODO: реализовать
    pass


def hw_3_5_is_alert(line: str) -> bool:
    """Вернуть True, если уровень 'ERROR' или 'WARN'."""
    # TODO: реализовать
    pass


def hw_3_6_date_ok(line: str) -> bool:
    """Вернуть True, если дата вида YYYY-MM-DD."""
    # TODO: реализовать
    pass


def hw_3_7_normalize(line: str) -> str:
    """Вернуть нормализованный лог."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    line = "2026-10-05 12:30:45|ERROR|disk full"
    assert hw_3_1_date(line) == "2026-10-05 12:30:45"
    assert hw_3_2_level(line) == "ERROR"
    assert hw_3_3_message(line) == "disk full"
    assert hw_3_4_well_formed(line) is True
    assert hw_3_4_well_formed("a|b") is False
    assert hw_3_4_well_formed("a||b") is False
    assert hw_3_5_is_alert(line) is True
    assert hw_3_5_is_alert("2026-10-05 12:30:45|INFO|start") is False
    assert hw_3_6_date_ok("2026-10-05 12:30:45|ERROR|x") is True
    assert hw_3_6_date_ok("2026/10/05 12:30:45|ERROR|x") is False
    assert hw_3_7_normalize("2026-10-05 12:30:45|error|DISK Full") == \
        "2026-10-05 12:30:45|ERROR|disk full"

    print("task3 (advanced): все assert-тесты пройдены.")
