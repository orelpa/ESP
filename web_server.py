
import socket
msg = "Тестовый принт"
class Web_SERV:
    "Простой веб сервер"
    def __init__(self):
        self.backlog = 10


        self.serv_sock = socket.socket(socket.AF_INET,  #задаём семейство протоколов Интернет (INET)
                                  socket.SOCK_STREAM, # задаём тип передачи данных потоковый (TCP)
                                  proto=0) #выбираем протокол по умолчанию для TCP т.е класс socket.socket
        #serv_sock.bind(('127.0.0.1', 5837))

        # явно переводим сокет в режим ожидания
        self.serv_sock.bind(('10.33.1.147', 5837))
        # размер очереди входящих подключений
        self.serv_sock.listen(self.backlog)

    def run_serv(self):
        while True:
            # Бесконечно оттрабатываем входящие подключения
            self.client_sock, self.client_addr = self.serv_sock.accept()
            print('Connected by', self.client_addr)
            while True:
                # Пока клиент не отклчился, читаем передаваемые
                # им данные и отправляем их обратно
                self.data = self.client_sock.recv(1024).decode('utf-8')
                print(str(msg + self.data))
                print(type(msg + self.data))
                print(str(msg + self.data))
                if not self.data:
                    # Клиент октлючился
                    break
                # client_sock.sendall(data)
            self.client_sock.close()

ms = Web_SERV()

ms.run_serv()









