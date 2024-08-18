import socket as sc

class Response():
    def __init__(self, content) -> None:
        self.response = {
            "version" : "HTTP/1.1",
            "status" : 200,
            "headers" : {
                "server" : "python",
                "accept-ranges" : "bytes",
                "content-length" : len(content)
            },
            "content" : content
        }

    
    def encodeResponse(self):
        encodedRes = f"{self.response["version"]} {self.response["version"]} {"OK " if self.response["status"] == 200 else "ERROR"}"


# "HTTP/1.1 200 OK\nServer: Python\nAccept-Ranges: bytes\nContent-Length: {len(content)}\nContent-Type: text/html\n\n{content}"

        return encodedRes.encode()

def parseRequest(request_string : str): 
    request_string = request_string.split("\n")    
    request = {}
    headers = {}

    request["method"] = request_string[0].split(" ")[0]
    request["route"] = request_string[0].split(" ")[1]
    request["version"] = request_string[0].split(" ")[2].strip()

    for line in request_string[1:]:
        line = line.strip().split(": ")
        if len(line[0]) > 0:
            headers[line[0]] = line[1]

    request["header"] = headers
    return request

PORT = 8080
ADRESSE = "localhost"
BUFFER_SIZE = 8*1024

server = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
server.setsockopt(sc.SOL_SOCKET, sc.SO_REUSEADDR, 1)

try : server.bind((ADRESSE,PORT))
except OSError: 
    print(f"Error binding adresse {ADRESSE}:{PORT}")
else:
    print(f"starting server on port {PORT}...")
    server.listen()
    while True:
        try:
            client, client_adresse = server.accept()
            request = client.recv(BUFFER_SIZE).decode()

            with open("index.html", "r") as file:
                content = file.read()

            print(parseRequest(request))
            
            client.send(f"HTTP/1.1 200 OK\nServer: Python\nAccept-Ranges: bytes\nContent-Length: {len(content)}\nContent-Type: text/html\n\n{content}".encode())
            print("respoonse sent")            
            client.close()
        except KeyboardInterrupt: break

print("\nServer closed")            
server.close()