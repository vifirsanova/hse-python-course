# p8_task4.py — Домашняя работа 8, базовый уровень.
# Задача 4. Лог-файл на диске: запись, чтение, сводка.
#
# Работаем с файлом во временной директории (tempfile),
# чтобы не зависеть от текущего каталога.
#
# Подзадачи:
#   4.1. Записать строки в файл (каждая — с переводом строки).
#   4.2. Прочитать все строки файла в список (без переводов строк).
#   4.3. Вернуть число непустых строк в файле.
#   4.4. Дописать строку в конец файла (режим "a").
#   4.5. Вернуть словарь {первое слово строки: количество строк}
#        по непустым строкам файла.


def write_lines(path: str, lines: list[str]) -> None:
    """Записать строки в файл, каждая с переводом строки."""
    # TODO: реализовать
    pass


def read_lines(path: str) -> list[str]:
    """Прочитать строки файла без символов перевода строки."""
    # TODO: реализовать
    pass


def count_nonempty(path: str) -> int:
    """Число непустых строк в файле."""
    # TODO: реализовать
    pass


def append_line(path: str, line: str) -> None:
    """Дописать строку в конец файла."""
    # TODO: реализовать
    pass


def first_word_counts(path: str) -> dict[str, int]:
    """{первое слово: количество строк} по непустым строкам."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    import os
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "log.txt")

        write_lines(path, ["alice login", "bob upload", "", "alice logout"])
        assert os.path.exists(path)

        assert read_lines(path) == ["alice login", "bob upload", "", "alice logout"]
        assert count_nonempty(path) == 3

        append_line(path, "carol login")
        assert read_lines(path)[-1] == "carol login"

        assert first_word_counts(path) == {"alice": 2, "bob": 1, "carol": 1}

        # перезапись
        write_lines(path, ["only one"])
        assert read_lines(path) == ["only one"]
        assert count_nonempty(path) == 1

        # пустой файл
        write_lines(path, [])
        assert read_lines(path) == []
        assert count_nonempty(path) == 0
        assert first_word_counts(path) == {}

    print("p8_task4 (base): все assert-тесты пройдены.")
