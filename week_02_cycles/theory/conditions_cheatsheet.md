# Шпаргалка: сравнения, логика, if/elif/else, строки, regex

## 1. Операторы сравнения

### Шесть операторов
```python
1 == 1   # True
1 != 2   # True
3 > 2    # True
3 < 2    # False
3 >= 3   # True
3 <= 2   # False
```

### Результат — всегда bool
```python
x = 5
type(x > 0)      # <class 'bool'>
```

### = и ==
```python
x = 5      # присваивание
x == 5     # сравнение
```

### Сравнение строк
```python
"abc" == "abc"   # True
"abc" < "abd"    # True
"a" < "ab"       # True (префикс меньше)
"apple" < "Apple" # False: 'a' (97) > 'A' (65)
```
Лексикографический порядок — по кодам символов. **[A]**

### Цепочки сравнений
```python
x = 5
0 < x < 10       # True
0 < x < 3        # False
# эквивалентно 0 < x and x < 10
```

### int и float
```python
1 == 1.0             # True
0.1 + 0.2 == 0.3     # False
0.1 + 0.2            # 0.30000000000000004
```

### Сравнение float через math.isclose
```python
import math
math.isclose(0.1 + 0.2, 0.3)   # True
```

---

## 2. Логические операторы

### and, or, not
```python
True and False   # False
True or False    # True
not True         # False
not False        # True
```

### Приоритет
`not` > `and` > `or`
```python
not True or True and False
# (not True) or (True and False)
# False or False -> False
```

### Таблицы истинности
| A | B | A and B | A or B |
|---|---|---------|--------|
| T | T | T | T |
| T | F | F | T |
| F | T | F | T |
| F | F | F | F |

| A | not A |
|---|-------|
| T | F |
| F | T |

### Ленивые вычисления
```python
x = 0
x != 0 and 10 / x > 1   # False, деления нет
# and: если слева False — правый не вычисляется
# or:  если слева True  — правый не вычисляется
```

### Возвращают не bool, а операнд
```python
0 or "default"    # "default"
"a" and "b"       # "b"
"" or 0 or None   # None
0 and 10 / 0      # 0 (деления не будет)
```

### Значение по умолчанию
```python
name = input("Name: ") or "guest"
port = config.get("port") or 8080
```

---

## 3. if / elif / else

### Базовый if
```python
x = 10
if x > 0:
    print("positive")
```
Двоеточие и отступ обязательны.

### Отступы
```python
if x > 0:
    print("a")
    print("b")
print("always")     # вне if
```
4 пробела на уровень. Смешивать табы и пробелы нельзя.

### if / else
```python
if x >= 0:
    print("non-negative")
else:
    print("negative")
```

### if / elif / else
```python
score = 75
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"
```
Срабатывает первая истинная проверка. **[B]**

### Порядок важен
```python
# Плохо: B никогда не сработает
if score >= 60: ...
elif score >= 90: ...
```

### Тернарный оператор
```python
label = "even" if x % 2 == 0 else "odd"
```
Использовать для простых случаев.

---

## 4. Вложенные условия

### Пример
```python
x = 12
if x > 0:
    if x % 2 == 0:
        print("positive even")
    else:
        print("positive odd")
else:
    print("non-positive")
```

### Через and / elif
```python
if x > 0 and x % 2 == 0:
    print("positive even")
elif x > 0:
    print("positive odd")
else:
    print("non-positive")
```

### Не углубляться
Больше 2–3 уровней — читать тяжело. Заменяйте на `and`.

### Классификация
```python
if n == 0:
    kind = "zero"
elif n > 0:
    kind = "positive"
else:
    kind = "negative"
```

---

## 5. Строки

### Индексы и срезы
```python
s = "python"
s[0]      # 'p'
s[-1]     # 'n'
s[1:4]    # 'yth'
s[:3]     # 'pyt'
s[3:]     # 'hon'
s[::-1]   # 'nohtyp'
```
Строки **неизменяемы**:
```python
s[0] = "P"        # TypeError
s = "P" + s[1:]   # ОК
```

### Длина и проверки
```python
len("abc")                  # 3
"a" in "cat"                # True
"x" not in "cat"            # True
"abc".startswith("ab")      # True
"abc".endswith("bc")        # True
```

