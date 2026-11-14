# p8_task5.py — Домашняя работа 8, продвинутый уровень.
# Задача 5. Скользящее окно по логу сессий с кортежами.
#
# Сессии — список кортежей (user, start, end), start/end — int.
# Гарантируется, что start <= end, но интервалы могут пересекаться.
#
# Подзадачи:
#   10.1. Вернуть кортеж (min_start, max_end) — общий диапазон времени.
#   10.2. Вернуть список кортежей (user, start, end) в порядке start,
#         при равенстве — по user (сортировка стабильна).
#   10.3. Вернуть максимальное число одновременно активных сессий
#         (через события +1/-1 и while по отсортированным событиям).
#   10.4. Вернуть множество пользователей, у которых был хотя бы
#         один интервал, полностью содержащийся в другом
#         (через двойной while).
#   10.5. Вернуть словарь {user: суммарное время, покрытое
#         объединением его сессий} (учёт пересечений, через while).


def time_span(sessions: list[tuple[str, int, int]]) -> tuple[int | None, int | None]:
    """Общий диапазон времени."""
    # TODO: реализовать
    pass


def sorted_sessions(sessions: list[tuple[str, int, int]]) -> list[tuple[str, int, int]]:
    """Сортировка по (start, user)."""
    # TODO: реализовать
    pass


def max_concurrent(sessions: list[tuple[str, int, int]]) -> int:
    """Максимальное число одновременно активных сессий."""
    # TODO: реализовать
    pass


def contained_users(sessions: list[tuple[str, int, int]]) -> set[str]:
    """Пользователи с интервалом, вложенным в другой интервал."""
    # TODO: реализовать
    pass


def merged_duration_by_user(sessions: list[tuple[str, int, int]]) -> dict[str, int]:
    """{user: длина объединения его интервалов}."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    S = [
        ("alice", 0, 10),
        ("bob", 5, 15),
        ("alice", 20, 30),
        ("carol", 8, 9),
    ]

    assert time_span(S) == (0, 30)
    assert time_span([]) == (None, None)

    assert sorted_sessions(S) == [
        ("alice", 0, 10),
        ("bob", 5, 15),
        ("carol", 8, 9),
        ("alice", 20, 30),
    ]
    assert sorted_sessions([]) == []

    assert max_concurrent(S) == 3
    assert max_concurrent([]) == 0

    assert contained_users(S) == {"carol"}
    assert contained_users([("a", 0, 5), ("b", 0, 5)]) == set()

    assert merged_duration_by_user(S) == {"alice": 20, "bob": 10, "carol": 1}
    assert merged_duration_by_user([("a", 0, 10), ("a", 5, 15)]) == {"a": 15}
    assert merged_duration_by_user([]) == {}

    print("p8_task10 (advanced): все assert-тесты пройдены.")
