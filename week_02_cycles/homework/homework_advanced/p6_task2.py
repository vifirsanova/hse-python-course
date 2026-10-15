# task2.py — Домашняя работа 6, продвинутый уровень.
# Задача 2. Условные премии и категории сотрудников.


# ============================================================
# Задача 2. Условные премии и категории сотрудников
# ============================================================
# По стажу и оценке performance (0..100) определяем категорию
# и премию.
#
# Категории:
#   - "senior": стаж >= 5 и оценка >= 80;
#   - "middle": стаж >= 2 и оценка >= 60;
#   - "junior": иначе.
#
# Премия (в процентах от оклада):
#   - senior и оценка >= 95 -> 30;
#   - senior                 -> 20;
#   - middle и оценка >= 75  -> 15;
#   - middle                 -> 10;
#   - junior                 -> 0.
#
# Подзадачи:
#   2.1. Вернуть категорию.
#   2.2. Вернуть процент премии.
#   2.3. Вернуть True, если стаж и оценка валидны
#        (стаж >= 0, 0 <= оценка <= 100).
#   2.4. Вернуть строку вида "senior:30" или "junior:0".
#   2.5. Вернуть True, если сотрудник получает премию больше 15%.
#   2.6. Вернуть True, если хотя бы один из двух сотрудников — senior.

def hw_2_1_category(exp: int, perf: int) -> str:
    """Вернуть 'senior', 'middle' или 'junior'."""
    # TODO: реализовать
    pass


def hw_2_2_bonus(exp: int, perf: int) -> int:
    """Вернуть процент премии (0/10/15/20/30)."""
    # TODO: реализовать
    pass


def hw_2_3_valid(exp: int, perf: int) -> bool:
    """Вернуть True, если стаж и оценка корректны."""
    # TODO: реализовать
    pass


def hw_2_4_line(exp: int, perf: int) -> str:
    """Вернуть 'категория:премия'."""
    # TODO: реализовать
    pass


def hw_2_5_big_bonus(exp: int, perf: int) -> bool:
    """Вернуть True, если премия > 15."""
    # TODO: реализовать
    pass


def hw_2_6_any_senior(a_exp: int, a_perf: int,
                     b_exp: int, b_perf: int) -> bool:
    """Вернуть True, если хотя бы один — senior."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    assert hw_2_1_category(6, 90) == "senior"
    assert hw_2_1_category(6, 70) == "middle"
    assert hw_2_1_category(1, 90) == "junior"
    assert hw_2_1_category(2, 60) == "middle"
    assert hw_2_2_bonus(6, 95) == 30
    assert hw_2_2_bonus(6, 90) == 20
    assert hw_2_2_bonus(3, 80) == 15
    assert hw_2_2_bonus(3, 70) == 10
    assert hw_2_2_bonus(1, 90) == 0
    assert hw_2_3_valid(0, 0) is True
    assert hw_2_3_valid(-1, 50) is False
    assert hw_2_3_valid(3, 101) is False
    assert hw_2_4_line(6, 95) == "senior:30"
    assert hw_2_4_line(1, 50) == "junior:0"
    assert hw_2_5_big_bonus(6, 95) is True
    assert hw_2_5_big_bonus(6, 80) is True
    assert hw_2_5_big_bonus(3, 80) is False
    assert hw_2_6_any_senior(6, 90, 1, 50) is True
    assert hw_2_6_any_senior(1, 50, 2, 70) is False

    print("task2 (advanced): все assert-тесты пройдены.")
