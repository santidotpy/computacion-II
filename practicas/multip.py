from multiprocessing import Process, Pipe, Queue
import sys
import codecs

def p1_func(conn):
    sys.stdin = open(0)
    msg = sys.stdin.readline()
    conn.send(msg)
    conn.close()
    print(q.get())

def p2_func(conn):
    msg = conn.recv()
    encrypted = codecs.encode(msg, 'rot_13')
    q.put(encrypted)


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    q = Queue()
    p1 = Process(target=p1_func, args=(child_conn,))
    p2 = Process(target=p2_func, args=(parent_conn,))

    p1.start()
    p2.start()

    p2.join()
    p1.join()