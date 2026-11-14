"""
Задача 2 (base). Снапшоты счётчика.

Счётчик каждую секунду увеличивается на 1, начиная с 0.
Нужно сохранить снапшоты его значений.

2.1. Верните список значений счётчика от 0 до n включительно.
2.2. Верните список значений от 0 до n, кратных 3.
2.3. Верните список значений от n до 0 в обратном порядке.
2.4. Верните список квадратов значений от 0 до n.
2.5. Верните сумму значений от 0 до n, кратных 5.
"""


def snapshots(n):
    # TODO
    pass


def multiples_of_three(n):
    # TODO
    pass


def reversed_snapshots(n):
    # TODO
    pass


def squares(n):
    # TODO
    pass


def sum_multiples_of_five(n):
    # TODO
    pass


if __name__ == "__main__":
    assert snapshots(4) == [0, 1, 2, 3, 4]
    assert multiples_of_three(10) == [0, 3, 6, 9]
    assert reversed_snapshots(3) == [3, 2, 1, 0]
    assert squares(3) == [0, 1, 4, 9]
    assert sum_multiples_of_five(12) == 0 + 5 + 10
    print("task2 (base): все тесты пройдены.")
