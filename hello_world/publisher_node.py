#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def publisher():
    rospy.loginfo("Node has been started.")

    pub = rospy.Publisher("/hello_world", String, queue_size = 10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        pub.publish("Hello World")
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node("hello_publisher")
        publisher()
    except rospy.ROSInterruptException:
        pass