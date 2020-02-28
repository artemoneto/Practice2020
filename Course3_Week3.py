import numpy as np
import math
import modern_robotics as mr

T = 5
t = 3
s = mr.QuinticTimeScaling(T,t)
print(s)

X_start = np.identity(4)
X_end = np.array([[0,0,1,1],[1,0,0,2],[0,1,0,3],[0,0,0,1]])
T_f = 10
N = 10
method = 3
trajectory = mr.ScrewTrajectory(X_start, X_end, T_f, N, method)
print(trajectory[-2])

method = 5
trajectory = mr.CartesianTrajectory(X_start, X_end, T_f, N, method)
print(trajectory[-2])



