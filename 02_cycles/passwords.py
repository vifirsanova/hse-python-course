"""
Password Checks — 5 задач на проверку пароля.

Базовый шаблон: перебор элементов - проверка условия -
True при первом совпадении, иначе False после цикла.

Документация:
- len(): https://docs.python.org/3/library/functions.html#len
- str.islower(): https://docs.python.org/3/library/stdtypes.html#str.islower
- str.isspace(): https://docs.python.org/3/library/stdtypes.html#str.isspace
- str.isalnum(): https://docs.python.org/3/library/stdtypes.html#str.isalnum
- str.isdigit(): https://docs.python.org/3/library/stdtypes.html#str.isdigit
- Индексация строк: https://docs.python.org/3/tutorial/introduction.html#strings

Запуск тестов:  python password_checks.py
"""


def is_long_enough(password, min_length=8):
    """True, если длина пароля >= min_length, иначе False.

    См.: https://docs.python.org/3/library/functions.html#len
    """
    pass


def has_lowercase(password):
    """True, если есть хотя бы одна строчная буква, иначе False.

    См.: https://docs.python.org/3/library/stdtypes.html#str.islower
    """
    pass


def has_no_spaces(password):
    """True, если нет пробельных символов, иначе False.

    См.: https://docs.python.org/3/library/stdtypes.html#str.isspace
    """
    pass


def is_alphanumeric(password):
    """True, если каждый символ — буква или цифра. Пустая строка валидна.

    См.: https://docs.python.org/3/library/stdtypes.html#str.isalnum
    """
    pass


def starts_not_with_digit(password):
    """True, если пароль пустой или первый символ не цифра.

    См.:
    - https://docs.python.org/3/library/stdtypes.html#str.isdigit
    - https://docs.python.org/3/tutorial/introduction.html#strings
    """
    pass


CASES = {
    "is_long_enough": {
        "func": is_long_enough,
        "cases": [
            (("abcdefgh",), True),
            (("abcdefg",), False),
            (("abcdefg", 5), True),
            (("", 1), False),
            (("abc", 3), True),
        ],
    },
    "has_lowercase": {
        "func": has_lowercase,
        "cases": [
            (("HELLOworld",), True),
            (("HELLOWORLD",), False),
            (("12345",), False),
            (("a",), True),
            (("",), False),
        ],
    },
    "has_no_spaces": {
        "func": has_no_spaces,
        "cases": [
            (("NoSpaces123",), True),
            (("Has Space",), False),
            (("Tab\there",), False),
            (("New\nline",), False),
            (("",), True),
        ],
    },
    "is_alphanumeric": {
        "func": is_alphanumeric,
        "cases": [
            (("abc123",), True),
            (("abc 123",), False),
            (("abc!",), False),
            (("",), True),
            (("ABC",), True),
            (("_",), False),
        ],
    },
    "starts_not_with_digit": {
        "func": starts_not_with_digit,
        "cases": [
            (("abc123",), True),
            (("1abc",), False),
            (("!abc",), True),
            (("",), True),
            (("9",), False),
        ],
    },
}


def run_tests():
    total = passed = 0
    for name, block in CASES.items():
        print(f"\n--- {name} ---")
        for args, expected in block["cases"]:
            total += 1
            try:
                result = block["func"](*args)
            except Exception as e:
                print(f"  FAIL {args}: исключение {e!r}")
                continue
            if result == expected:
                passed += 1
                print(f"  OK   {args} -> {result}")
            else:
                print(f"  FAIL {args}: получено {result!r}, ожидалось {expected!r}")
    print(f"\nИтог: {passed}/{total} тестов пройдено")
    return passed == total


if __name__ == "__main__":
    import sys
    ok = run_tests()
    sys.exit(0 if ok else 1)
