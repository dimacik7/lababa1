#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("SMS:\n %s", msg.data)

rospy.init_node('lovilka_smsok')
rospy.Subscriber('topic_100', String, callback, queue_size=10)
rospy.spin()