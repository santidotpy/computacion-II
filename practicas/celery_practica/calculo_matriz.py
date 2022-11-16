import argparse
from math import log10
from calc_config import app


def read_file(file_name):

    with open(file_name, "r") as f:
        l = [[int(num) for num in line.split(',')] for line in f]
        return l

@app.task
def power_matrix(file_name):
    matrix = read_file(file_name)
    print('Potencia: ')
    return [[num ** num for num in row] for row in matrix]

@app.task
def square_root_matrix(file_name):
    matrix = read_file(file_name)
    print('Raiz cuadrada: ')
    return [[num ** 0.5 for num in row] for row in matrix]

@app.task
def decimal_log_matrix(file_name):
    matrix = read_file(file_name)
    print('Logaritmo decimal: ')
    return [[log10(num)  for num in row] for row in matrix]



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Archivo a leer la matriz", default="matriz.txt")
    parser.add_argument("-c", "--calculo", help="Tipo de calculo a realizar", default="potencia")

    args = parser.parse_args()

    f = args.file
    c = args.calculo

    if c == "potencia":
        power_matrix.delay(f)
    elif c == "raiz":
        square_root_matrix.delay(f)
    elif c == "log":
        decimal_log_matrix.delay(f)
    else:
        print("No se reconoce el calculo")
