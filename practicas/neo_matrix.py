import argparse
import numpy as np
from multiprocessing import Pool

def read_matrix(txt):
    with open(txt, 'r') as f:
        l = [[int(num) for num in line.split(',')] for line in f]
    return l


def calcuate(matriz, operation):
    if operation == 'raiz':
        pass
    elif operation == 'pot':
        for i in range(len(matrix)):
            print(matrix[0][i] ** matrix[0][i])
    elif operation == 'log':
        pass
    else:
        raise ValueError






if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #parser.add_argument("-c", "--calculo", help="calculo a utilizar")
    parser.add_argument("-f", "--file", help="archivo donde se encuentra la matriz")
    parser.add_argument("-p", "--processes", default=2, help="cantidad de procesos")

    args = parser.parse_args()
    txt = args.file
    p = args.processes
    pool = Pool(processes=p)

    matrix = read_matrix(txt)
    #matrix = np.array(matrix)

    for i in range(len(matrix)):
        print(matrix[0][i] * 5)
        #for j in range(len(matrix)):
        #    matrix[i][j] = matrix[i][j] ** matrix[i][j]

    #print(len(matrix))
    calcuate(matrix, 'pot')