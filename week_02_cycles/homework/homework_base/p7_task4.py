"""
Задача 4 (base). Корзина покупок.

Корзина — список цен (числа).

4.1. Добавьте к корзине новую цену price (метод append).
4.2. Удалите первую цену из корзины (метод pop(0)).
4.3. Отсортируйте корзину по возрастанию (метод sort).
4.4. Верните копию корзины (метод copy).
4.5. Верните список цен со скидкой 10% (x * 0.9).
"""


def add_price(cart, price):
    # TODO
    pass


def remove_first(cart):
    # TODO
    pass


def sorted_cart(cart):
    # TODO
    pass


def copy_cart(cart):
    # TODO
    pass


def discounted(cart):
    # TODO
    pass


if __name__ == "__main__":
    assert add_price([100, 200], 300) == [100, 200, 300]
    assert remove_first([100, 200, 300]) == [200, 300]
    assert sorted_cart([300, 100, 200]) == [100, 200, 300]
    assert copy_cart([100, 200]) == [100, 200]
    assert discounted([100, 200]) == [90.0, 180.0]
    print("task4 (base): все тесты пройдены.")
