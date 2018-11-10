'''
Xiaochi Ma
2018-11-08
'''

class MaxQueue:
    def __init__(self):
        self.q = []
        
    def push(self, item):
        while len(self.q) > 0 and self.q[-1] < item:
            self.q.pop(-1)
        self.q.append(item)
        
    def pop(self):
        return self.q.pop(0)
    
    def getMax(self):
        return self.q[0]

class Solution:
    
    def maxSlidingWindow(self, nums, k):
        
        ans = []
        qu = MaxQueue()
        for i in range(len(nums)):
            qu.push(nums[i])
            if i - k + 1 >= 0:
                ans.append(qu.getMax())
                if nums[i-k+1] == qu.getMax():
                    qu.pop()
        
        return ans
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.maxSlidingWindow( [1,3,-1,-3,5,3,6,7], 3))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    