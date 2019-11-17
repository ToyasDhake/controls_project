from numpy import arange
from numpy import pi
from numpy import sin
from numpy import cos

def plotPerformanceGraph(plt, xGWO, yGWO, xPSO, yPSO, xGA, yGA):
    plt.subplot(2, 2, 1)
    t = arange(-pi/2, pi/2, 0.01)
    r = 100
    x = r*sin(t)+100
    y = r*cos(t)
    xn = [0, 200]
    yn = [0,0]
    plt.plot(x, y, color='black', label='reference')
    plt.plot(xn, yn, color='black')
    plt.plot(xGWO, yGWO, color='red', label='GWO')
    plt.plot(xPSO, yPSO, color='blue', label='PSO')
    plt.plot(xGA, yGA, color='green', label='GA')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Trajectory control')
    plt.legend()

def plotPoseGraph(plt, xGWO, yGWO, xPSO, yPSO, xGA, yGA):
    plt.subplot(2, 2, 2)
    plt.plot(xGWO, yGWO, color='red', label='GWO')
    plt.plot(xPSO, yPSO, color='blue', label='PSO')
    plt.plot(xGA, yGA, color='green', label='GA')
    plt.xlabel('Time')
    plt.ylabel('Trajectory Tracking error')
    plt.title('Absolute trajectory errors ')
    plt.legend()

def plotTorqueGraph(plt, xGWO, yGWO, xPSO, yPSO, xGA, yGA):
    plt.subplot(2, 2, 3)
    plt.plot(xGWO, yGWO, color='red', label='GWO')
    plt.plot(xPSO, yPSO, color='blue', label='PSO')
    plt.plot(xGA, yGA, color='green', label='GA')
    plt.xlabel('Time')
    plt.ylabel('Torque')
    plt.title('Input torques')
    plt.legend()

def plotCostGraph(plt, xGWO, yGWO, xPSO, yPSO, xGA, yGA):
    plt.subplot(2, 2, 4)
    plt.plot(xGWO, yGWO, color='red', label='GWO')
    plt.plot(xPSO, yPSO, color='blue', label='PSO')
    plt.plot(xGA, yGA, color='green', label='GA')
    plt.xlabel('Iteration')
    plt.ylabel('Cost')
    plt.title('Input torques')
    plt.legend()