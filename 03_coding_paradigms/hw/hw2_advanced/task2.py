# task2.py — Домашняя работа 10, продвинутый уровень.
# Задача 2. Продвинутая аналитика заказов e-commerce в pandas.


# ============================================================
# Задача 2. Продвинутая аналитика заказов e-commerce в pandas
# ============================================================
# Дана таблица заказов df со столбцами:
#   "order_id" (int), "city" (str), "category" (str),
#   "price" (float), "qty" (int), "discount" (float с пропусками NaN),
#   "status" (str: "paid", "cancelled", "refunded").
#
# Подзадачи:
#   2.1. Вернуть копию df, где пропуски в "discount" заменены на 0.0,
#        и добавлен столбец "net" = price * qty * (1 - discount / 100).
#   2.2. Из подготовленной таблицы оставить только заказы со статусом "paid"
#        из списка городов allowed_cities и с net >= min_net.
#   2.3. По оплаченным заказам ("paid") построить сводную таблицу по "category"
#        со столбцами ["orders", "total_net", "avg_net"] (число заказов, сумма и
#        среднее по "net", округлённые до 2 знаков), отсортированную по убыванию
#        "total_net".
#   2.4. Посчитать долю каждого города в общей оплаченной выручке в процентах
#        (round(..., 2)) и вернуть словарь {city: share_percent}.
#   2.5. Найти категорию с наибольшей долей отменённых заказов
#        (доля строк со status == "cancelled" внутри категории).

import pandas as pd


def hw_2_1_prepare_orders(df: pd.DataFrame) -> pd.DataFrame:
    """Заполнить NaN в 'discount' нулями и добавить столбец 'net'."""
    # TODO: реализовать
    pass


def hw_2_2_filter_paid(
    df: pd.DataFrame,
    allowed_cities: list[str],
    min_net: float,
) -> pd.DataFrame:
    """Оставить оплаченные заказы в allowed_cities с net >= min_net."""
    # TODO: реализовать
    pass


def hw_2_3_category_report(df: pd.DataFrame) -> pd.DataFrame:
    """Сформировать сводку по категориям для оплаченных заказов."""
    # TODO: реализовать
    pass


def hw_2_4_city_revenue_share(df: pd.DataFrame) -> dict[str, float]:
    """Вернуть словарь {city: процент от оплаченной выручки}."""
    # TODO: реализовать
    pass


def hw_2_5_worst_cancel_category(df: pd.DataFrame) -> str:
    """Вернуть категорию с максимальной долей заказов со статусом 'cancelled'."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    raw_df = pd.DataFrame({
        "order_id": [1, 2, 3, 4, 5],
        "city": ["Berlin", "Berlin", "Munich", "Munich", "Hamburg"],
        "category": ["Books", "Tech", "Tech", "Books", "Books"],
        "price": [500.0, 1000.0, 2000.0, 400.0, 300.0],
        "qty": [2, 1, 1, 1, 1],
        "discount": [None, 10.0, 25.0, 0.0, None],
        "status": ["paid", "paid", "paid", "cancelled", "cancelled"],
    })

    prep = hw_2_1_prepare_orders(raw_df)
    assert list(prep["net"]) == [1000.0, 900.0, 1500.0, 400.0, 300.0]

    filt = hw_2_2_filter_paid(prep, ["Berlin", "Munich"], 950.0)
    assert list(filt["order_id"]) == [1, 3]

    rep = hw_2_3_category_report(prep)
    assert list(rep.columns) == ["orders", "total_net", "avg_net"]
    assert list(rep.index) == ["Tech", "Books"]
    assert float(rep.loc["Tech", "total_net"]) == 2400.0

    shares = hw_2_4_city_revenue_share(prep)
    assert shares == {"Berlin": 55.88, "Munich": 44.12}

    assert hw_2_5_worst_cancel_category(prep) == "Books"

    print("task2 (hw2_advanced): все assert-тесты пройдены.")
