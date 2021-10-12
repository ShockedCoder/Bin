import os
import platform
import socket
import threading

# https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/

HEADER = 64
FORMAT = 'utf-8'

PORT = 8080
HOST = socket.gethostbyname(socket.gethostname())
#HOST = "192.168.10.87"
ADDR = (HOST, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"
SILENT_DISCONNECT_MESSAGE = "!SILENTDISCONNECT"
Banned = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    global connected
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                conn.send("\nDisconnected\n".encode(FORMAT))
            elif msg == SILENT_DISCONNECT_MESSAGE:
                connected = False
                conn.send("\nDisconnected\n".encode(FORMAT))
            elif msg == "cum":
                connected = False
                conn.send("\nYou have been kicked by the server\n".encode(FORMAT))
            elif msg == "semen":
                connected = False
                conn.send("\nYou have been banned by the server\n".encode(FORMAT))
                Banned.append(addr[0])
            elif msg.replace(" ", "") == "":
                pass
            else:
                print(f"[{addr[0]}] {msg}")
                conn.send("msg received".encode(FORMAT))

def start():    # Starts the server
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}")
    print(f"[LISTENING] PORT: {PORT}")
    while True:
        global conn
        conn, addr = server.accept()
        if addr[0] in Banned:
            conn.send("You are banned from the server".encode(FORMAT))     
        else:
            global thread
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == '__main__':
    try:
        if platform.system() == "Windows":  # Clear screen
            os.system("cls")
        else:
            os.system("clear")
            
        print("[STARTING] Server is starting...")
        start() # Start the server
    except KeyboardInterrupt:
        print("Server shutting down.")
        try:
            conn.send("Server shutting down.".encode(FORMAT))
            # connected = False
            conn.send("kick".encode(FORMAT))
        except NameError:
            print("No connections to kick.")
        
        exit()


