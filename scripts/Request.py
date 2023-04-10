#!/usr/bin/env python3

import rospy
from sys import stdout
from std_msgs.msg import Int32MultiArray as I32MA
from std_msgs.msg import Int32 as I32
from std_msgs.msg import Bool

rospy.init_node('Request_node')
t_n = rospy.Publisher('transfer_numbers',I32MA,queue_size=1,latch=True)
num = [0,0,0]
sum = 0
flag= Bool()


def sub_in(msg_in):
    global sum
    sum = msg_in.data
    flag.data = True

def sum_of_num_poly():
    while not rospy.is_shutdown():    
        if flag.data == True:
            print(f"Сумма: {sum}")
            flag.data = False
            break



# Проверка и копирование или создание параметров чисел полинома

if rospy.has_param('/data_of_req'):
    num[0] = rospy.get_param('/data_of_req/f')
    num[1] = rospy.get_param('/data_of_req/s')
    num[2] = rospy.get_param('/data_of_req/t')
else:
    print("Введите числа для возведения в степень!")
    for i in range(len(num)):
        if i != 2:
            s = "-ое"
        else:
            s = "-е"
        print(f"Введите {i+1}{s} число:")
        num[i] = int(input("--->"))
        stdout.flush()
    rospy.set_param('/data_of_req/f',num[0])
    rospy.set_param('/data_of_req/s',num[1])
    rospy.set_param('/data_of_req/t',num[2])

# Отправляем числа в топик

msg_out = I32MA()
msg_out.data = [num[0],num[1],num[2]]
t_n.publish(msg_out)

# Принимаем число из топика

rospy.Subscriber('sum_of_tn',I32,sub_in,queue_size=1)
sum_of_num_poly()
