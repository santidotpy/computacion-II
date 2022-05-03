import argparse
import mmap
import os
import signal, sys

def show_me_what_you_got(s,f):
    #for line in mapped_f:
    print(len(mapped_f.readline().decode()))
        #print(line.readline().decode())

def popa(a,f):
    print('\nContenido de memoria:')
    print(mapped_f.readline().decode())

def nene2(a,s):
    mapped_f.seek(0)
    f.writelines(mapped_f.readline().decode())
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=False, default='mmap_file.txt', help="Archivo para leer")

    args = parser.parse_args()
    signal.signal(signal.SIGUSR1, popa)
    signal.signal(signal.SIGUSR2, nene2)
    
    with open(args.file, mode='a+', encoding='utf-8') as f:
        #with mmap.mmap(-1, 30, access=mmap.ACCESS_WRITE) as mapped_f:
        with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_WRITE) as mapped_f:
            n = os.fork()
            # HIJO1
            if n == 0:
                for line in sys.stdin:
                    mapped_f.write(line.encode())
                    if line == 'bye\n':
                        #os.kill(os.getppid(), signal.SIGUSR2)
                        break
                    os.kill(os.getppid(), signal.SIGUSR1)
                    os.kill(os.getppid(), signal.SIGUSR2)
                #signal.signal(signal.SIGUSR1, popa)
                exit()
            os.wait()