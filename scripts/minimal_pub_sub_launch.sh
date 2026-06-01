#! /bin/bash
# Launch publisher and subscriber nodes with cleanup handling

cleanup() {
    echo "Restaring ROS 2 deamon to cleanup before shutting down all processes..."
    ros2 deamon stop
    sleep 1
    ros2 deamon start
    echo "Terminating all ROS 2-related processes..."
    kill 0
    exit
}

# start cleanup function on SIGINT (Ctrl+C)
trap 'cleanup' SIGINT

#Launch the publisher node
ros2 run ros2_fundamentals_examples py_minimal_publisher.py &

sleep 2

#Launch the subscriber node
ros2 run ros2_fundamentals_examples py_minimal_subscriber.py



