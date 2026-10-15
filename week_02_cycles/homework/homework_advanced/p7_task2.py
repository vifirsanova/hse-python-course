"""
Задача 2 (advanced). Снапшоты состояния счётчика.

Счётчик меняется по шагам. Дан список изменений deltas.
Начальное значение — start.

2.1. Верните список снапшотов состояния после каждого шага
     (включая начальное значение).
2.2. Верните список только положительных снапшотов.
2.3. Верните список пар (шаг, значение) для снапшотов,
     где значение изменилось относительно предыдущего.
2.4. Верните множество уникальных значений снапшотов.
2.5. Верните кортеж (max, min) значений снапшотов.
"""


def snapshots(start, deltas):
    # TODO
    pass


def positive_snapshots(start, deltas):
    # TODO
    pass


def changes(start, deltas):
    # TODO
    pass


def unique_values(start, deltas):
    # TODO
    pass


def min_max(start, deltas):
    # TODO
    pass


if __name__ == "__main__":
    assert snapshots(0, [1, 2, -1, 3]) == [0, 1, 3, 2, 5]
    assert positive_snapshots(0, [1, 2, -1, 3]) == [1, 3, 2, 5]
    assert changes(0, [1, 2, -1, 3]) == [(1, 1), (2, 3), (3, 2), (4, 5)]
    assert unique_values(0, [1, 2, -1, 3]) == {0, 1, 2, 3, 5}
    assert min_max(0, [1, 2, -1, 3]) == (5, 0)
    print("task2 (advanced): все тесты пройдены.")
