import time
import numpy as np
import math
#import matplotlib.pyplot as plt

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

def voronoigrid(grid, Nbots, BotNo, locations):
	VPartition=[]
	N_Grid_Points = len(grid[:,0,0])
	for i in range(N_Grid_Points):
		for j in range(N_Grid_Points):
                   	#This iterates over all points in the domain.
			#inPartition=True 			#This stays one as long as the point is closer to the botIn question than any other point.
			#for N in range(Nbots):
			#	if N!=BotNo and inPartition:
			#		inPartition = inPartition and cartesianDist(grid[i,j,:],locations[:,BotNo])<cartesianDist(grid[i,j,:],locations[:,N])
			#if(inPartition):
                        #a = cartesianDist(grid[i,j,:],locations[:,BotNo])<cartesianDist(grid[i,j,:],locations[:,0]) 
                        #b = cartesianDist(grid[i,j,:],locations[:,BotNo])<cartesianDist(grid[i,j,:],locations[:,2])
                        #c = cartesianDist(grid[i,j,:],locations[:,BotNo])<cartesianDist(grid[i,j,:],locations[:,3])
                        #print(grid[i,j,:])                         
                        if(cartesianDist(grid[i,j,:],locations[:,BotNo])<cartesianDist(grid[i,j,:],locations[:,0]) and cartesianDist(grid[i,j,:],locations[:,BotNo])<cartesianDist(grid[i,j,:],locations[:,2]) and cartesianDist(grid[i,j,:],locations[:,BotNo])<cartesianDist(grid[i,j,:],locations[:,3])):
                            VPartition.append(np.array([i,j]))
        
	return VPartition

t1 = time.time()
a =voronoigrid(pos_grid, N_bots, BotNo, bot_loc)
t2 = time.time()
print(t2-t1)
