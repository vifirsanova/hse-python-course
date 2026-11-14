# p8_task2.py — Домашняя работа 8, базовый уровень.
# Задача 2. Инвентаризация склада: множества тегов и пересечения.
#
# Есть словарь поставок: {поставка: множество тегов}.
# Например:
#     SUPPLIES = {
#         "A": {"fruit", "red"},
#         "B": {"fruit", "yellow"},
#         "C": {"veg", "green"},
#     }
#
# Подзадачи:
#   2.1. Вернуть множество всех тегов (объединение).
#   2.2. Вернуть множество тегов, общих для всех поставок.
#   2.3. Вернуть кортеж (тег, число поставок) для тега,
#        встречающегося чаще всех; при равенстве — лексикографически меньший.
#   2.4. Вернуть список поставок, у которых есть тег "fruit"
#        (в порядке ключей словаря, через enumerate).
#   2.5. Вернуть словарь {поставка: число тегов только у неё}
#        (теги, которых нет ни в одной другой поставке).


def all_tags(supplies: dict[str, set[str]]) -> set[str]:
    """Объединение всех тегов."""
    # TODO: реализовать
    pass


def common_tags(supplies: dict[str, set[str]]) -> set[str]:
    """Пересечение тегов всех поставок."""
    # TODO: реализовать
    pass


def most_common_tag(supplies: dict[str, set[str]]) -> tuple[str, int]:
    """Самый частый тег и число поставок с ним."""
    # TODO: реализовать
    pass


def supplies_with_fruit(supplies: dict[str, set[str]]) -> list[str]:
    """Поставки с тегом 'fruit' в порядке ключей."""
    # TODO: реализовать
    pass


def unique_tag_counts(supplies: dict[str, set[str]]) -> dict[str, int]:
    """Сколько уникальных (только у этой поставки) тегов у каждой поставки."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    SUPPLIES = {
        "A": {"fruit", "red"},
        "B": {"fruit", "yellow"},
        "C": {"veg", "green"},
    }

    assert all_tags(SUPPLIES) == {"fruit", "red", "yellow", "veg", "green"}
    assert all_tags({}) == set()

    assert common_tags(SUPPLIES) == set()
    assert common_tags({"A": {"x", "y"}, "B": {"x"}}) == {"x"}
    assert common_tags({"A": {"x"}}) == {"x"}
    assert common_tags({}) == set()

    assert most_common_tag(SUPPLIES) == ("fruit", 2)
    assert most_common_tag({"A": {"x", "y"}, "B": {"x"}}) == ("x", 2)

    assert supplies_with_fruit(SUPPLIES) == ["A", "B"]
    assert supplies_with_fruit({"A": {"veg"}, "B": {"fruit"}}) == ["B"]

    assert unique_tag_counts(SUPPLIES) == {"A": 1, "B": 1, "C": 2}
    assert unique_tag_counts({"A": {"x"}, "B": {"x"}}) == {"A": 0, "B": 0}

    print("p8_task2 (base): все assert-тесты пройдены.")
