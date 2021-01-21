#!/usr/bin/env python
import rospy
# need to import rospy when writing ROS node in python
from std_msgs.msg import String


# type of msg

def callback(data):
    rospy.loginfo("I heard %s", data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    # declare this node subscribe 'chatter' topic
    rospy.spin()

if __name__ == '__main__':
    listener()