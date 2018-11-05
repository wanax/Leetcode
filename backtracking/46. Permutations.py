'''
Xiaochi Ma
2018-10-23
'''
class Solution:
    
    def backTracking(self, nums, res, curArr):
        if len(curArr) == len(nums):
            res.append(curArr[:])
        for i in range(len(nums)):
            if nums[i] in curArr:
                continue
            curArr.append(nums[i])
            self.backTracking(nums, res, curArr)
            curArr.pop()
    
    def permute(self, nums):
        
        if len(nums) == 0 or nums == None:
            return []
        
        res = []
        self.backTracking(nums, res, [])
        return res
    
    def backTracking2(self, nums, res, curArr, used):
        
        if len(curArr) == len(nums):
            res.append(curArr[:])
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
            used[i] = True
            curArr.append(nums[i])
            self.backTracking2(nums, res, curArr, used)
            used[i] = False
            curArr.pop()
    
    def permuteUnique(self, nums):
        
        if len(nums) == 0 or nums == None:
            return []
        
        res = []
        nums.sort()
        used = [False for i in range(len(nums))]
        self.backTracking2(nums, res, [], used)
        return res


if __name__ == '__main__':
    
    solution = Solution()
    print(solution.permuteUnique([1,1,2]))  























