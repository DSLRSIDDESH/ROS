#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback_fn(msg: String):
    rospy.loginfo(msg.data)

def subscriber(msg: String):
    sub = rospy.Subscriber("/hello_world", String, callback = callback_fn)

    rospy.loginfo("Node has been started.")
    rospy.spin()

if __name__ == '__main__':
    try:
        rospy.init_node("hello_subscriber")
        subscriber()
    except rospy.ROSInterruptException:
        pass