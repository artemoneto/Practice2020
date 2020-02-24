import modern_robotics as mr
import numpy as np
import math
from numpy import linalg as LA

L1=0.425
L2=0.392
H1=0.089
H2=0.095
W1=0.109
W2=0.082
Blist = np.array([[0, 1, 0, W1+W2, 0,   L1+L2],
                 [0, 0,  1, H2, -L1-L2,   0],
                 [0, 0,  1, H2, -L2, 0],
                 [0, 0,  1, H2, 0,   0],
                 [0, -1,  0, -W2, 0,   0],
                 [0, 0,  1, 0, 0,   0]]).T
M = np.array([[-1, 0,  0, L1+L2],
             [ 0, 0,  1, W1+W2],
             [ 0, 1, 0, H1-H2],
             [ 0, 0,  0, 1]])
T = np.array([[ 0, 1,   0,     -0.5],
              [ 0, 0,  -1,      0.1],
              [-1, 0,   0,      0.1],
              [ 0, 0,   0,        1]])
thetalist0 = np.array([1.5, 2.5, 3 ,1,1,1])
eomg = 0.001
ev = 0.0001

test = mr.IKinBodyIterates(Blist, M, T, thetalist0, eomg, ev)
print(test)

