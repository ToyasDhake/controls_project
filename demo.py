import graphs
import matplotlib.pyplot as plt
from numpy import arange
from numpy import pi
from numpy import sin
from numpy import cos
import itertools
import Simulator
from math import acos, atan, sqrt
import PSO
import gademo
import GWO1
import test

itr = 50
def getPositionFromSimulation(x, y):
    th1, th2 = Simulator.Update(x, y)
    xcor = 200 * sin(th1) + 200 * sin(th2)
    ycor = 200 * cos(th1) + 200 * cos(th2)
    ycor = ycor - 282.84
    return xcor, ycor


performanceXGWO, performanceYGWO, performanceXPSO, performanceYPSO, performanceXGA, performanceYGA = [], [], [], [], [], []
poseXGWO, poseYGWO, poseXPSO, poseYPSO, poseXGA, poseYGA = [], [], [], [], [], []
torqueXGWO, torqueYGWO, torqueXPSO, torqueYPSO, torqueXGA, torqueYGA = [], [], [], [], [], []
costXGWO, costYGWO, costXPSO, costYPSO, costXGA, costYGA = [], [], [], [], [], []

t = arange(-pi / 2, pi / 2, 0.01)
r = 100
xRef = r * sin(t) + 100
yRef = r * cos(t)
xRef = list(xRef)
yRef = list(yRef)
xn = list(range(200, 0, -1))
yn = [0] * 200
xRef.extend(xn)
yRef.extend(yn)

xReference = list(itertools.chain.from_iterable(itertools.repeat(x, 10) for x in xRef))
yReference = list(itertools.chain.from_iterable(itertools.repeat(x, 10) for x in yRef))
thRef1 = []
thRef2 = []

for xref, yref in zip(xReference, yReference):
    distance = sqrt((xref - 0) * (xref - 0) + (yref - 282.84) * (yref - 282.84))

    thref2 = (pi) - acos(((200 * 200) + (200 * 200) - (distance * distance)) / (2 * 200 * 200))
    thref1 = atan((0 - xref) / (yref - 282.84))

    thref1 = thref1 - acos(((200 * 200) - (200 * 200) + (distance * distance)) / (2 * 200 * distance))
    thRef1.append(thref1)
    thRef2.append(thref2)

yCostPSO, KpidPSO = PSO.runPSO(itr)
yCostGWO, KpidGWO = GWO1.runGWO(itr)

# yCostGA, KpidGA = gademo.runGA(itr)
# yCostGA = [1000-x for x in yCostGA]

trackingErrorPSO = test.resultPlot(KpidPSO[0], KpidPSO[1], KpidPSO[2])
trackingErrorGWO = test.resultPlot(KpidGWO[0], KpidGWO[1], KpidGWO[2])
print(trackingErrorGWO)


# graphs.plotPerformanceGraph(plt, xRef, yRef, list(range(1,5)), list(range(1,5)), list(range(1,5)), list(range(1,5)), list(range(1,5)), list(range(1,5)))
# graphs.plotPoseGraph(plt, list(range(len(trackingErrorGWO))), trackingErrorGWO, list(range(len(trackingErrorPSO))), trackingErrorGWO, list(range(5, 10)), list(range(5, 10)))
# graphs.plotTorqueGraph(plt, list(range(10, 15)), list(range(10, 15)), list(range(10, 15)), list(range(10, 15)), list(range(10, 15)), list(range(10, 15)))
graphs.plotCostGraph(plt, list(range(itr)), yCostGWO, list(range(itr)), yCostPSO, list(range(itr)), list(range(itr)))

plt.show()
