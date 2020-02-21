import modern_robotics as mr
import numpy as np
import math

M=np.array([[1,0,0,3.732],[0,1,0,0],[0,0,1,2.732],[0,0,0,1]])
thetalist=np.array([-math.pi/2,math.pi/2,math.pi/3,-math.pi/4,1,math.pi/6])

Slist=np.array([[0,0,0,0,0,0],[0,1,1,1,0,0],[1,0,0,0,0,1],[0,0,1,-0.732,0,0],[-1,0,0,0,0,-3.732],[0,1,-2.732,3.732,1,0]])
Blist=np.array([[0,0,0,0,0,0],[0,1,1,1,0,0],[1,0,0,0,0,1],[0,-2.732,3.732,2,0,0],[2.732,0,0,0,0,0],[0,2.732,-1,0,-1,0]])

S=mr.FKinSpace(M,Slist,thetalist)
B=mr.FKinBody(M,Blist, thetalist)

print(S)
print(B)
