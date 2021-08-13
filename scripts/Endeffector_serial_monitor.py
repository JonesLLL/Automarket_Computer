import os
import serial
import time
ser = serial.Serial('COM6', 9600)

A = "Start system"
print(A)

def detecting_Serial():

    # while True:
    #     try:
    #         if os.name == 'nt':# if the system is windows
    #             ser = serial.Serial('COM6', 9600)
    #         else:
    #             ser = serial.Serial('/dev/ttyUSB0', 9600)
    #     except IOError:
    #         print("[ERROR]: cannot open /dev/ttyUSB0, no such file or permission denied")
    #     else:
    #         if ser.is_open:
    #             break
    #     time.sleep(2)

    # b = 0
    while True:
        time.sleep(0.1)
        b = ord(ser.read(1))
        print (b)
  









detecting_Serial()
