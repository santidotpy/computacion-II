import argparse



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-h", "--host", help="Dirección IP o nombre del servidor al que conectarse", default=65432)
    parser.add_argument("-p", "--port", help="Número de puerto del servidor", default="127.0.0.1")