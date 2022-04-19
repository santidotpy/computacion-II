import argparse
import os


    #o_file = os.open(args.output_file, os.O_WRONLY | os.O_CREAT | os.O_APPEND)
    #l_file = os.open(args.log_file, os.O_WRONLY | os.O_CREAT | os.O_APPEND)


def create_child():
    n = os.fork()
    if n == 0:
        p_id = os.getpid()
        print(f'Hijo: {p_id}')
        os._exit(0)
    else:
        os.wait()
        print(f'PADRE: {os.getpid()}\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=False, default=os.getcwd(), help="Archivo para leer")
    parser.add_argument("-v", "--verboso",required=False, default=0, help="Activa el modo verboso (1 para activarlo)")

    args = parser.parse_args()
    txt = args.file
    verb = int(args.verboso)

    # abro el archivo o lo crea
    #if txt == os.getcwd():
    #    f = open('tuberiadeMario.txt')
        #number_of_lines = len(f.readlines())
        #os.close(f)
    #else:
    #    f = open(txt, 'r')

    if txt == os.getcwd():
        f = os.open('tuberiadeMario.txt', os.O_RDONLY)
        #os.close(f)
    else:
        f = os.open(txt, os.O_RDONLY)

    #n_lines = len(f.readlines())
    #with open(txt) as f:
    #    n_lines = len(f.readlines())
    #    print(n_lines)
    #    print(f.readlines())

    #r, w = os.pipe()
    reading = os.read(f, 1024)
    n_lines = len(list(reading.decode().splitlines()))
    lineas_list = list(reading.decode().splitlines())

    #r = os.fdopen(r)
    #w = os.fdopen(w, 'w')


    for i in range(n_lines):
        r, w = os.pipe()
        r = os.fdopen(r)
        w = os.fdopen(w, 'w')
        w.write(lineas_list[i])
        w.close()
        n = os.fork()

        if n == 0:
            leido = r.readline()[::-1]
            print(leido)
            r.close()
            p_id = os.getpid()
            print(f'Hijo: {p_id}')
            os._exit(0)

        else:
            os.wait()
            print(f'PADRE: {os.getpid()}\n')

        w.close()
        
    os.close(f)



