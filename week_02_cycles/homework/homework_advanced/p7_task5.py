"""
Задача 5 (advanced). Таблица оценок: аналитика по студентам.

Таблица — список списков: строки — студенты, столбцы — оценки.
Имена студентов — отдельный список names той же длины.

5.1. Верните плоский список всех оценок.
5.2. Верните список средних оценок по студентам.
5.3. Верните список имён студентов со средним >= 4.5.
5.4. Верните dict: {имя: средняя оценка}.
5.5. Верните список имён студентов, отсортированных
     по средней оценке по убыванию.
"""


def flat(grades):
    # TODO
    pass


def averages(grades):
    # TODO
    pass


def top_students(names, grades):
    # TODO
    pass


def name_to_average(names, grades):
    # TODO
    pass


def sorted_names(names, grades):
    # TODO
    pass


if __name__ == "__main__":
    names = ["Ann", "Bob", "Cara"]
    grades = [[5, 5, 4], [3, 3, 4], [5, 5, 5]]
    assert flat(grades) == [5, 5, 4, 3, 3, 4, 5, 5, 5]
    assert averages(grades) == [14 / 3, 10 / 3, 5.0]
    assert top_students(names, grades) == ["Cara"]
    assert name_to_average(names, grades) == {
        "Ann": 14 / 3,
        "Bob": 10 / 3,
        "Cara": 5.0,
    }
    assert sorted_names(names, grades) == ["Cara", "Ann", "Bob"]
    print("task5 (advanced): все тесты пройдены.")
