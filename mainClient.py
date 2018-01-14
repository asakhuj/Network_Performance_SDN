import time
import sys
import socket
import datetime
import thread

print('Client program')

def serverThread(address,portNumber) :
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
    serverSocket.bind((address, portNumber))
    while True:
        print("Client working as server")
        dataReceived, receivedFrom = serverSocket.recvfrom(4096)
        print("data received")
        print(dataReceived.decode());

message = "PROBE "
print("After starting thread")
thread.start_new_thread(serverThread,("10.0.0.1",1301));
#Create probe packet
while True :
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("10.0.0.2", 1200)
    #sock.bind(("127.0.0.1",1300))
    #print(sock.getsockname());
    #myAddr,myPort = sock.getsockname();
    newStart = time.time()
    message += str(newStart);
    print(message)
    try :
        sent = sock.sendto(message.encode(),server_address)
        message = "PROBE ";
        sock.close();
        time.sleep(1);
    finally :
     sock.close();


