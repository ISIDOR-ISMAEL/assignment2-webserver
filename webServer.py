from socket import *
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind(("127.0.0.1", port))

    serverSocket.listen(1)

    while True:
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]

            f = open(filename[1:], "rb")
            htmlcontent = f.read()
            f.close()

            outputdata = (
                "HTTP/1.1 200 OK\r\n"
                "Server: webServerHello\r\n"
                "Content-Type: text/html; charset=UTF-8\r\n"
                "Connection: close\r\n"
                "\r\n"
            )
            connectionSocket.sendall(outputdata.encode() + htmlcontent)

            for i in f:
                connectionSocket.sendall(i)

        except Exception as e:
            outputdata = (
                "HTTP/1.1 404 Not Found\r\n"
                "Server: webServerHello\r\n"
                "Content-Type: text/html; charset=UTF-8\r\n"
                "Connection: close\r\n"
                "\r\n"
            )
            connectionSocket.sendall(outputdata.encode())
        connectionSocket.close()


if __name__ == "__main__":
    webServer(13331)