"""
ДЗ презентации 5, повышенный уровень, задача 2.
Время: 25–35 минут.

Тема: минимальное число платформ.

Условие:
    Даны arrivals и departures поездов.
    Верните минимальное число платформ.

Пример:
    arrivals   = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]
    Ответ: 3
"""

def min_platforms(arrivals: list, departures: list) -> int:
    # TODO: реализовать
    pass


if __name__ == "__main__":
    assert min_platforms([], []) == 0
    assert min_platforms([900], [910]) == 1
    assert min_platforms(
        [900, 940, 950, 1100, 1500, 1800],
        [910, 1200, 1120, 1130, 1900, 2000]
    ) == 3
    assert min_platforms([100, 200, 300], [150, 250, 350]) == 1
    print("task_02 (p5 advanced): тесты пройдены")
