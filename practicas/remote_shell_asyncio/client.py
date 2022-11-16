# import socket


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-ip", "--host", help="Dirección IP o nombre del servidor al que conectarse", default="127.0.0.1")
#     parser.add_argument("-p", "--port", help="Número de puerto del servidor", default=9999)

#     args = parser.parse_args()
#     h = str(args.host)
#     p = int(args.port)

#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((h, p))
#         while True:
#             word = input('Write something to send: ')
#             if word == 'exit':
#                 break
#             else:
#                 s.sendall(word.encode())
#                 data = s.recv(1024).decode()
#                 print(f"Output:\n {data}")


import argparse
import asyncio

async def tcp_echo_client(host, port):
    reader, writer = await asyncio.open_connection(host, port)


    while True:
        word = input('Write something to send: ')
        if word == 'exit':
            #await writer.wait_closed()
            print('Close the socket')
            writer.close()
            break

        else:
            writer.write(word.encode())
            data = await reader.read(1024)
            print(f"Output:\n {data.decode()}")

            print('Close the connection')
            await writer.drain()

            # s.sendall(word.encode())
            # data = s.recv(1024).decode()
            # print(f"Output:\n {data}")



    #print(reader, writer)
    # print(f'Send: {message!r}')
    # writer.write(message.encode())
    #await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    print(asyncio.current_task())
    await writer.wait_closed()
    

#asyncio.run(tcp_echo_client('Hello World!'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--host", help="Dirección IP o nombre del servidor al que conectarse", default="127.0.0.1")
    parser.add_argument("-p", "--port", help="Número de puerto del servidor", default=1234)

    args = parser.parse_args()
    h = str(args.host)
    p = int(args.port)

    asyncio.run(tcp_echo_client(h, p))