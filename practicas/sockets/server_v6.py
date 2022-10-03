# Modificar el código de shell remota realizado con anterioridad ([serversocket]) para que atienda en todas las IP's del sistema operativo, independientemente de que se trate de IPv4 o IPv6.

# Lance un thread para cada socket.

# El servidor de shell debe mantener la concurrencia para atender a varios clientes, ya sea por procesos o hilos, dependiendo del parámetro pasado por argumento "-c".



import socketserver, socket, threading

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())




class server_forking(socketserver.TCPServer, socketserver.ForkingMixIn):
    pass

class server_threading(socketserver.TCPServer, socketserver.ThreadingMixIn):
    pass


class server_forking_v6(socketserver.TCPServer, socketserver.ForkingMixIn):
    address_family = socket.AF_INET6
    pass

class server_threading_v6(socketserver.TCPServer, socketserver.ThreadingMixIn):
    address_family = socket.AF_INET6
    pass




# class server6 (socketserver.TCPServer):
#     address_family = socket.AF_INET6
#     pass
# class server (socketserver.TCPServer):
#     pass

def servicio(d, c):
    # en la pos 0 de d esta address family
    if c=='t':
        if d[0] == socket.AF_INET: 
            print("ipv4")
            with server_threading((HOST, PORT), MyTCPHandler) as servidor:
                servidor.serve_forever()
        elif d[0] == socket.AF_INET6:
            print("ipv6")
            with server_threading_v6((HOST, PORT), MyTCPHandler) as servidor:
                servidor.serve_forever()
    elif c=='p':
        if d[0] == socket.AF_INET: 
            print("ipv4")
            with server_forking((HOST, PORT), MyTCPHandler) as servidor:
                servidor.serve_forever()
        elif d[0] == socket.AF_INET6:
            print("ipv6")
            with server_forking_v6((HOST, PORT), MyTCPHandler) as servidor:
                servidor.serve_forever()


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    socketserver.TCPServer.allow_reuse_address = True
    c = 't'
    # Create the server, binding to localhost on port 9999
    direcciones = socket.getaddrinfo("localhost", 5000, socket.AF_UNSPEC, socket.SOCK_STREAM)
    hilo = []
    print(direcciones)
    for d in direcciones:
        print(d[0])
        hilo.append(threading.Thread(target=servicio, args=(d, c)))

    for h in hilo:
        h.start()




"""

server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
server.serve_forever()
server.handle_request()

"""
