'''
Xiaochi Ma
2018-11-08
'''

class Solution:
    
    def checkSubarraySum(self, nums, k):
        
        if len(nums) == 0:
            return False
        
        sums = [0] * len(nums)
        sums[0] = nums[0]
        for i in range(1, len(nums)):
            sums[i] = sums[i-1] + nums[i]
            
            if k == 0:
                if sums[i] == 0:
                    return True
                
            else:
                if sums[i] % k == 0:
                    return True
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum1 = sums[j] - sums[i]
                if j - i > 1:
                    if k == 0:
                        if sum1 == 0:
                            return True
                    else:
                        if sum1 % k == 0:
                            return True
        
        return False
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.checkSubarraySum([0, 1, 0], 0))