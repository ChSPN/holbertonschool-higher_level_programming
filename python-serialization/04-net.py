#!/usr/bin/env python3
def start_server():
    """
    Starts a server that listens for incoming connections, deserializes
    received data, and prints it.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    while True:
        client_socket, addr = server_socket.accept()
        data = client_socket.recv(1024)
        dictionary = json.loads(data.decode())
        print(f"Received Dictionary from Client:\n{dictionary}")

        client_socket.close()
        break

    server_socket.close()


def send_data(dictionary):
    """
    Connects to a server, serializes a Python dictionary, and sends it.

    Args:
        dictionary (dict): The dictionary to serialize and send.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    data = json.dumps(dictionary).encode()
    client_socket.send(data)

    client_socket.close()
