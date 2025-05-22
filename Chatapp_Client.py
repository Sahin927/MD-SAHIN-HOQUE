import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if message:
                print(message)
        except:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))

    name = input("Enter your name: ")
    client.send(name.encode())

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        msg = input()
        client.send(msg.encode())

main()

