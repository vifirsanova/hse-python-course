## Темы презентаций 6–7

| № | Тема | Ключевые понятия |
|---|------|------------------|
| 6 | Условные операторы, строки и регулярные выражения | сравнения, and/or/not, if/elif/else, вложенные условия, строки, regex |
| 7 | Цикл for, списки, методы списков и list comprehension | for, range, списки, срезы, методы списков, вложенные циклы, list comprehension, lambda |

## Дедлайн

**8 ноября 2026, 23:59**

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

- `classwork_base/p6_base.py`
- `classwork_base/p7_base.py`
- `homework/p6_base/task_01.py`, `task_02.py`, `task_03.py`, `task_04.py`, `task_05.py`
- `homework/p7_base/task_01.py`, `task_02.py`, `task_03.py`, `task_04.py`, `task_05.py`

### Повышенный уровень

- `classwork_advanced/p6_base.py`
- `classwork_advanced/p7_base.py`
- `homework/p6_advanced/task_01.py`, `task_02.py`, `task_03.py`, `task_04.py`, `task_05.py`
- `homework/p7_advanced/task_01.py`, `task_02.py`, `task_03.py`, `task_04.py`, `task_05.py`

## Запуск тестов (для повышенного уровня)

```bash
python task_01.py        # assert-тесты в конце файла
pytest test_task_01.py -v  # если используете pytest
```
