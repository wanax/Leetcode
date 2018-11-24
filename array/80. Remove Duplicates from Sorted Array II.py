'''
Xiaochi Ma
2018-11-16
'''

class Solution:
    
    def removeDuplicates(self, nums):
        
        count = 1
        pre = -999
        tag = -1000
        for i in range(len(nums)):
            if nums[i] == pre:
                count += 1
            else:
                pre = nums[i]
                count = 1
            if count >= 3:
                nums[i] = tag
                
        r = len(nums) - 1
        l = 0
        while l < r:
            if nums[l] == tag:
                if nums[r] != tag:
                    nums[l] = nums[r]
                    nums[r] = tag
                r -= 1
            else:
                l += 1
        
        while len(nums) > 0 and nums[-1] == tag:
            nums.pop()

        nums.sort()
        return len(nums)
    

    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.removeDuplicates([0,0,0,1,1,1,1,2,3,3,3])) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    