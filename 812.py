import math
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        temp = []
        for i, e in enumerate(points):
            for j, p in enumerate(points[i+1:]):
                for k, q in enumerate(points[j+1:]):
                    temp.append(Area(e,p,q))
        return max(temp)
    
def length_2_points(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def Area(a, b, c):
    length_1 = length_2_points(a,b)
    length_2 = length_2_points(c,b)
    length_3 = length_2_points(a,c)
    s = (length_1 + length_2 + length_3)/2
    if s > length_1 and s > length_2 and s > length_3:
        return math.sqrt((s*(s-length_1)*(s-length_2)*(s-length_3)))
    return 0
