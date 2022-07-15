import socket
import random
import json
from time import sleep

def connectSocket(ip, port):
    s = socket.socket()
    s.connect((ip, port))
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
    print("Your Computer Name is:"+hostname)
    print("Your Computer IP Address is:"+IPAddr)
    
    s = connectSocket(IPAddr, 1755)
    for i in range (100):
        sendRandomColors(s)
        sleep(1)
