"""
ДЗ презентации 4, повышенный уровень, задача 2.
Время: 25–35 минут.

Тема: Fraction.

Условие:
    Запросите две дроби в формате "числитель/знаменатель".
    Сложите их с помощью Fraction и выведите несократимую дробь.

Пример:
    In: 1/3
    In: 1/6
    Out: 1/2
"""
from fractions import Fraction


def sum_fractions(f1: str, f2: str) -> str:
    # TODO: реализовать
    pass


if __name__ == "__main__":
    assert sum_fractions("1/3", "1/6") == "1/2"
    assert sum_fractions("1/2", "1/2") == "1"
    print("task_02 (p4 advanced): тесты пройдены")
