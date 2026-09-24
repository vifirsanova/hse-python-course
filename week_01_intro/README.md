## Темы презентаций 2–5

| № | Тема | Ключевые понятия |
|---|------|------------------|
| 2 | Первая программа, переменные и арифметика | print, комментарии, переменные, присваивание, арифметические операторы |
| 3 | Базовые типы данных, ввод и вывод | int, float, str, bool, input, приведение типов, decimal, fractions |
| 4 | Основы алгоритмов | свойства алгоритма, оценка сложности, O(n), O(n²), O(log n), O(n log n) |
| 5 | Жадные алгоритмы | жадный выбор, оптимальная подструктура, размен монет, интервалы, рюкзак, платформы |

## Дедлайн

**8 октября 2026, 23:59**

## Как сдавать

1. Создайте свой GitHub-репозиторий по этой структуре.
2. Решайте задачи в соответствующих файлах.
3. Загружайте файлы в репозиторий в нужную папку (или пушьте коммиты).
4. Каждая задача — отдельный файл `.py`.
5. Проверка: работоспособность, читаемость (PEP8), комментарии, история коммитов.

### Коммиты

Шаблон: `<тип>: <что сделано>`

Примеры:
```
add task_01 solution
fix: correct variable name
docs: update README
```

## Список файлов к сдаче

### Базовый уровень

- `classwork_base/p2_base.py`
- `classwork_base/p3_base.py`
- `classwork_base/p4_base.py`
- `classwork_base/p5_base.py`
- `homework/p2_base/task_01.py`, `task_02.py`
- `homework/p3_base/task_01.py`, `task_02.py`
- `homework/p4_base/task_01.py`, `task_02.py`
- `homework/p5_base/task_01.py`, `task_02.py`

### Повышенный уровень

- `classwork_advanced/p2_advanced.py`
- `classwork_advanced/p3_advanced.py`
- `classwork_advanced/p4_advanced.py`
- `classwork_advanced/p5_advanced.py`
- `homework/p2_advanced/task_01.py`, `task_02.py`
- `homework/p3_advanced/task_01.py`, `task_02.py`
- `homework/p4_advanced/task_01.py`, `task_02.py`
- `homework/p5_advanced/task_01.py`, `task_02.py`

## Запуск тестов (для повышенного уровня)

```bash
python task_01.py        # assert-тесты в конце файла
pytest test_task_01.py -v  # если используете pytest
```
