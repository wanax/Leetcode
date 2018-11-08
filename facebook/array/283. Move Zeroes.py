'''
Xiaochi Ma
2018-11-05
'''

class Solution(object):
    
    def moveZeroes(self, nums):
        
        lastNone = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[lastNone]
                nums[lastNone] = nums[i]
                nums[i] = temp
                lastNone += 1
        
        return nums
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.moveZeroes([0,0,1]))