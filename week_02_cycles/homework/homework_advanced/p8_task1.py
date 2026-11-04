# p8_task1.py — Домашняя работа 8, продвинутый уровень.
# Задача 1. Дедупликация событий с приоритетом.
#
# События — список кортежей (event_id, priority, payload).
# Одинаковые event_id считаются дубликатами; нужно оставить
# одно событие на id — с максимальным приоритетом
# (при равенстве — первое встреченное).
#
# Подзадачи:
#   7.1. Вернуть множество всех event_id.
#   7.2. Вернуть словарь {event_id: лучший приоритет}.
#   7.3. Вернуть список уникальных событий (по одному на id)
#        в порядке первого появления id, с лучшим приоритетом.
#   7.4. Вернуть кортеж (event_id, payload) события с максимальным
#        приоритетом среди уникальных; при равенстве — меньший event_id.
#        Если событий нет — (None, None).
#   7.5. Вернуть словарь {payload: количество уникальных id},
#        у которых этот payload; порядок ключей — по первому появлению.


def all_ids(events: list[tuple[int, int, str]]) -> set[int]:
    """Множество всех event_id."""
    # TODO: реализовать
    pass


def best_priority(events: list[tuple[int, int, str]]) -> dict[int, int]:
    """{event_id: максимальный приоритет}."""
    # TODO: реализовать
    pass


def unique_events(events: list[tuple[int, int, str]]) -> list[tuple[int, int, str]]:
    """Уникальные события с лучшим приоритетом в порядке первого появления."""
    # TODO: реализовать
    pass


def top_event(events: list[tuple[int, int, str]]) -> tuple[int | None, str | None]:
    """(event_id, payload) события с максимальным приоритетом."""
    # TODO: реализовать
    pass


def payload_id_counts(events: list[tuple[int, int, str]]) -> dict[str, int]:
    """{payload: число уникальных id} в порядке первого появления payload."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    EVENTS = [
        (1, 5, "a"),
        (2, 3, "b"),
        (1, 7, "a"),
        (3, 7, "c"),
        (2, 3, "b"),
        (1, 2, "a"),
    ]

    assert all_ids(EVENTS) == {1, 2, 3}
    assert all_ids([]) == set()

    assert best_priority(EVENTS) == {1: 7, 2: 3, 3: 7}
    assert best_priority([]) == {}

    assert unique_events(EVENTS) == [(1, 7, "a"), (2, 3, "b"), (3, 7, "c")]
    assert unique_events([]) == []

    assert top_event(EVENTS) == (1, "a")
    assert top_event([(2, 1, "x"), (1, 1, "y")]) == (1, "y")
    assert top_event([]) == (None, None)

    assert payload_id_counts(EVENTS) == {"a": 1, "b": 1, "c": 1}
    assert payload_id_counts([(1, 1, "x"), (2, 1, "x"), (3, 1, "y")]) == {"x": 2, "y": 1}
    assert payload_id_counts([]) == {}

    print("p8_task7 (advanced): все assert-тесты пройдены.")
