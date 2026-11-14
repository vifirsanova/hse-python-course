# task1.py — Домашняя работа 6, базовый уровень.
# Задача 1. Валидатор пользовательских данных.


# ============================================================
# Задача 1. Валидатор пользовательских данных
# ============================================================
# При регистрации проверяем логин и возраст.
#
# Правила:
#   - логин не пустой;
#   - длина логина от 3 до 20 символов;
#   - возраст от 18 до 120 включительно.
#
# Подзадачи:
#   1.1. Вернуть True, если логин корректен.
#   1.2. Вернуть True, если возраст корректен.
#   1.3. Вернуть True, если оба условия выполнены.
#   1.4. Вернуть строку с первой ошибкой:
#        "empty login", "short login", "long login",
#        "too young", "too old", "ok".

def hw_1_1_login_ok(login: str) -> bool:
    """Вернуть True, если логин от 3 до 20 символов."""
    # TODO: реализовать
    pass


def hw_1_2_age_ok(age: int) -> bool:
    """Вернуть True, если 18 <= age <= 120."""
    # TODO: реализовать
    pass


def hw_1_3_both_ok(login: str, age: int) -> bool:
    """Вернуть True, если логин и возраст корректны."""
    # TODO: реализовать
    pass


def hw_1_4_first_error(login: str, age: int) -> str:
    """Вернуть текст первой ошибки или 'ok'."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    assert hw_1_1_login_ok("ira") is True
    assert hw_1_1_login_ok("ab") is False
    assert hw_1_1_login_ok("a" * 21) is False
    assert hw_1_2_age_ok(18) is True
    assert hw_1_2_age_ok(120) is True
    assert hw_1_2_age_ok(17) is False
    assert hw_1_3_both_ok("ira", 20) is True
    assert hw_1_3_both_ok("ab", 20) is False
    assert hw_1_4_first_error("", 20) == "empty login"
    assert hw_1_4_first_error("ab", 20) == "short login"
    assert hw_1_4_first_error("a" * 21, 20) == "long login"
    assert hw_1_4_first_error("ira", 17) == "too young"
    assert hw_1_4_first_error("ira", 121) == "too old"
    assert hw_1_4_first_error("ira", 20) == "ok"

    print("task1: все assert-тесты пройдены.")
