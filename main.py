import json
import socket
from _thread import *

from command import *
from game import Game


def get_response(req, game, id):
    if req.type == CommandType.HELLO:
        hello = HelloCommand()
        hello.payload = f"PLAYER:{id}"
        return hello
    if game.status:
        if req.type == CommandType.STEP:
            try:
                if len(req.payload) > 0:
                    json.loads(req.payload)
                game.state = req.payload
                game.next_round()
            except Exception as e:
                print(e)
                return ErrorCommand(req.payload)
        return GameStateCommand(game)
    else:
        return WaitCommand()


def threaded_client(conn, game, id):
    conn.send(str.encode("welcome"))
    while True:
        try:
            data = conn.recv(2048).decode()
            req = Command.parse(data)

            if not data:
                print("Disconnected")
                break
            else:
                res = get_response(req, game, id)

                print("=>", req.print())
                print("<=", res.print())

            conn.sendall(str.encode(res.print()))
        except error:
            print(error)
            break

    print("Lost connection")
    conn.close()


if __name__ == '__main__':

    server = ""  # listens all interfaces
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)

    s.listen(2)
    print("Waiting for a connection, Server Started")

    g = Game()

    while True:
        conn, addr = s.accept()
        print("Connected to:", addr)

        if len(g.players) == 2:
            g = Game()

        g.add_player(start_new_thread(threaded_client, (conn, g, len(g.players),)))
