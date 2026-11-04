# p8_task3.py — Домашняя работа 8, базовый уровень.
# Задача 3. Очередь задач: кортежи и while.
#
# Очередь задач — список кортежей (id, приоритет, описание).
# Приоритет — целое число, чем меньше, тем важнее.
#
# Подзадачи:
#   3.1. Вернуть кортеж (самый важный id, описание)
#        по минимальному приоритету; при равенстве — меньший id.
#   3.2. Вернуть список id в порядке выполнения
#        (сортировка по (приоритет, id), через while построить результат).
#   3.3. Вернуть словарь {приоритет: количество задач}.
#   3.4. Вернуть кортеж (id, описание) первой задачи,
#        у которой описание содержит слово "urgent".
#        Если таких нет — вернуть (None, None).
#   3.5. Вернуть список описаний задач с приоритетом <= порога threshold
#        в порядке исходной очереди (через enumerate).


def next_task(tasks: list[tuple[int, int, str]]) -> tuple[int, str]:
    """Самый важный id и описание."""
    # TODO: реализовать
    pass


def execution_order(tasks: list[tuple[int, int, str]]) -> list[int]:
    """Порядок выполнения: сортировка по (приоритет, id), собрать через while."""
    # TODO: реализовать
    pass


def priority_counts(tasks: list[tuple[int, int, str]]) -> dict[int, int]:
    """Сколько задач на каждый приоритет."""
    # TODO: реализовать
    pass


def first_urgent(tasks: list[tuple[int, int, str]]) -> tuple[int | None, str | None]:
    """Первая задача со словом 'urgent' в описании."""
    # TODO: реализовать
    pass


def descriptions_upto(tasks: list[tuple[int, int, str]], threshold: int) -> list[str]:
    """Описания задач с приоритетом <= threshold в исходном порядке."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    TASKS = [
        (3, 5, "cleanup"),
        (1, 2, "urgent fix login"),
        (2, 2, "review PR"),
        (4, 1, "urgent deploy"),
    ]

    assert next_task(TASKS) == (4, "urgent deploy")
    assert next_task([(2, 3, "b"), (1, 3, "a")]) == (1, "a")
    assert next_task([]) == (None, None)

    assert execution_order(TASKS) == [4, 1, 2, 3]
    assert execution_order([]) == []

    assert priority_counts(TASKS) == {1: 1, 2: 2, 5: 1}
    assert priority_counts([]) == {}

    assert first_urgent(TASKS) == (1, "urgent fix login")
    assert first_urgent([(1, 1, "calm")]) == (None, None)

    assert descriptions_upto(TASKS, 2) == ["urgent fix login", "review PR", "urgent deploy"]
    assert descriptions_upto(TASKS, 0) == []

    print("p8_task3 (base): все assert-тесты пройдены.")
