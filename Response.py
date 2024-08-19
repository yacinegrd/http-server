class Response():
    def __init__(self, body: str) -> None:
        self.response = {
            "version" : "HTTP/1.1",
            "status" : 200,
            "headers" : {
                "server" : "python",
                "accept-ranges" : "bytes",
                "content-length" : len(body)
            },
            "body" : body
        }
    
    def responseToStr(self) -> str:
        encodedRes = f"{self.response['version']} {str(self.response['status'])} {'OK ' if self.response['status'] == 200 else 'ERROR'}\r\n"
        
        for header, value in self.response["headers"].items():
            encodedRes += f"{header}: {value}\r\n"

        encodedRes += f"\n{self.response['body']}"

        return encodedRes