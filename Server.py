import socketserver
import threading

class ClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.username = self.request.recv(1024).decode('utf-8').strip()
        print(f"{self.username} connected.")
        
        while True:
            try:
                data = self.request.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8')
                print(f"{self.username}: {message}")
                
                for client in server.clients:
                    if client != self.request:
                        try:
                            client.sendall(f"{self.username}: {message}".encode('utf-8'))
                        except:
                            server.clients.remove(client)
            except:
                break
        
        print(f"{self.username} disconnected.")
        server.clients.remove(self.request)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    clients = []

    def process_request(self, request, client_address):
        self.clients.append(request)
        super().process_request(request, client_address)


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 9999

    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    with server:
        print(f"Server started on {HOST}:{PORT}")
        server.serve_forever()