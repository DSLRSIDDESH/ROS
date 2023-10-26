#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

msg_count = 0

def msg_callback(data):
    rospy.loginfo(f"{data.data}")
    
    global msg_count
    msg_count += 1

def subscriber_node():
    rospy.init_node("subscriber_node", anonymous = True)

    sub = rospy.Subscriber("chatter", String, msg_callback)

    start_time = rospy.Time.now()
    rate = rospy.Rate(1)

    global msg_count
    while not rospy.is_shutdown():
        current_time = rospy.Time.now()
        elapsed_time = current_time - start_time
        if elapsed_time.to_sec() >= 5:

            msg_frequency = msg_count / elapsed_time.to_sec()
            rospy.loginfo(f"Frequency of messages received is {msg_frequency}")

            start_time = current_time
            msg_count = 0
        rate.sleep()

    rospy.spin()


if __name__ == "__main__":
    subscriber_node()