import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    client, addr = server_socket.accept()  # wait for client

    data = client.recv(1024)  # receive data from client
    if b"PING" in data:
        client.send(b"+PONG\r\n")

    client.close()  # close the client connection


if __name__ == "__main__":
    main()
