import numpy as np
import math
import modern_robotics as mr

M01 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0.089159], [0, 0, 0, 1]]
M12 = [[0, 0, 1, 0.28], [0, 1, 0, 0.13585], [-1, 0, 0, 0], [0, 0, 0, 1]]
M23 = [[1, 0, 0, 0], [0, 1, 0, -0.1197], [0, 0, 1, 0.395], [0, 0, 0, 1]]
M34 = [[0, 0, 1, 0], [0, 1, 0, 0], [-1, 0, 0, 0.14225], [0, 0, 0, 1]]
M45 = [[1, 0, 0, 0], [0, 1, 0, 0.093], [0, 0, 1, 0], [0, 0, 0, 1]]
M56 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0.09465], [0, 0, 0, 1]]
M67 = [[1, 0, 0, 0], [0, 0, 1, 0.0823], [0, -1, 0, 0], [0, 0, 0, 1]]

G1 = np.diag([0.010267495893, 0.010267495893,  0.00666, 3.7, 3.7, 3.7])
G2 = np.diag([0.22689067591, 0.22689067591, 0.0151074, 8.393, 8.393, 8.393])
G3 = np.diag([0.049443313556, 0.049443313556, 0.004095, 2.275, 2.275, 2.275])
G4 = np.diag([0.111172755531, 0.111172755531, 0.21942, 1.219, 1.219, 1.219])
G5 = np.diag([0.111172755531, 0.111172755531, 0.21942, 1.219, 1.219, 1.219])
G6 = np.diag([0.0171364731454, 0.0171364731454, 0.033822, 0.1879, 0.1879, 0.1879])

Glist = [G1, G2, G3, G4, G5, G6]

Mlist = [M01, M12, M23, M34, M45, M56, M67]

Slist = [[0,         0,         0,         0,        0,        0],
         [0,         1,         1,         1,        0,        1],
         [1,         0,         0,         0,       -1,        0],
         [0, -0.089159, -0.089159, -0.089159, -0.10915, 0.005491],
         [0,         0,         0,         0,  0.81725,        0],
         [0,         0,     0.425,   0.81725,        0,  0.81725]]

theta = np.array([0, 0, 0, 0, 0, 0]).T
theta_dot = np.array([0, 0, 0, 0, 0, 0]).T
theta_double_dot = np.array([0, 0, 0, 0, 0, 0]).T
g = np.array([0, 0, -9.81]).T
tau = np.array([0, 0, 0, 0, 0, 0]).T
Ftip = np.array([0, 0, 0, 0, 0, 0]).T

T = 0
t_start = 0
t_finish = 5
delta_t = 0.001
THETAS = np.array([theta]).copy()

while (T < (t_finish - t_start)) :
    print('\nFor iteration ',T,' positions are: ', theta)
    theta_double_dot = mr.ForwardDynamics(theta, theta_dot, tau, g, Ftip, Mlist, Glist, Slist)
    print('\nFor iteration ',T,' accelerations are: ', theta_double_dot)
    theta = theta + theta_dot*delta_t
    theta_dot = theta_dot + theta_double_dot*delta_t
    THETAS = np.append(THETAS, [theta], axis=0)
    T = T + delta_t

np.savetxt('THETAS.csv', THETAS, fmt='%.6f', delimiter=",")
