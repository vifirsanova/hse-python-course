"""
Задача 3 (base). Обработка логов.

Лог — список строк вида "LEVEL:message", например "INFO:start".

3.1. Верните список только сообщений (без "LEVEL:").
3.2. Верните список только уровней (INFO, WARN, ERROR).
3.3. Верните количество записей уровня "ERROR".
3.4. Верните список сообщений, длина которых больше 5.
3.5. Верните True, если есть хотя бы одна запись "ERROR:...".
"""


def messages(logs):
    # TODO
    pass


def levels(logs):
    # TODO
    pass


def error_count(logs):
    # TODO
    pass


def long_messages(logs):
    # TODO
    pass


def has_error(logs):
    # TODO
    pass


if __name__ == "__main__":
    logs = ["INFO:start", "WARN:slow", "ERROR:fail", "INFO:done", "ERROR:crash"]
    assert messages(logs) == ["start", "slow", "fail", "done", "crash"]
    assert levels(logs) == ["INFO", "WARN", "ERROR", "INFO", "ERROR"]
    assert error_count(logs) == 2
    assert long_messages(logs) == ["start", "crash"]
    assert has_error(logs) is True
    print("task3 (base): все тесты пройдены.")
