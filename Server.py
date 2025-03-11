import socketserver
import os

# Class to handle to client data being transfered and sending it to those connected.
class ClientHandler(socketserver.BaseRequestHandler):
    # Handles each client using 'self' as the client ID
    def handle(self):
        # Gets the client's username and prints to the server that they have connected.
        self.username = self.request.recv(1024).decode('utf-8').strip()
        print(f"{self.username} connected.")

        # Tells all connected clients if a new client connects
        for client in server.clients:
            if client != self.request:
                client.sendall(f"{self.username} connected\n".encode('utf-8'))
        
        # Loop receive and send data to clients on the server.
        while True:
            try:
                # Gets the message from a client and decodes it before displaying it to the terminal.
                # If no data was recieved then it breaks out of the loop.
                data = self.request.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8')
                print(f"{self.username}: {message}")

                # Loop to send the data from a client to the other clients connected to the server.
                for client in server.clients:
                    # As long as the client isn't the sender it will send the data to the clients in the client list. 
                    # If it can't send a message it removes that client from the list.
                    if client != self.request:
                        try:
                            client.sendall(f"{self.username}: {message}".encode('utf-8'))
                        except:
                            server.clients.remove(client)
            except:
                break
        
        # Tells the server terminal that a client has disconnected
        print(f"{self.username} disconnected.")

        # Displays to other clients when someone disconnects
        for client in server.clients:
            if client != self.request:
                client.sendall(f"{self.username} disconnected\n".encode('utf-8'))

        # Removes client from the clients list.
        server.clients.remove(self.request)

# Class handles the connection of devices through the HOST and PORT given. Creates a list of users and passes that data to Client handler.
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    clients = []

    # Function designed to process requests from clients
    def process_request(self, request, client_address):
        self.clients.append(request)
        super().process_request(request, client_address)


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 9999

    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    with server:
        os.system('cls')
        os.system('clear')
        print(f"Server started on {HOST}:{PORT}")
        server.serve_forever()