# Базы данных (чтение)
"""
1. Импорт библиотеки sqlite3
2. Подключаемся к БД
3. Назначить курсор
4. Работа с БД (запросы ответы)
5. Отключаем БД
"""
import sqlite3

connection = sqlite3.connect('db/movies.sqlite')
cursor = connection.cursor()
result = cursor.execute(
    """
    select title, year from films where year = 2010
    """
)
# fetchall - Всё    fetchone - Только первое соответствие   fetchmany(N) - N-соответствий
array = result.fetchall()
print(array)
for title, year in array:
    print(title, year)
connection.close()

# Запись в БД
# 4.5 Подтвердить изменения (commit)
connection = sqlite3.connect('db/movies.sqlite')
cursor = connection.cursor()
result = cursor.execute(
    """
    insert into users(name, age) values('Marks', 55)
    """
)
connection.commit()
connection.close()