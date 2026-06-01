#! usr/bin/env python3

"""
    Test suite for ROS 2 minimal publisher node.

    This script contains unit tests for verifying the functionality of a minimal ROS 2 publisher.
    It tests the node creation, message counter increment, and message content formatting.

------
Subscription Topics:
    None
------
Publishing Topics:
    /py_example_topic - std_msgs/String : Example messages with incrementing counter
"""
import pytest
import rclpy
from std_msgs.msg import String
from ros2_fundamentals_examples.py_minimal_publisher import MinimalPyPublisher

def test_publisher_creation():
    """
        Test if the publisher node is created correctly.

        This test verifies:
        1. The node name is set correctly.
        2. The publisher object exists.
        3. The topic name is correct.

        :raises AssertionError: If any of the assertions fail.
    """
    #Initialize ROS 2 communication
    rclpy.init()

    try:
        #Create an instance of the publisher node
        node = MinimalPyPublisher()

        #Test 1 : Check if the node name is correct
        assert node.get_name() == 'minimal_py_publisher'

        #Test 2 : Check if the publisher object is created and has the correct topic name
        assert hasattr(node, 'publisher1')
        assert node.publisher1.topic_name == '/py_example_topic'
    finally:
        #Shutdown ROS 2 communication
        rclpy.shutdown()

def test_message_counter():
    """
        Test if the message counter increments correctly.

        This test verifies that the counter(node.i) increments by 1 each time the timer callback is called.

        :raises AssertionError: If the counter does not increment as expected.   
    """    
    rclpy.init()
    try:
        node = MinimalPyPublisher()

        initial_counter = node.i

        node.timer_callback() # Simulate a timer callback to publish a message
        assert node.i == initial_counter + 1, "Counter did not increment correctly after first callback"
    finally:
        rclpy.shutdown()


def test_message_content():
    """
        Test if the message content is formatted correctly.

        This test verifies that the message string is properly formatted using an f-string with the current
        counter value.

        :raises AssertionError: If the message content does not match the expected format.
    """    
    rclpy.init()
    try:
        node = MinimalPyPublisher()

        #Set counter to a known value for testing
        node.i = 5
        msg = String()
        
        #Using f-string instead of the old string formatting method
        msg.data = f'Hello World: {node.i}'
        assert msg.data == 'Hello World: 5'
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    pytest.main(['-v'])