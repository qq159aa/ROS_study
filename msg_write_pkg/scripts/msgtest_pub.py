#!/usr/bin/env python
import rospy
from msg_write_pkg.msg import test_custom

def talker():
    pub = rospy.Publisher('chatter',test_custom, queue_size=10) 
    rospy.init_node('talker',anonymous=0)
    rate = rospy.Rate(10)
    msg_to_publish = test_custom()
    counter = 0
    
    while not rospy.is_shutdown():
        string_to_publish = "hello world %d" %counter
        counter +=1
        msg_to_publish.data = string_to_publish
        msg_to_publish.counter = counter
        pub.publish(msg_to_publish)
        rospy.loginfo(string_to_publish)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass