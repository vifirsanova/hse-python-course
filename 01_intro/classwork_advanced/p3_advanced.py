"""
Презентация 3 — повышенный уровень.
Задачи про алгоритмы: проверка дубликатов, оценка сложности,
улучшение решения с O(n^2) до O(n).
"""

# ============================================================
# Задача 1. Проверка дубликатов (решение коллеги)
# ============================================================
# Условие:
#   Дан список целых чисел nums. Необходимо определить,
#   содержит ли список повторяющиеся элементы.
#   Вернуть True, если хотя бы одно значение встречается
#   больше одного раза, иначе False.
#
# Ограничения:
#   0 <= n <= 100_000
#   -10^9 <= nums[i] <= 10^9
#
# Требуется:
#   1) проверить корректность решения коллеги;
#   2) определить сложность в лучшем и худшем случаях;
#   3) построить входные данные большого размера;
#   4) найти узкое место;
#   5) реализовать улучшенное решение;
#   6) сравнить оба решения.

def has_duplicates_slow(nums: list) -> bool:
    """Решение коллеги за O(n^2)."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def has_duplicates_fast(nums: list) -> bool:
    """
    Улучшенное решение.
    Подсказка: используйте set для хранения уже встреченных чисел.
    Ожидаемая сложность: O(n) по времени, O(n) по памяти.
    """
    # TODO: реализовать
    raise NotImplementedError


# ============================================================
# Задача 2. Оценка сложности фрагментов
# ============================================================
# Условие:
#   Определите временную сложность каждого фрагмента.
#   Ответ запишите в виде строки: "O(1)", "O(log n)", "O(n)",
#   "O(n log n)", "O(n^2)".
#
# Фрагмент A:
#   for x in items:
#       print(x)
#
# Фрагмент B:
#   for x in items:
#       for y in items:
#           print(x, y)
#
# Фрагмент C:
#   i = 0
#   while i < n:
#       i *= 2
#
# Фрагмент D:
#   for x in items:
#       pass
#   for x in items:
#       for y in items:
#           pass

def complexity_a() -> str:
    # TODO
    raise NotImplementedError


def complexity_b() -> str:
    # TODO
    raise NotImplementedError


def complexity_c() -> str:
    # TODO
    raise NotImplementedError


def complexity_d() -> str:
    # TODO
    raise NotImplementedError


# ============================================================
# Тесты
# ============================================================

if __name__ == "__main__":
    assert has_duplicates_slow([]) is False
    assert has_duplicates_slow([1]) is False
    assert has_duplicates_slow([1, 2, 3]) is False
    assert has_duplicates_slow([1, 2, 1]) is True
    assert has_duplicates_slow([5, 5]) is True

    assert has_duplicates_fast([]) is False
    assert has_duplicates_fast([1, 2, 3]) is False
    assert has_duplicates_fast([1, 2, 1]) is True

    data = list(range(100_000))
    assert has_duplicates_fast(data) is False
    data2 = list(range(99_999)) + [0]
    assert has_duplicates_fast(data2) is True

    assert complexity_a() == "O(n)"
    assert complexity_b() == "O(n^2)"
    assert complexity_c() == "O(log n)"
    assert complexity_d() == "O(n^2)"

    print("p4_advanced: все тесты пройдены")
