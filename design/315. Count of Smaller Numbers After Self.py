'''
Xiaochi Ma
2018-12-26
'''

class FenwickTree:
    def __init__(self, n):
        self.sums = [0] * (n+1)
        
    def update(self, i, diff):
        while i < len(self.sums):
            self.sums[i] += diff
            i += (i&(-i))
    
    def presum(self, i):
        t = 0
        while i > 0:
            t += self.sums[i]
            i -= (i&(-i))
        return t

class Solution:
    
    def countSmaller(self, nums):
        
        ranks = sorted(set(nums))
        rank = 0
        res = []
        tr = FenwickTree(len(ranks))
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            rank = ranks.index(num)
            tr.update(rank+1, 1)
            res.append(tr.presum(rank))
        
        return res[::-1]
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.countSmaller([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41])) 
#    print(solution.countSmaller([-1,0])) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    