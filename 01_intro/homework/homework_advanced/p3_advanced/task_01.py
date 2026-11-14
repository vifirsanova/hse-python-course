"""
ДЗ презентации 3, повышенный уровень, задача 1.
Время: 25–35 минут.

Тема: улучшение O(n^2) до O(n) через set.

Условие:
    Реализуйте has_duplicates_fast за O(n) по времени
    и O(n) по памяти.

Ограничения:
    0 <= n <= 100_000
    -10^9 <= nums[i] <= 10^9
"""

def has_duplicates_fast(nums: list) -> bool:
    # TODO: реализовать
    pass


if __name__ == "__main__":
    assert has_duplicates_fast([]) is False
    assert has_duplicates_fast([1]) is False
    assert has_duplicates_fast([1, 2, 3]) is False
    assert has_duplicates_fast([1, 2, 1]) is True
    assert has_duplicates_fast([5, 5]) is True

    data = list(range(100_000))
    assert has_duplicates_fast(data) is False
    data2 = list(range(99_999)) + [0]
    assert has_duplicates_fast(data2) is True

    print("task_01 (p3 advanced): тесты пройдены")
