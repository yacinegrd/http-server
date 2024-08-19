
class Request():
    def __init__(self, request_string: str):
        self.request_string = request_string
        self.request = self.parseRequest()
        self.uri = self.parseUri()

    def parseRequest(self) -> dict[str, str | dict[str, str]]: 
        request_string = self.request_string.split("\r\n")    
        request = {}
        headers = {}
        request["method"] = request_string[0].split(" ")[0]
        request["uri"] = request_string[0].split(" ")[1]
        request["version"] = request_string[0].split(" ")[2].strip()

        for line in request_string[1:]:
            line = line.strip().split(": ")
            if len(line[0]) > 0:
                headers[line[0]] = line[1]

        request["headers"] = headers
        return request
    
    def parseUri(self):
        return self.request["uri"]

