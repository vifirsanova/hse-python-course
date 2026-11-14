# task1.py — Домашняя работа 9, базовый уровень.
# Задача 1. Учёт товаров на складе (словари).


# ============================================================
# Задача 1. Учёт товаров на складе
# ============================================================
# Склад хранится в словаре stock вида {товар: количество},
# а цены — в словаре prices вида {товар: цена}.
#
# Подзадачи:
#   1.1. Вернуть остаток товара name на складе (или 0, если товара нет).
#   1.2. Обновить копию склада: прибавить delta к товару name
#        (если товара не было — создать запись).
#   1.3. Вернуть отсортированный список товаров, у которых остаток равен 0.
#   1.4. Посчитать общую стоимость всех товаров на складе по словарю prices
#        (если цены товара нет в prices, считать её равной 0).
#   1.5. Проверить, хватит ли остатков на складе для выполнения заказа
#        order вида {товар: нужное_количество}.


def hw_1_1_get_qty(stock: dict[str, int], name: str) -> int:
    """Вернуть количество товара name или 0, если его нет."""
    # TODO: реализовать
    pass


def hw_1_2_add_stock(stock: dict[str, int], name: str, delta: int) -> dict[str, int]:
    """Вернуть копию словаря stock с увеличенным на delta остатком name."""
    # TODO: реализовать
    pass


def hw_1_3_out_of_stock(stock: dict[str, int]) -> list[str]:
    """Вернуть отсортированный список товаров с нулевым остатком."""
    # TODO: реализовать
    pass


def hw_1_4_total_value(stock: dict[str, int], prices: dict[str, float]) -> float:
    """Вернуть суммарную стоимость товаров на складе."""
    # TODO: реализовать
    pass


def hw_1_5_can_fulfill(stock: dict[str, int], order: dict[str, int]) -> bool:
    """Вернуть True, если каждого товара из order хватает в stock."""
    # TODO: реализовать
    pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    sample_stock = {"pen": 10, "book": 0, "bag": 3, "ruler": 0}
    sample_prices = {"pen": 50.0, "book": 400.0, "bag": 1200.0}

    assert hw_1_1_get_qty(sample_stock, "pen") == 10
    assert hw_1_1_get_qty(sample_stock, "laptop") == 0

    updated = hw_1_2_add_stock(sample_stock, "pen", 5)
    assert updated["pen"] == 15
    assert sample_stock["pen"] == 10
    assert hw_1_2_add_stock(sample_stock, "pencil", 4)["pencil"] == 4

    assert hw_1_3_out_of_stock(sample_stock) == ["book", "ruler"]
    assert hw_1_4_total_value(sample_stock, sample_prices) == 4100.0

    assert hw_1_5_can_fulfill(sample_stock, {"pen": 5, "bag": 3}) is True
    assert hw_1_5_can_fulfill(sample_stock, {"pen": 5, "bag": 4}) is False
    assert hw_1_5_can_fulfill(sample_stock, {"laptop": 1}) is False

    print("task1 (hw1_basic): все assert-тесты пройдены.")
