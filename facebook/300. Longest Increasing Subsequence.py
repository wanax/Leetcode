'''
Xiaochi Ma
2018-11-04
'''

class Solution:
    
    def helper(self, nums, pre, pos):
        
        if pos == len(nums):
            return 0
        
        token = 0
        if nums[pos] > pre:
            token = 1 + self.helper(nums, nums[pos], pos+1)
        notoken = self.helper(nums, pre, pos+1)
        
        return max(token, notoken)
    
    def lengthOfLIS2(self, nums):
        
        if len(nums) == 0:
            return 0
        count = self.helper(nums, -999, 0)
        
        return count
    
    def lengthOfLIS(self, nums):
        
        if len(nums) == 0:
            return 0
        
        dp = [0] * len(nums)
        dp[0] = 1
        
        res = 1
        for i in range(1, len(nums)):
            maxV = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxV = max(maxV, dp[j])
            dp[i] = maxV + 1
            res = max(res, dp[i])
        
        return res
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.lengthOfLIS([4,10,4,3,8,9]))  
    print(2**31)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    