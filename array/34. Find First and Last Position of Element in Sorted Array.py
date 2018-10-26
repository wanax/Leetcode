'''
Xiaochi Ma
2018-10-25
'''

class Solution:
    
    def searchRange(self, nums, target):
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = int(l + (r - l)/2)
            if nums[mid] == target:
                l = mid
                while l >= 0 and nums[l] == target:
                    l -= 1
                r = mid
                while r < len(nums) and nums[r] == target:
                    r += 1
                return [l+1, r-1]
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
    
    def searchInsert(self, nums, target):
        
        i = 0
        while i < len(nums):
            if nums[i] < target:
                i += 1 
                continue
            break
        return i
    
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.searchInsert([1,3,5,6], 0))   
    
    



















