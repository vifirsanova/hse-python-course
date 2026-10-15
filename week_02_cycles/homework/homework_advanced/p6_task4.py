# task4.py — Домашняя работа 6, продвинутый уровень.
# Задача 4. Анализ снапшотов метрики.


# ============================================================
# Задача 4. Анализ снапшотов метрики
# ============================================================
# Есть список целых чисел — снапшоты метрики за день.
#
# Подзадачи:
#   4.1. Вернуть True, если значение положительное и чётное.
#   4.2. Вернуть True, если значение отрицательное и делится на 3.
#   4.3. Вернуть True, если значение равно 0.
#   4.4. Вернуть описание значения:
#        "positive even", "positive odd",
#        "negative div3", "negative not div3",
#        "zero".
#   4.5. Вернуть True, если все снапшоты положительные.
#   4.6. Вернуть True, если хотя бы один снапшот равен 0.
#   4.7. Вернуть True, если все снапшоты корректны:
#        положительные чётные, отрицательные делящиеся на 3
#        или ноль.
#   4.8. Вернуть первое "плохое" значение или None, если все хорошие.
#        Плохое — не подходящее ни под одну из категорий:
#        положительное нечётное, отрицательное не делящееся на 3.

def hw_4_1_pos_even(x: int) -> bool:
    """Вернуть True, если x > 0 и x % 2 == 0."""
    # TODO: реализовать
    pass


def hw_4_2_neg_div3(x: int) -> bool:
    """Вернуть True, если x < 0 и x % 3 == 0."""
    # TODO: реализовать
    pass


def hw_4_3_is_zero(x: int) -> bool:
    """Вернуть True, если x == 0."""
    # TODO: реализовать
    pass


def hw_4_4_describe(x: int) -> str:
    """Вернуть описание значения."""
    # TODO: реализовать
    pass


def hw_4_5_all_positive(values: list[int]) -> bool:
    """Вернуть True, если все значения > 0."""
    # TODO: реализовать
    pass


def hw_4_6_has_zero(values: list[int]) -> bool:
    """Вернуть True, если есть хотя бы один 0."""
    # TODO: реализовать
    pass


def hw_4_7_all_valid(values: list[int]) -> bool:
    """Вернуть True, если все значения корректны."""
    # TODO: реализовать
    pass


def hw_4_8_first_bad(values: list[int]) -> int | None:
    """Вернуть первое плохое значение или None."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    assert hw_4_1_pos_even(4) is True
    assert hw_4_1_pos_even(3) is False
    assert hw_4_2_neg_div3(-9) is True
    assert hw_4_2_neg_div3(-4) is False
    assert hw_4_3_is_zero(0) is True
    assert hw_4_3_is_zero(1) is False
    assert hw_4_4_describe(4) == "positive even"
    assert hw_4_4_describe(3) == "positive odd"
    assert hw_4_4_describe(-9) == "negative div3"
    assert hw_4_4_describe(-4) == "negative not div3"
    assert hw_4_4_describe(0) == "zero"
    assert hw_4_5_all_positive([1, 2, 3]) is True
    assert hw_4_5_all_positive([1, -2, 3]) is False
    assert hw_4_6_has_zero([1, 0, 3]) is True
    assert hw_4_6_has_zero([1, 2, 3]) is False
    assert hw_4_7_all_valid([4, -9, 0]) is True
    assert hw_4_7_all_valid([4, 3, 0]) is False
    assert hw_4_8_first_bad([4, -9, 0, 5]) == 5
    assert hw_4_8_first_bad([4, -9, 0]) is None

    print("task4 (advanced): все assert-тесты пройдены.")
