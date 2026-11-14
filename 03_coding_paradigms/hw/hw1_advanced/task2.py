# task2.py — Домашняя работа 9, продвинутый уровень.
# Задача 2. Конвейер расчёта выплат сотрудникам (функции, *args, **kwargs).


# ============================================================
# Задача 2. Конвейер расчёта выплат сотрудникам
# ============================================================
# Разрабатываем гибкие функции расчёта заработной платы.
#
# Правила:
#   - первые 40 часов оплачиваются по ставке rate, часы свыше 40 —
#     по ставке rate * overtime_mult (по умолчанию 1.5);
#   - функция бонусов принимает базовую сумму и произвольное число премий *bonuses;
#   - функция корректировок принимает сумму gross и именованные коэффициенты
#     надбавок/удержаний: tax (доля налога, по умолчанию 0.13) и любые
#     фиксированные выплаты через **allowances (например, meal=3000, gym=2000),
#     которые прибавляются ПОСЛЕ вычета налога из gross:
#     net = gross * (1 - tax) + sum(allowances.values());
#   - итоговая ведомость по списку записей сотрудников возвращает словарь
#     {имя: итоговая_выплата_округлённая_до_2_знаков}.
#
# Подзадачи:
#   2.1. Посчитать оплату по часам hours, ставке rate и overtime_mult=1.5.
#   2.2. Прибавить к base произвольное количество положительных премий *bonuses
#        (отрицательные числа игнорировать).
#   2.3. Посчитать чистую выплату net по gross, tax=0.13 и **allowances.
#   2.4. Собрать полный расчёт одного сотрудника.
#   2.5. По списку словарей сотрудников вернуть словарь выплат {name: net}.


def hw_2_1_base_pay(hours: float, rate: float, overtime_mult: float = 1.5) -> float:
    """Посчитать базовую оплату с учётом сверхурочных (> 40 ч)."""
    # TODO: реализовать
    pass


def hw_2_2_with_bonuses(base: float, *bonuses: float) -> float:
    """Прибавить к base все положительные премии из *bonuses."""
    # TODO: реализовать
    pass


def hw_2_3_apply_tax_and_allowances(
    gross: float,
    tax: float = 0.13,
    **allowances: float,
) -> float:
    """Посчитать round(gross * (1 - tax) + sum(allowances.values()), 2)."""
    # TODO: реализовать
    pass


def hw_2_4_employee_payout(
    hours: float,
    rate: float,
    *bonuses: float,
    tax: float = 0.13,
    **allowances: float,
) -> float:
    """Полный расчёт выплаты одного сотрудника."""
    # TODO: реализовать
    pass


def hw_2_5_payroll_summary(records: list[dict]) -> dict[str, float]:
    """Построить словарь {name: payout} по списку карточек сотрудников.

    Формат элемента records:
    {"name": str, "hours": float, "rate": float, "bonuses": list[float], "meal": float}
    """
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    assert hw_2_1_base_pay(40, 1000) == 40000.0
    assert hw_2_1_base_pay(45, 1000) == 47500.0
    assert hw_2_1_base_pay(42, 1000, overtime_mult=2.0) == 44000.0

    assert hw_2_2_with_bonuses(40000.0, 5000.0, -100.0, 2000.0) == 47000.0
    assert hw_2_2_with_bonuses(40000.0) == 40000.0

    assert hw_2_3_apply_tax_and_allowances(100000.0) == 87000.0
    assert hw_2_3_apply_tax_and_allowances(100000.0, tax=0.10, meal=3000, gym=2000) == 95000.0

    assert hw_2_4_employee_payout(40, 1000, 10000, tax=0.13, meal=2000) == 45500.0

    staff = [
        {"name": "Ira", "hours": 40, "rate": 1000, "bonuses": [10000], "meal": 2000},
        {"name": "Max", "hours": 42, "rate": 1000, "bonuses": [], "meal": 0},
    ]
    assert hw_2_5_payroll_summary(staff) == {"Ira": 45500.0, "Max": 37410.0}

    print("task2 (hw1_advanced): все assert-тесты пройдены.")
