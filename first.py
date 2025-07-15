import sqlite3
from venv import create


class Crud:
    def __init__(self, db_path):
        self._conn = sqlite3.connect(db_path)
        self._cur = self._conn.cursor()

    def create(self,table_name, name, age):
        res = self._cur.execute(
            f'insert into {table_name}(name, age) values (?, ?)'
            ,(name, int(age))
        )
        self._conn.commit()

# Метод чтения таблицы
    def read(self, table_name):
        res = self._cur.execute(
             f""" select * from {table_name}"""
        ).fetchall()
        for num, name, age in res:
            print(num, name, age)

    def update(self, table_name, id_num, name=None, age=None):
        self._cur.execute(
            f'update {table_name} set name="{name}", age={age} where id={id_num}'
        )
        self._conn.commit()

# Метод удаления строки по id из таблицы
    def delete(self, id_num, table_name):
        res = self._cur.execute(
            f'delete from {table_name} where id={id_num}'
        )
        self._conn.commit()

# Отключаем курсор и БД (уничтожение объекта из памяти)
    def __del__(self):
        self._cur.close()
        self._conn.close()
        print('Object kills')

db = Crud('db/movies.sqlite')
# db.delete(3, 'users')
db.create('users', 'Dima', 18)
db.update('users', 8, 'Kostya', 44 )
db.read('users')