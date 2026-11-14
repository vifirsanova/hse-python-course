# task3.py — Домашняя работа 9, базовый уровень.
# Задача 3. Безопасный конвертер данных (обработка ошибок).


# ============================================================
# Задача 3. Безопасный конвертер данных
# ============================================================
# При чтении пользовательских анкет и таблиц часто встречаются
# пустые строки, опечатки и выходы за границы списка.
#
# Подзадачи:
#   3.1. Преобразовать строку s в int; при ValueError или TypeError
#        вернуть значение default (по умолчанию 0).
#   3.2. Безопасно вернуть элемент списка items по индексу idx;
#        при IndexError вернуть None.
#   3.3. Из словаря data взять ключ key и преобразовать значение в float;
#        при KeyError, ValueError или TypeError вернуть None.
#   3.4. Принять список строк raw_values и вернуть список только тех целых
#        чисел, которые успешно преобразовались через int().
#   3.5. Разделить сумму корректных целых чисел из raw_values на их количество;
#        если корректных чисел нет (ZeroDivisionError), вернуть 0.0.


def hw_3_1_safe_int(s, default: int = 0) -> int:
    """Вернуть int(s) или default при ValueError / TypeError."""
    # TODO: реализовать
    pass


def hw_3_2_safe_index(items: list, idx: int):
    """Вернуть items[idx] или None при IndexError."""
    # TODO: реализовать
    pass


def hw_3_3_extract_float(data: dict, key: str) -> float | None:
    """Вернуть float(data[key]) или None при отсутствии ключа / ошибке типа."""
    # TODO: реализовать
    pass


def hw_3_4_parse_ints(raw_values: list[str]) -> list[int]:
    """Вернуть список успешно распознанных целых чисел."""
    # TODO: реализовать
    pass


def hw_3_5_safe_average(raw_values: list[str]) -> float:
    """Вернуть среднее распознанных чисел или 0.0, если их нет."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    assert hw_3_1_safe_int("42") == 42
    assert hw_3_1_safe_int("abc", -1) == -1
    assert hw_3_1_safe_int(None, 0) == 0

    assert hw_3_2_safe_index(["a", "b"], 1) == "b"
    assert hw_3_2_safe_index(["a", "b"], 5) is None

    assert hw_3_3_extract_float({"price": "19.5"}, "price") == 19.5
    assert hw_3_3_extract_float({"price": "free"}, "price") is None
    assert hw_3_3_extract_float({}, "price") is None

    assert hw_3_4_parse_ints(["10", "x", "20", "", "-6"]) == [10, 20, -6]
    assert hw_3_5_safe_average(["10", "bad", "20"]) == 15.0
    assert hw_3_5_safe_average(["bad", "none"]) == 0.0

    print("task3 (hw1_basic): все assert-тесты пройдены.")
