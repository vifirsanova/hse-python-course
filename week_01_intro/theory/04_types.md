## Типы данных

| Тип | Описание |
|-----|----------|
| `int` | целые числа |
| `float` | вещественные числа |
| `str` | строки |
| `bool` | логический тип |

Динамическая типизация: тип определяется значением.

## int

```python
a = 10
b = -7
big = 10 ** 100
```

Особенности:
- размер не ограничен;
- `/` всегда даёт `float`;
- `//` — целочисленное деление;
- `%` — остаток;
- `**` — возведение в степень.

## float

```python
pi = 3.14
sci = 1.5e3  # 1500.0
```

Особенности:
- IEEE 754;
- погрешность: `0.1 + 0.2 != 0.3`;
- `inf`, `-inf`, `nan`;
- `/` — всегда `float`.

Для точных вычислений — `decimal` или `fractions`.

### decimal

```python
from decimal import Decimal, ROUND_HALF_UP

price = Decimal('19.99')
tax = Decimal('0.13')
total = price * (1 + tax)
res = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
```

### fractions

```python
from fractions import Fraction

f1 = Fraction(1, 3)
f2 = Fraction(1, 6)
print(f1 + f2)  # 1/2
```

## str

```python
s1 = 'hello'
s2 = "world"
```

Методы:

```python
"Hi".upper()       # "HI"
" a b ".strip()    # "a b"
"a,b,c".split(",") # ["a", "b", "c"]
"-".join(["a","b"])# "a-b"
```

Операции:

```python
"ab" + "cd"  # "abcd"
"ab" * 3     # "ababab"
len("hello") # 5
"hello"[0]   # "h"
```

Строки неизменяемы.

## bool

```python
True and False  # False
True or False   # True
not True        # False
```

Приведение:

```python
bool(0)     # False
bool(42)    # True
bool("")    # False
bool("abc") # True
```

`bool` — подкласс `int`: `True == 1`.

## Преобразование типов

```python
int("42")      # 42
int(3.99)      # 3
float("3.14")  # 3.14
str(42)        # "42"
```

Неявное:

```python
1 + 2.5  # 3.5
"a" + 1  # TypeError
```

`int("abc")` → `ValueError`.

## Ввод: input()

```python
name = input("What's your name? ")
age = int(input("Age: "))
```

`input()` всегда возвращает `str`.

## Вывод: print()

```python
print("Sum:", a + b)
print(f"Sum: {a + b}")
print("a", "b", sep="-", end="!\n")
```

## Форматирование

```python
f"{value:>10.2f}"  # выравнивание вправо, 2 знака
f"{value:.2f}"     # 2 знака
```
