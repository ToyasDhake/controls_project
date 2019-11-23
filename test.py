import Simulator
from numpy import sin, cos
from numpy import arange, pi
import itertools
from math import sqrt, acos, atan
from time import sleep

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

def Result(Kp, Ki, Kd):
    global thRef1
    global thRef2
    resultX = []
    resultY = []
    prevTh1 = - (pi / 4)
    prevTh2 = pi / 4
    prevTh1error = 0
    prevTh2error = 0
    th1integral = 0
    th2integral = 0
    Simulator.reset()
    for x, y in zip(thRef1, thRef2):
        th1error = (x - prevTh1)
        th2error = (y - prevTh2)
        # print(Kp, Ki, Kd)
        # print(th1error, prevTh1error, th1integral)
        # sleep(0.01)

        t1 = Kp * th1error + Kd * prevTh1error + Ki * th1integral
        t2 = Kp * th2error + Kd * prevTh2error + Ki * th2integral

        th1integral += th1error
        th2integral += th2error
        if th1integral > 20:
            th1integral = 20
        elif th1integral < -20:
            th1integral = -20
        if th2integral > 20:
            th2integral = 20
        elif th2integral < -20:
            th2integral = -20
        prevTh1error, prevTh2error = th1error, th2error
        th1, th2 = Simulator.Update(t1, t2)
        # print("th", th1, th2)
        prevTh1, prevTh2 = th1, th2
        xcor = 200 * sin(th1) + 200 * sin(th2)
        ycor = 200 * cos(th1) + 200 * cos(th2)
        ycor = ycor - 282.84
        resultX.append(xcor)
        resultY.append(ycor)
        # print(xcor, ycor)
    result = 0
    # print("result", resultX,resultY)
    for x, y, rx, ry in zip(xReference, yReference, resultX, resultY):
        result += sqrt((x - rx) * (x - rx) + (y - ry) * (y - ry))
    result /= len(xReference)
    return result


def resultPlot(Kp, Ki, Kd):
    global thRef1
    global thRef2
    resultX = []
    resultY = []
    prevTh1 = - (pi / 4)
    prevTh2 = pi / 4
    prevTh1error = 0
    prevTh2error = 0
    th1integral = 0
    th2integral = 0
    Simulator.reset()
    for x, y in zip(thRef1, thRef2):
        th1error = (x - prevTh1)
        th2error = (y - prevTh2)
        t1 = Kp * th1error + Kd * prevTh1error + Ki * th1integral
        t2 = Kp * th2error + Kd * prevTh2error + Ki * th2integral

        th1integral += th1error
        th2integral += th2error
        if th1integral > 20:
            th1integral = 20
        elif th1integral < -20:
            th1integral = -20
        if th2integral > 20:
            th2integral = 20
        elif th2integral < -20:
            th2integral = -20
        prevTh1error, prevTh2error = th1error, th2error
        th1, th2 = Simulator.Update(t1, t2)
        # print("th", th1, th2)
        prevTh1, prevTh2 = th1, th2
        xcor = 200 * sin(th1) + 200 * sin(th2)
        ycor = 200 * cos(th1) + 200 * cos(th2)
        ycor = ycor - 282.84
        resultX.append(xcor)
        resultY.append(ycor)
        # print(xcor, ycor)
    result = []
    # print("result", resultX,resultY)
    for x, y, rx, ry in zip(xReference, yReference, resultX, resultY):
        result.append(sqrt((x - rx) * (x - rx) + (y - ry) * (y - ry)))
    return result

def test(Kp, Ki, Kd):
    result = Result(Kp, Ki, Kd)
    return result

def testga(val):
    Kp, Ki, Kd = val[0], val[1], val[2]
    # print(Kp, Ki, Kd)
    result = Result(Kp, Ki, Kd)
    result = 1000-result
    # print(result)
    return result

def testgwo(val):
    Kp, Ki, Kd = val[0], val[1], val[2]
    result = Result(Kp, Ki, Kd)

    return result