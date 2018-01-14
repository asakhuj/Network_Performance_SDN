import time
import sys
import socket
import datetime

print('Client program')

#server_address = ("10.0.0.2", 9999)

message = "PROBE "
#Create probe packet
while True :
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("127.0.0.1", 1200)
    newStart = time.time()
    message += str(newStart);
    print(message)
    try :
        sent = sock.sendto(message.encode(),server_address)
        time.sleep(10)
        message = "PROBE ";
    finally :
     sock.close();


