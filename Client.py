import socket

HOST = "localhost"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
    username = input("Enter your username: ")
    client.sendall(username.encode('utf-8'))

    while True:
        message = input(f"{username} > ")
        client.sendall(message.encode('utf-8'))
        data = client.recv(1024)
        print(f"{data.decode('utf-8')}")
except ConnectionRefusedError:
    print("Connection refused. Ensure the server is running.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()