#!/usr/bin/env python
import rospy
from msg_write_pkg.msg import test_custom

def callback(data):
    string_received = data.data
    counter_received = data.counter
    rospy.loginfo("I heard %d" %counter_received)
    rospy.loginfo(string_received)

def listener():
    rospy.init_node('listener', anonymous=0)
    rospy.Subscriber("chatter", test_custom, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()