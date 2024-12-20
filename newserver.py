import socket
from _thread import *
import pydirectinput as pd

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.43.174'
print(host)
ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = 8008
ThreadCount = 0
print(f"Please connect to this server ip {host} and port {port}")

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)


def send(conn):
    message = input("")
    conn.send(bytes(message, 'utf-8'))

def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server'))
    while True:
        data = connection.recv(2048)
        hello = str(data, 'utf-8').strip()
        # print(hello)
        if not data:
            break
        if hello == 'close':
            ServerSocket.close()
        if hello == 'h':
            pd.press('left')
            print('left')
            # playsound.playsound('2.mp3')
        if hello == 'j':
            pd.press('right')
            print('right')
        if hello == 'what':
            send(connection)
        # connection.sendall(str.encode(reply))
    connection.close()


while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client,))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))


# AF_INET is an address family that is used to designate the type of addresses that your socket
# can communicate with (in this case, Internet Protocol v4 addresses).
# When you create a socket, you have to specify its address family, and then you can
# only use addresses of that type with the socket.



# The SOCK_STREAM means connection-oriented TCP protocol.

# SO_REUSEADDR allows your server to bind to an address which is in a
# TIME_WAIT state.
#
# This socket option tells the kernel that even if this port is busy (in the TIME_WAIT state), go ahead and reuse it anyway.


# socket.accept()
# Accept a connection. The socket must be bound to an address and listening for connections.
# The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection, and
# address is the address bound to the socket on the other end of the connection.
