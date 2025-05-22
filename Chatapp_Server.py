import socket
import threading

clients = {}

def handle_client(client_socket):
    name = client_socket.recv(1024).decode()
    clients[client_socket] = name
    print(f"[CONNECTED] {name} has joined the chat.")

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"[MESSAGE] From {name}: {message}")
                broadcast(f"{name}: {message}", client_socket)
            else:
                break
        except:
            break

    print(f"[DISCONNECTED] {name} has left the chat.")
    client_socket.close()
    del clients[client_socket]

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(message.encode())

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen()
    print("[SERVER STARTED] Waiting for connections...")

    while True:
        client_socket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

start_server()

