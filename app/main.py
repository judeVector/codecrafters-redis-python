import socket


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    client, addr = server_socket.accept()  # wait for client

    data = client.recv(1024)
    if b"PING" in data:
        client.send(b"+PONG\r\n")

    client.close()


if __name__ == "__main__":
    main()
