import socket
import random
import json
from time import sleep

PORT = 1755

def connectSocket(ip):
    s = socket.socket()
    s.connect((ip, PORT))
    return s

def sendRandomColors(s):
    s.send((
        str(random.randint(0,255)) + ","+ 
        str(random.randint(0,255)) + ","+ 
        str(random.randint(0,255)) + ","+ 
        str(random.randint(0,255))).encode())
    s.close()

# Alone will connect to a socket provided
if __name__ == '__main__':
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)
    

    for i in range (100):
        s = connectSocket(IPAddr)
        sendRandomColors(s)
        sleep(1)
