from socket import *
import time
import json

# with open('json.json', 'r') as file:
#             data_j = json.loads(file.read())
#             print(data_j.get[0]('message'))

HOST = 'localhost'
PORT = 9090

clients = []

s = socket(AF_INET, SOCK_DGRAM)
s.bind((HOST, PORT))

print('Server started!')
quit = False
# s.listen(5)

while not quit:
    try:
        data, addr = s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + itsatime + "]/", end="")
        print(data.decode("utf-8"))
        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except Exception as e:
        print(e)
        print('\nServer stopped!')
        quit = True

s.close()

print('Socket stoped!')