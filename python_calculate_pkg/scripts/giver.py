#!/usr/bin/env python
# line that every python_ros node need

import rospy
# need to import rospy when writing ROS node in python
from std_msgs.msg import Float64MultiArray
# type of msg
from random import *


def giver():
    pub = rospy.Publisher('randint', Float64MultiArray, queue_size=10)
    rospy.init_node('giver',anonymous=True)   
    rate = rospy.Rate(10) #10hz
    
    while not rospy.is_shutdown():
        randomint_array = Float64MultiArray()
        randomint_array.data = [randint(1,100),randint(1,100)]
        rospy.loginfo(randomint_array.data)
        pub.publish(randomint_array)
        rate.sleep()
        
        
if __name__ == '__main__':
    try:
        giver()
    except rospy.ROSInterruptException:
        pass