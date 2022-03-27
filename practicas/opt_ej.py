import getopt
import sys


def main():
    # parsear del primero al ultimo
    argv = sys.argv[1:]

    options = 'n:o:m:'
    options_names = ['numero1=', 'operador=', 'numero2=']
    operadores = ['+', '-', '*', '/']

    
    opts, args = getopt.getopt(argv, options, options_names)

    for opt, arg in opts:
        #print(type(opt), type(arg))
        if opt in ['-n', '--numero1']:
            numero1 = int(arg)
            #print(numero1)
        elif opt in ['-o', '--operador']:
            operador = arg
            print(operador)
            if operador not in operadores:
                raise ValueError
        elif opt in ['-m', '--numero2']:
            numero2 = int(arg)
            #print(numero2)

    calc(numero1, numero2, operador)

    
def calc(numero1, numero2, operador):
    if operador == '+':
        print(f'{numero1} + {numero2} = {numero1 + numero2}')
    elif operador == '-':
        print(f'{numero1} - {numero2} = {numero1 - numero2}')
    elif operador == '*':
        print(f'{numero1} * {numero2} = {numero1 * numero2}')
    elif operador == '/':
        if numero2 == 0:
            raise ValueError
        print(f'{numero1} / {numero2} = {numero1 / numero2}')



main()
# -n 10 -o / -m 5