# p8_task1.py — Домашняя работа 8, продвинутый уровень.
# Задача 1. Инкрементальный агрегатор логов из файла.
#
# Файл лога содержит строки вида:
#     "<timestamp> <user> <action>"
# Нужно прочитать файл построчно, не загружая всё в память,
# и построить сводку.
#
# Подзадачи:
#   6.1. Вернуть словарь {user: количество строк}, читая файл итеративно
#        (через for line in f, без readlines).
#   6.2. Вернуть множество действий (третий столбец) из файла.
#   6.3. Вернуть словарь {user: множество действий} — какие действия
#        делал каждый пользователь (без дубликатов).
#   6.4. Вернуть кортеж (user, action, count) — самая частая пара
#        (пользователь, действие); при равенстве — лексикографически
#        меньшая пара. Считать через while по списку пар.
#   6.5. Вернуть список пользователей, у которых есть действие "login",
#        но нет "logout" (в порядке первого появления в файле).
#        Использовать enumerate и множества.


def user_line_counts(path: str) -> dict[str, int]:
    """{user: количество строк} через итеративное чтение файла."""
    # TODO: реализовать
    pass


def all_actions(path: str) -> set[str]:
    """Множество всех действий из файла."""
    # TODO: реализовать
    pass


def actions_by_user(path: str) -> dict[str, set[str]]:
    """{user: множество действий}."""
    # TODO: реализовать
    pass


def top_user_action(path: str) -> tuple[str | None, str | None, int]:
    """Самая частая пара (user, action) и её count."""
    # TODO: реализовать
    pass


def logged_in_not_out(path: str) -> list[str]:
    """Пользователи с login, но без logout, в порядке появления."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    import os
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "app.log")
        with open(path, "w", encoding="utf-8") as f:
            f.write("10:00 alice login\n")
            f.write("10:01 bob login\n")
            f.write("10:02 alice upload\n")
            f.write("10:03 alice login\n")
            f.write("10:04 carol login\n")
            f.write("10:05 bob logout\n")
            f.write("10:06 carol upload\n")

        assert user_line_counts(path) == {"alice": 3, "bob": 2, "carol": 2}

        assert all_actions(path) == {"login", "upload", "logout"}

        assert actions_by_user(path) == {
            "alice": {"login", "upload"},
            "bob": {"login", "logout"},
            "carol": {"login", "upload"},
        }

        assert top_user_action(path) == ("alice", "login", 2)

        # login есть у всех, logout только у bob -> alice и carol
        assert logged_in_not_out(path) == ["alice", "carol"]

    # пустой файл
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "empty.log")
        open(path, "w", encoding="utf-8").close()

        assert user_line_counts(path) == {}
        assert all_actions(path) == set()
        assert actions_by_user(path) == {}
        assert top_user_action(path) == (None, None, 0)
        assert logged_in_not_out(path) == []

    print("p8_task6 (advanced): все assert-тесты пройдены.")
