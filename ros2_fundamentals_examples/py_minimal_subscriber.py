#! /usr/bin/env python3

"""
Description:
    This ROS 2 node subscribes to "Hello World" messages published on a topic and logs them.
------
Publishing Topics:
    None
------
Subscription Topics:
    The channel containing the "Hello World" messages
    /py_example_topic - std_msgs/String

author
date
"""

import rclpy # import the ROS 2 Python client library
from rclpy.node import Node # import the Node class, used for creating ROS 2 nodes

from std_msgs.msg import String # Import String message type for ROS 2

class MinimalPySubscriber(Node):
    def __init__(self):
        super().__init__('minimal_py_subscriber')

        self.subscriber1 = self.create_subscription(
                                String, 
                                '/py_example_topic', 
                                self.listener_callback, 
                                10)
        
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    minimal_py_subscriber = MinimalPySubscriber()

    rclpy.spin(minimal_py_subscriber)

    minimal_py_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()