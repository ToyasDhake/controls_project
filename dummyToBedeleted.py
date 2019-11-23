from math import sqrt, acos, atan
from numpy import pi, cos, sin

xref, yref = 200, 0
distance = sqrt((xref-0)*(xref-0) + (yref-282.84)*(yref-282.84))

thref2 = (pi) - acos(((200*200) + (200*200) - (distance*distance))/(2*200*200))
thref1 = atan((0-xref)/(yref-282.84))

thref1 = thref1 - acos(((200*200) - (200*200) + (distance*distance))/(2*200*distance))

xcor = 200 * sin(thref1) + 200 * sin(thref1+thref2)
ycor = 200 * cos(thref1) + 200 * cos(thref1+thref2)
ycor = ycor - 282.84
print(xcor, ycor)