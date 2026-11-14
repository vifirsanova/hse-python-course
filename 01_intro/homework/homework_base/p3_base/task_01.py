"""
ДЗ презентации 3, базовый уровень, задача 1.
Время: 10–15 минут.

Тема: алгоритмы, сложность O(n^2).

Условие:
    Дана функция, которая сравнивает два числа nums[i] и nums[j].
    Допишите тело: если они равны, верните True.
    Циклы уже написаны — вписывать их не нужно.

Подсказка:
    Внутри if нужно вернуть True.
"""

def has_duplicates_slow(nums: list) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # TODO: если nums[i] == nums[j], верните True
            pass
    return False


if __name__ == "__main__":
    data = [1, 2, 3, 2]
    print(has_duplicates_slow(data))   # True
    print(has_duplicates_slow([1, 2, 3]))  # Falsetask_01.py
