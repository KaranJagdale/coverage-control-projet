#Written by Karan Jagdale

import time
import numpy as np
import matplotlib.pyplot as plt

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
#print(X_grid)
bot_loc = np.empty((2,N_bots))

# Bot locations
bot_loc[:,0] = np.array([0.2 ,0.3])
bot_loc[:,1] = np.array([-1.2 ,2])
bot_loc[:,2] = np.array([-0.7 ,-0.3])
bot_loc[:,3] = np.array([0.8 ,2.1])


def checkside(x,y,n,m):  #(x,y) is the point to check and n,m is the pair of bots
    x1 = bot_loc[0,n]
    y1 = bot_loc[1,n]
    x2 = bot_loc[0,m]
    y2 = bot_loc[1,m]   
    if y1!=y2:
        return (x1-x2)/(y2-y1)*(x-(x1+x2)/2)-y+(y1+y2)/2      
    else:
        return x - (x1+x2)/2

X = []
Y = []
X1 = []
Y1 = []
X2 = []
Y2 = []
partition = []
partition1 = []
partition2 = []
def pointappend(grid):
    global partition,partition1,partition2,X,Y,BotNo,X1,Y1,X2,Y2

    botSign = checkside(bot_loc[0,BotNo],bot_loc[1,BotNo],BotNo,0)
    print(botSign)
    for i in range(N_Grid_Points):
        for j in range(N_Grid_Points):
            
            if checkside(grid[i,j,0],grid[i,j,1],BotNo,0)*botSign > 0:
                partition.append(np.array([i,j]))
    
    #Plotting partition in stage1
    for m in partition:
        
        X1.append(grid[m[0],m[1],0])
        Y1.append(grid[m[0],m[1],1])
    
    X1 = np.array(X1)
    Y1 = np.array(Y1)
    plt.figure(1)    
    plt.plot(X1,Y1,'b.')
   
    plt.show() 
    
    k = 0
    
    botSign = checkside(bot_loc[0,BotNo],bot_loc[1,BotNo],BotNo,2)
    while k < len(partition):
        if checkside(grid[partition[k][0],partition[k][1],0],grid[partition[k][0],partition[k][1],1],BotNo,2)*botSign > 0:
            partition1.append(np.array([partition[k][0],partition[k][1]]))
            
            
        k=k+1
    print(len(partition1))
    
    #Partition in stage 2
    for m in partition1:
        
        X2.append(grid[m[0],m[1],0])
        Y2.append(grid[m[0],m[1],1])
   
    X2 = np.array(X2)
    Y2 = np.array(Y2)
    plt.figure(4)    
    plt.plot(X2,Y2,'g.')
   
    plt.show()
    

    botSign = checkside(bot_loc[0,BotNo],bot_loc[1,BotNo],BotNo,3)
    l = 0
    while l < (len(partition1)):
        if checkside(grid[partition1[l][0],partition1[l][1],0],grid[partition1[l][0],partition1[l][1],1],BotNo,3)*botSign > 0:
            partition2.append(np.array([partition1[l][0],partition1[l][1]]))
            
        l = l+1


    print(len(partition2))
    

    #Final partition plotting 
    for m in partition2:
        
        X.append(grid[m[0],m[1],0])
        Y.append(grid[m[0],m[1],1])
    
    X = np.array(X)
    Y = np.array(Y)
    plt.figure(2)    
    plt.plot(X,Y,'r.')
    
    plt.show()
    print(X)   

t1 = time.time()
pointappend(pos_grid)       #Time to run the code 
t2 = time.time()
print(t2-t1)






