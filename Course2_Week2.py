import modern_robotics as mr
import numpy as np
import math
from numpy import linalg as LA

thetalist=np.array([math.pi/2,math.pi/2,1])

Slist=np.array([[0,1,0],[0,0,0],[1,0,0],[0,0,0],[0,2,1],[0,0,0]])

J=mr.JacobianSpace(Slist,thetalist)

print(J)

Blist=np.array([[0,-1,0],[1,0,0],[0,0,0],[3,0,0],[0,3,0],[0,0,1]])

B=mr.JacobianBody(Blist,thetalist)

print(B)

Jv=np.array([[-0.105, 0, 0.006, -0.045, 0, 0.006, 0],[-0.889, 0.006, 0, -0.844, 0.006, 0, 0],[0, -0.105, 0.889, 0, 0, 0, 0]])

A=np.dot(Jv,np.transpose(Jv))
eig=LA.eig(A)
print(eig)


