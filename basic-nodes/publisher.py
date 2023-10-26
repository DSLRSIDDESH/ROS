#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def publisher_node():
    rospy.init_node("publisher_node", anonymous = True)
    pub = rospy.Publisher("chatter", String, queue_size = 10)

    rate = rospy.Rate(20) #20 Hz
    counter = 0

    while not rospy.is_shutdown():
        msg = f"This is a message from publisher {counter}"
        pub.publish(msg)

        rate.sleep()
        counter += 1

if __name__ == "__main__":
    publisher_node()