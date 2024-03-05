from web_server import *
from db_class import DB
import threading
from tcp_server import *


def start_server():
    if __name__ == '__main__':
        t = threading.Thread(target=tcp_server)
        t.start()
        app.run()
start_server()



my_bd.check_valid_date()
