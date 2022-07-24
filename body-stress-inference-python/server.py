import socket
import json
from time import sleep

PORT = 1755

def connectSocket(PORT):
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    
    s = socket.socket()
    s.connect((IPAddr, PORT))
    return s

def sendJSONDataToUnity(s, dic):
    jsonResult = json.dumps(dic)
    
    s.send(jsonResult.encode())
    s.close()

# Alone will connect to a socket provided
if __name__ == '__main__':   
    s = connectSocket(PORT)
    sleep(1)
