#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray as I32MA
from std_msgs.msg import Bool

flag = Bool()
rospy.init_node('Polynominal_node')
t_op_n = rospy.Publisher('transfer_of_powered_numbers',I32MA,queue_size=1,latch=True)
num_tf = [0,0,0]

def sub_in(msg_in):
    global num_tf
    for i in range(3):
        num_tf[i] = msg_in.data[i]
    flag.data = True
    

msg_out = I32MA()
def polynome():
    while not rospy.is_shutdown():
        if flag.data == True:
            for i in range(3):
                pn = num_tf[i]**(i+1)
                num_tf[i] = pn
            msg_out.data = [num_tf[0],num_tf[1],num_tf[2]]
            t_op_n.publish(msg_out)
            flag.data = False

rospy.Subscriber('transfer_numbers',I32MA,sub_in,queue_size=1)
polynome()
#try:
#    polynome()
#except (rospy.ROSInterruptException, KeyboardInterrupt):
#    rospy.logerr('Exception catched')
