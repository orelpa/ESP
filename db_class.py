import psycopg2
import logging
import time
logging.basicConfig(level=logging.INFO, filename=('log/' + time.strftime("%d-%m-%Y") +".log"), filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")



msg = "Тестовый принт"
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class DB:
    'Модель подключения, чтения, записи в БД'
    def __init__(self, user, password, host, port):

            self.user = user
            self.password = password
            self.host = host
            self.port = port
            self.result_box = {}
            self.result_paper ={}
            self.result_all ={}
            #Соединяемся с БД
            self.con = psycopg2.connect(user=self.user, password=self.password, host=self.host, port=self.port)

            # Автоматическое сохранение изменений
            self.con.autocommit = True
            #создаём курсор для работы с БД
            self.cur = self.con.cursor()

            #создаём таблицу если её не существует
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS count (id serial PRIMARY KEY, box INTEGER, paper INTEGER, posting_date DATE NOT NULL DEFAULT CURRENT_DATE)"
            )



    def insert(self,id, box, paper):

        self.cur.execute(
            "INSERT INTO count(id, box, paper) VALUES ('%s', '%s', '%s' );"%(id,box,paper)
        )

    def new_day_insert(self):
        "Метод создания новой сторки на новый день"
        self.cur.execute(
                "INSERT INTO count(box, paper) VALUES ('0', '0');"
        )



    def view_box(self):
        'Просмотр всех значений коробок на текущей дате'

        self.cur.execute(
            "SELECT box FROM count WHERE posting_date = NOW()::DATE "
            )
        result = self.cur.fetchone()
        self.result_box['box'] = result[0]
        return self.result_box

    def view_paper(self):
        'Просмотр всех значений картона на текущей дате'

        self.cur.execute(
            "SELECT paper FROM count WHERE posting_date = NOW()::DATE "
            )
        result = self.cur.fetchone()
        self.result_paper['paper'] = result[0]
        return self.result_paper

    def viev_all(self):
        "Просмотр записей картона и коробок на текущий день для вывода в веб"
        self.cur.execute(
            "SELECT box, paper FROM count WHERE posting_date = NOW()::DATE"
        )
        result = self.cur.fetchone()
        self.result_all['box'] = result[0]
        self.result_all['paper'] = result[1]
        return self.result_all


    def check_valid_date(self):
        #получение последней записи даты
        self.cur.execute(
            "SELECT EXISTS(SELECT posting_date FROM count)" #Запрашивает существоание записи возвращает True False
        )
        last_posted_data_value = self.cur.fetchone()[0]
        if last_posted_data_value:
            self.cur.execute(
                "SELECT posting_date FROM count"
            )
            last_posted_data =self.cur.fetchone()[0]
        else:
            print(msg + "Текущей даты нет, создаём запись")
            self.new_day_insert()
            self.cur.execute(
                "SELECT posting_date FROM count"
            )
            last_posted_data = self.cur.fetchone()[0]

        return True



        self.cur.execute(
            "SELECT NOW()::DATE;"
        )
        current_posted_date = self.cur.fetchone()[0]

        if current_posted_date == last_posted_data:
            print("Тестовый вывод: Сегодняшняя дата есть")

        else:
            self.new_day_insert()
            #"INSERT INTO count(id, box, paper) VALUES ('%s', '%s', '%s' );"%(0,0,0)
            print(msg + " Текущей даты нет, делаем новую запись")

    def update(self, used):
        "Метод обновлят записи box и paper в БД"
        match used:
            case "box":
                self.cur.execute(
                    "UPDATE count SET box = box +1"
                )
            case "paperboard":
                self.cur.execute(
                    "UPDATE count SET paper = paper +1"
                )


