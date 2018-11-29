'''
Xiaochi Ma
2018-11-28
'''

class Solution(object):
    
    def findPeakElement(self, nums):
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            n = max(nums)
            return nums.index(n)
        
        for i in range(len(nums)):
            left, right = True, True
            if i-1 >= 0 and nums[i] < nums[i-1]:
                left = False
            if i+1 < len(nums) and nums[i] < nums[i+1]:
                right = False
            if left and right:
                return i
        
        return 0

    
    def findMissingRanges(self, nums, lower, upper):
        
        res = []
        
        for i in range(len(nums)):
            if nums[i] == float("-inf"):
                lower = nums[i]+1
                continue
            if lower < nums[i] - 1:
                res.append(str(lower)+"->"+str(nums[i]-1))
            elif lower == nums[i] - 1:
                res.append(str(lower))
            if nums[i] == float("inf"):
                return res
            lower = nums[i] + 1
            
        if lower < upper:
            res.append(str(lower)+"->"+str(upper))
        elif lower == upper:
            res.append(str(lower))
        return res
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.findMissingRanges([0, 1, 3, 50, 75], 0, 99))  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    