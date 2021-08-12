import serial
import time
ser = serial.Serial('COM6',9600)
time.sleep(2)

b = "both box is not reached"
print (b)
while True: 
#for i in range(10):

    b = ser.readline()

    #print ("number ", i, "is", b)
    print (b)

#ser.close()



