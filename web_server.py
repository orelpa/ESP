
import socket

serv_sock = socket.socket(socket.AF_INET,  #задаём семейство протоколов Интернет (INET)
                          socket.SOCK_STREAM, # задаём тип передачи данных потоковый (TCP)
                          proto=0) #выбираем протокол по умолчанию для TCP т.е класс socket.socket
#serv_sock.bind(('127.0.0.1', 5837))
serv_sock.bind(('10.33.1.147', 5837))


#явно переводим сокет в режим ожидания

backlog = 10 # размер очереди входящих подключений
serv_sock.listen(backlog)

while True:
    #Бесконечно оттрабатываем входящие подключения

    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        #Пока клиент не отклчился, читаем передаваемые
        #им данные и отправляем их обратно
        data = client_sock.recv(1024).decode('utf-8')
        print(str(data))
        print(type(data))
        print(str(data))
        if not data:
            #Клиент октлючился
           break
        #client_sock.sendall(data)
    client_sock.close()

