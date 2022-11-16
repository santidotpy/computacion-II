import argparse
import asyncio

async def tcp_echo_client(host, port):
    reader, writer = await asyncio.open_connection(host, port)

    while True:
        word = input('Write something to send: ')
        if word == 'exit':
            print('Close the connection')
            break

        else:
            writer.write(word.encode())
            data = await reader.read(1024)
            print(f"Output:\n {data.decode()}")
            await writer.drain()

    print('Connection ended')
    writer.close()
    await writer.wait_closed()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--host", help="Dirección IP o nombre del servidor al que conectarse", default="127.0.0.1")
    parser.add_argument("-p", "--port", help="Número de puerto del servidor", default=1234)

    args = parser.parse_args()
    h = str(args.host)
    p = int(args.port)

    asyncio.run(tcp_echo_client(h, p))