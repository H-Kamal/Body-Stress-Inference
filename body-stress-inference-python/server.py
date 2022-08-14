import socket
import json
from time import sleep

# Connects to your own IP which is what the Unity server is set up to receive
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

# Tests the server standalone. will connect to a socket provided
if __name__ == '__main__':
    PORT = 1755   
    s = connectSocket(PORT)
    sleep(1)
