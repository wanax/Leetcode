'''
Xiaochi Ma
2018-10-17
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        
        nums.sort()
        
        n, result = len(nums), []
        
        minDiff = 999
        for i in range(n):
            t = target - nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                diff = t - (nums[l] + nums[r])
                if abs(diff) < minDiff:
                    minDiff = abs(diff)
                    result = [nums[i], nums[l], nums[r]]
                if diff == 0:
                    return sum(result)
                if diff > 0:
                    l += 1
                elif diff < 0:
                    r -= 1
        
        return sum(result)
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.threeSumClosest([0,2,1,-3], 1))
                
                
            



























