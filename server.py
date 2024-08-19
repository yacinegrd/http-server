import socket as sc
from Request import Request
from Response import Response
import json

class Server():
    def __init__(self, adresse: str, port: int, buff_size = 8*1024):
        self.adresse = adresse
        self.port = port 
        self.buff_size = buff_size

        self.sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
        self.sock.setsockopt(sc.SOL_SOCKET, sc.SO_REUSEADDR, 1) # This unables the socket to be reuseable
        try : self.sock.bind((adresse,port))
        except OSError: 
            self.sock.close()
            raise OSError(f"Error binding adresse {adresse}:{port}")


    def run(self):
        print(f"starting server on port {self.port}...")
        self.sock.listen()
        while True:
            try:
                client, client_adresse = self.sock.accept()
                request = client.recv(self.buff_size).decode()

                req = Request(request)

                print(json.dumps(req.request, indent=2))

                with open("index.html", "r") as file:
                    content = file.read()

                res = Response(content)
                client.send(res.responseToStr().encode())
                
                print("respoonse sent")            
                client.close()
            except KeyboardInterrupt: break

        print("\nServer closed")            
        self.sock.close()




PORT = 8080
ADRESSE = "localhost"
BUFFER_SIZE = 8*1024

app = Server(ADRESSE, PORT, BUFFER_SIZE)

app.run()