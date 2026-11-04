# p8_task3.py — Домашняя работа 8, продвинутый уровень.
# Задача 3. Ротация и слияние лог-файлов на диске.
#
# Есть директория с несколькими лог-файлами *.log.
# Нужно их прочитать, объединить, отфильтровать и записать сводку.
#
# Подзадачи:
#   8.1. Вернуть список путей к *.log в директории (отсортированный).
#   8.2. Вернуть список всех непустых строк из всех файлов
#        (в порядке файлов, затем строк).
#   8.3. Вернуть множество пользователей (первое слово строки)
#        по всем файлам.
#   8.4. Записать в out_path объединённые строки, содержащие
#        подстроку needle, и вернуть число записанных строк.
#   8.5. Вернуть словарь {file_name: число непустых строк}
#        для всех *.log в директории.


def list_logs(dir_path: str) -> list[str]:
    """Отсортированный список путей к *.log."""
    # TODO: реализовать
    pass


def read_all_lines(dir_path: str) -> list[str]:
    """Все непустые строки из всех *.log (порядок файлов сохраняется)."""
    # TODO: реализовать
    pass


def users_in_logs(dir_path: str) -> set[str]:
    """Множество первых слов строк по всем файлам."""
    # TODO: реализовать
    pass


def filter_to_file(dir_path: str, out_path: str, needle: str) -> int:
    """Записать строки с needle в out_path, вернуть их число."""
    # TODO: реализовать
    pass


def line_counts_by_file(dir_path: str) -> dict[str, int]:
    """{имя файла: число непустых строк}."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    import os
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        a = os.path.join(tmp, "a.log")
        b = os.path.join(tmp, "b.log")
        c = os.path.join(tmp, "c.txt")  # не .log, не должен попасть

        with open(a, "w", encoding="utf-8") as f:
            f.write("alice login\n")
            f.write("bob upload\n")
            f.write("\n")

        with open(b, "w", encoding="utf-8") as f:
            f.write("alice logout\n")
            f.write("carol login\n")

        with open(c, "w", encoding="utf-8") as f:
            f.write("ignored line\n")

        assert list_logs(tmp) == [a, b]

        assert read_all_lines(tmp) == [
            "alice login", "bob upload",
            "alice logout", "carol login",
        ]

        assert users_in_logs(tmp) == {"alice", "bob", "carol"}

        out = os.path.join(tmp, "out.log")
        n = filter_to_file(tmp, out, "login")
        assert n == 3
        with open(out, encoding="utf-8") as f:
            assert [ln.rstrip("\n") for ln in f] == [
                "alice login", "alice logout", "carol login",
            ]

        assert line_counts_by_file(tmp) == {
            os.path.basename(a): 2,
            os.path.basename(b): 2,
        }

    # пустая директория
    with tempfile.TemporaryDirectory() as tmp:
        assert list_logs(tmp) == []
        assert read_all_lines(tmp) == []
        assert users_in_logs(tmp) == set()
        assert line_counts_by_file(tmp) == {}

    print("p8_task8 (advanced): все assert-тесты пройдены.")
