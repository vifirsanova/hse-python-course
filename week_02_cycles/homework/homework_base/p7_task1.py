"""
Задача 1 (base). Журнал температур.

Устройство пишет температуру каждый час. Дан список чисел temps.

1.1. Верните список только тех температур, которые выше 0.
1.2. Верните сумму всех температур.
1.3. Верните среднее арифметическое (как float).
1.4. Верните количество температур ниже -10.
1.5. Верните список температур, округлённых до целого
     (используйте int(x) для простоты).
"""


def above_zero(temps):
    # TODO
    pass


def total(temps):
    # TODO
    pass


def average(temps):
    # TODO
    pass


def below_minus_ten(temps):
    # TODO
    pass


def rounded(temps):
    # TODO
    pass


if __name__ == "__main__":
    temps = [3, -5, 0, 12, -15, 7, -20, 4]
    assert above_zero(temps) == [3, 12, 7, 4]
    assert total(temps) == -14
    assert average(temps) == -14 / 8
    assert below_minus_ten(temps) == 2
    assert rounded(temps) == [3, -5, 0, 12, -15, 7, -20, 4]
    print("task1 (base): все тесты пройдены.")
