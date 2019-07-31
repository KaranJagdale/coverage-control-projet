# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:19:20 2019

@author: karan
"""

import time
import rospy
from fb5_torque_ctrl.msg import Array
import numpy as np 

def callback0(a):
    global initialTime
    b = np.reshape(a.data,(a.len,2))
    t = time.time()
    print("time to subscribe0",t-initialTime)
    #print(b)

def callback1(a):
    global initialTime
    b = np.reshape(a.data,(a.len,2))
    t = time.time()
    print("time to subscribe1",t-initialTime)
    #print(b)

def callback2(a):
    global initialTime
    b = np.reshape(a.data,(a.len,2))
    t = time.time()
    print("time to subscribe2",t-initialTime)
    #print(b)

def callback3(a):
    global initialTime
    b = np.reshape(a.data,(a.len,2))
    t = time.time()
    print("time to subscribe3",t-initialTime)
    #print(b)


def sub():
    global initialTime
    rospy.init_node('sub', anonymous=True)

    sub0 = rospy.Subscriber('AP0',Array,callback0)
    sub1 = rospy.Subscriber('AP1',Array,callback1)
    sub2 = rospy.Subscriber('AP2',Array,callback2)
    sub3 = rospy.Subscriber('AP3',Array,callback3)

    initialTime = time.time()
    rospy.spin()
    
if __name__ == '__main__':
    sub()

