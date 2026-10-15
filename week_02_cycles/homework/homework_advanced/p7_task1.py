"""
Задача 1 (advanced). Анализ температурных рядов.

Дан список температур temps.

1.1. Верните список температур без выбросов:
     только значения в диапазоне [-50, 50] включительно.
1.2. Верните список "нормализованных" значений:
     каждое значение минус среднее по исходному списку.
1.3. Верните список индексов, где температура отрицательная.
1.4. Верните dict: {индекс: температура} только для
     отрицательных температур.
1.5. Верните список температур, отсортированных по abs.
"""


def filter_outliers(temps):
    # TODO
    pass


def normalized(temps):
    # TODO
    pass


def negative_indices(temps):
    # TODO
    pass


def negative_dict(temps):
    # TODO
    pass


def sorted_by_abs(temps):
    # TODO
    pass


if __name__ == "__main__":
    temps = [3, -5, 120, -15, 7, -60, 4, 0]
    assert filter_outliers(temps) == [3, -5, -15, 7, 4, 0]
    avg = sum(temps) / len(temps)
    assert normalized(temps) == [t - avg for t in temps]
    assert negative_indices(temps) == [1, 3, 5]
    assert negative_dict(temps) == {1: -5, 3: -15, 5: -60}
    assert sorted_by_abs(temps) == [0, 3, 4, -5, 7, -15, -60, 120]
    print("task1 (advanced): все тесты пройдены.")
