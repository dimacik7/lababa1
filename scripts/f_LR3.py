#!/usr/bin/env python3
import rospy as ry
# Our case:     std_msgs/String     -> from std_msgs.msg import String
# Example:      geometry_msgs/Pose  -> from geometry_msgs.msg import Pose
from std_msgs.msg import String
import math

ry.init_node('cifri')
pub = ry.Publisher('mmmy_topic', String, queue_size=10)
pub_100 = ry.Publisher('topic_100', String, queue_size=10)
rate = ry.Rate(10)

def start_num():
    msg = String()
    num = 0
    while not ry.is_shutdown():
        if num%2==0:
            sms = "Num is %i" % num
            ry.loginfo(sms)
            msg.data = sms
            pub.publish(msg)
        num = num + 1
        if num == 100:
            sms = "Num is %i" % num
            ry.loginfo(sms)
            sms = "Counter is full - %i\nPlease, stop!" % num 
            num = 0
            msg.data = sms
            pub_100.publish(msg)
        rate.sleep()
        


try:
    start_num()
except (ry.ROSInterruptException, KeyboardInterrupt):
    ry.logerr('Exception catched')

