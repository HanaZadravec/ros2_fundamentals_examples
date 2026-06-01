#! /usr/bin/env python3

"""
    Description:
        This ROS 2 node periodically publishes "Hello World" messages to a topic.

------
Publishing Topics:
    The channel containing the "Hello World" messages
    /py_example_topic - std_msgs/String

Subscription Topics:
    None
------
author
date
"""

import rclpy # import the ROS 2 Python client library
from rclpy.node import Node # import the Node class, used for creating ROS 2 nodes

from std_msgs.msg import String # Import String message type for ROS 2

class MinimalPyPublisher(Node):
    """"
        Create a minimal publisher node
    """

    def __init__(self):
        """
            Create a custom node class for publishing messages
        """
        # Initialize the node with the name 'minimal_py_publisher'
        super().__init__('minimal_py_publisher')

        #Create a publisher on the topic with a queue size of 10 messages
        self.publisher1 = self.create_publisher(String, '/py_example_topic', 10)

        #Create a timer with a period of 0.5 seconds to trigger publishing of message
        timer_period = 0.5 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        #Initialize a counter variable for message counter
        self.i = 0
    def timer_callback(self):
        """
            Callback function executed persiodically by the timer
        """

        #Create a new String message object 
        msg = String()

        #Set the message data with a counter
        msg.data = 'Hello World: %d' % self.i

        #publish the message you created above to the topic
        self.publisher1.publish(msg)

        # Log a message indicating the message has been published
        self.get_logger().info('Publishing: "%s"' % msg.data)

        self.i += 1 # Increment the counter for the next message

def main(args=None):
    """
        Main function to start the ROS 2 node
    """
    rclpy.init(args=args) # Initialize the ROS 2 Python client library

    #Create an instance of the MinimalPyPublisher node
    minimal_py_publisher = MinimalPyPublisher()

    rclpy.spin(minimal_py_publisher) # Keep the node running and processing callbacks

    #Destroy the node explicitly 
    minimal_py_publisher.destroy_node()

    #Shutdown the ROS 2 client library/communication
    rclpy.shutdown()

if __name__ == '__main__':
    main() # Call the main function to start the node