from math import pi
from numpy import cos
from numpy import sin
import numpy as np
from numpy.linalg import inv
from scipy import integrate
import matplotlib.pyplot as plt


def r2dof(x,ths,spec,Kpid):
    xdot = [0] * 8
    th1s = ths[0]
    th2s = ths[1]
    M1 = spec[2]
    M2 = spec[3]
    L1 = spec[0]
    L2 = spec[1]
    g = 9.8

    b11 = (M1 + M2) * L1 ** 2 + M2 * L2 ** 2 + 2 * M2 * L1 * L2 * cos(x[3])
    b12 = M2 * L2 ** 2 + M2 * L1 * L2 * cos(x[3])
    b21 = M2 * L2 ** 2 + M2 * L1 * L2 * cos(x[3])
    b22 = M2 * L2 ** 2
    Bq = [[b11, b12],[b21, b22]]

    c1 = -M2 * L1 * L2 * sin(x[3]) * (2 * x[4] * x[5] + x[5] ** 2)
    c2 = -M2 * L1 * L2 * sin(x[3]) * x[4] * x[5]
    Cq = [[c1], [c2]]

    g1 = -(M1 + M2) * g * L1 * sin(x[2] - M2 * g * L2 * sin(x[2] + x[3]))
    g2 = -M2 * g * L2 * sin(x[2] + x[3])
    Gq = [[g1], [g2]]

    Kp1 = Kpid[0]
    Kd1 = Kpid[1]
    Ki1 = Kpid[2]

    Kp2 = Kpid[3]
    Kd2 = Kpid[4]
    Ki2 = Kpid[5]

    f1 = Kp1 * (th1s - x[2]) - Kd1 * x[4] + Ki1 * (x[0])
    f2 = Kp2 * (th2s - x[3]) - Kd2 * x[5] + Ki2 * (x[1])
    Fhat = [[f1], [f2]]
    F = np.matmul(np.array(Bq), np.array(Fhat))

    xdot[0] = (th1s - x[2])
    xdot[1] = (th2s - x[3])
    xdot[2] = x[4]
    xdot[3] = x[5]
    q2dot = np.matmul(inv(np.array(Bq)), np.subtract(np.subtract(np.array(F), np.array(Gq)), np.array(Cq)))
    xdot[4] = q2dot[0]
    xdot[5] = q2dot[1]
    xdot[6] = F[0]
    xdot[7] =F[1]
    return xdot


th_int = [-pi / 2, pi / 2]
ths = [pi / 2, -pi / 2]
x0 = [0, 0, -pi / 2, pi / 2, 0, 0, 0, 0]
Ts = [0, 20]
L1, L2, M1, M2 = 1, 1, 1, 1
spec = [L1, L2, M2, M2]
Kp1, Kd1, Ki1 = 15, 7, 10
Kp2, Kd2, Ki2 = 15, 10, 10
Kpid = [Kp1, Kd1, Ki1, Kp2, Kd2, Ki2]


ans = []
for i in range(20):
    x = [0]*6

    temp = r2dof(x, ths, spec,Kpid)
    ans.append(temp)