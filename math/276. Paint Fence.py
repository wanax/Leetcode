'''
Xiaochi Ma
2018-12-19
'''
import math
class Solution(object):
    
    def numWays(self, n, k):
        
        if n == 0 or k == 0:
            return 0
        if n == 1:
            return k
        
        same = k
        dif = k*(k-1)
        for i in range(3, n+1):
            same, dif = dif, (same+dif) * (k-1)
        return same + dif
    
    def __init__(self):
        self.m = 2**32
        
    def back(self, n, count):
        
        if n <= 3:
            count += n
            self.m = min(count, self.m)
            return
        
        close = int(math.sqrt(n))
        while close >= 2:
            self.back(n%(close**2), count+(n//(close**2)))
            close -= 1
    
    def numSquares(self, n):
        
        if n <= 3:
            return n
        
        dp = [9999 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            j = 1
            while i - j*j >= 0:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        
        return dp[n]
    
    def wiggleSort(self, nums):
        
        for i in range(len(nums)-1):
            if i%2 == 0:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                if nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                
        return nums
    
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.vs = [v1, v2]
        self.k = 2
        self.count = 0
        self.total = sum([len(v) for v in self.vs])

    def next(self):
        idx = self.count%self.k
        while len(self.vs[idx]) == 0:
            idx += 1
            if idx%self.k == 0:
                idx = 0
        n = self.vs[idx].pop(0)
        self.count += 1
        return n
        

    def hasNext(self):
        return True if self.count < self.total else False
        
    
if __name__ == '__main__':
    
#    solution = Solution()
#    print(solution.wiggleSort([3,5,2,1,6,4])) 
    i, v = ZigzagIterator([1,2], [] ), []
    while i.hasNext(): v.append(i.next())
    print(v)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    