from socket import *
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind(("", port))

    serverSocket.listen(1)

    while True:
        print('Ready to serve...')
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
                print("200 OK")

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
                print("404 Not Found")
            connectionSocket.close()

        except Exception as e:
            print(f"Error: {e}")
            outputdata = (
                b"HTTP/1.1 500 Internal Server Error\r\n"
                b"Content-Type: text/html; charset=UTF-8\r\n"
                b"\r\n"
            )
            connectionSocket.send(outputdata)
            print("500 Internal Server Error")
        connectionSocket.close()
        sys.exit()


if __name__ == "__main__":
    webServer(13331)