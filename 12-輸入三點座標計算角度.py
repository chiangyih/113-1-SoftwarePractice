import math
a=[0,0]
b=[1,0]
c=[1,1.732]
# 計算a點到b點的距離
def distance(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
# 計算b點到c點的距離
def distance(b,c):
    return math.sqrt((b[0]-c[0])**2+(b[1]-c[1])**2)
# 計算a點到c點的距離
def distance(a,c):
    return math.sqrt((a[0]-c[0])**2+(a[1]-c[1])**2)
# 計算abc三點，b點的角度
def angle(a,b,c):
    def angle(a, b, c):
        """
        Calculate the angle (in degrees) at point 'a' formed by the line segments ab and ac.

        Parameters:
        a (tuple): Coordinates of point a (x, y).
        b (tuple): Coordinates of point b (x, y).
        c (tuple): Coordinates of point c (x, y).

        Returns:
        float: The angle at point 'a' in degrees.
        """
    # return math.degrees(math.acos((distance(a,b)**2+distance(b,c)**2-distance(a,c)**2)/(2*distance(a,b)*distance(b,c))))
    return math.degrees(math.acos(distance(a,b)/distance(a,c)))
print(angle(a,b,c)) # 90.0