import socket
import threading
import os

# Functions for continuously checking for messages to receive from the server
def receive_messages(client):
    while True:
        # Make sure the client is connected to the server and able to reviece messages
        try:
            # Insert the message into the variable from the server then display it
            message = client.recv(1024).decode('utf-8')
            print(message)
        except ConnectionResetError:
            print("Server disconnected.")
            break
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

# Function for sending messages to server
def send_messages(client):
    while True:
        # Get message from user
        message = input()
        # If message is exit confirm they want to exit and then close the connection to the server
        if message.lower() == "exit":
            confirm = input("Are you sure you wish to exit the program? (Y/N) ")
            if confirm.lower() == "y" or confirm.lower() == "yes":
                client.close()
                print("Disconnected.")
                break
        # If the messages isn't exit then send it to the server for the other client to recieve
        else:
            client.send(message.encode('utf-8'))

# Main program code for connecting to the server and setting up threads to communicate with another client on the server
def client_program():
    # Create variables that tell the socket library what Port and IP to connect to
    HOST = "localhost"
    PORT = 9999

    # create a variable to manipulate the classes inside socket library and using AF_INET to use HOST and PORT to connect to a network
    # SOCK_STREAM is used to send data through TCP or Transmission Control Protocol
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # try running the code and if it fails then output an error using 'except'
    try:
        # Connect to the IP and Port for sending data
        client.connect((HOST, PORT))
            
    # Exceptions created to push errors to the terminal if an unexpected issue occurs
    except ConnectionRefusedError:
        print("Connection refused. Ensure the server is running.")
    except Exception as e:
        print(f"An error occurred: {e}")

    username = input("Enter your username: ")
    # Sending the username to the server and encoding it using utf-8 standard encoding
    client.sendall(username.encode('utf-8'))

    # Build manipulatable variables to access the functions in the thread library
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    send_thread = threading.Thread(target=send_messages, args=(client,))

    # Clear the screen to clean up text and create a header for the user's chat
    os.system("cls")
    os.system("clear")
    print(f"{username}'s Chat\n")

    # Using the variables start the thread process
    receive_thread.start()
    send_thread.start()

    # Using .join to keep the threads executing until the program stops   
    send_thread.join()
    receive_thread.join()
        

if __name__ == "__main__":
    os.system("cls")
    os.system("clear")
    client_program()