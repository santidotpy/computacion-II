import argparse
import asyncio
from ecommands import exe_commands

async def handle(reader, writer):
    for t in asyncio.all_tasks():
        print(f"Task: {t}")
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
        
    
    print(f"Close the connection {addr}")
    writer.close()
    for t in asyncio.all_tasks():
        print(f"Ending Task: {t}")

async def main(port):
    server = await asyncio.start_server(
        handle, '127.0.0.1', port)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr} {asyncio.current_task()}')

    #async with server:
    print(f"Tasks:\n{asyncio.all_tasks()}")
    await server.serve_forever()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="Número de puerto del servidor", default=1234)

    args = parser.parse_args()
    p = int(args.port)

    asyncio.run(main(p))

