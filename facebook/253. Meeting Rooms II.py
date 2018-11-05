'''
Xiaochi Ma
2018-10-31
'''

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
import heapq

class Solution:
    
    def minMeetingRooms(self, intervals):
        
        if len(intervals) == 0:
            return 0
        
        free_rooms = []
        intervals.sort(key=lambda k : k.start)
        
        heapq.heappush(free_rooms, intervals[0].end)
        
        for inter in intervals[1:]:
            if free_rooms[0] <= inter.start:
                heapq.heappop(free_rooms)
                
            heapq.heappush(free_rooms, inter.end)
            
        return len(free_rooms)
    
    
    
if __name__ == '__main__':
    
    inter1 = Interval(0,30)
    inter2 = Interval(5,10)
    inter3 = Interval(15,20)
    inter4 = Interval(15,18)
    
    q = [inter1, inter2, inter3]
    
    solution = Solution()
    print(solution.minMeetingRooms(q))    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    