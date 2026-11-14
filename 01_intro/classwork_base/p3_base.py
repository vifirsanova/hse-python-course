"""
Презентация 4 — базовый уровень.
Алгоритмы: проверка дубликатов и оценка сложности.

Код уже написан. Впишите пропущенные строки там, где стоит # TODO.
Разрешены только присваивания и арифметические операторы.
"""

# ============================================================
# Задача 1. Проверка дубликатов (медленное решение)
# ============================================================
# Условие:
#   Дан список nums. Вернуть True, если есть повторяющиеся
#   элементы, иначе False.

def has_duplicates_slow(nums: list) -> bool:
    result = False
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # TODO: если nums[i] == nums[j], присвойте result = True
            pass
    return result


# ============================================================
# Задача 2. Проверка дубликатов (быстрое решение)
# ============================================================
# Условие:
#   То же самое, но через set.

def has_duplicates_fast(nums: list) -> bool:
    seen = set()
    result = False
    for x in nums:
        if x in seen:
            # TODO: присвойте result = True
            pass
        # TODO: добавьте x в seen, seen.add(x)
        pass
    return result


# ============================================================
# Задача 3. Оценка сложности
# ============================================================
# Ниже — готовые функции. Впишите правильную строку сложности
# вместо многоточия (это присваивание значения переменной).
#
# Варианты: "O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)"

def complexity_a() -> str:
    # for x in items:
    #     print(x)
    answer = "..."  # TODO
    return answer


def complexity_b() -> str:
    # for x in items:
    #     for y in items:
    #         print(x, y)
    answer = "..."  # TODO
    return answer


def complexity_c() -> str:
    # i = 0
    # while i < n:
    #     i *= 2
    answer = "..."  # TODO
    return answer


def complexity_d() -> str:
    # for x in items:
    #     pass
    # for x in items:
    #     for y in items:
    #         pass
    answer = "..."  # TODO
    return answer


if __name__ == "__main__":
    print("p4_base: впишите пропущенные строки вместо TODO.")
