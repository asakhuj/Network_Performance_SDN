import socket
import time
import datetime

print('Server  program')
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 1200
serverIp = "10.0.0.2"
#serverIp = "127.0.0.1"
serverSocket.bind((serverIp, port))
numberOfSamples =0;
timeList =[0];
while True:
      print('Inside')
      data,address = serverSocket.recvfrom(4096)
      print('Data received at server port')
      print(data)
      newData = data.decode();
      print(newData[0:5] == 'PROBE')
      if (newData[0:5] == 'PROBE') :
          startTime = newData[6:];
          newEndTime = time.time();
          newDelay = newEndTime - float(startTime);
          print("delay");
          print(newDelay)
          numberOfSamples = numberOfSamples +1;
          timeList = timeList +[newDelay];
          print(timeList)
          print(numberOfSamples)
          sumTotal =0;
          if(numberOfSamples == 10) :
              print('inside 2')
              while ( numberOfSamples >0 ) :
                  sumTotal = sumTotal + float(timeList[numberOfSamples]);
                  numberOfSamples = numberOfSamples -1;
              average = sumTotal/10;
              print("average is ");
              print(average)
              timeList=[0];
              numberOfSamples=0;
              #Create Delay packet now
              delayMessage = "DELAY "+ str(average*1000);
              sendDelayMessage = serverSocket.sendto(delayMessage.encode(),("10.0.0.1", 1301));
              print("After sending")


