from socket import *
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.connect(("127.0.0.1", port))

    serverSocket.listen(1)

    while True:
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]

            f = open(filename[1:], "rb")

            if f:
                outputdata = (
                    b"HTTP/1.1 200 OK\r\n"
                    b"Content-Type: text/html; charset=UTF-8\r\n"
                    b"\r\n"
                )
                connectionSocket.send(outputdata)

                for i in f:
                    connectionSocket.send(i)
                f.close()

            else:
                outputdata = (
                    b"HTTP/1.1 404 Not Found\r\n"
                    b"Content-Type: text/html; charset=UTF-8\r\n"
                    b"\r\n"
                )
                connectionSocket.send(outputdata)
            connectionSocket.close()

        except Exception as e:
            outputdata = (
                b"HTTP/1.1 500 Internal Server Error\r\n"
                b"Content-Type: text/html; charset=UTF-8\r\n"
                b"\r\n"
            )
            connectionSocket.send(outputdata)
        connectionSocket.close()
        sys.exit()


if __name__ == "__main__":
    webServer(13331)