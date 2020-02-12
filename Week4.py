import modern_robotics as mr
import numpy as np

T=np.array([[0, -1, 0, 3],[1, 0, 0, 0],[0, 0, 1, 1],[0, 0, 0, 1]])
x=mr.TransInv(T)
print(x)

T=np.array([[1],[0],[0],[0],[2],[3]])
x=mr.VecTose3(T)
print(x)


q=np.array([0,0,2])
s=np.array([1,0,0])
h=1
x=mr.ScrewToAxis(q,s,h)
print(x)


T=([[0,-1.5708,0,2.3562],[1.5708,0,0,-2.3562],[0,0,0,1],[0,0,0,0]])
x=mr.MatrixExp6(T)
print(x)


T=([[0,-1,0,3],[1,0,0,0],[0,0,1,1],[0,0,0,1]])
x=mr.MatrixLog6(T)
print(x)
