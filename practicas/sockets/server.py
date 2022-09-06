import socket
import argparse
from ecommands import exe_commands
from multiprocessing import Process
from threading import Thread

# HOST = "127.0.0.1"
# PORT = 65432
def new_connection(host="127.0.0.1", port=65432):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--host", help="Dirección IP o nombre del servidor al que conectarse", default="127.0.0.1")
    parser.add_argument("-p", "--port", help="Número de puerto del servidor", default=65432)
    parser.add_argument("-c", "--concurrency", help="Tipo de concurrencia a utilizar", default=None)

    args = parser.parse_args()
    p = int(args.port)
    c = str(args.concurrency) if args.concurrency != None else None # str si es distinto de None

    # usara Process o Thread segun se indique, o ninguno en caso de no especificar
    if c == None:
        new_connection()
    elif c == 'p':
        pr = Process(target=new_connection, args=("127.0.0.1", p,))
        pr.start()
        pr.join()
    elif c == 't':
        t = Thread(target = new_connection, args=("127.0.0.1", p,))
        t.start()
        t.join()
    