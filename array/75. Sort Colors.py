'''
Xiaochi Ma
2018-11-16
'''
class Solution:
    
    def sortColors(self, nums):
        
        if len(nums) <= 1:
            return nums
        
        l, r, idx = 0, len(nums)-1, 0
        while True:
            if l > r or idx > r:
                break
            if nums[idx] == 2:
                if nums[r] != 2:
                    nums[idx] = nums[r]
                    nums[r] = 2
                r -= 1
            elif nums[idx] == 0:
                if nums[l] != 0:
                    nums[idx] = nums[l]
                    nums[l] = 0
                l += 1
                idx += 1
            else:
                idx += 1
        return nums
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.sortColors([0,1,0])) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    