import argparse
from math import log10
import numpy as np
from multiprocessing import Pool


def read_matrix(txt):
    with open(txt, 'r') as f:
        l = [[int(num) for num in line.split(',')] for line in f]
    return l

def calcuate_pot(matriz):
    for item in matriz:
        print(item ** item)

def calculate_sqrt(matriz):
    for item in matriz:
        print(item ** 0.5)
        
def calculate_log(matriz):
    for item in matriz:
        print(np.log10(item))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--calculo", help="calculo a utilizar")
    parser.add_argument("-f", "--file", help="archivo donde se encuentra la matriz")
    parser.add_argument("-p", "--processes", default=2, help="cantidad de procesos")

    args = parser.parse_args()
    txt = args.file
    p = int(args.processes)
    c = args.calculo
    pool = Pool(processes=p)

    matrix = read_matrix(txt)
    matrix = np.array(matrix)
    matrix = np.split(matrix, len(matrix))


    if c == 'pot':
        pool.map(calcuate_pot, matrix)
    elif c == 'raiz':
        pool.map(calculate_sqrt, matrix)
    elif c == 'log':
        pool.map(calculate_log, matrix)

    pool.close()
    pool.join()
