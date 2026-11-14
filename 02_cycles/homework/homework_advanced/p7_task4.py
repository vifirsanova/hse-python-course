"""
Задача 4 (advanced). Корзина с категориями.

Корзина — список кортежей (название, цена, количество).

4.1. Верните список названий товаров.
4.2. Верните общую стоимость корзины (цена * количество).
4.3. Верните список товаров дороже 100 (по цене за штуку).
4.4. Верните список кортежей (название, стоимость позиции),
     отсортированных по стоимости по убыванию.
4.5. Верните dict: {название: стоимость позиции}.
"""


def names(cart):
    # TODO
    pass


def total(cart):
    # TODO
    pass


def expensive(cart):
    # TODO
    pass


def sorted_by_position_cost(cart):
    # TODO
    pass


def position_costs(cart):
    # TODO
    pass


if __name__ == "__main__":
    cart = [("apple", 50, 2), ("laptop", 1000, 1), ("pen", 10, 5)]
    assert names(cart) == ["apple", "laptop", "pen"]
    assert total(cart) == 50 * 2 + 1000 * 1 + 10 * 5
    assert expensive(cart) == [("laptop", 1000, 1)]
    assert sorted_by_position_cost(cart) == [
        ("laptop", 1000),
        ("apple", 100),
        ("pen", 50),
    ]
    assert position_costs(cart) == {
        "apple": 100,
        "laptop": 1000,
        "pen": 50,
    }
    print("task4 (advanced): все тесты пройдены.")
