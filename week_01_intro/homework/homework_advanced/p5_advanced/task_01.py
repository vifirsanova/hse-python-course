"""
ДЗ презентации 5, повышенный уровень, задача 1.
Время: 25–35 минут.

Тема: дробный рюкзак.

Условие:
    items — список кортежей (weight, value).
    Верните максимальную суммарную стоимость.

Пример:
    capacity = 50
    items = [(10, 60), (20, 100), (30, 120)]
    Ответ: 240.0
"""

def fractional_knapsack(capacity: float, items: list) -> float:
    # TODO: реализовать
    pass


if __name__ == "__main__":
    items = [(10, 60), (20, 100), (30, 120)]
    assert abs(fractional_knapsack(50, items) - 240.0) < 1e-9
    assert fractional_knapsack(0, items) == 0.0
    print("task_01 (p5 advanced): тесты пройдены")
