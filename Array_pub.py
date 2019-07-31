# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:55:59 2019

@author: karan
"""

import rospy
from fb5_torque_ctrl.msg import Array
import numpy as np
import time
import math

N_bots = 4
BotNo = 1

origin = np.array([0.0,0.0])

grid_Size = 5.0 #in meters
grid_Res = 0.02 #in meters. Each square is 2 cm width.

N_Grid_Points = int(grid_Size/grid_Res) #We gonna assume square grids. Else even the Voronoi partition function has to change.

x_grid=np.arange(-grid_Size/2+origin[0], grid_Size/2+origin[0], grid_Res)+grid_Res/2 #+grid_Res/2 gives the centroid
y_grid=np.arange(-grid_Size/2+origin[1], grid_Size/2+origin[1], grid_Res)+grid_Res/2

X_grid, Y_grid = np.meshgrid(x_grid,y_grid)

#pos_grid is a three 250x250 matrix with each point holding the coordinate of the centroid of a given grid square.
#eg. pos_grid[0,0,:] will give the 1st squares centroid as [-2.49,-2.49]
pos_grid = np.empty(X_grid.shape + (2,))
pos_grid[:, :, 0] = X_grid; pos_grid[:, :, 1] = Y_grid

bot_loc = np.empty((2,N_bots))
#print (np.shape(bot_loc),bot_loc[0][:])
#print(bot_loc)

bot_loc[:,0] = np.array([0.2 ,0.3])
bot_loc[:,1] = np.array([-1.2 ,2])
bot_loc[:,2] = np.array([-0.7 ,-0.3])
bot_loc[:,3] = np.array([0.8 ,2.1])

def cartesianDist(a,b):
	return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def voronoi(grid, Nbots, BotNo, locations):
	VPartition=[]
	N_Grid_Points = len(grid[:,0,0])
	for i in range(N_Grid_Points):
		for j in range(N_Grid_Points):	#This iterates over all points in the domain.
			inPartition=True 			#This stays one as long as the point is closer to the botIn question than any other point.
			for N in range(Nbots):
				if N!=BotNo and inPartition:
					inPartition = inPartition and cartesianDist(grid[i,j,:],locations[:,BotNo])<cartesianDist(grid[i,j,:],locations[:,N])
			if(inPartition):
				VPartition.append(np.array([i,j]))
	return VPartition


def pub():
    rospy.init_node('pub',anonymous = True)
    t1 = time.time()
    partition0 = voronoi(pos_grid, N_bots, 0, bot_loc)
    partition1 = voronoi(pos_grid, N_bots, 1, bot_loc)
    partition2 = voronoi(pos_grid, N_bots, 2, bot_loc)
    partition3 = voronoi(pos_grid, N_bots, 3, bot_loc)

    pub0 = rospy.Publisher('AP0',Array,queue_size = 10)
    pub1 = rospy.Publisher('AP1',Array,queue_size = 10) 
    pub2 = rospy.Publisher('AP2',Array,queue_size = 10)
    pub3 = rospy.Publisher('AP3',Array,queue_size = 10)
    
    a0 = Array()
    a1 = Array()
    a2 = Array()
    a3 = Array()
    #data = np.array([[1.2,2.3],[3.4,4.5],[3.5,5.2]])

    data0 = np.array(partition0)
    data1 = np.array(partition1)
    data2 = np.array(partition2)
    data3 = np.array(partition3)

    a0.len = len(data0)
    a1.len = len(data1)
    a2.len = len(data2)
    a3.len = len(data3)

    a0.data = np.reshape(data0,2*(a0.len))
    a1.data = np.reshape(data1,2*(a1.len))
    a2.data = np.reshape(data2,2*(a2.len))
    a3.data = np.reshape(data3,2*(a3.len))

    rate = rospy.Rate(1)
    #while not rospy.is_shutdown():
    #print(data)
    t2 = time.time()
    print("time to publish - ",t2 - t1)
    while not rospy.is_shutdown():
        #pub0.publish(a0)
        #pub1.publish(a1)
        #pub2.publish(a2) 
        pub3.publish(a3)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        pub()
    except rospy.ROSInterruptException:
        pass
