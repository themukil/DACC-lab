import socket
import threading

def receive_messages(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break  
        print("Received from server: {}".format(data.decode('utf-8')))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
client_socket.connect(server_address)
print("Connected to {}:{}".format(*server_address))

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

while True:
    message = input("Type your message (or 'exit' to close): ")
    client_socket.send(message.encode('utf-8'))
    
    if message.lower() == 'exit':
        break

    response = client_socket.recv(1024)
    print("Received from server: {}".format(response.decode('utf-8')))
client_socket.close()
