import socket

# Create variables that tell the socket library what Port and IP to connect to.
HOST = "localhost"
PORT = 9999

# create a variable to manipulate the classes inside socket library and using AF_INET to use HOST and PORT to connect to a network.
# SOCK_STREAM is used to send data through TCP or Transmission Control Protocol.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# try running the code and if it fails then output an error using 'except'
try:
    # Connect to the IP and Port for sending data
    client.connect((HOST, PORT))
    username = input("Enter your username: ")
    # Sending the username to the server and encoding it using utf-8 standard encoding.
    client.sendall(username.encode('utf-8'))

    # Loop to allow the user to continue sending messages. Leave loop if the user types 'exit' and confirms to exit.
    while True:
        message = input(f"{username} > ")
        # Send the message to the server encoding it in utf-8 standard
        client.sendall(message.encode('utf-8'))
        # Receive data from the server
        data = client.recv(1024)
        # Display the data and decoding it from the utf-8 standard
        print(f"{data.decode('utf-8')}")
        # Allow to user to quit the program
        if message.lower() == "exit":
            quit = input("Would you like to EXIT the program? (Y/N) ")
            if quit.lower() == "y" or quit.lower() == "yes":
                break

# Exceptions created to push errors to the terminal if an unexpected issue occurs.
except ConnectionRefusedError:
    print("Connection refused. Ensure the server is running.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the connection to the IP and Port.
    client.close()