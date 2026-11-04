# p8_task1.py — Домашняя работа 8, базовый уровень.
# Задача 1. Журнал сервиса: парсинг лога и сводка по пользователям.
#
# На вход подаётся список строк лога. Формат строки:
#     "<timestamp> <user> <action>"
# например:
#     "10:00 alice login"
#     "10:01 bob upload"
#     "10:02 alice logout"
#
# Подзадачи:
#   1.1. Вернуть список кортежей (timestamp, user, action).
#   1.2. Вернуть множество пользователей, встречающихся в логе.
#   1.3. Вернуть словарь {user: количество строк} (через while по индексам).
#   1.4. Вернуть список пользователей в порядке первого появления
#        (использовать enumerate и множество seen).
#   1.5. Вернуть кортеж (самый активный пользователь, число строк);
#        при равенстве — тот, кто встретился раньше.


def log_parse(lines: list[str]) -> list[tuple[str, str, str]]:
    """Разобрать строки лога в список кортежей."""
    # TODO: реализовать
    pass


def log_users(lines: list[str]) -> set[str]:
    """Множество пользователей из лога."""
    # TODO: реализовать
    pass


def log_counts(lines: list[str]) -> dict[str, int]:
    """Сколько строк у каждого пользователя (while по индексам)."""
    # TODO: реализовать
    pass


def log_first_seen(lines: list[str]) -> list[str]:
    """Пользователи в порядке первого появления (enumerate + set)."""
    # TODO: реализовать
    pass


def log_top_user(lines: list[str]) -> tuple[str, int]:
    """Самый активный пользователь и число его строк."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    LOG = [
        "10:00 alice login",
        "10:01 bob upload",
        "10:02 alice logout",
        "10:03 carol login",
        "10:04 alice upload",
    ]

    assert log_parse(LOG) == [
        ("10:00", "alice", "login"),
        ("10:01", "bob", "upload"),
        ("10:02", "alice", "logout"),
        ("10:03", "carol", "login"),
        ("10:04", "alice", "upload"),
    ]
    assert log_parse([]) == []

    assert log_users(LOG) == {"alice", "bob", "carol"}
    assert log_users([]) == set()

    assert log_counts(LOG) == {"alice": 3, "bob": 1, "carol": 1}
    assert log_counts([]) == {}

    assert log_first_seen(LOG) == ["alice", "bob", "carol"]
    assert log_first_seen([]) == []

    assert log_top_user(LOG) == ("alice", 3)
    assert log_top_user(["1 x a", "2 y b"]) == ("x", 1)
    assert log_top_user(["1 x a", "2 y b", "3 x c", "4 y d"]) == ("x", 2)

    print("p8_task1 (base): все assert-тесты пройдены.")
