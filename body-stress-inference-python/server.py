import socket
# import random
import json
from time import sleep
# import pose

PORT = 1755

def connectSocket(PORT):
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    
    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)
    
    s = socket.socket()
    s.connect((IPAddr, PORT))
    return s

# def sendRandomColors(s):
#     dic = pose.determining_joints()
#     print(dic)
#     jsonResult = json.dumps(dic)
#     # print(jsonResult)
    
#     s.send(jsonResult.encode())
#     s.close()
    
def sendJSONDataToUnity(s, dic):
    jsonResult = json.dumps(dic)
    
    s.send(jsonResult.encode())
    s.close()

# Alone will connect to a socket provided
if __name__ == '__main__':
    # hostname = socket.gethostname()
    # IPAddr = socket.gethostbyname(hostname)
    # print("Your Computer Name is:" + hostname)
    # print("Your Computer IP Address is:" + IPAddr)
    
    s = connectSocket(PORT)
    # sendRandomColors(s)
    sleep(1)
