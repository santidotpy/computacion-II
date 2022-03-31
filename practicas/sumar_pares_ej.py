import argparse
import os
import time


def create_child():
    n = os.fork()
    if n != 0:
        os.wait()
        show_this = f'SOY TU PADRE: {os.getpid()}'
        #return 'SOY TU PADRE ID: ', os.getpid()
        return show_this
    else:
        p_id = os.getpid()
        show_this = f'Soy el hijo {p_id}, la suma de mis numeros pares es: {sumar_pares(p_id)}'
        #print('Total de la suma de sus numeros pares: ', sumar_pares(p_id))
        #return 'Hijo ID: ', p_id
        return show_this

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


    # ver como implementar esto del verboso
    if args.verboso:
        for p in range(number_of_p):
            print(create_child())
            time.sleep(.5)

    else:
        for p in range(number_of_p):
            print(create_child())
            time.sleep(.5)

        