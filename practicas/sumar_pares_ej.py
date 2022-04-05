import argparse
import os
import time


def create_child():
    n = os.fork()
    if n == 0:
        p_id = os.getpid()
        print(f'{p_id} - {os.getppid()}: {sumar_pares(p_id)}')
    else:
        os.wait()
        print(f'SOY TU PADRE: {os.getpid()}\n')
        

def create_verbose_child():
    n = os.fork()
    if n == 0:
        p_id = os.getpid()
        print('Inicio del nene: ', os.getpid())
        print(f'{p_id} - {os.getppid()}: {sumar_pares(p_id)}')
        print(f'Fin del nene {p_id}\n')
    else:
        os.wait()
        print(f'SOY TU PADRE: {os.getpid()}\n')


def sumar_pares(pid):
    n = 0
    suma = 0

    while n <= pid:
        if n % 2 == 0:
            suma = suma + n
        n += 1
    return suma



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--numero", help="numero de procesos para generar")
    parser.add_argument("-v", "--verboso", help="activa el modo verboso")

    args = parser.parse_args()

    number_of_p = int(args.numero)

    if args.verboso:
        for p in range(1, number_of_p):
            create_verbose_child()
            time.sleep(.5)

    else:
        for p in range(1, number_of_p):
            create_child()
            time.sleep(.5)

        