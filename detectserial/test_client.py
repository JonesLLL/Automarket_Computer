from aubo_messages.srv import NotSwitch

import rclpy
from rclpy.node import Node


class SwitchClientAsync(Node):

    def __init__(self):
        super().__init__('switch_client_async')
        self.cli = self.create_client(NotSwitch, 'switch_state_feedback')       # CHANGE
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')


    def send_request(self):
        req = NotSwitch.Request()
        req.request = True
        self.future = self.cli.call_async(req)


def main(args=None):
    rclpy.init(args=args)

    minimal_client = SwitchClientAsync()
    minimal_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
            try:
                response = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                minimal_client.get_logger().info(
                    'Result: for %d, left open:%r, right open:%r' %
                    (response.stamp, response.left_open, response.right_open))
            break

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()