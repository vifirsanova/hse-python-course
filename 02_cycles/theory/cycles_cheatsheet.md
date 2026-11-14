# Шпаргалка: for, range, списки, методы, вложенность, comprehension

## 1. Цикл for и range

### Синтаксис
```python
for i in range(3):      # 0 1 2
    print(i)

for ch in "abc":        # a b c
    print(ch)
```

### range
```python
range(5)         # 0 1 2 3 4
range(2, 6)      # 2 3 4 5
range(0, 10, 2)  # 0 2 4 6 8
range(5, 0, -1)  # 5 4 3 2 1  **[A]**
```
Правая граница **не включается**.

### Накопление
```python
total = 0
for i in range(1, 6):
    total += i          # 15
```

### break и continue
```python
for i in range(10):
    if i == 3:
        break           # 0 1 2
    print(i)

for i in range(5):
    if i % 2 == 0:
        continue        # 1 3
    print(i)
```

### Аккумулятор-список (снапшоты)
```python
snapshots = []
value = 0
for d in [1, 2, -1, 3]:
    value += d
    snapshots.append(value)
# [1, 3, 2, 5]
```

---

## 2. Списки

### Создание и индексы
```python
nums = [1, 2, 3]
empty = []
mixed = [1, "a", True]

nums[0]     # 1
nums[-1]    # 3
len(nums)   # 3
```

### Изменение
```python
nums = [1, 2, 3]
nums[0] = 10        # [10, 2, 3]
```
Списки **изменяемы**, строки — нет.

### Срезы 
```python
nums = [0, 1, 2, 3, 4]
nums[1:3]   # [1, 2]
nums[:2]    # [0, 1]
nums[3:]    # [3, 4]
nums[::-1]  # [4, 3, 2, 1, 0]
```
Срез создаёт **новый** список.

### Срез с шагом
```python
nums[::2]   # [0, 2, 4]
nums[1::2]  # [1, 3]
```

### Перебор
```python
for x in [10, 20, 30]:
    print(x)

for i in range(len(nums)):
    print(i, nums[i])
```

### Ссылка vs копия
```python
a = [1, 2, 3]
b = a               # b — та же ссылка
b[0] = 99
print(a)            # [99, 2, 3]

c = a.copy()        # независимая копия
d = a[:]            # тоже копия
```

---

## 3. Методы списков

| Метод | Действие | Уровень |
|-------|----------|---------|
| `append(x)` | добавить `x` в конец | B |
| `insert(i, x)` | вставить `x` на позицию `i` | B |
| `extend(iter)` | добавить все элементы | B |
| `remove(x)` | удалить первое вхождение `x` | B |
| `pop([i])` | удалить и вернуть элемент | B |
| `clear()` | очистить список | B |
| `index(x)` | индекс первого вхождения | B |
| `count(x)` | сколько раз встречается | B |
| `sort()` | отсортировать на месте | B |
| `reverse()` | развернуть на месте | B |
| `copy()` | поверхностная копия | B |

```python
nums = [1, 2]
nums.append(3)          # [1, 2, 3]
nums.insert(0, 0)       # [0, 1, 2, 3]
nums.extend([4, 5])     # [0, 1, 2, 3, 4, 5]
nums.remove(0)          # [1, 2, 3, 4, 5]
last = nums.pop()       # last = 5, nums = [1, 2, 3, 4]
nums.sort()             # сортировка на месте
nums.reverse()          # разворот на месте
b = nums.copy()         # копия
```

### Важно
- `sort()` меняет список и возвращает `None`; `sorted()` возвращает новый. **[B]**
- `append`, `sort`, `reverse` возвращают `None`. **[B]**
- `b = a` — ссылка, для копии: `a.copy()` или `a[:]`. **[A]**

```python
nums = [3, 1, 2]
new = sorted(nums)      # [1, 2, 3], nums не изменился
nums.sort()             # nums = [1, 2, 3]
```

### sort с key
```python
words = ["bb", "a", "ccc"]
words.sort(key=len)                 # ['a', 'bb', 'ccc']
words.sort(key=len, reverse=True)   # ['ccc', 'bb', 'a']

pairs = [(1, "b"), (2, "a")]
pairs.sort(key=lambda p: p[1])      # [(2, 'a'), (1, 'b')]
```

### Удаление всех вхождений 
```python
nums = [2, 1, 2, 3, 2]
while 2 in nums:
    nums.remove(2)
# [1, 3]
```

---

## 4. Вложенные циклы и списки

### Вложенные циклы 
```python
for i in range(2):
    for j in range(3):
        print(i, j)
# 0 0, 0 1, 0 2, 1 0, 1 1, 1 2
```
Внешний цикл — строки, внутренний — столбцы.

