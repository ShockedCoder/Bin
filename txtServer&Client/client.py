import socket
import threading
import platform
import os

HEADER = 64
FORMAT = 'utf-8'

PORT = 8080
DISCONNECT_MESSAGES = ["!DISCONNECT", "!D", "!SILENTDISCONNECT", "!SD"]
#HOST = input("Server IP/Hostname: ")
HOST = "127.0.1.1"
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def serverStateHandler():
    thread = threading.Thread(target=client.recv(2048).decode(FORMAT))
    thread.start()

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

    serverResponse = client.recv(2048).decode(FORMAT)
    if "kick" in serverResponse or "ban" in serverResponse:# or "shut" in serverResponse:
        global connected
        connected = False
    else:
        print(serverResponse)

if __name__ == '__main__':
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    connected = True
    try:
        while connected:
            msg = input("Message: ")
            msg_upper = msg.upper().replace(" ", "")
            if msg_upper in DISCONNECT_MESSAGES:
                send(DISCONNECT_MESSAGES[0])
                connected = False
                exit()
            send(msg)
    except KeyboardInterrupt:
        send(DISCONNECT_MESSAGES[2])
        connected = False
        exit()