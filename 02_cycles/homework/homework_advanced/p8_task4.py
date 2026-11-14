# p8_task4.py — Домашняя работа 4, продвинутый уровень.
# Задача 4. Валидатор пакетов зависимостей.
#
# Пакеты описаны словарём {пакет: множество зависимостей}.
# Зависимости — имена других пакетов.
#
# Подзадачи:
#   9.1. Вернуть множество пакетов, от которых никто не зависит
#        (листья: нет входящих рёбер).
#   9.2. Вернуть множество пакетов, у которых нет зависимостей
#        (корни: пустое множество зависимостей).
#   9.3. Вернуть True, если есть цикл зависимостей
#        (простой DFS с while и множеством visited/stack).
#   9.4. Вернуть список пакетов в порядке топологической сортировки
#        (Kahn: while + словарь входящих степеней + множество готовых).
#        Если есть цикл — вернуть пустой список.
#   9.5. Вернуть словарь {пакет: число транзитивных зависимостей}
#        (все достижимые пакеты, без самого пакета).


def leaf_packages(graph: dict[str, set[str]]) -> set[str]:
    """Пакеты, от которых никто не зависит."""
    # TODO: реализовать
    pass


def root_packages(graph: dict[str, set[str]]) -> set[str]:
    """Пакеты без зависимостей."""
    # TODO: реализовать
    pass


def has_cycle(graph: dict[str, set[str]]) -> bool:
    """True, если есть цикл зависимостей."""
    # TODO: реализовать
    pass


def topo_order(graph: dict[str, set[str]]) -> list[str]:
    """Топологический порядок или [] при цикле."""
    # TODO: реализовать
    pass


def transitive_counts(graph: dict[str, set[str]]) -> dict[str, int]:
    """{пакет: число всех достижимых зависимостей}."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    G = {
        "app": {"lib", "utils"},
        "lib": {"utils"},
        "utils": set(),
    }

    assert leaf_packages(G) == {"app"}
    assert leaf_packages({}) == set()

    assert root_packages(G) == {"utils"}
    assert root_packages({}) == set()

    assert has_cycle(G) is False
    assert has_cycle({"a": {"b"}, "b": {"a"}}) is True
    assert has_cycle({"a": {"b"}, "b": {"c"}, "c": set()}) is False
    assert has_cycle({}) is False

    order = topo_order(G)
    assert order.index("utils") < order.index("lib") < order.index("app")
    assert topo_order({"a": {"b"}, "b": {"a"}}) == []
    assert topo_order({}) == []

    assert transitive_counts(G) == {"app": 2, "lib": 1, "utils": 0}
    assert transitive_counts({"a": {"b"}, "b": {"a"}}) == {"a": 1, "b": 1}
    assert transitive_counts({}) == {}

    print("p8_task9 (advanced): все assert-тесты пройдены.")
