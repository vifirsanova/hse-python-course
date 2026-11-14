# task1.py — Домашняя работа 10, базовый уровень.
# Задача 1. Карточка позиции и корзина покупателя (простые классы ООП).


# ============================================================
# Задача 1. Карточка позиции и корзина покупателя
# ============================================================
# Моделируем корзину онлайн-магазина с помощью двух простых классов.
#
# Подзадачи:
#   1.1. В классе CartItem(name, price, qty=1) сохранить атрибуты
#        self.name, self.price, self.qty.
#   1.2. В CartItem реализовать метод subtotal(), возвращающий price * qty,
#        и метод __str__(), возвращающий строку "<name> x<qty> = <subtotal>".
#   1.3. В классе Cart() инициализировать пустой список позиций self.items = []
#        и метод add_item(item: CartItem).
#   1.4. В Cart реализовать метод total_units() (сумма qty всех позиций)
#        и метод total_cost() (сумма subtotal() всех позиций).
#   1.5. В Cart реализовать метод clear(), очищающий корзину.


class CartItem:
    def __init__(self, name: str, price: float, qty: int = 1):
        # TODO: реализовать (подзадача 1.1)
        pass

    def subtotal(self) -> float:
        """Вернуть стоимость позиции price * qty."""
        # TODO: реализовать (подзадача 1.2)
        pass

    def __str__(self) -> str:
        """Вернуть строку '<name> x<qty> = <subtotal>'."""
        # TODO: реализовать (подзадача 1.2)
        pass


class Cart:
    def __init__(self):
        # TODO: реализовать (подзадача 1.3)
        pass

    def add_item(self, item: CartItem) -> None:
        """Добавить позицию item в корзину."""
        # TODO: реализовать (подзадача 1.3)
        pass

    def total_units(self) -> int:
        """Вернуть общее число единиц товаров в корзине."""
        # TODO: реализовать (подзадача 1.4)
        pass

    def total_cost(self) -> float:
        """Вернуть общую стоимость корзины."""
        # TODO: реализовать (подзадача 1.4)
        pass

    def clear(self) -> None:
        """Очистить список позиций корзины."""
        # TODO: реализовать (подзадача 1.5)
        pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    p1 = CartItem("Pen", 50.0, 3)
    p2 = CartItem("Book", 400.0)
    assert p1.subtotal() == 150.0
    assert p2.qty == 1 and p2.subtotal() == 400.0
    assert str(p1) == "Pen x3 = 150.0"

    cart = Cart()
    assert cart.total_units() == 0 and cart.total_cost() == 0.0
    cart.add_item(p1)
    cart.add_item(p2)
    assert cart.total_units() == 4
    assert cart.total_cost() == 550.0

    c_other = Cart()
    assert c_other.total_units() == 0  # проверка отсутствия общего списка!

    cart.clear()
    assert cart.total_units() == 0 and cart.total_cost() == 0.0

    print("task1 (hw2_basic): все assert-тесты пройдены.")
