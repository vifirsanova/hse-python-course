# task1.py — Домашняя работа 10, продвинутый уровень.
# Задача 1. Система управления библиотекой (ООП: Book и Library).


# ============================================================
# Задача 1. Система управления библиотекой
# ============================================================
# Проектируем два взаимодействующих класса: Book и Library.
#
# Правила для Book(title, author, year, genre):
#   - если year < 1450 или year > 2100 -> выбросить ValueError("bad year");
#   - атрибут self.is_borrowed изначально равен False;
#   - __str__() возвращает "<title> — <author> (<year>)".
#
# Правила для Library():
#   - хранит список книг self.books = [];
#   - add_book(book) добавляет экземпляр Book;
#   - find_by_author(author) возвращает список книг, где автор совпадает
#     без учёта регистра;
#   - borrow(title) находит первую книгу с данным названием: если книги нет —
#     выбрасывает LookupError("not found"); если уже выдана —
#     выбрасывает ValueError("already borrowed"); иначе ставит is_borrowed = True;
#   - return_book(title) снимает флаг is_borrowed = False (если книги нет —
#     LookupError("not found"));
#   - available_by_genre() возвращает словарь {genre: число_доступных_книг}
#     (только книги с is_borrowed == False и только жанры, где >= 1 доступной книги).


class Book:
    def __init__(self, title: str, author: str, year: int, genre: str):
        # TODO: реализовать
        pass

    def __str__(self) -> str:
        # TODO: реализовать
        pass


class Library:
    def __init__(self):
        # TODO: реализовать
        pass

    def add_book(self, book: Book) -> None:
        """Добавить книгу в фонд библиотеки."""
        # TODO: реализовать
        pass

    def find_by_author(self, author: str) -> list[Book]:
        """Вернуть список книг указанного автора (без учёта регистра)."""
        # TODO: реализовать
        pass

    def borrow(self, title: str) -> Book:
        """Выдать книгу по названию или выбросить LookupError / ValueError."""
        # TODO: реализовать
        pass

    def return_book(self, title: str) -> None:
        """Вернуть книгу в библиотеку или выбросить LookupError."""
        # TODO: реализовать
        pass

    def available_by_genre(self) -> dict[str, int]:
        """Вернуть словарь {genre: количество доступных книг}."""
        # TODO: реализовать
        pass


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    b1 = Book("Clean Code", "Robert Martin", 2008, "CS")
    b2 = Book("Fluent Python", "Luciano Ramalho", 2022, "CS")
    b3 = Book("Dune", "Frank Herbert", 1965, "Sci-Fi")
    assert str(b1) == "Clean Code — Robert Martin (2008)"
    assert b1.is_borrowed is False

    try:
        Book("Ancient", "Anon", 1200, "History")
        assert False, "Ожидалось исключение ValueError"
    except ValueError:
        pass

    lib = Library()
    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(b3)

    assert len(lib.find_by_author("robert martin")) == 1
    assert lib.available_by_genre() == {"CS": 2, "Sci-Fi": 1}

    lib.borrow("Dune")
    assert b3.is_borrowed is True
    assert lib.available_by_genre() == {"CS": 2}

    try:
        lib.borrow("Dune")
        assert False, "Повторная выдача должна вызывать ValueError"
    except ValueError:
        pass

    try:
        lib.borrow("Unknown")
        assert False, "Неизвестная книга должна вызывать LookupError"
    except LookupError:
        pass

    lib.return_book("Dune")
    assert b3.is_borrowed is False
    assert lib.available_by_genre() == {"CS": 2, "Sci-Fi": 1}

    print("task1 (hw2_advanced): все assert-тесты пройдены.")
