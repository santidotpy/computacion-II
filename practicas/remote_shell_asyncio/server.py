# import socket
# from multiprocessing import Process
# from threading import Thread

# # HOST = "127.0.0.1"
# # PORT = 65432
# def new_connection(host="127.0.0.1", port=9999):

#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         s.bind((host, port))
#         s.listen()
#         conn, addr = s.accept()
#         with conn:
#             print(f"Connected by {addr}")
#             while True:
#                 try:
#                     data = conn.recv(1024)
#                 except ConnectionResetError:
#                     print('Connection ended')
#                     break
#                 output = exe_commands(data.decode())
#                 if not data:
#                     break
#                 conn.sendall(output.encode())

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-ip", "--host", help="Dirección IP o nombre del servidor al que conectarse", default="127.0.0.1")
#     parser.add_argument("-p", "--port", help="Número de puerto del servidor", default=65432)
#     parser.add_argument("-c", "--concurrency", help="Tipo de concurrencia a utilizar", default=None)

#     args = parser.parse_args()
#     p = int(args.port)
#     c = str(args.concurrency) if args.concurrency != None else None # str si es distinto de None

#     # usara Process o Thread segun se indique, o ninguno en caso de no especificar
#     if c == None:
#         new_connection()
#     elif c == 'p':
#         pr = Process(target=new_connection, args=("127.0.0.1", p,))
#         pr.start()
#         pr.join()
#     elif c == 't':
#         t = Thread(target = new_connection, args=("127.0.0.1", p,))
#         t.start()
#         t.join()
    


import argparse
import asyncio
from ecommands import exe_commands
import time

async def handle_echo(reader, writer):
    #print(f"Esperando datos del cliente (durmiendo {asyncio.all_tasks()})")
    for t in asyncio.all_tasks():
        print(f"Tarea: {t}")
    #data = await reader.read(100)
    #message = data.decode()
    addr = writer.get_extra_info('peername')


    while True:
        try:
            data = await reader.read(1024)
        except ConnectionResetError:
            print('Connection ended')
            break
        output = exe_commands(data.decode())
        if not data:
            break
        writer.write(output.encode())
        await writer.drain()
        
        #conn.sendall(output.encode())

    #await writer.drain()

    print("Close the connection")
    writer.close()
    for t in asyncio.all_tasks():
        print(f"Cerrando Tarea: {t}")

async def main(port):
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', port)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr} {asyncio.current_task()}')

#    async with server:
    print(f"Tareas:\n{asyncio.all_tasks()}")
    await server.serve_forever()

#asyncio.run(main())



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="Número de puerto del servidor", default=1234)

    args = parser.parse_args()
    p = int(args.port)

    asyncio.run(main(p))

