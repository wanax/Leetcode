'''
Xiaochi Ma
2018-11-04
'''

class Solution:
    
    def lengthOfLIS(self, nums):
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        length = 1
        maxLength = 1
        for i in range(len(nums)):
            pre = nums[i]
            length = 1
            for j in range(i, len(nums)):
                if nums[j] > pre:
                    pre = nums[j]
                    length += 1
                    if length > maxLength:
                        maxLength = length
        
        return maxLength
    
    def intersection(self, nums1, nums2):
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        return list(set1.intersection(set2))
    
    def firstUniqChar(self, s):
        
        if len(s) == 0:
            return -1
        
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        
        index = -1
        for i in range(len(s)):
            if counts[s[i]] == 1:
                index = i
                break
        
        return index
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.lengthOfLIS([10,9,2,5,3,4]))  
