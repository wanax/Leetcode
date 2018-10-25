'''
Xiaochi Ma
2018-10-23
'''

class Solution:
    
    def helper(self, nums, index, res, curArr):
        res.append(curArr[:])
        for i in range(index, len(nums)):
            curArr.append(nums[i])
            self.helper(nums, i+1, res, curArr)
            curArr.pop()
    
    def subsets(self, nums):
        
        if len(nums) == 0 or nums == None:
            return []
        
        res = []
        self.helper(nums, 0, res, [])
        return res
    
    def helper2(self, nums, index, res, curArr, taken):
        
        if index == len(nums):
            res.append(curArr[:])
        else:
            self.helper2(nums, index+1, res, curArr, False)
            if taken or nums[index-1] != nums[index]:
                curArr.append(nums[index])
                self.helper2(nums, index+1, res, curArr, True)
                curArr.pop()
                
    
    def subsetsWithDup(self, nums):
        
        if len(nums) == 0 or nums == None:
            return []
        
        res = []
        nums.sort()
        self.helper2(nums, 0, res, [], True)
        
        return res


if __name__ == '__main__':
    
    solution = Solution()
    print(solution.subsets([1,2,3]))  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    