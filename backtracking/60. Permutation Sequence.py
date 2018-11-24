'''
Xiaochi Ma
2018-11-14
'''

class Solution:
    
    def getPermutation(self, n, k):
        
        def factorial(k):
            if k == 1:
                return 1
            return k * factorial(k-1)
        
        def helper(nums, k):
            if k == 1:
                return nums
            group_size = factorial(k-1)
            idx = (k-1) // group_size
            return [nums[idx]] + helper(nums[:idx]+nums[idx+1:], k - group_size*idx)
        
        return "".join(map(str, helper([i for i in range(1, n + 1)], k)))
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.getPermutation(3, 2))  