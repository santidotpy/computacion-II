import argparse
import os
from string import ascii_uppercase


#def create_child(letra):
#   n = os.fork()
#    if n == 0:
#        p_id = os.getpid()
#        print(letra)
#        os._exit(0)

    #else:
    #    os.wait()
    #    print(f'SOY TU PADRE: {os.getpid()}\n')


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
    print(repeticiones)
    #this_is_my_file = os.open(args.path, os.O_WRONLY | os.O_CREAT | os.O_APPEND)

    if txt == os.getcwd():
        f = os.open('abc.txt', os.O_WRONLY | os.O_CREAT)
        #os.close(f)
    else:
        f = os.open(txt, os.O_WRONLY | os.O_CREAT | os.O_APPEND)

    # aca va el codigo que interactua con el archivo
    for i in range(args.numero):
        #create_child(alphabet[i])

        n = os.fork()
        if n == 0:
            p_id = os.getpid()
            if verb == 1:
                print(f'Proceso <{p_id}> escribiendo letra {alphabet[i]}')

            os.write(f, (alphabet[i]).encode())
            if repeticiones > 1:
                r = 1
                while r < repeticiones:
                    print(f'Proceso <{p_id}> escribiendo letra {alphabet[i]}')
                    os.write(f, (alphabet[i]).encode())
                    r += 1



            #os.write(f, (alphabet[i]).encode())
            os._exit(0)

        else:
            os.wait()

        #os.write(f, (alphabet[i]+'\n').encode())

    
    
    os.close(f)



    


