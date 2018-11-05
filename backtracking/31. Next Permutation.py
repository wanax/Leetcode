'''
Xiaochi Ma
2018-10-25
'''

class Solution:
    def nextPermutation(self, nums):
        
        if len(nums) == 0:
            return []
        
        i = len(nums) - 1
        while i > 0:
            if nums[i]< nums[i-1]:
                i -= 1
            else:
                break
        l = i - 1
        minN = nums[i]
        index = i
        for i in range(i, len(nums)):
            if nums[i] < minN:
                minN = nums[i]
                index = i
        
        nums[index] = nums[l]
        nums[l] = minN
        
        return nums


if __name__ == '__main__':
    
    solution = Solution()
    print(solution.nextPermutation([1,2,6,5,4,3,2,1]))
























