#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("SMS:\n %s", msg.data)

rospy.init_node('Counter')
rospy.Subscriber('mmmy_topic', String, callback, queue_size=10)
rospy.spin()