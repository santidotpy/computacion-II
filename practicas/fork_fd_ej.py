import argparse
import os
from string import ascii_uppercase



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--numero", help="Cantidad de procesos hijos")
    parser.add_argument("-r", "--repeticion", default=1, required=False, help="Cantidad de veces que el proceso escribe la letra")
    parser.add_argument("-f", "--path", required=False, default=os.getcwd(), help="Path del archivo de texto")
    parser.add_argument("-v", "--verboso",required=False, default=0, help="Activa el modo verboso (1 para activarlo)")

    args = parser.parse_args()
    txt = args.path

    alphabet = list(ascii_uppercase)
    #this_is_my_file = os.open(args.path, os.O_WRONLY | os.O_CREAT | os.O_APPEND)

    if txt == os.getcwd():
        f = os.open('abc.txt', os.O_WRONLY | os.O_CREAT | os.O_APPEND)
        #os.close(f)
    else:
        f = os.open(txt, os.O_WRONLY | os.O_CREAT | os.O_APPEND)

    # aca va el codigo que interactua con el archivo    
    
    
    os.close(f)



    


