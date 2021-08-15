from aubo_messages.srv import NotSwitch
import rclpy
from rclpy.node import Node
import os
import serial
import time
import _thread

class SwitchServer(Node):
    def __init__(self, lock):
        super().__init__('switch_server')
        self.srv = self.create_service(NotSwitch, 'switch_state_feedback', self.switch_callback)
        self.left = 4   # 3 is closed; 4 is opened
        self.right = 2  # 1 is closed; 2 is opened
        self.lock = lock

    def switch_callback(self, request, response):
        self.get_logger().info('Incoming request: %r' % (request.request))
        response.stamp = int(time.time())

        self.lock.acquire()
        if self.left == 4:
            response.left_open = True
        else:
            response.left_open = False
        if self.right == 2:
            response.right_open = True
        else:
            response.right_open = False
        self.lock.release()

        return response

    def detecting_Serial(self):

        # waiting until the com port has been opened
        while True:
            try:
                if os.name == 'nt':  # if the system is windows
                    ser = serial.Serial('COM6', 9600)
                else:
                    ser = serial.Serial('/dev/ttyUSB0', 9600)
            except IOError:
                print("[ERROR]: cannot open /dev/ttyUSB0, no such file or permission denied")
            else:
                if ser.is_open:
                    break
            time.sleep(2)

        while True:
            state = ord(ser.read(1))  # this read is a synchronizied read, will stop until data is received
            self.lock.acquire()
            if state == 1:
                self.right = 1
            elif state == 2:
                self.right = 2
            elif state == 3:
                self.left = 3
            elif state == 4:
                self.left = 4
            self.lock.release()

def main(args=None):
    rclpy.init(args=args)

    lock = _thread.allocate_lock()
    minimal_server = SwitchServer(lock)

    if rclpy.ok():
        detector_handler = _thread.start_new_thread(minimal_server.detecting_Serial, ())
    rclpy.spin(minimal_server)
    rclpy.shutdown()


if __name__ == '__main__':
    main()



