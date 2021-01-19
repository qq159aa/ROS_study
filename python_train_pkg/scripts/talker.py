#!/usr/bin/env python
# line that every python_ros node need

import rospy
# need to import rospy when writing ROS node in python
from std_msgs.msg import String
# type of msg


def talker():
    pub = rospy.Publisher('chatter',String, queue_size=10)
    # declare this node is Publishing to the 'chatter' topic
    # 'chatter' topic is String and that is actually class std_msgs.msg.String
    # queue size limits the amount of msgs
    
    rospy.init_node('talker',anonymous=True)
    # 'name' of this node, communicate with this name with master(roscore)
    # anonymous=true ensure this node has unique name by adding random numbers end of 'name'
    
    rate = rospy.Rate(10) #10hz
    # create Rate object named rate rate(n), loop 'n' time per sec
    
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        # declare String will publish
        rospy.loginfo(hello_str)
        # print msg to screen
        pub.publish(hello_str)
        # publish
        rate.sleep()
        # similar to time.sleep but, it work with simulated time
        
if __name__ == '__main__':
    try:talker()
    except rospy.ROSInterruptException:
        pass