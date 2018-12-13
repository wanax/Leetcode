'''
Xiaochi Ma
2018-12-09
'''

class Solution(object):
    
    def computeArea(self, A, B, C, D, E, F, G, H):
        
        r1_l = abs(A - C)
        r1_h = abs(B - D)
        area1 = r1_l * r1_h
        
        r2_l = abs(E - G)
        r2_h = abs(F - H)
        area2 = r2_l * r2_h
        
        points = []
        contianer = []
        if area1 >= area2:
            points = [[E,F],[E,H],[G,H],[G,F]]
            contianer = [range(A, C+1), range(B, D+1)]
            re = []
            for point in points:
                if point[0] in contianer[0] and point[1] in contianer[1]:
                    re.append(point)
        else:
            points = [[A,B], [A,D], [C,D], [C,B]]
            contianer = [range(E, G+1), range(F, H+1)]
            re = []
            for point in points:
                if point[0] in contianer[0] and point[1] in contianer[1]:
                    re.append(point)
                    
        if len(re) == 1:
            idx = points.index(re[0])
            l, h = 0, 0
            if idx == 0:
                l = abs(list(contianer[0])[-1]-re[0][0])
                h = abs(list(contianer[1])[-1]-re[0][1])
            elif idx == 1:
                l = abs(list(contianer[0])[-1]-re[0][0])
                h = abs(re[0][1]-list(contianer[1])[0]) 
            elif idx == 2:
                l = abs(re[0][0]-list(contianer[0])[0])
                h = abs(re[0][1]-list(contianer[1])[0]) 
            elif idx == 3:
                l = abs(re[0][0]-list(contianer[0])[0])
                h = abs(list(contianer[1])[-1]-re[0][1])
            return area1 + area2 - l*h
        elif len(re) == 2:
            id1, id2 = points.index(re[0]), points.index(re[1])
            l, h = 0, 0
            if [id1, id2] == [0,1]:
                l = abs(list(contianer[0])[-1]-re[0][0])
                h = abs(re[0][1] - re[1][1])
            elif [id1, id2] == [1,2]:
                l = abs(re[0][0] - re[1][0])
                h = abs(re[0][1]-list(contianer[1])[0])
            elif [id1, id2] == [2,3]:
                l = abs(re[0][0]-list(contianer[0])[0])
                h = abs(re[0][1] - re[1][1])
            elif [id1, id2] == [3,0]:
                l = abs(re[0][0] - re[1][0])
                h = abs(list(contianer[0])[-1]-re[0][1])
            return area1 + area2 - l*h
        elif len(re) == 4:
            return area1 + area2 - min(area1, area2)
        
        return area1 + area2
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.computeArea(-2, -2, 2, 2, -3, -3, 3, -1)) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    