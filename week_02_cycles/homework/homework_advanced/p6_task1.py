# task1.py — Домашняя работа 6, продвинутый уровень.
# Задача 1. Валидатор учётных записей.


# ============================================================
# Задача 1. Валидатор учётных записей
# ============================================================
# Проверяем логин, email и возраст при регистрации.
#
# Правила:
#   - логин не пустой;
#   - длина логина от 3 до 20 символов;
#   - логин без пробелов;
#   - email вида "name@domain.xx" (упрощённо: \w+@\w+\.[a-z]{2,3});
#   - возраст от 18 до 120 включительно.
#
# Подзадачи:
#   1.1. Вернуть True, если логин корректен (3..20 и без пробелов).
#   1.2. Вернуть True, если email соответствует шаблону (re.fullmatch).
#   1.3. Вернуть True, если возраст 18..120.
#   1.4. Вернуть True, если корректны все три поля.
#   1.5. Вернуть первую ошибку в порядке:
#        "empty login", "short login", "long login", "space in login",
#        "bad email", "too young", "too old", "ok".

import re


def hw_1_1_login_ok(login: str) -> bool:
    """Вернуть True, если логин корректен."""
    # TODO: реализовать
    pass


def hw_1_2_email_ok(email: str) -> bool:
    """Вернуть True, если email подходит под шаблон."""
    # TODO: реализовать
    pass


def hw_1_3_age_ok(age: int) -> bool:
    """Вернуть True, если 18 <= age <= 120."""
    # TODO: реализовать
    pass


def hw_1_4_all_ok(login: str, email: str, age: int) -> bool:
    """Вернуть True, если все поля корректны."""
    # TODO: реализовать
    pass


def hw_1_5_first_error(login: str, email: str, age: int) -> str:
    """Вернуть текст первой ошибки или 'ok'."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    assert hw_1_1_login_ok("ira") is True
    assert hw_1_1_login_ok("ab") is False
    assert hw_1_1_login_ok("a b c") is False
    assert hw_1_1_login_ok("a" * 21) is False
    assert hw_1_2_email_ok("a@b.ru") is True
    assert hw_1_2_email_ok("a@b") is False
    assert hw_1_2_email_ok("a@b.russia") is False
    assert hw_1_3_age_ok(18) is True
    assert hw_1_3_age_ok(121) is False
    assert hw_1_4_all_ok("ira", "a@b.ru", 20) is True
    assert hw_1_4_all_ok("ira", "a@b", 20) is False
    assert hw_1_5_first_error("", "a@b.ru", 20) == "empty login"
    assert hw_1_5_first_error("ab", "a@b.ru", 20) == "short login"
    assert hw_1_5_first_error("a" * 21, "a@b.ru", 20) == "long login"
    assert hw_1_5_first_error("a b", "a@b.ru", 20) == "space in login"
    assert hw_1_5_first_error("ira", "a@b", 20) == "bad email"
    assert hw_1_5_first_error("ira", "a@b.ru", 17) == "too young"
    assert hw_1_5_first_error("ira", "a@b.ru", 121) == "too old"
    assert hw_1_5_first_error("ira", "a@b.ru", 20) == "ok"

    print("task1 (advanced): все assert-тесты пройдены.")
