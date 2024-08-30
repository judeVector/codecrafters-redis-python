import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    pong = "+PONG\r\n"

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    server_socket.accept()  # wait for client
    conn, addr = server_socket.accept()

    with conn:
        conn.recv(1024)
        conn.sendallS(pong.encode())

    server_socket.close()


if __name__ == "__main__":
    main()
