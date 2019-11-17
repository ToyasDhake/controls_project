import graphs
import matplotlib.pyplot as plt

performanceXGWO, performanceYGWO, performanceXPSO, performanceYPSO, performanceXGA, performanceYGA = [], [], [], [], [], []
poseXGWO, poseYGWO, poseXPSO, poseYPSO, poseXGA, poseYGA = [], [], [], [], [], []
torqueXGWO, torqueYGWO, torqueXPSO, torqueYPSO, torqueXGA, torqueYGA = [], [], [], [], [], []
costXGWO, costYGWO, costXPSO, costYPSO, costXGA, costYGA = [], [], [], [], [], []


# graphs.plotPerformanceGraph(plt, list(range(1,5)), list(range(1,5)), list(range(1,5)), list(range(1,5)), list(range(1,5)), list(range(1,5)))
# graphs.plotPoseGraph(plt, list(range(5, 10)), list(range(5, 10)), list(range(5, 10)), list(range(5, 10)), list(range(5, 10)), list(range(5, 10)))
# graphs.plotTorqueGraph(plt, list(range(10, 15)), list(range(10, 15)), list(range(10, 15)), list(range(10, 15)), list(range(10, 15)), list(range(10, 15)))
# graphs.plotCostGraph(plt, list(range(15, 20)), list(range(15, 20)), list(range(15, 20)), list(range(15, 20)), list(range(15, 20)), list(range(15, 20)))
#
# plt.show()