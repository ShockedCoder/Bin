#!/bin/python

import socket
import threading

HEADER = 64
FORMAT = 'utf-8'

PORT = 8080
DISCONNECT_MESSAGE = "!DISCONNECT"
#HOST = input("Server IP/Hostname: ")
HOST = "127.0.1.1"
ADDR = (HOST, PORT)

client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client1.send(send_length)
    client1.send(message)
    client2.send(send_length)
    client2.send(message)
    client3.send(send_length)
    client3.send(message)
    client4.send(send_length)
    client4.send(message)
    client5.send(send_length)
    client5.send(message)

if __name__ == '__main__':

    # threading.Thread(target=client2.connect(ADDR))._stopthreading.Thread(target=client1.connect(ADDR))._stop()
    
    threading.Thread(target=client1.connect(ADDR)).start()
    threading.Thread(target=client2.connect(ADDR)).start()
    threading.Thread(target=client3.connect(ADDR)).start()
    threading.Thread(target=client4.connect(ADDR)).start()
    threading.Thread(target=client5.connect(ADDR)).start()
    
    threading.Thread(target=client1.close()).start()
    threading.Thread(target=client2.close()).start()
    threading.Thread(target=client3.close()).start()
    threading.Thread(target=client4.close()).start()
    threading.Thread(target=client5.close()).start()
    
    while True:
        try:
            print("",end="")
            # serverResponse = client5.recv(2048).decode(FORMAT)
            # if "shut" in serverResponse.lower():
            #     print("Disconnecting...")
            #     message = "All clients have been disconnected.".encode(FORMAT)
            #     msg_length = len(message)
            #     send_length = str(msg_length).encode(FORMAT)
            #     send_length += b' ' * (HEADER - len(send_length))
            #     client5.send(send_length)
            #     client5.send(message)
            #     send(DISCONNECT_MESSAGE)
            #     print("Disconnected")
            #     print("Server has shutdown.")
            #     exit()
        except KeyboardInterrupt:
            print("Disconnecting...")
            try:
                message = "All clients have been disconnected.".encode(FORMAT)
                msg_length = len(message)
                send_length = str(msg_length).encode(FORMAT)
                send_length += b' ' * (HEADER - len(send_length))
                client5.send(send_length)
                client5.send(message)
                send(DISCONNECT_MESSAGE)
            except:
                pass
            print("Disconnected")
            exit()

        # serverResponse = client1.recv(2048).decode(FORMAT)
        # if serverResponse == "off":
        #     exit()


