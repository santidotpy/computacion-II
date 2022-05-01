import argparse
import mmap
import os
import signal, sys

def show_me_what_you_got():
    for line in mapped_f:
        print(mapped_f.readline().decode())
        #print(line.readline().decode())
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=False, default='mmap_file.txt', help="Archivo para leer")

    args = parser.parse_args()
    
    with open(args.file, mode='a+', encoding='utf-8') as f:
        with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_WRITE) as mapped_f:
            #print(mapped_f.readline().decode())
            n = os.fork()
            # HIJO1
            if n == 0:
                for line in sys.stdin:
                    mapped_f.write(line.encode())
                    if line == 'bye\n':
                        break
                    #print(line)
                mapped_f.flush()
                exit()
                #signal.signal(signal.SIGUSR1, show_me_what_you_got)
            os.wait()
            show_me_what_you_got()

            