import math
def distance_point(p1,p2):
    distancea=math.sqrt(((p1[0]-p2[0]**2)-(p1[1]-p2[1]**2)))
    return distancea

print(distance_point([4,0],[0,6]))
