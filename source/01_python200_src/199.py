import socketserver
import threading

HOST = ''
PORT = 9009
lock = threading.Lock()


class UserManager:
    def __init__(self):
        self.users = {}

    def addUser(self, username, conn, addr):
        if username in self.users:
            conn.send('�씠誘� �벑濡앸맂 �궗�슜�옄�엯�땲�떎.\n'.encode())
            return None

        # �깉濡쒖슫 �궗�슜�옄瑜� �벑濡앺븿
        lock.acquire()
        self.users[username] = (conn, addr)
        lock.release()

        self.sendMessageToAll('[%s]�떂�씠 �엯�옣�뻽�뒿�땲�떎.' % username)
        print('+++ ����솕 李몄뿬�옄 �닔 [%d]' % len(self.users))

        return username

    def removeUser(self, username):
        if username not in self.users:
            return

        lock.acquire()
        del self.users[username]
        lock.release()

        self.sendMessageToAll('[%s]�떂�씠 �눜�옣�뻽�뒿�땲�떎.' % username)
        print('--- ����솕 李몄뿬�옄 �닔 [%d]' % len(self.users))

    def messageHandler(self, username, msg):
        if msg[0] != '/':
            self.sendMessageToAll('[%s] %s' % (username, msg))
            return

        if msg.strip() == '/quit':
            self.removeUser(username)
            return -1

    def sendMessageToAll(self, msg):
        for conn, addr in self.users.values():
            conn.send(msg.encode())


class MyTcpHandler(socketserver.BaseRequestHandler):
    userman = UserManager()

    def handle(self):
        print('[%s] �뿰寃곕맖' % self.client_address[0])

        try:
            username = self.registerUsername()
            msg = self.request.recv(1024)
            while msg:
                print(msg.decode())
                if self.userman.messageHandler(username, msg.decode()) == -1:
                    self.request.close()
                    break
                msg = self.request.recv(1024)

        except Exception as e:
            print(e)

        print('[%s] �젒�냽醫낅즺' % self.client_address[0])
        self.userman.removeUser(username)

    def registerUsername(self):
        while True:
            self.request.send('濡쒓렇�씤ID:'.encode())
            username = self.request.recv(1024)
            username = username.decode().strip()
            if self.userman.addUser(username, self.request, self.client_address):
                return username


class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def runServer():
    print('+++ 梨꾪똿 �꽌踰꾨�� �떆�옉�빀�땲�떎.')
    print('+++ 梨꾪뀉 �꽌踰꾨�� �걹�궡�젮硫� Ctrl-C瑜� �늻瑜댁꽭�슂.')

    try:
        server = ChatingServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('--- 梨꾪똿 �꽌踰꾨�� 醫낅즺�빀�땲�떎.')
        server.shutdown()
        server.server_close()


runServer()
