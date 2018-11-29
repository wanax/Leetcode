'''
Xiaochi Ma
2018-10-30
'''

class Solution:
    
    def maxSubArray2(self, nums):
        
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
    
    def maxSubArray(self, nums):
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        maxn = dp[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0)
            maxn = max(maxn, dp[i])
            
        return maxn
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.maxSubArray([-1, -2]))