### Матрица 
```python
matrix = [
    [1, 2],
    [3, 4]
]
matrix[0][1]        # 2

for row in matrix:
    for x in row:
        print(x)    # 1 2 3 4
```

### Сумма элементов 
```python
total = 0
for row in matrix:
    for x in row:
        total += x
```

### Максимум в матрице 
```python
mx = matrix[0][0]
for row in matrix:
    for x in row:
        if x > mx:
            mx = x
```

### Таблица умножения 
```python
n = 3
table = []
for i in range(1, n + 1):
    row = []
    for j in range(1, n + 1):
        row.append(i * j)
    table.append(row)
# [[1,2,3],[2,4,6],[3,6,9]]
```

### Средние по строкам 
```python
avgs = [sum(row) / len(row) for row in matrix]
```

---

## 5. List comprehension

### База 
```python
nums = [i * i for i in range(5)]    # [0, 1, 4, 9, 16]
```

### Условие-фильтр 
```python
even = [x for x in range(6) if x % 2 == 0]   # [0, 2, 4]
```

### Условие-выражение (if-else) 
```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(4)]
# ['even', 'odd', 'even', 'odd']
```

### Запомнить
- `if` **после** `for` — фильтр.
- `if-else` **до** `for` — выбор значения.

### Вложенные циклы 
```python
pairs = [(i, j) for i in range(2) for j in range(2)]
# [(0,0),(0,1),(1,0),(1,1)]

matrix = [[1, 2], [3, 4]]
flat = [x for row in matrix for x in row]   # [1, 2, 3, 4]
```

### Функции внутри 
```python
words = ["hi", "there"]
lens = [len(w) for w in words]              # [2, 5]
ints = [int(s) for s in ["1", "22", "333"]] # [1, 22, 333]
```

### Индексы через enumerate
```python
idx = [i for i, x in enumerate(nums) if x < 0]
```

### Filter + map одновременно
```python
result = [x * x for x in nums if x > 0]
```

### Лямбды: late binding 
```python
funcs = [lambda x: x + i for i in range(3)]
print([f(0) for f in funcs])    # [2, 2, 2], а не [0, 1, 2]

# Как исправить:
funcs = [lambda x, i=i: x + i for i in range(3)]
print([f(0) for f in funcs])    # [0, 1, 2]
```

---

## 6. Set и dict comprehension 

### Set — уникальные значения
```python
nums = [1, 1, 2, 3, 3]
uniq = {x for x in nums}            # {1, 2, 3}
```

### Dict — пары ключ-значение
```python
words = ["a", "bb", "ccc"]
d = {w: len(w) for w in words}
# {'a': 1, 'bb': 2, 'ccc': 3}

d = {w: len(w) for w in words if len(w) > 1}
```

### Счётчик частот
```python
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1

# или по уникальным
counts = {x: nums.count(x) for x in set(nums)}
```

---

## 7. Строки в комбинации со списками

### split / join **[B]**
```python
s = "a b c"
words = s.split()               # ['a', 'b', 'c']
back = " ".join(words)          # 'a b c'

parts = "a,b,,c".split(",")     # ['a', 'b', '', 'c']
```

### Разбор логов
```python
logs = ["INFO:start", "ERROR:fail"]
levels = [line.split(":")[0] for line in logs]      # ['INFO', 'ERROR']
messages = [line.split(":")[1] for line in logs]    # ['start', 'fail']
```

### Фильтр по префиксу 
```python
errors = [line for line in logs if line.startswith("ERROR:")]
```

### Верхний регистр 
```python
upper = [line.upper() for line in logs]
```

---

## 8. Шаблоны

```python
# Сумма
total = 0
for x in nums:
    total += x

# Фильтр
result = [x for x in nums if x > 0]

# Преобразование
result = [x * 2 for x in nums]

# Индексы
for i in range(len(nums)):
    print(i, nums[i])

# Копия
b = a.copy()

# Сортировка по ключу
words.sort(key=len)

# Снапшоты счётчика
snapshots = []
value = start
snapshots.append(value)
for d in deltas:
    value += d
    snapshots.append(value)

# Уникальные с сохранением порядка
result = []
for x in nums:
    if x not in result:
        result.append(x)

# Словарь частот
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1

# Топ по ключу
top = sorted(items, key=lambda p: p[1], reverse=True)

# Flatten
flat = [x for row in matrix for x in row]

# Индексы по условию
idx = [i for i, x in enumerate(nums) if x < 0]

# Средние по строкам
avgs = [sum(row) / len(row) for row in matrix]
```
