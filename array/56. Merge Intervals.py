'''
Xiaochi Ma
2018-10-30
'''

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:

    
    def merge(self, intervals):
        
        intervals.sort(key=lambda x: x.start)
        
        merged = []
        for inter in intervals:
            if not merged or merged[-1].end < inter.start:
                merged.append(inter)
            else:
                merged[-1].end = max(merged[-1].end, inter.end)
        
        return merged
    
    def insert(self, intervals, newInterval):
        
        intervals.append(newInterval)
        return self.merge(intervals)
    
    
if __name__ == '__main__':
    
    inter1 = Interval(1,3)
    inter2 = Interval(2,6)
    inter3 = Interval(8,10)
    inter4 = Interval(15,18)
    
    q = [inter1, inter2, inter3, inter4]
    
    solution = Solution()
    print(solution.merge(q))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    