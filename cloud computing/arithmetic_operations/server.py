import socket
import threading

def handle_client(client_socket, client_address):
    print("Accepted connection from {}:{}".format(*client_address))
    
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break  
            
            numbers = data.decode('utf-8').split(',')
            
            if len(numbers) == 2:
                num1, num2 = map(float, numbers)
                add_result = num1 + num2
                sub_result = num1 - num2
                mul_result = num1 * num2
                if num2 != 0:
                    div_result = num1 / num2
                else:
                    div_result = "Cannot divide by zero"

                response = "Addition: {:.2f}, Subtraction: {:.2f}, Multiplication: {:.2f}, Division: {}".format(
                    add_result, sub_result, mul_result, div_result)
                client_socket.send(response.encode('utf-8'))
            else:
                client_socket.send("Invalid input. Please provide two numbers separated by a comma.".encode('utf-8'))
    except Exception as e:
        print("Error in handle_client: {}".format(e))

    print("Connection from {}:{} closed".format(*client_address))
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)
server_socket.listen(5)
print("Server is listening on {}:{}".format(*server_address))

while True:
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
