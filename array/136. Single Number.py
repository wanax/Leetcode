'''
Xiaochi Ma
2018-11-25
'''

class Solution(object):
    
    def singleNumber2(self, nums):
        
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                if i == len(nums) - 1:
                    return nums[i]
                if count == 1:
                    return nums[i-1]
                count = 1
        
        return 0
    
    def singleNumber(self, nums):
        
        for index in range( len( nums ) - 1 ):
            nums[ index + 1 ] ^= nums[index]
        return nums[ -1 ]
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.singleNumber([4,1,2,1,2]))

    