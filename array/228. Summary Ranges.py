'''
Xiaochi Ma
2018-12-10
'''

class Solution(object):
    
    def summaryRanges(self, nums):
        
        res = []
        l, r = 0, 1
        while l < len(nums):
            if r >= len(nums):
                if l == r-1:
                    res.append(str(nums[l]))
                else:
                    res.append(str(nums[l])+"->"+str(nums[r-1]))
                break
            pre = l
            while r < len(nums) and nums[r] - nums[pre] == 1:
                r += 1
                pre += 1
            if l == pre:
                res.append(str(nums[l]))
            else:
                res.append(str(nums[l])+"->"+str(nums[r-1]))
            l = r
            r += 1
        
        return res
    
    def majorityElement(self, nums):
        
        if len(nums) == 0:
            return []
        
        c1 = nums[0]
        c2 = nums[0]
        count1 = 0
        count2 = 0
        for num in nums:
            if num == c1:
                count1 += 1
                continue
            if num == c2:
                count2 += 1
                continue
            if count1 == 0:
                c1 = num
                count1 += 1
                continue
            if count2 == 0:
                c2 = num
                count2 += 1
                continue
            count1 -= 1
            count2 -= 1
        
        count1 = 0
        count2 = 0
        
        for num in nums:
            if num == c1:
                count1 += 1
            elif num == c2:
                count2 += 1
                
        res = []
        if count1 > len(nums)/3:
            res.append(c1)
        if count2 > len(nums)/3:
            res.append(c2)
        
        return res
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.majorityElement([1,1,1,3,3,2,2,2]))  
#    print(solution.summaryRanges([0,2,3,4,6,8,9]))  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    