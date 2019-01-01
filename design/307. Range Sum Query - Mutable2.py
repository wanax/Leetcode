'''
Xiaochi Ma
2018-12-26
'''

class NumArray:
    
    def _update(self, i, val):
        trees = self.trees
        while i < len(self.nums)+1:
            trees[i] += val
            i += (i&(-i))
        self.trees = trees
            

    def __init__(self, nums):
        self.nums = nums;
        self.trees = [0] * (len(nums)+1)
        for i in range(len(nums)):
            self._update(i+1, nums[i])

    def update(self, i, val):
        diff = val - self.nums[i]
        self._update(i+1, diff)
        self.nums[i] = val
        
    def _sum(self, n):
        t = 0
        while n > 0:
            t += self.trees[n]
            n -= (n&(-n))
        return t

    def sumRange(self, i, j):
        return self._sum(j+1) - self._sum(i)
        

obj = NumArray([1,3,5])
obj.update(1, 2)
print(obj.sumRange(0, 2)) 