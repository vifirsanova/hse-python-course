"""
Презентация 5 — базовый уровень.
Жадные алгоритмы: размен монет, интервалы, рюкзак, платформы.

Код уже написан. Впишите пропущенные строки там, где стоит # TODO.
Разрешены только присваивания и арифметические операторы.
"""

# ============================================================
# Задача 1. Размен монет
# ============================================================
# Условие:
#   Дана сумма amount и номиналы coins. Выдать сумму минимальным
#   количеством монет (жадно: берём самую крупную).
#
# Пример:
#   amount = 87, coins = [50, 10, 5, 1] -> 7 монет

def min_coins(amount: int, coins: list) -> int:
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            # TODO: вычтите coin из amount
            # TODO: увеличьте count на 1
            pass
    return count


# Подсказка:
#   amount -= coin
#   count += 1

# ============================================================
# Задача 2. Выбор интервалов
# ============================================================
# Условие:
#   Даны интервалы. Выбрать максимальное количество
#   непересекающихся (жадно: сортируем по окончанию).
#
# Пример:
#   intervals = [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11)]
#   Ответ: 4

def max_intervals(intervals: list) -> int:
    intervals.sort(key=lambda x: x[1])
    count = 0
    last_end = float("-inf")
    for start, end in intervals:
        if start >= last_end:
            # TODO: увеличьте count на 1
            # TODO: присвойте last_end = end
            pass
    return count


# Подсказка:
#   count += 1
#   last_end = end

# ============================================================
# Задача 3. Дробный рюкзак
# ============================================================
# Условие:
#   Рюкзак вместимостью capacity, предметы (weight, value).
#   Можно брать части. Максимизировать стоимость
#   (жадно: сортируем по value/weight).
#
# Пример:
#   capacity = 50, items = [(10,60), (20,100), (30,120)] -> 240.0

def fractional_knapsack(capacity: float, items: list) -> float:
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    total = 0.0
    for weight, value in items:
        if capacity >= weight:
            # TODO: добавьте value к total
            # TODO: вычтите weight из capacity
            pass
        else:
            # TODO: добавьте value * (capacity / weight) к total
            # TODO: присвойте capacity = 0
            pass
    return total


# Подсказка:
#   total += value
#   capacity -= weight
#   total += value * (capacity / weight)
#   capacity = 0

# ============================================================
# Задача 4. Минимальное число платформ
# ============================================================
# Условие:
#   Даны arrivals и departures поездов. Найти минимальное
#   число платформ (жадно: прибытие +1, отправление -1).
#
# Пример:
#   arrivals   = [900, 940, 950, 1100, 1500, 1800]
#   departures = [910, 1200, 1120, 1130, 1900, 2000]
#   Ответ: 3

def min_platforms(arrivals: list, departures: list) -> int:
    events = [(t, 1) for t in arrivals] + [(t, -1) for t in departures]
    events.sort()
    current = 0
    best = 0
    for _, delta in events:
        # TODO: прибавьте delta к current
        # TODO: если current > best, присвойте best = current
        pass
    return best


# Подсказка:
#   current += delta
#   if current > best:
#       best = current

# ============================================================
# Подсказки
# ============================================================
# Все задачи — жадные, сложность O(n log n) или O(n).

if __name__ == "__main__":
    print("p5_base: впишите пропущенные строки вместо TODO.")
