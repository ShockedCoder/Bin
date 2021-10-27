#!/bin/python

import socket
import threading

PORT = 5912
HOST = "192.168.10.87"
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[PING] {addr[0]}")


def start():
    server.listen()
    print(f"[LISTENING] IP:   {HOST}")
    print(f"[LISTENING] PORT: {PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == '__main__':
    try:    
        print("[STARTING]  Collector is awakening...")
        start()
    except KeyboardInterrupt:
        print("Server shutting down.")
        exit()

