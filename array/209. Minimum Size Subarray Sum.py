'''
Xiaochi Ma
2018-12-07
'''

class Solution(object):
    
    def minSubArrayLen(self, s, nums):
        
        minL = 2**32
        left = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= s:
                minL = min(minL, i-left+1)
                total -= nums[left]
                left += 1
            
        return 0 if minL==2**32 else minL
    
    
if __name__ == '__main__':
    
    solution = Solution()
#    print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))
    print(solution.minSubArrayLen(11, [1,2,3,4,5]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    