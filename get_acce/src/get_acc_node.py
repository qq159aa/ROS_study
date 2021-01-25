#!/usr/bin/env python
import rospy
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250
from get_acce.msg import custommsg

mpu = MPU9250(
    address_ak=AK8963_ADDRESS, 
    address_mpu_master=MPU9050_ADDRESS_68, # In 0x68 Address
    address_mpu_slave=None, 
    bus=1, 
    gfs=GFS_1000, 
    afs=AFS_16G, 
    mfs=AK8963_BIT_16, 
    mode=AK8963_MODE_C100HZ)
mpu.configure()

def raw_data():
    acc_data = custommsg()
    rospy.init_node('get_acc',anonymous=0)
    pub = rospy.Publisher('acc_data', custommsg, queue_size=10)        
    rate = rospy.Rate(10) #10hz
    
    while not rospy.is_shutdown():

        data_raw = mpu.readAccelerometerMaster()

        acc_data.acc_x = data_raw[0]
        acc_data.acc_y = data_raw[1]
        acc_data.acc_z = data_raw[2]
        
        pub.publish(acc_data)
        rospy.loginfo(acc_data)               
        rate.sleep()


if __name__ == '__main__':
    try:
        print('acc data start...')
        raw_data()
    except rospy.ROSInterruptException:
        pass
