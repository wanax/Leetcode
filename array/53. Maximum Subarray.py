'''
Xiaochi Ma
2018-10-30
'''

class Solution:
    def maxSubArray(self, nums):
        
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.maxSubArray([-1, -2]))