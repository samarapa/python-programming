import math
def distance():
    x1,y1 = 1,2
    x2,y2 = 2,3

    return round(math.sqrt(((x1 - x2)**2) + (( y1- y2)**2)),6)


print("Distance :" + str(distance()))
