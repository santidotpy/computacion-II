import argparse
import os
from subprocess import Popen, PIPE
from datetime import datetime



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--command", help="comando a ejecutar")
    parser.add_argument("-f", "--output_file", help="archivo para almacenar la salida")
    parser.add_argument("-l", "--log_file", help="arcivo log")

    args = parser.parse_args()

    o_file = os.open(args.output_file, os.O_WRONLY | os.O_CREAT | os.O_APPEND)
    l_file = os.open(args.log_file, os.O_WRONLY | os.O_CREAT | os.O_APPEND)

    p1 = Popen(args.command, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p1.communicate()
    log_out = f'Fecha y hora: {datetime.now()}, Comando: {args.command} ejecutado correctamente\n'.encode()

    if p1.returncode == 0:
        #print(p1.stdout)
        os.write(o_file, out)
        os.write(l_file, log_out)
    else:
        os.write(l_file, err)


    os.close(o_file)
    os.close(l_file)

