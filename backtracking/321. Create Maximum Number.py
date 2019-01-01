'''
Xiaochi Ma
2018-12-29
'''

class Solution:
    
    def get(self, nums, k):
        stack = []
        for i in range(len(nums)):
            while stack and len(nums) - i > k - len(stack) and stack[-1] < nums[i]:
                stack.pop()
            stack.append(nums[i])
        return stack[:k]
    
    def merge(self, n1, n2):
        res, i, j = [], 0, 0
        while i < len(n1) and j < len(n2):
            if n1[i:] > n2[j:]:
                res.append(n1[i])
                i += 1
            else:
                res.append(n2[j])
                j += 1
        if i < len(n1):
            res += n1[i:]
        if j < len(n2):
            res += n2[j:]
        return res
        
    
    def maxNumber(self, nums1, nums2, k):
        
        res = []
        for m in range(k+1):
            if m > len(nums1) or (k-m) > len(nums2):
                continue
            res = max(res, self.merge(self.get(nums1, m), self.get(nums2, k-m)))
        
        return res
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.maxNumber([6, 7], [6, 0, 4], 5))
    print(solution.maxNumber([3, 9], [8, 9], 3))
    print(solution.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))
    print(solution.maxNumber([6,6,8], [5,0,9], 3))
#    print(solution.merge([3,1,2], [2,3,1]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
