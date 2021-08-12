import os
import serial
import time

# if the system is windows
if os.name == 'nt':
    ser = serial.Serial('COM6', 9600)
else:
    ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)

b = 0
while True:
    b = ser.readline()
    print (b)


