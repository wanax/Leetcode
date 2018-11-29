'''
Xiaochi Ma
2018-11-27
'''

class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    
    def eq(self, p1, p2):
        if p1.x == p2.x and p1.y == p2.y:
            return True
        else:
            return False
    
    def calK(self, p1, p2):
        if p1.y == p2.y:
            return 0
        if p1.x == p2.x:
            return 9999
        if p1.x > p2.x:
            t = p1
            p1 = p2
            p2 = t
        return round((p2.y - p1.y)/(p2.x - p1.x), 2)
    
    def maxPoints(self, points):
        
        if len(points) == 0:
            return 0
        
        slopes = {}
        
        mcount = 1
        for i in range(len(points)):
            k = None
            dup = 0
            for j in range(i+1, len(points)):
                if self.eq(points[i], points[j]):
                    dup += 1
                else:
                    k = self.calK(points[i], points[j])
                    slopes[k] = slopes.get(k, 1) + 1
            if k != None:
                mcount = max(mcount, slopes[k]+dup)
                slopes[k] = 1
            else:
                mcount = max(mcount, 1+dup)
        return mcount
    
if __name__ == '__main__':
    
    p1 = Point(84,250)
    p2 = Point(0,0)
    p3 = Point(1,0)
    p4 = Point(0,-70)
    p5 = Point(0,-70)
    p6 = Point(1,-1)
    p7 = Point(21,10)
    p8 = Point(42,90)
    p9 = Point(-42,-230)
    
    solution = Solution()
    print(solution.maxPoints([p1,p2,p3,p4,p5,p6,p7,p8,p9])) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    