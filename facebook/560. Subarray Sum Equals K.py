'''
Xiaochi Ma
2018-11-02
'''


class Solution:
    
    def subarraySum(self, nums, k):
        
        count = 0
        for i in range(len(nums)):
            sumi = 0
            for j in range(i, len(nums)):
                sumi += nums[j]
                if sumi == k:
                    count += 1
        
        return count
    

if __name__ == '__main__':
    
    solution = Solution()
    print(solution.subarraySum([1,1,1], 2))   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    