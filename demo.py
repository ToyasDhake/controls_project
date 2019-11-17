import graphs
import matplotlib.pyplot as plt
from numpy import arange
from numpy import pi
from numpy import sin
from numpy import cos

performanceXGWO, performanceYGWO, performanceXPSO, performanceYPSO, performanceXGA, performanceYGA = [], [], [], [], [], []
poseXGWO, poseYGWO, poseXPSO, poseYPSO, poseXGA, poseYGA = [], [], [], [], [], []
torqueXGWO, torqueYGWO, torqueXPSO, torqueYPSO, torqueXGA, torqueYGA = [], [], [], [], [], []
costXGWO, costYGWO, costXPSO, costYPSO, costXGA, costYGA = [], [], [], [], [], []

t = arange(-pi/2, pi/2, 0.01)
r = 100
xRef = r*sin(t)+100
yRef = r*cos(t)
xRef = list(xRef)
yRef = list(yRef)
xn = list(range(200,0, -1))
yn = [0]*200
xRef.extend(xn)
yRef.extend(yn)

graphs.plotPerformanceGraph(plt, xRef, yRef, list(range(1,5)), list(range(1,5)), list(range(1,5)), list(range(1,5)), list(range(1,5)), list(range(1,5)))
graphs.plotPoseGraph(plt, list(range(5, 10)), list(range(5, 10)), list(range(5, 10)), list(range(5, 10)), list(range(5, 10)), list(range(5, 10)))
graphs.plotTorqueGraph(plt, list(range(10, 15)), list(range(10, 15)), list(range(10, 15)), list(range(10, 15)), list(range(10, 15)), list(range(10, 15)))
graphs.plotCostGraph(plt, list(range(15, 20)), list(range(15, 20)), list(range(15, 20)), list(range(15, 20)), list(range(15, 20)), list(range(15, 20)))

plt.show()