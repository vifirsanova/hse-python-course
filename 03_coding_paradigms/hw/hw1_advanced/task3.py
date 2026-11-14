# task3.py — Домашняя работа 9, продвинутый уровень.
# Задача 3. Валидатор и парсер банковских транзакций (try/except, raise).


# ============================================================
# Задача 3. Валидатор и парсер банковских транзакций
# ============================================================
# Каждая строка лога транзакций должна иметь формат:
#   "TX_ID;USER;TYPE;AMOUNT"
# например: "101;ira;DEPOSIT;1500.50"
#
# Правила валидации одной строки:
#   - ровно 4 поля при разбиении по ";" -> иначе ValueError("bad format");
#   - TX_ID преобразуется в положительный int (> 0) -> иначе ValueError("bad id");
#   - USER (после strip) не пустой -> иначе ValueError("empty user");
#   - TYPE равен "DEPOSIT" или "WITHDRAW" -> иначе ValueError("bad type");
#   - AMOUNT преобразуется в float и строго > 0 -> иначе ValueError("bad amount").
#
# Подзадачи:
#   3.1. Распарсить одну строку в словарь {"id": int, "user": str, "type": str, "amount": float}
#        или выбросить соответствующий ValueError.
#   3.2. Вернуть текст ошибки ("bad format", "bad id", ..., или "ok") для одной строки.
#   3.3. Обработать список строк lines: вернуть кортеж (valid_txs, errors),
#        где errors — список пар (индекс_строки, текст_ошибки).
#   3.4. По списку валидных транзакций посчитать итоговый баланс каждого пользователя
#        (DEPOSIT увеличивает баланс, WITHDRAW уменьшает).
#   3.5. Применить транзакции по порядку с запретом ухода в минус: если у пользователя
#        недостаточно средств для WITHDRAW, транзакция отклоняется и её id добавляется
#        в список declined_ids. Вернуть (balances, declined_ids).


def hw_3_1_parse_tx(line: str) -> dict:
    """Распарсить и провалидировать строку транзакции или выбросить ValueError."""
    # TODO: реализовать
    pass


def hw_3_2_check_tx(line: str) -> str:
    """Вернуть 'ok' или сообщение первой ошибки ValueError."""
    # TODO: реализовать
    pass


def hw_3_3_parse_batch(lines: list[str]) -> tuple[list[dict], list[tuple[int, str]]]:
    """Разделить пакет строк на валидные транзакции и список ошибок (idx, msg)."""
    # TODO: реализовать
    pass


def hw_3_4_compute_balances(txs: list[dict]) -> dict[str, float]:
    """Посчитать балансы пользователей без ограничения на овердрафт."""
    # TODO: реализовать
    pass


def hw_3_5_apply_no_overdraft(txs: list[dict]) -> tuple[dict[str, float], list[int]]:
    """Применить транзакции без ухода в минус, вернуть (balances, declined_ids)."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    tx = hw_3_1_parse_tx("101;ira;DEPOSIT;1500.5")
    assert tx == {"id": 101, "user": "ira", "type": "DEPOSIT", "amount": 1500.5}

    assert hw_3_2_check_tx("101;ira;DEPOSIT;100") == "ok"
    assert hw_3_2_check_tx("101;ira;DEPOSIT") == "bad format"
    assert hw_3_2_check_tx("abc;ira;DEPOSIT;100") == "bad id"
    assert hw_3_2_check_tx("-5;ira;DEPOSIT;100") == "bad id"
    assert hw_3_2_check_tx("101;  ;DEPOSIT;100") == "empty user"
    assert hw_3_2_check_tx("101;ira;TRANSFER;100") == "bad type"
    assert hw_3_2_check_tx("101;ira;DEPOSIT;-10") == "bad amount"
    assert hw_3_2_check_tx("101;ira;DEPOSIT;nan_str") == "bad amount"

    raw_batch = [
        "1;ira;DEPOSIT;500",
        "bad_line",
        "2;ira;WITHDRAW;200",
        "3;ira;WITHDRAW;400",
        "4;max;DEPOSIT;0",
    ]
    valid, errs = hw_3_3_parse_batch(raw_batch)
    assert len(valid) == 3
    assert errs == [(1, "bad format"), (4, "bad amount")]

    assert hw_3_4_compute_balances(valid) == {"ira": -100.0}
    assert hw_3_5_apply_no_overdraft(valid) == ({"ira": 300.0}, [3])

    print("task3 (hw1_advanced): все assert-тесты пройдены.")
