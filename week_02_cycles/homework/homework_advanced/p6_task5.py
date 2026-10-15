# task5.py — Домашняя работа 6, продвинутый уровень.
# Задача 5. Парсер и валидатор конфигурации.


# ============================================================
# Задача 5. Парсер и валидатор конфигурации
# ============================================================
# На вход приходит строка с настройками вида "k=v;k=v;...".
# Например: "host=localhost;port=8080;debug=true".
#
# Подзадачи:
#   5.1. Вернуть список ключей.
#   5.2. Вернуть список значений.
#   5.3. Вернуть True, если все значения непустые.
#   5.4. Вернуть True, если все ключи — только латинские буквы/цифры.
#   5.5. Вернуть True, если строка содержит хотя бы одну цифру.
#   5.6. Вернуть True, если есть ключ "port" и его значение — число
#        (re.fullmatch \d+).
#   5.7. Вернуть True, если есть ключ "host" и его значение
#        непустое и без пробелов.
#   5.8. Вернуть словарь {key: value} для всех пар
#        (предполагая корректный ввод).

import re


def hw_5_1_keys(data: str) -> list[str]:
    """Вернуть список ключей."""
    # TODO: реализовать
    pass


def hw_5_2_values(data: str) -> list[str]:
    """Вернуть список значений."""
    # TODO: реализовать
    pass


def hw_5_3_all_nonempty(data: str) -> bool:
    """Вернуть True, если все значения непустые."""
    # TODO: реализовать
    pass


def hw_5_4_keys_latin(data: str) -> bool:
    """Вернуть True, если все ключи — только латинские буквы/цифры."""
    # TODO: реализовать
    pass


def hw_5_5_has_digit(data: str) -> bool:
    """Вернуть True, если есть хотя бы одна цифра."""
    # TODO: реализовать
    pass


def hw_5_6_port_ok(data: str) -> bool:
    """Вернуть True, если port задан числом."""
    # TODO: реализовать
    pass


def hw_5_7_host_ok(data: str) -> bool:
    """Вернуть True, если host непустой и без пробелов."""
    # TODO: реализовать
    pass


def hw_5_8_to_dict(data: str) -> dict[str, str]:
    """Вернуть словарь пар ключ=значение."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    data = "host=localhost;port=8080;debug=true"
    assert hw_5_1_keys(data) == ["host", "port", "debug"]
    assert hw_5_2_values(data) == ["localhost", "8080", "true"]
    assert hw_5_3_all_nonempty(data) is True
    assert hw_5_3_all_nonempty("host=;port=8080") is False
    assert hw_5_4_keys_latin(data) is True
    assert hw_5_4_keys_latin("хост=localhost") is False
    assert hw_5_5_has_digit(data) is True
    assert hw_5_5_has_digit("host=localhost;debug=true") is False
    assert hw_5_6_port_ok(data) is True
    assert hw_5_6_port_ok("host=localhost;port=abc") is False
    assert hw_5_6_port_ok("host=localhost") is False
    assert hw_5_7_host_ok(data) is True
    assert hw_5_7_host_ok("host=;port=8080") is False
    assert hw_5_7_host_ok("host=local host;port=8080") is False
    assert hw_5_8_to_dict(data) == {
        "host": "localhost",
        "port": "8080",
        "debug": "true",
    }

    print("task5 (advanced): все assert-тесты пройдены.")
