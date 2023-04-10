#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray as I32MA
from std_msgs.msg import Int32 as I32
from std_msgs.msg import Bool

rospy.init_node('Summing_node')
s_of_tn = rospy.Publisher('sum_of_tn',I32,queue_size=1,latch=True)
num_pow = [0,0,0]
flag = Bool()

def sub_in(msg_in):
    global num_pow 
    for i in range(3):
        num_pow[i] = msg_in.data[i]
    flag.data = True


msg_out = I32()


def summ_num_p():
    while not rospy.is_shutdown():
        if flag.data == True:
            summa = sum(num_pow)
            msg_out.data = summa
            s_of_tn.publish(msg_out)
            flag.data = False
            rospy.set_param('/data_of_req/sum',summa)
                


rospy.Subscriber('transfer_of_powered_numbers',I32MA,sub_in,queue_size=1)           
summ_num_p()
#try:
#    summ_num_p()
#except (rospy.ROSInterruptException, KeyboardInterrupt):
#   rospy.logerr('Exception catched')