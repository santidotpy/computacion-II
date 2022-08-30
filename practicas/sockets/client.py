import socket
import argparse




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--host", help="Dirección IP o nombre del servidor al que conectarse", default="127.0.0.1")
    parser.add_argument("-p", "--port", help="Número de puerto del servidor", default=65432)

    args = parser.parse_args()
    h = str(args.host)
    p = int(args.port)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((h, p))
        word = 'xd'
        while True:
            word = input('Write something to send: ')
            if word == 'exit':
                break
            else:
                s.sendall(word.encode())
                data = s.recv(1024).decode()
                print(f"Output:\n {data!r}")