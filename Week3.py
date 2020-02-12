import modern_robotics as mr
import numpy as np

w=np.array([1, 2, 0.5])
x=mr.VecToso3(w)
print(x)

w=np.array([[0, 0.5, -1],[-0.5, 0, 2],[1, -2, 0]])
x=mr.MatrixExp3(w)
print(x)

w=np.array([[0, 0, 1],[-1, 0, 0],[0, -1, 0]])
x=mr.MatrixLog3(w)
print(x)
