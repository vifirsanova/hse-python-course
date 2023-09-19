# Руководство по работе с GitHub

## Работа с git
`git version` - проверяем установленную версию

**Первое использование**: указываем имя пользователя и привязанный e-mail

`git config --global user.name "username"`

`git config --global user.email username@example.com`

**Работа с репозиторием**

`git clone https://github.com/username/example.git` - клонируем репозиторий

`git add` - добавляем отслеживание содержимого рабочего каталога

Примеры: `git add .` - отслеживаем все файлы; `git add helloworld.py` - отслеживаем файл "helloworld.py"

`git status` - смотрим, какие изменения произошли

`git reset` - отменяем незафиксированные изменения

`git commit` - фиксируем изменения

Пример: `git commit -m "Add helloworld.py"`

`git push` - отправляем изменения на сервер

Пример: `git push origin main`

**Стандартный процесс**

`git add .`

`git commit -m "Add helloworld.py`

`git push`

## Markdown

**Заголовки**

```
# Заголовки
## Заголовки второго уровня
### И т.д.
```
## Пример заголовка второго уровня
### Пример заголовка третьего уровня

**Форматирование текста**

```
*курсив*  
**жирный**  
***жирный курсив***  
~~зачеркнутый~~
```

*курсив*  
**жирный**  
***жирный курсив***  
~~зачеркнутый~~

**Ссылки**

```
[Текст ссылки](https://www.github.com)
```

[Пример ссылки](https://www.github.com)

**Изображения**

```
![Текст описания изображения](https://upload.wikimedia.org/wikipedia/commons/f/f0/Mops_oct09_cropped2.jpg)
```
![Mops_oct09.jpg: Dagur Brynjólfsson from Hafnarfjordur, Iceland;derivative work: Anka Friedrich, CC BY-SA 2.0 <https://creativecommons.org/licenses/by-sa/2.0>, via Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/f/f0/Mops_oct09_cropped2.jpg)
Mops_oct09.jpg: Dagur Brynjólfsson from Hafnarfjordur, Iceland;derivative work: Anka Friedrich, CC BY-SA 2.0 <https://creativecommons.org/licenses/by-sa/2.0>, via Wikimedia Commons

**Код**

```
# Пример оформления кода
`print(“Hello world!”)`

# Пример оформления блока кода
\```
print(“Hello world!”)
\``` 
```

`print(“Hello world!”)`

```
print(“Hello world!”)
``` 

**Таблицы**

```
| Шапка | таблицы |
| --------- | ------------ |
| Числа  | Слова      |
```

| Шапка | таблицы |
| ----- | ------- |
| Числа | Слова   |
