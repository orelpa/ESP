import sqlite3

class DB:
    "Простая модель БД"

    def __init__(self):
        #соединение с файлом БД
        self.conn = sqlite3.connect("my.db")

        #создаём курсор для виртуального управления бд
        self.cur = self.conn.cursor()

        #если нужной таблицы в бд нет, создаём её

        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS buy (id INTEGER PRIMARY KEY, box INTEGER, paper INTEGER, data TEXT)"
        )

        #сохраняем сделанные изменения в базе
        self.conn.commit()

    #деструктор класаа
    def __del__(self):
        #отключаемся от базы при завершении работы
        self.conn.close()

    #просмотр всех записей
    def viev(self):
        #ыбираем все записи о покупках

        self.cur.execute(
            "UPDATE buy SET prouct ?, price? WHERE id =?", (product, price, id)
        )


db = DB()