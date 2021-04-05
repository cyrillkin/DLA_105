import socket
import threading
import time
import json


shutdown = False
join = False

def receiving(name, sock):
    while not shutdown:
        try:
            while True:
                data, attr = sock.recvfom(1024)
                print(data,decode("utf-8"))
                time.sleep(0.2)
        except:
            pass


server = ('localhost', 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('localhost', 0))

name = input('Name: ')

rT = threading.Thread(target=receiving, args=('RecvThread', s))
rT.start()

while not shutdown:
    if not join:
        s.sendto(("[" + name + "] => join chat").encode('utf-8'), server)
        join = True
    else:
        try:
            message = input('[You] :: ')
            if message != "":
                s.sendto(("[" + name + "] :: " + message).encode("utf-8"), server)
                itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
                data_for_json = {'action': 'msg_from_chat',
                        'time': itsatime,
                        'message': message,
                        'user':
                            {'name': name,
                             'status': 'online'}}
                with open('json.json', 'w') as file:
                    json.dump(data_for_json, file)
        except Exception as e:
            s.sendto(("[" + name + "] => left chat").encode("utf-8"), server)
            shutdown = True

rT.join()
s.close()