### Методы
| Метод | Действие |
|-------|----------|
| `upper()` | в верхний регистр |
| `lower()` | в нижний регистр |
| `strip()` | убрать пробелы по краям |
| `replace(a, b)` | заменить |
| `split(sep)` | разбить в список |
| `join(iter)` | склеить |
| `find(x)` | индекс первого вхождения (-1) |
| `count(x)` | число вхождений |

```python
"Hi".upper()                 # "HI"
"Hi".lower()                 # "hi"
" a b ".strip()              # "a b"
"a b".replace(" ", "_")      # "a_b"
"a,b,c".split(",")           # ['a', 'b', 'c']
"-".join(["a", "b"])         # "a-b"
"abc".find("b")              # 1
"abc".count("a")             # 1
```

### split без аргумента
```python
"a  b   c".split()      # ['a', 'b', 'c']
"a  b   c".split(" ")   # ['a', '', 'b', '', '', 'c']
```

### Проверки содержимого
```python
"123".isdigit()   # True
"abc".isalpha()   # True
"a1".isalnum()    # True
" ".isspace()     # True
```

### f-строки
```python
name = "Ira"
age = 20
f"{name}: {age}"          # "Ira: 20"
f"{3.14159:.2f}"          # "3.14"
f"{42:>10}"               # "        42"
```

---

## 6. Регулярные выражения

### Импорт и raw-строки
```python
import re
r"\d+"     # raw: \d не интерпретируется Python
"\d+"      # \d — обычный символ, DeprecationWarning
```

### Метасимволы
| Шаблон | Значение |
|--------|----------|
| `.` | любой символ (кроме \n) |
| `\d` | цифра |
| `\w` | буква/цифра/_ |
| `\s` | пробел |
| `^` | начало строки |
| `$` | конец строки |

### Квантификаторы
| Шаблон | Значение |
|--------|----------|
| `*` | 0 или больше |
| `+` | 1 или больше |
| `?` | 0 или 1 |
| `{n}` | ровно n |
| `{n,m}` | от n до m |

### Классы символов
```python
[abc]        # a, b или c
[a-z]        # любая строчная латинская
[^0-9]       # НЕ цифра
(A|B)        # A или B
```

### Основные функции
```python
re.search(r"\d+", "abc 123")     # <Match '123'>
re.match(r"\d+", "123 abc")      # <Match '123'> (с начала)
re.fullmatch(r"\d+", "123")      # <Match '123'> (вся строка)

re.findall(r"\d+", "a1b22")      # ['1', '22']
re.sub(r"\d+", "#", "a1b22")     # 'a#b#'
re.split(r"\s+", "a  b c")       # ['a', 'b', 'c']
```

### match vs search vs fullmatch
- `match` — с начала строки.
- `search` — в любом месте.
- `fullmatch` — вся строка целиком.

### Примеры шаблонов
```python
re.fullmatch(r"\d{4}", "2026")                # год
re.fullmatch(r"\+7\d{10}", "+79161234567")    # телефон
re.fullmatch(r"\w+@\w+\.\w+", "a@b.ru")       # email
re.fullmatch(r"\d{4}-\d{2}-\d{2}", "2026-10-05")
```

### Извлечение числа
```python
m = re.search(r"\d+", "Price: 1500 RUB")
if m:
    print(int(m.group()))    # 1500
```

### Все числа сразу
```python
nums = re.findall(r"\d+", "a1b22c333")   # ['1', '22', '333']
total = sum(int(x) for x in nums)        # 356
```

---

## 7. Шаблоны

```python
# Положительное и чётное
x > 0 and x % 2 == 0

# Диапазон включительно
1 <= x <= 100

# Високосный год
y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

# Значение по умолчанию
name = input() or "guest"

# Классификация числа
if n == 0:
    kind = "zero"
elif n > 0:
    kind = "positive"
else:
    kind = "negative"

# Разбор лога
level, msg = line.split(":", 1)
level = level.upper()
msg = msg.lower()

# Проверка даты
re.fullmatch(r"\d{4}-\d{2}-\d{2}", s) is not None

# Сумма чисел в строке
sum(int(x) for x in re.findall(r"\d+", s))

# Убрать пробелы и в верхний регистр
s.strip().upper()

# Палиндром без учёта регистра
t = s.lower()
t == t[::-1]

# Нормализация "LEVEL:msg"
lvl, msg = line.split(":", 1)
f"{lvl.upper()}:{msg.lower()}"
```
