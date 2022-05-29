from threading import Thread
from queue import Queue
import sys
import codecs

def p1_func():
    sys.stdin = open(0)
    msg = sys.stdin.readline()
    q.put(msg)
    print(q2.get())

def p2_func():
    msg = q.get()
    encrypted = codecs.encode(msg, 'rot_13')
    q2.put(encrypted)


if __name__ == '__main__':
    q = Queue()
    q2 = Queue()
    
    t1 = Thread(target=p1_func)
    t2 = Thread(target=p2_func)

    t1.start()
    t2.start()

    t1.join()
    t2.join()