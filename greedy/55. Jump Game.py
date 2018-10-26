'''
Xiaochi Ma
2018-10-24
'''

class Solution:
    
    def canJump(self, nums):
        
        lastPosition = len(nums) - 1
        for i in range(lastPosition - 1, -1, -1):
            if i + nums[i] >= lastPosition:
                lastPosition = i
        return lastPosition == 0
    
    def jump(self, nums):
        
        step = 0
        rached = 0
        maxRange = 0
        for i in range(len(nums)):
            if rached < i:
                step += 1
                rached = maxRange
            maxRange = max(maxRange, i+nums[i])
            
        return step
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.jump([2,3,1,1,4]))



























