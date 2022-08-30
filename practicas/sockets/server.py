import socket
from ecommands import exe_commands

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            try:
                data = conn.recv(1024)
            except ConnectionResetError:
                print('Connection ended')
                break
            output = exe_commands(data.decode())
            if not data:
                break
            conn.sendall(output.encode())