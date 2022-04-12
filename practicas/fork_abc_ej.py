import argparse
import os
from string import ascii_uppercase
import time



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--numero", type=int, default=1, help="Cantidad de procesos hijos")
    parser.add_argument("-r", "--repeticion", default=1, required=False, help="Cantidad de veces que el proceso escribe la letra")
    parser.add_argument("-f", "--path", required=False, default=os.getcwd(), help="Path del archivo de texto")
    parser.add_argument("-v", "--verboso",required=False, default=0, help="Activa el modo verboso (1 para activarlo)")

    args = parser.parse_args()
    txt = args.path
    verb = int(args.verboso)
    repeticiones = int(args.repeticion)
    alphabet = list(ascii_uppercase)
    
    # abro el archivo o lo crea
    if txt == os.getcwd():
        f = open('abc.txt', 'w')
        #os.close(f)
    else:
        f = open(txt, 'w')

    # lo recorro para crear a los nenes
    for i in range(args.numero):

        n = os.fork()
        if n == 0:
            p_id = os.getpid()
            
            # modo verboso
            if verb == 1:
                print(f'Proceso <{p_id}> escribiendo letra {alphabet[i]}')

            # escribo en el archivo
            f.write(alphabet[i])
            #os.write(f, (alphabet[i]).encode())

            f.flush()
            time.sleep(1)
            # segun la cantidad de repeticines especificada
            if repeticiones > 1:
                r = 1
                while r < repeticiones:
                    print(f'Proceso <{p_id}> escribiendo letra {alphabet[i]}')
                    f.write(alphabet[i])
                    #os.write(f, (alphabet[i]).encode())
                    f.flush()
                    time.sleep(1)
                    r += 1

            #os.write(f, (alphabet[i]).encode())
            os._exit(0)
        else:
            os.wait()
        #os.write(f, (alphabet[i]+'\n').encode()) 
    f.close()
    
    # Leo de nuevo los archivos para mostrarlos
    if txt == os.getcwd():
        with open('abc.txt') as fl:
            print('\n\nContenido del archivo: ')
            print(fl.read())
    else:
        with open(txt) as fl:
            print('\n\nContenido del archivo: ')
            print(fl.read())
