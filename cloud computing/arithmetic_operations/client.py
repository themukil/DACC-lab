import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
client_socket.connect(server_address)
print("Connected to {}:{}".format(*server_address))

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    numbers_to_send = "{},{}".format(num1, num2)
    client_socket.send(numbers_to_send.encode('utf-8'))
    response = client_socket.recv(1024)
    print("Server's response: {}".format(response.decode('utf-8')))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
client_socket.close()
