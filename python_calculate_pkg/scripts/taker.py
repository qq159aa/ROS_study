#!/usr/bin/env python
import rospy
# need to import rospy when writing ROS node in python
from std_msgs.msg import Float64MultiArray
import numpy as np


# type of msg

def callback(data):    
    
    rospy.loginfo(data.data)

def taker():
    rospy.init_node('taker', anonymous=True)
    rospy.Subscriber("randint", Float64MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    taker()