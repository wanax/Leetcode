'''
Xiaochi Ma
2018-11-04
'''

class Solution:
    
    def productExceptSelf(self, nums):
        
        res = [1] * len(nums)
        
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        r = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * r
            r *= nums[i]
        
        return res
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.productExceptSelf([1,2,3,4]))   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    