'''
Xiaochi Ma
2018-10-25
'''

class Solution:
    
    def search(self, nums, target):
        
        l = 0
        r = len(nums) - 1
        
        while l<=r:
            mid = int(l + (r - l) / 2)
            if nums[mid] == target:
                return True
            if nums[mid] > nums[r]:
                if nums[mid] > target and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[r]:
                if nums[mid] < target and nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                r -= 1
        
        return False


if __name__ == '__main__':
    
    solution = Solution()
    print(solution.search([3,1,1], 3))


























