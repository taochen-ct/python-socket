import socket

def relay(source_port, destination_port):
    source_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    source_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    source_socket.bind(('', source_port))
    source_socket.listen()

    destination_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    destination_socket.connect(('localhost', destination_port))

    while True:
        source_conn, source_addr = source_socket.accept()
        destination_conn, destination_addr = destination_socket.accept()

        while True:
            data = source_conn.recv(4096)
            if len(data) == 0:
                break
            destination_conn.sendall(data)

        source_conn.close()
        destination_conn.close()

relay(8080, 3000)

