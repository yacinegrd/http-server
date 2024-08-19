from Server import Server

PORT = 8080
ADRESSE = "localhost"
BUFFER_SIZE = 8*1024

app = Server(ADRESSE, PORT, BUFFER_SIZE)


def returnIndex(req, res):
    with open("index.html", "r") as file:
        content = file.read()
    res.response["body"] = content
    

app.get("/", returnIndex)

app.run()