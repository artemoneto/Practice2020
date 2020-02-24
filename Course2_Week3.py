import modern_robotics as mr
import numpy as np
import math
from numpy import linalg as LA

guess=np.array([math.pi/4,math.pi/4,math.pi/4])

Tsd=np.array([[-0.585,-0.811,0, 0.076],[0.811,-0.585,0,2.608],[0,0,1,0],[0,0,0,1]])
Slist=np.array([[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,-1,-2],[0,0,0]])
M=np.array([[1,0,0,3],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

ev=0.0001
ew=0.001

Jv=np.array([[-0.105, 0, 0.006, -0.045, 0, 0.006, 0],[-0.889, 0.006, 0, -0.844, 0.006, 0, 0],[0, -0.105, 0.889, 0, 0, 0, 0]])

solution=mr.IKinSpace(Slist, M, Tsd, guess, ew, ev)
print(solution)


