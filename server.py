import socket
from _thread import *
import pickle
from game import Game

server = "192.168.1.36"
port = 5555


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(1)
print("Waiting for a connection, Server Started")


def client_method(conn, game):
    conn.send(pickle.dumps(game))

    while True:
        try:
            pass

        except:
            break

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()

    start_new_thread(client_method, (conn,))
